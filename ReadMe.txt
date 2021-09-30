Ademir Vila
2299217
5/21/2021
CPSC408

The final assignment for CPSC408 included gathering a bunch of revelant data and creating a database with a front-end application. For my project, I decided to focus of COIVD vaccination stats in the sense of allocations to each state and comparing that to various other stats such as confirmed cases or total deaths. To run the application, main.py is the python application that runs the frontend and finalproject.sql is the database file the data connects to and is stored in (5 tables are created in the datatgrip). On initial start, lines 14-126 creates the table and inserts the data into the database 'vaccinations.' Once data is loaded, lines 14-126 must be commented out or the 5 tables must be dropped or else there will be an error 'Table ____ already exists' if the application is run multiple times, as the data will be saved from a previous visit.

Files included:
main.py
final project.sql (setting in datagrip should be set to mysql)
5 csv files of state data (US Gen, US COVID, Pfizer/moderna//janssen)
408 Final WriteUp

References:
Class Videos
Lectures
Rao Ali
Sources on the internet (commented in code)
