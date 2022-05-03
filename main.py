# -*- coding:utf-8 -*-

import calendar
import holidays
import MySQLdb

from datetime import date

num = date.today().weekday()

sem = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")

if num < 5:
    print(f"Tenha uma boa {sem[num]}-feira =D")
else:
    print(f"Tenha um bom {sem[num]} =D")