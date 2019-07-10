from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

#postgresql+pg8000://twoflower:mork@localhost/ank


engine = create_engine(
   "postgresql+psycopg2://twoflower:mork@localhost/ank",
    isolation_level="READ UNCOMMITTED",
    echo=True
)

Base = declarative_base()
from sqlalchemy import Column, Integer, String

class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	name = Column(String, unique=True)
	fullname = Column(String)
	nickname = Column("nick", String)
	def __repr__(self):
		return "<User(name='%s', fullname='%s', nickname='%s')>" % (
			self.name, self.fullname, self.nickname)

Base.metadata.create_all(engine)

users = [
	User(name="sjefen", fullname="Kjetilokt", nickname="riverolf"),
	User(name="nils", fullname="Nils Vogt", nickname="nils"),
	User(name="trine", fullname="Trine Lise", nickname="trollo"),
	User(name="anders", fullname="Anders Hagen", nickname="ando")
]

from sqlalchemy.orm import sessionmaker

Session = sessionmaker()
Session.configure(bind=engine)

session = Session()

from sqlalchemy import exc
# for user in users:
# 	session.add(user)
session.add_all(users)
session.commit()
try:
	
	session.commit()
except exc.SQLAlchemyError as error:
	print("Users allready exists")

record = session.query(User).filter_by(name="nils")
print(record)