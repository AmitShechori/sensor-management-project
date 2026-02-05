import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from datetime import datetime
from typing import List, Dict

app = FastAPI()

# חיבור נכסים סטטיים ותבניות
base_path = os.path.dirname(os.path.realpath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(base_path, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(base_path, "templates"))

# מודל נתונים
class SensorEvent(BaseModel):
    event_id: str
    sensor_id: str
    location: str
    value: float
    timestamp: str = datetime.now().strftime("%H:%M:%S")

# מאגר נתונים בזיכרון
all_events: List[Dict] = []

@app.get("/", name="home")
def home(request: Request):
    # קיבוץ נתונים וחישוב סטטיסטיקה
    grouped_data = {}
    
    for event in all_events:
        s_id = event['sensor_id']
        if s_id not in grouped_data:
            grouped_data[s_id] = {
                "events": [], 
                "location": event['location'],
                "avg_temp": 0
            }
        grouped_data[s_id]["events"].append(event)

    # חישוב ממוצע ללא ערכים קיצוניים (רק בין 15 ל-35 מעלות)
    for s_id, data in grouped_data.items():
        normal_readings = [e['value'] for e in data["events"] if 15 <= e['value'] <= 35]
        if normal_readings:
            data["avg_temp"] = round(sum(normal_readings) / len(normal_readings), 1)
        else:
            data["avg_temp"] = "N/A"
    
    return templates.TemplateResponse("home.html", {
        "request": request,
        "grouped_data": grouped_data,
        "title": "Sensor Dashboard"
    })

@app.post("/ingest")
async def receive_data(event: SensorEvent):
    # הוספה לראש הרשימה כדי לראות נתונים חדשים קודם
    all_events.insert(0, event.model_dump())
    return {"status": "success"}