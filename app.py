import sqlalchemy
import pandas as pd
import flask
import PIL
import calendar
from models import Course

kursas = Course("Python kursas", 500)

metai = int(input("Įveskite metus: "))

if calendar.isleap(metai):
    print("Keliamieji")
else:
    print("Nekeliamieji")

input()
