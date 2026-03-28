from fastapi import FastAPI ,HTTPException
from pydantic import BaseModel
app=FastAPI()
db = []
class Student(BaseModel):
    name : str
    rollno : int
    course : str

@app.get('/list')
def get():
    return db

@app.post('/')
def create(student:Student):
    db.append(student)
    return 'upadte successfully'

@app.get('/list/{id}')
def task(id : int):
    return db[id]

@app.put('/update/{id}/{value}')
def upform(id : int,value:int, student : Student):
    for index , data in enumerate(db):
        if data.id == id:
            db[index].rollno = value
        return HTTPException(status_code=404,detail='wrong data')
    return "update succesfully"

@app.delete('/delete/{id}')
def upform(id : int):
    db.pop(id)
    return 'delete succesfully'