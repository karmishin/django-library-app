A simple library website written in Django.
**Warning**: This is my first programming project. It may or may not work. 

# What it does

Retrieves data from database and shows it in beautifully formatted Bootstrap table.
Table consists of 4 columns: book, author, year and publisher.
Each author is clickable, so you can see all books written by this author (see author.html template).

# How to use it

You will need Python 3 and Django (2.0.4 used in this project).
1. Firstly, run `python3 manage.py makemigrations` and `python3 manage.py migrate`
2. Run the development server with `python3 manage.py runserver`
3. Go to `http://localhost:8000/admin/` and see if server works. If it does you will see an admin panel. There you should populate the database of our library with books.
4. Click Books, add, enter stuff in fields, then click 'Save'. Do this multiple times if you want to.
5. Head to `http://localhost:8000/library`. If everything works you will see an HTML table with books you entered in Step 4.
