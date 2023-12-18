def show_description(book_id):
    with open(f'books_description/{book_id}.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    return text
