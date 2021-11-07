# Your personal Diary.
It is a web based app that makes it easy for you to keep your secrets.

<br>
<a href="https://youtu.be/i9e0uKmePPk">See it in action</a>
## Installation
- You need to have **flask** installed on your local machine.
- Download this zip code.
- Go into this project's directory and run `flask run`.
- You'll be able to run the application.
- To install flask on your machine, [click here](https://phoenixnap.com/kb/install-flask).

## Usage
- After running the application, you need to register (if you're new a user) to use the webapp.
- Then you can click on **New** to create a new page in your diary.
- You can start writing your diary with a subject and body.
- Clicking on **Save** button to save the writeup.
- On the index, you can see the date and subject of your writeup.

## Structure/Design of program
It is mainly written in Flask. HTML and CSS are used for layout and styling.
<br>
Main files:
<br>
* *application.py* - It is configured to render the layout pages for the webapp as per the requirement. Also, it helps to act as a mediator between database and webapp. It takes the data that the user typed and store in the database.
* *static files* - It include the required styling css page to help user to have a good experience of the webapp.
* *templates* - These include all the html pages of the webapp from a basic layout file to each and every html page of the webapp.
* *helpers.py* - It contains the functions required in application.py like apology to generate user-friendly errors.
* *requirements.txt* - It contains all the library and tools required to run this webapp.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
