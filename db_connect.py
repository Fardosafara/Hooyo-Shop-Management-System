from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Setting up the database connection
engine = create_engine('sqlite:///shop.db')
Session = sessionmaker(bind=engine)

def connect_db():
    import models.user
    import models.product
    import models.order
    import models.order_item

    Base.metadata.create_all(engine)

if __name__ == '__main__':
    connect_db()
