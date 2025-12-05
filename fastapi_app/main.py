from fastapi import FastAPI
from .connection import get_connection

app = FastAPI()

@app.get("/products")
def products():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT name, price FROM catalog_app_product WHERE is_approved = TRUE;")
    rows = cur.fetchall()
    conn.close()
    return {"products": [{"name": r[0], "price": float(r[1])} for r in rows]}

@app.get("/users")
def users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users_app_user where is_admin = FALSE ORDER BY id ASC ;")
    rows = cur.fetchall()
    conn.close()
    return {"User_Name": [{"name": r[2], "id":r[0]} for r in rows]}

