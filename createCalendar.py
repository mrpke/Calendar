#!/usr/bin/python

from subprocess import call
import os.path
import functions as f

birth=raw_input('In which file can I find the birthdays? (arranged by Date tab Name)\n Type none if you don\'t want to have them included.\n >')
while not os.path.isfile(birth) and birth != 'none':
    birth=raw_input('Tell me... or type none >')


feier=raw_input('In which file can I find the days you don\'t want to work? (arranged by Date tab Name)\n Type none if you don\'t want to have them included.\n >')
while not os.path.isfile(feier) and feier != 'none':
    feier=raw_input('Tell me... or type none >')


image=raw_input('Image for the background? >')
while not os.path.isfile(image) and image != 'none':
    birth=raw_input('Tell me... or type none >')

yr=int(raw_input('Type the year! >'))
while not yr>2000:
    yr=int(raw_input('Are you trying to go back to the past? >'))

output=raw_input('Last question, I promise! What should the calendar file be named?\n>')

color=raw_input('I lied. What color do you like? (HTML notation) >')

f.composeCalendar(output, yr, birth, feier, image, "a0", color)
call(["pdflatex", output])
