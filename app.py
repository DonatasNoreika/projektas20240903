import sqlalchemy
import pandas as pd
import flask
import calendar

metai = int(input("Įveskite metus: "))

print(calendar.isleap(metai))
