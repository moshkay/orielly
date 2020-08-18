<h5>Endpoints</h5>
<h6>To add a book</h6>
endpoint: [Base url]/books/ method: POST

body: {
    "title":"title of book",
    "description":"description of book",
    "author":["name", "name"],
    "isbn":"122345678"
}

<h6>To retrieve all books<h6>
<b>endpoint:</b> [Base_url]/books/ method: GET

params:
page: specify page number
limit: specify number per page
query: word to filter with

<h6>retrieve a book</h6>
######endpoint: [Base url]/book/<book_id> method: GET
