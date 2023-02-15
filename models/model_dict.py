#!/usr/bin/python3

from datetime import datetime
class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if "created_at" in kwargs:
                setattr(self, "created_at", datetime.strptime(kwargs["created_at"], '%Y-%m-%dT%H:%M:%S.%f'))
                if "updated_at" in kwargs:
                    setattr(self, "updated_at", datetime.strptime(kwargs["updated_at"], '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()
