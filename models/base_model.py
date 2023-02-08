#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    """This class defines all common attributes and methods for other classes.

    Attributes:
        id (str): Unique identifier for each instance, generated using uuid.uuid4().
        created_at (datetime): The date and time the instance was created.
        updated_at (datetime): The date and time the instance was last updated.
    """

    def __init__(self):
        """Initialize an instance of the BaseModel class.
        Generates a unique identifier for the instance, sets the created_at and
        updated_at attributes to the current date and time.
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the BaseModel instance.

        Returns:
        str: A string in the format [<class name>] (<self.id>) <self.__dict__>.
        """

        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

        def save(self):
            """Update the updated_at attribute with the current date and time."""
            self.updated_at = datetime.now()

        def to_dict(self):
            """Return a dictionary representation of the BaseModel instance.

            Returns:
            dict: A dictionary containing all keys/values of __dict__ of the instance.
            The dictionary will only include instance attributes that have been set.
            A key "__class__" must be added to this dictionary with the class name of the object.
            The "created_at" and "updated_at" attributes must be converted to string objects in
            ISO format (e.g. %Y-%m-%dT%H:%M:%S.%f).
            """
            d = self.__dict__.copy()
            d["__class__"] = type(self).__name__
            d["created_at"] = self.created_at.isoformat()
            d["updated_at"] = self.updated_at.isoformat()
            return d
