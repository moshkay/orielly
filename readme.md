##Endpoints
###To add a book
**endpoint:** [Base url]/books/ method: POST

`body: {
    "title":"title of book",
    "description":"description of book",
    "author":["name", "name"],
    "isbn":"122345678"
}`

###To retrieve all books
**endpoint:** [Base_url]/books/ method: GET

params:
page: specify page number
limit: specify number per page
query: word to filter with

###retrieve a book
**endpoint**: [Base url]/book/<book_id> method: GET


<h1>Documentation</h1>
**Programming language used**
---
This problem was created using Django Rest Framework and sqlite as the database.

(Django Rest framework): which is an MVC(Models-Views-Controller) framework.

The models is the schema/structure of the database. oreilly_api/models.py contains the model for this project where each class signifies
a table. which means we only have two tables for this project namely **Book** and the **AbstractModel**.
The abstractmodel tracks the datetime of every record on the book table while the book table stores all books.


Data was pulled from the oreilly search api, with help of the **requests** library, which is used for making HTTP requests.
The python script that was used in pulling from the api is **get_books.py**

The **urls.py** is responsible for the route of the api. it contains the endpoints of the project.
The **views.py** is the views that processes the request and returns a response back to the front end
The **serializers.py** is serializes the responses of the views to give a json response.

##Tests
`Method: GET url: 127.0.0.1:5001/books/?limit=1&page=1&query=Toba

{
    "Data": [
        {
            "id": 404,
            "date_created": "2020-08-18T08:34:16.766235Z",
            "date_updated": "2020-08-18T08:34:16.766326Z",
            "title": "Toba book",
            "isbn": "",
            "description": "",
            "author": "['oyen']"
        }
    ],
    "Total": 204,
    "previous_page": "",
    "next_page": 2,
    "total_pages": 204,
    "current_page": 1
}`

`Method: GET url: 127.0.0.1:5001/book/1

{
    "data": {
        "id": 206,
        "date_created": "2020-08-18T04:26:47.391774Z",
        "date_updated": "2020-08-18T04:26:47.391866Z",
        "title": "Automate the Boring Stuff with Python, 2nd Edition",
        "isbn": "9781593279929",
        "description": "<span><div><p>If you’ve ever spent hours renaming files or updating hundreds of spreadsheet cells, you know how tedious tasks like these can be. But what if you could have your computer do them for you?</p><p>In this fully revised second edition of the best-selling classic <i>Automate the Boring Stuff with Python</i>, you’ll learn how to use Python to write programs that do in minutes what would take you hours to do by hand—no prior programming experience required. You’ll learn the basics Python and explore Python’s rich library of modules for performing specific tasks, like scraping data off websites, reading PDF and Word documents, and automating clicking and typing tasks.</p><p>The second edition of this international fan favorite includes a brand-new chapter on input validation, as well as tutorials on automating Gmail and Google Sheets, plus tips on automatically updating CSV files. You’ll learn how to create programs that effortlessly perform useful feats of automation to:</p><p>•Search for text in a file or across multiple files<br/><br/>•Create, update, move, and rename files and folders<br/><br/>•Search the Web and download online content<br/><br/>•Update and format data in Excel spreadsheets of any size<br/><br/>•Split, merge, watermark, and encrypt PDFs<br/><br/>•Send email responses and text notifications<br/><br/>•Fill out online forms</p><p>Step-by-step instructions walk you through each program, and updated practice projects at the end of each chapter challenge you to improve those programs and use your newfound skills to automate similar tasks.</p><p>Don't spend your time doing work a well-trained monkey could do. Even if you've never written a line of code, you can make your computer do the grunt work. Learn how in <i>Automate the Boring Stuff with Python, 2nd Edition</i>.</p><p/></div></span>",
        "author": "[\"Al Sweigart\"]"
    },
    "status": 200
}`

`Method: POST url: 127.0.0.1:5001/books/

{
    "title":"Toba book",
    "isbn":"123456u",
    "description":"The forst book",
    "author":["oyen"]
}
`




