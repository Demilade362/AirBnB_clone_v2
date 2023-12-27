#!/usr/bin/python3
from os import getenv
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
            'User': User, 'Place': Place,
            'State': State, 'City': City,
            'Amenity': Amenity, 'Review': Review
          }


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, password, host, database), pool_pre_ping=True)

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        new_dict = {}
        if cls:
            tmp_cls = cls
            if type(cls) is str:
                if cls == kcls:
                    tmp_cls = vcls

            session_query = self.__session.query(tmp_cls)
            for query in session_query:
                key = "{}.{}".format(query.__class__.__name__, query.id)
                new_dict[key] = query
        else:
            for kcls, vcls in classes.items():
                session_query = self.__session.query(vcls)
                for query in session_query:
                    key = "{}.{}".format(query.__class__.__name__, query.id)
                    new_dict[key] = query

        return (new_dict)

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        ses = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ses)
        self.__session = Session()

    def close(self):
        self.__session.close()