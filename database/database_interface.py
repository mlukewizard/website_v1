import os

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_NAME = os.path.join('database', 'website_db')

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    email_address = Column(String(250), primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

    def __repr__(self):
        return "email_address = {0}, first_name = {1}, last_name = {2}, password = {3}".format(self.email_address, self.first_name, self.last_name, self.password)

def check_or_create_database():
    if not os.path.exists(DATABASE_NAME):
        create_database()

def create_database():
    # Create an engine that stores data in the local directory's
    # sqlalchemy_example.db file.
    engine = create_engine('sqlite:///{0}.db'.format(DATABASE_NAME))

    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.
    Base.metadata.create_all(engine)

def add_user(user):
    check_or_create_database()
    engine = create_engine('sqlite:///{0}.db'.format(DATABASE_NAME))
    Base.metadata.bind = engine
    # Adds some stuff to the database
    DBSession = sessionmaker(bind=engine)

    session = DBSession()
    session.add(user)
    session.commit()



def get_user_from_email(query_email):
    check_or_create_database()
    engine = create_engine('sqlite:///{0}.db'.format(DATABASE_NAME))
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    session = DBSession()
    # Make a query to find all Persons in the database
    try:
        return session.query(User).filter(User.email_address == query_email).one()
    except:
        return None

def get_all_users():
    check_or_create_database()
    engine = create_engine('sqlite:///{0}.db'.format(DATABASE_NAME))
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    session = DBSession()
    return session.query(User).all()

if __name__ == "__main__":

    add_user(User(email_address = 'sarah@gmail.com', first_name = "sarah", last_name = "craddock", password="Sarah<3luke"))
    get_user_from_email('sarah@gmail.com')