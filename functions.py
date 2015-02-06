#defining the functions used for creating the tex file.
import datetime
from calendar import Calendar

def createRectangle(sx, s0y, day, month, length=286, height=64, ro="", mi=""):
    if day.month != month:
        return ""
    sy=80*(day.day-1)
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
    drawString=""
    #(149,363) / (433,427)
    #fill=use,opacity=0.25
    drawString+="\path[draw=black,"+color+"opacity=0.250, even odd rule,line width=1.4pt] ("+str(sx)+","+str(sy)+") rectangle ("+str(sx+length)+","+str(sy+height)+");\n"
    drawString+="\path[fill=black] ("+str(sx+4)+","+str(sy+27)+") node[above right, font=\Huge] {"+str(day.day)+"};\n"
    drawString+="\path[fill=black] ("+str(sx+length-4)+","+str(sy+height-27)+") node[above right, font=\Huge, anchor=south east] {"+days[day.weekday()]+"};\n"
    return drawString


def createMonths(yr):
    cal=Calendar(0)
    x,y=0,0
    drawString="\\begin{tikzpicture}[y=0.80pt, x=0.8pt,yscale=-1, inner sep=0pt,outer sep=0pt]"
    for i in range(1, 3):
        x=x+300
        y=0
        for ii in cal.itermonthdates(yr,i):
            drawString+="\n"+createRectangle(x, y, ii, i)
    drawString+="\end{tikzpicture}"
    return drawString

def loadPackages(papersize):

    packages="\usepackage[landscape,"+papersize+"paper]{geometry}\n\usepackage{tikz} \n\usepackage{xcolor}\n"
    return packages

def composeCalendar(yr, papersize="a0", color="FF7F00"):

    if not 'color' in globals():
        color="\definecolor{use}{HTML}{"+color+"}\n"
    packg=loadPackages(papersize)

    rect = createMonths(yr)
    top="\documentclass{article}\n"
    mid="\\begin{document}\n\hoffset=0pt\n\\voffset=0pt\n\\topmargin=0pt\n\oddsidemargin=0pt\n\evensidemargin=0pt"
    end="\end{document}"
    A = open("test3.tex", "w")
    A.write(top+"\n"+packg+"\n"+color+"\n"+mid+"\n"+rect+"\n"+end)
    A.close()




