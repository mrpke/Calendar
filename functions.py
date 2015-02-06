#defining the functions used for creating the tex file.
import datetime
from calendar import Calendar
import csv


def createYear(yr):
    drawString="\path[fill=gray, opacity=0.8] ("+str(286+300*12)+",0) node[above right, color=gray, opacity=0.8, font=\Huge, scale=8, anchor=south east] {\\textbf{"+str(yr)+"}};\n "
    return drawString


def createRectangle(sx, s0y, day, month, birth, feier, pm=0, length=286, height=64, ro="", mi=""):
    drawString=""
    if pm == 1:
        sy=0
        Month ={1:"Januar",
                2:"Februar",
                3:"M\\\"arz",
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
        drawString+="\path[draw=black, fill=use,fill opacity=0.4, even odd rule,line width=1.4pt] ("+str(sx)+","+str(sy)+") rectangle ("+str(sx+length)+","+str(sy+height)+");\n"
        drawString+="\path[draw=black] ("+str(sx+(length/2))+","+str(sy+(height/2))+") node[above right,anchor=center, font=\\Huge, scale=1.5, text depth=0] {\\textbf{"+Month[month]+"}};"
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
    colorized={5: "fill=use, fill opacity=0.2,",
                6: "fill=use, fill opacity=0.4,"
                }
    if day.weekday() in colorized:
        color=colorized[day.weekday()]
    else:
        color=""

    #drawString="\\fill["+str(color)+"] ("+str(sx)+","+str(sy)+") rectangle ("+str((sx+length))+","+str((sy+height))+")"
    #return drawString
    #(149,363) / (433,427)
    #fill=use,opacity=0.25
    drawString+="\path[draw=black,"+color+" even odd rule,line width=1.4pt] ("+str(sx)+","+str(sy)+") rectangle ("+str(sx+length)+","+str(sy+height)+");\n"
    drawString+="\path[fill=black] ("+str(sx+30)+","+str(sy+(height/2)-10)+") node[above right, font=\Huge, scale=1.1, anchor=center] {\\textbf{"+str(day.day)+"}};\n"
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

def createMonths(yr,birth, feier, bild):
    cal=Calendar(0)
    x,y=0,0
    drawString="\\begin{figure}[!h]\n\\centering\n"

    drawString+="\\tikz[overlay,remember picture]\\node[opacity=0.4]at (current page.center) {\includegraphics{"+bild+"}};"
    drawString+="\\begin{tikzpicture}[y=0.80pt, x=0.8pt,yscale=-1, inner sep=0pt,outer sep=0pt]"
    drawString+=createYear(yr)
    for i in range(1, 13):
        x=x+300
        y=0
        drawString+="\n"+createRectangle(x,y,0,i,dict(),dict(),1)
        for ii in cal.itermonthdates(yr,i):
            drawString+="\n"+createRectangle(x, y, ii, i, birth, feier)
    drawString+="\end{tikzpicture}\n \n \end{figure}"
    return drawString

def loadPackages(papersize):

    packages="\usepackage{graphicx}\n\usepackage[margin=20pt, landscape, "+papersize+"paper]{geometry}\n\usepackage{tikz} \n\usepackage{xcolor}\n"
    packages+="\usepackage{helvet}\n\\renewcommand{\\familydefault}{\sfdefault}\n \\fontfamily{phv}\\selectfont"
    return packages

def composeCalendar(yr, birthdays, feiertage,  bild, papersize="a0", color="FF7F00"):

    birth=createSpecialDatesDict(birthdays)
    feier=createSpecialDatesDict(feiertage)
    color="\definecolor{use}{HTML}{"+color+"}\n"
    packg=loadPackages(papersize)

    rect = createMonths(yr, birth, feier, bild)
    top="\documentclass{article}\n"
    mid="\\begin{document}\n"
    end="\end{document}"
    A = open("test3.tex", 'w')
    A.write(top+"\n"+packg+"\n"+color+"\n"+mid+"\n"+rect+"\n"+end)
    A.close()




