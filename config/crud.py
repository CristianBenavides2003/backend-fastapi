from sqlalchemy.orm import Session
from model.user import User
from schema import schemas
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()
    
def create_user(db: Session, user: schemas.UserCreate):
    db_user = User(id=user.id,nombre=user.nombre, correo=user.correo)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

def update_user(db: Session, user_id: int, user_update: schemas.UserCreate):
    # Busca el usuario por ID
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    
    # Actualiza los campos necesarios
    db_user.nombre = user_update.nombre
    db_user.correo = user_update.correo
    
    # Guarda los cambios en la base de datos
    db.commit()
    db.refresh(db_user)
    return db_user