from API import db, app
from sqlalchemy import Column, String, Integer


class User(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(db.String(50), nullable=False)
    last_name = Column(db.String(50), nullable=False)
    mobile = Column(db.String(15), nullable=False)
    email = Column(db.String(50), nullable=False)
    gender = Column(db.String(10), nullable=False)
    pincode= Column(db.String(10), nullable=False)
    city = Column(db.String(50), nullable=False)
    state = Column(db.String(50), nullable=False)
    

# if __name__ == '__main__':
#     db.create_all()
#     db.init_app(app)


 





