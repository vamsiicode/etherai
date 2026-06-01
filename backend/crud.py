from sqlalchemy.orm import Session, selectinload

if __package__ is None or __package__ == '':
    import models, schemas
else:
    from . import models, schemas

# Products

def get_product_by_sku(db: Session, sku: str):
    return db.query(models.Product).filter(models.Product.sku == sku).first()


def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def get_products(db: Session):
    return db.query(models.Product).order_by(models.Product.id.desc()).all()


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Customers

def get_customer_by_email(db: Session, email: str):
    return db.query(models.Customer).filter(models.Customer.email == email).first()


def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()


def get_customers(db: Session):
    return db.query(models.Customer).order_by(models.Customer.id.desc()).all()


def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(**customer.model_dump())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

# Orders

def get_orders(db: Session):
    return (
        db.query(models.Order)
        .options(selectinload(models.Order.product), selectinload(models.Order.customer))
        .order_by(models.Order.created_at.desc())
        .all()
)


def create_order(db: Session, order: schemas.OrderCreate):
    product = get_product(db, order.product_id)
    product.stock -= order.quantity
    db_order = models.Order(**order.model_dump())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
