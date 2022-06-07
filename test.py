from cmath import sqrt
from datetime import datetime
from random import random, uniform
from xml.sax.handler import feature_external_ges
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractScrollArea
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch
import openpyxl
import os
from reportlab.lib.pagesizes import letter
import textwrap
from reportlab.lib import colors
from datetime import datetime
import random


#print(int(uniform(1,4)))
p = "$35%.90"
speChars = '%"|$'
pp = p.replace(speChars, '')
print(pp)
