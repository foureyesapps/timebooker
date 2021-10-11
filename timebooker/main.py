from functools import lru_cache
from . import models, schemas, config
from fastapi import FastAPI, status, Response, HTTPException, Depends
from .database import engine, SessionLocal
from .config import Settings
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(engine)


@lru_cache()
def get_settings():
    return config.Settings()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/health', status_code=status.HTTP_200_OK)
def health():
    return {'status': 'OK'}


@app.get('/info')
def get_app_info(settings: Settings = Depends(get_settings)):
    return {
        'app_name': settings.app_name,
        'admin_email': settings.admin_email,
        'sqlalchemy_database_url': settings.sqlalchemy_database_url
    }


@app.post('/user', status_code=status.HTTP_201_CREATED)
def create(request: schemas.User, db: Session = Depends(get_db)):
    user = models.User(name=request.name, cellphone=request.cellphone, email=request.email, username=request.username,
                       password=request.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@app.delete('/user/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    user.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put('/user/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.User, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    user.update(request.dict())
    db.commit()


@app.get('/user')
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


@app.get('/user/{id}', status_code=status.HTTP_200_OK)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return user

# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=8000)
