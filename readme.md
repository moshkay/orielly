<h1>Endpoints</h1>
####To add a book
######endpoint: [Base url]/books/ method: POST

body: {
    "title":"title of book",
    "description":"description of book",
    "author":["name", "name"],
    "isbn":"122345678"
}

####To retrieve all books
######endpoint: [Base_url]/books/ method: GET
params:
page: specify page number
limit: specify number per page
query: word to filter with

####retrieve a book
######endpoint: [Base url]/book/<book_id> method: GET
