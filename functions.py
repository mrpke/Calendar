#defining the functions used for creating the tex file.
import datetime
import calendar

def createRectangles():
    if not 'color' in globals():
        color="\definecolor{use}{HTML}{FF7F00}"

    drawString="\\fill["+str(color)+"] ("+str(sx)+","+str(sy)+") rectangle ("+str((sx+length))+","+str((sy+height))+")"
    return drawString

def createMonths(yr):

    for i in range(1, 13):
        for ii in calendar.itermonthdates(yr,i):
            print ii

def loadPackages():

    packages="\usepackage{tikz} \n \usepackage{xcolor}"
    return packages

def composeCalender():

    packg=loadPackages()


