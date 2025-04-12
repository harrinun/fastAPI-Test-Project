from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def index():
    return {
        'data': {'name': 'Nana'}
    }

@app.get('/about')
def about():
    return {
        'id': 1,
        'name': 'Nana',
        'age': 100
    }