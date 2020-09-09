#!/usr/bin/python3
"""DBStorage class for AirBnB"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session, relationship
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
    """db storage"""
    __engine = None
    __session = None

    def __init__(self):
        """constructor"""
        db_user = getenv('HBNB_MYSQL_USER')
        db_pwd = getenv('HBNB_MYSQL_PWD')
        db_host = getenv('HBNB_MYSQL_HOST')
        db_name = getenv('HBNB_MYSQL_DB')
        DBStorage.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'.format(
                db_user, db_pwd, db_host, db_name), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ALL METHOD TO GET ALL ROW OF CLS"""
        classes_ = [User, State, City, Amenity, Place, Review]
        # list.. every row of the table.... each row is an object User..exmpl..
        query_result = []

        if not cls:
            for cls_ in classes:
                query_result += self.__session.query(cls_).all()
            """
            all_dict[User.__name__] = self.__session.query(User).all()
            all_dict[State.__name__] = self.__session.query(State).all()
            all_dict[City.__name__] = self.__session.query(City).all()
            all_dict[Amenity.__name__] = self.__session.query(Amenity).all()
            all_dict[Place.__name__] = self.__session.query(Place).all()
            all_dict[Review.__name__] = self.__session.query(Review).all()
            """
        else:
            query_result += self.__session.query(cls).all()
        return {
            '{}.{}'.format(
                type(obj_).__name__,
                obj_.id): obj_ for obj_ in query_result}

    def new(self, obj):
        """add object to session"""
        if not obj:
            return
        self.__session.add(obj)

    def save(self):
        """ commit changes to session to make then appear"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj(row) from table.. expmle delete user 1 from User table"""
        if not obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """basically initialize the ORM object"""
        if getenv("HBNB_ENV") == "test":  # ON INIT OF .
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)  # create like database..

        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
        # all session objects share the same registry
        # to end registry call sccoped_session.remove()

    def close(self):
        """close mthod for mysql database"""
        self.__session.close()
