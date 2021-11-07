# Dear Diary

## Description: Your personal Diary.
It is a web based app that makes it easy for you to keep your secrets.

## Installation
- You need to have flask installed on your local machine.
- Download the zip.
- Go into this project's directory and run `flask run`.
- Your application will run.
- To install flask on your machine, [click here](https://phoenixnap.com/kb/install-flask).


So here's a decription for my code:
1.  application.py
In appliaction.py I have first included all the files required for it
mainly cs50, flask, and session. Then I have configured the application
and autoreloaded the templates. To ensure the responses that server receive
aren't cached I have included  the app route for that. Configured session to use
filesystem instead of using signed cookies. Then linked my SQL database file.
To store date and time, made a variable using the library.
The first route is for index page wherein the necessary condition is that you need to
login. then index.html is loaded. The next route is for login wherein all the
session that is stored is cleared then you can type your username and passwords(which will be stored as hash in database)
to login to your account. If any error occurs that will be redirected to apology page via apology function in helper.py(for this I have refered it from finance problem in CS50).
In logout route simply the session that is stored when you login is cleared.
If you're new to this website you can register for a account by creating a username
and password, it checks for your username that it shouldn't be present in database and you passwords labels should match.
Then the route for new is defined if you logged in your account you can create a new writeup for
your diary by simply clicking on new button in your webpage. Whaterver you type in subject and content that is stored.
Then the route for content is defined it will load its html page.
At last to handle errors some routes are defined (took references from CS50 finance problem).


2. static
In static only the elements for style are defined which are used to create webpages somewhat pretty!

3. templates
It has 7 html files. first is apology wherein the content for apology is defined to give you user-friendly errors.
Second is content.html it provides you the content of your writeup.
Third is index.html, it gives you the index page of your webpage. Fourth is layout.html which helps you to remove
redundancy in your html pages. Fivth is login.html, it helps you to provide the lookup of your login page.
Sixth is new.html it helps you to create new writeups for your diary. And last is register.html
which helps you to register in your diary.

4. data.db
It keeps track of your data.
It has two table user_info to keep track of your login information and second to contain your wrtieups.

5. helpers.py
It contains some of the functions that help in application.py like apology to generate user_friendly erros.

6. README.md
That's what it is!

7. requirements.txt
This text file contains all the libraries that you would need to run this application.

Conclusion
You can simply copy these your files in your text-editor by use it.
:).# Dear-Diary
