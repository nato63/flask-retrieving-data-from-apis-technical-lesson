import requests

url = "https://openlibrary.org/search.json"


def search_books(title):
    params = {"title": title}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        book_data = response.json()
        return book_data
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None


name = input("Enter the book title to search: ")
if search_books(name):
    book_data = search_books(name)
    print(f"title: {book_data['docs'][0]['title']}")
    print(f"author: {book_data['docs'][0]['author_name']}")
else:
    print("No data found for the given title.")
