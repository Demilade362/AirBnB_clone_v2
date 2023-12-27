from models.base_model import BaseModel, Base
from models import storage
from os import getenv

class State(BaseModel, Base):
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Returns the list of City objects linked to the current State."""
            from models.city import City  # Import City model here
            city_list = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
