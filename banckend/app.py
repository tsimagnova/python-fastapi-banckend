from fastapi import FastAPI
from database import db_connection

app = FastAPI()

@app.get("liste/")
async def read_root():
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM etudiants")
    result = cursor.fetchall()
    cursor.close()
    return {"message": "Connexion réussie à la base de données RDS", "data": result}


