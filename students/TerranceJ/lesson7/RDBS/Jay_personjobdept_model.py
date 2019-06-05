"""
    Simple database examle with Peewee ORM, sqlite and Python
    Here we define the schema

"""

import logging
from peewee import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('One off program to build the classes from the model in the database')

logger.info('Here we define our data (the schema)')
logger.info('First name and connect to a database (sqlite here)')

logger.info('The next 3 lines of code are the only database specific code')

database = SqliteDatabase('personjob.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;') #needede for sqlite only

logger.info('This means we can easilyf switch to a different database')
logger.info('Enable the Peewee magic! This base class does it all')
logger.info('By inheritance only we keep our model (almost) technology neutral')

class BaseModel(Model):
    class Meta:
        database = database


class Person(BaseModel):
    """
        This class defines Person, which maintains details of someone
        for whom we want to research career to date.
    """
    logger.info('Specify fileds in person databasefrom datetime import datetime')
    logger.info('Each person mush have a unique identifier')
    person_name = CharField(primary_key = True, max_length = 30)
    lives_in_town = CharField(max_length = 40)
    nickname = CharField(max_length = 20, null = True)

class Job(BaseModel):
    """
        This class defines Job, which maintains details of past Jobs
        held by a Person.
    """
    logger.info('Specify fields in Job')
    job_name = CharField(primary_key = True, max_length = 30)
    start_date = DateField(formats = 'YYYY-MM-DD')
    end_date = DateField(formats = 'YYYY-MM-DD')
    salary = DecimalField(max_digits = 7, decimal_places = 2)
    person_employed = ForeignKeyField(Person, related_name='was_filled_by', null = False)


class Department(BaseModel):
    """ 
        This class defines a Department, which maintains details about a department
    """
    logger.info('Specify fields in Department')
    department_number = CharField(primary_key = True, max_length=4)
    department_name = CharField(max_length=30)
    deparment_manager = CharField(max_length=30)
 

database.create_tables([
    Person,
    Job,
    Department])   

database.close()

logger.info('Databases created')
