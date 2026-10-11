import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Запуск из кода!"}

# Добавляем этот блок в конец файла
if __name__ == "__main__":
    # Обратите внимание: имя файла передается как строка
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)