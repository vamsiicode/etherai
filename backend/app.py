import sys
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

if __package__ is None or __package__ == '':
    from database import SessionLocal, engine, Base
    import models, schemas, crud
else:
    from .database import SessionLocal, engine, Base
    from . import models, schemas, crud

Base.metadata.create_all(bind=engine)
app = FastAPI(title='Inventory & Order Management')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/products', response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    existing = crud.get_product_by_sku(db, product.sku)
    if existing:
        raise HTTPException(status_code=400, detail='SKU already exists')
    return crud.create_product(db, product)

@app.get('/products', response_model=list[schemas.ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return crud.get_products(db)

@app.post('/customers', response_model=schemas.CustomerResponse)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    existing = crud.get_customer_by_email(db, customer.email)
    if existing:
        raise HTTPException(status_code=400, detail='Customer email already exists')
    return crud.create_customer(db, customer)

@app.get('/customers', response_model=list[schemas.CustomerResponse])
def list_customers(db: Session = Depends(get_db)):
    return crud.get_customers(db)

@app.post('/orders', response_model=schemas.OrderResponse)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    product = crud.get_product(db, order.product_id)
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')
    if product.stock < order.quantity:
        raise HTTPException(status_code=400, detail='Insufficient stock')
    customer = crud.get_customer(db, order.customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail='Customer not found')
    return crud.create_order(db, order)

@app.get('/orders', response_model=list[schemas.OrderResponse])
def list_orders(db: Session = Depends(get_db)):
    return crud.get_orders(db)
