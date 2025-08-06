'''The Python documentation for the datetime module 
provides two attributes to retrieve the year from a date 
or datetime object: year and isocalendar.

from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]

What is the difference between the year attribute and 
the isocalendar method?'''

'''Answer:

date.year
Between MINYEAR and MAXYEAR inclusive.

The year() attribute returns the calendar year of the date.

date.isocalendar()
Return a named tuple object with 
component year.

The isocalendar() method returns a year based on the
ISO 8601 standard. The ISO year may differ from the 
calendar year for dates near the start or end of the year. '''








