import sqlalchemy
import pandas as pd
import flask
import calendar
from models import Course

kursas = Course("Python kursas")

metai = int(input("Įveskite metus: "))

print(calendar.isleap(metai))
