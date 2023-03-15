from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from mysql.connector import connect, Error

app = FastAPI(version="1.1.0")

# MySQL connection settings
db_config = {
    "host": "localhost",
    "user": "user",
    "password": "password",
    "database": "database",
}

# Get all users from the database
@app.get("/users")
def read_users():
    try:
        with connect(**db_config) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM users")
                results = cursor.fetchall()
                users = []
                for result in results:
                    user = {
                        "id": result[0],
                        "name": result[1],
                        "email": result[2]
                    }
                    users.append(user)
                return JSONResponse(content=jsonable_encoder(users))
    except Error as e:
        print(e)

# Get a specific user by ID
@app.get("/users/{user_id}")
def read_user(user_id: int):
    try:
        with connect(**db_config) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))
                result = cursor.fetchone()
                if result is None:
                    return JSONResponse(content="User not found")
                user = {
                    "id": result[0],
                    "name": result[1],
                    "email": result[2]
                }
                return JSONResponse(content=jsonable_encoder(user))
    except Error as e:
        print(e)

# Create a new user
@app.post("/users")
def create_user(name: str, email: str):
    try:
        with connect(**db_config) as conn:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
                conn.commit()
                user_id = cursor.lastrowid
                user = {
                    "id": user_id,
                    "name": name,
                    "email": email
                }
                return JSONResponse(content=jsonable_encoder(user), status_code=201)
    except Error as e:
        print(e)

# Update an existing user by ID
@app.put("/users/{user_id}")
def update_user(user_id: int, name: str, email: str):
    try:
        with connect(**db_config) as conn:
            with conn.cursor() as cursor:
                cursor.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (name, email, user_id))
                conn.commit()
                user = {
                    "id": user_id,
                    "name": name,
                    "email": email
                }
                return JSONResponse(content=jsonable_encoder(user))
    except Error as e:
        print(e)

# Delete a user by ID
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    try:
        with connect(**db_config) as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
                conn.commit()
                return JSONResponse(content=None, status_code=204)
    except Error as e:
        print(e)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
