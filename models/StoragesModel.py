from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from database import Base

import pytz 
from datetime import datetime

class YDiskStoragesModel(Base):
    __tablename__ = "ydisk_storages"

    storages_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    storage_name = Column(String, nullable=False)
    yid_key = Column(String, nullable=False, unique=True)

def get_time():
    return datetime.now(pytz.timezone('Europe/Moscow')).replace(tzinfo=None)

class UsersModel(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    domain_name = Column(String, nullable=False)
    # access_mode
    # business_unit_id
    # cal_type
    # created_by
    # employee_id
    # entity_image
    # full_name
    # state_code
    # status_code
    # middle_name
    # mobile_phone
    # modified_on
    # modified_by

    full_name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    mail = Column(String, nullable=False)
    date_create = Column(DateTime(timezone=True), nullable=False, default=get_time)