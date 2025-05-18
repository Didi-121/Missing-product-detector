# supabase_utils.py
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")


supabase: Client = create_client(SUPABASE_URL, SUPABASE_API_KEY)

def insert_detection(label, confidence, timestamp):
    data = {
        "label": label,
        "confidence": confidence,
        "timestamp": timestamp
    }

    print("Insertando:", data)
    
    try:
        response = supabase.table("Detections").insert(data).execute()
        return response
    except Exception as e:
        print("Error grave en Python o conexión:", e)    
        return None

def receive_data():
    try:
        response = supabase.table("Detections").select("*").execute()
        return response
    except Exception as e:
        print("Error grave en Python o conexion:", e)
        return None

