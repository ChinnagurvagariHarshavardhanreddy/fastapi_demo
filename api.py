from fastapi import FastAPI
from pydantic import BaseModel

db=[]

app=FastAPI()

class Student(BaseModel):
    id : int
    name : str
    age : int

@app.get('/item')
def show():
    return db

@app.post('/item')
def create(student:Student):
    db.append(student)
    return f'update succefully'

@app.put('/item')
def update(student:Student):
    updatedata = student
    if db[student.id] == student.id:
        db[student.id] = updatedata
        return ' update successfully'
    return 'not there'

@app.delete('/item')
def delete(student:Student):
    if db[student.id] == student.id:
        del db[student.id]
        return db
    return 'not there'

@app.get('/item/{id}')
def take(id):
    return db[id]