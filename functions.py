#defining the functions used for creating the tex file.
import datetime
from calendar import Calendar
import csv

def createRectangle(sx, s0y, day, month, birth, feier, pm=0, length=286, height=64, ro="", mi=""):
    drawString=""
    if pm == 1:
        sy=0
        Month ={1:"Januar",
                2:"Februar",
                3:"Maerz",
                4:"April",
                5:"Mai",
                6:"Juni",
                7:"Juli",
                8:"August",
                9:"September",
                10:"Oktober",
                11:"November",
                12:"Dezember"
                }
        drawString+="\path[draw=black, fill=use, opacity=0.250, even odd rule,line width=1.4pt] ("+str(sx)+","+str(sy)+") rectangle ("+str(sx+length)+","+str(sy+height)+");\n"
        drawString+="\path[fill=black] ("+str(sx+4)+","+str(sy+27)+") node[above right, font=\Huge] {"+Month[month]+"};\n"
        return drawString

    if day.month != month:
        return ""
    sy=80*(day.day)
    days={0:"Mo",
            1:"Di",
            2:"Mi",
            3:"Do",
            4:"Fr",
            5:"Sa",
            6:"So"
            }
    colorized={5: "fill=use, ",
                6: "fill=use, "
                }
    if day.weekday() in colorized:
        color=colorized[day.weekday()]
    else:
        color=""

    #drawString="\\fill["+str(color)+"] ("+str(sx)+","+str(sy)+") rectangle ("+str((sx+length))+","+str((sy+height))+")"
    #return drawString
    #(149,363) / (433,427)
    #fill=use,opacity=0.25
    drawString+="\path[draw=black,"+color+"opacity=0.250, even odd rule,line width=1.4pt] ("+str(sx)+","+str(sy)+") rectangle ("+str(sx+length)+","+str(sy+height)+");\n"
    drawString+="\path[fill=black] ("+str(sx+4)+","+str(sy+27)+") node[above right, font=\Huge] {"+str(day.day)+"};\n"
    drawString+="\path[fill=black] ("+str(sx+length-4)+","+str(sy+height-4)+") node[above right, font=\Huge, anchor=south east] {"+days[day.weekday()]+"};\n"
    if str(day.day)+"."+str(day.month)+"." in birth:
        drawString+="\path[fill=black] ("+str(sx+length-4)+","+str(sy+4)+") node[above right, font=\Large, anchor=north east] {"+birth[str(day.day)+"."+str(day.month)+"."]+"};"
    if str(day.day)+"."+str(day.month)+"." in feier:
        drawString+="\path[fill=black] ("+str(sx+4)+","+str(sy+height-4)+") node[above right, font=\Large, anchor=south west] {"+feier[str(day.day)+"."+str(day.month)+"."] +"};"
    return drawString

def createSpecialDatesDict(fname):
    with open(fname, 'rb') as B:
        d=dict()
        reader=csv.reader(B, delimiter="\t")
        for row in reader:
            st=row.pop()
            date=row.pop()
            if date in d:
                d[date]+=", "+st # im file: Datum (dd.mm.) \t Name
            else:
                d[date]=st
            print date
    return d

def createMonths(yr,birth, feier):
    cal=Calendar(0)
    x,y=0,0
    drawString="\\begin{figure}\n\\centering\n\\begin{tikzpicture}[y=0.80pt, x=0.8pt,yscale=-1, inner sep=0pt,outer sep=0pt]"
    for i in range(1, 13):
        x=x+300
        y=0
        drawString+="\n"+createRectangle(x,y,0,i,dict(),dict(),1)
        for ii in cal.itermonthdates(yr,i):
            drawString+="\n"+createRectangle(x, y, ii, i, birth, feier)
    drawString+="\end{tikzpicture}\n \end{figure}"
    return drawString

def loadPackages(papersize):

    packages="\usepackage[landscape,"+papersize+"paper]{geometry}\n\usepackage{tikz} \n\usepackage{xcolor}\n"
    return packages

def composeCalendar(yr, papersize="a0", color="FF7F00"):

    birth=createSpecialDatesDict("birthdays.txt")
    feier=createSpecialDatesDict("feier.txt")
    color="\definecolor{use}{HTML}{"+color+"}\n"
    packg=loadPackages(papersize)

    rect = createMonths(yr, birth, feier)
    top="\documentclass{article}\n"
    mid="\\begin{document}\n\hoffset=0pt\n\\voffset=0pt\n\\topmargin=0pt\n\oddsidemargin=0pt\n\evensidemargin=0pt"
    end="\end{document}"
    A = open("test3.tex", 'w')
    A.write(top+"\n"+packg+"\n"+color+"\n"+mid+"\n"+rect+"\n"+end)
    A.close()




