from celery import shared_task

@shared_task
def add_book_to_library(book_title):
    print(f"'{book_title}' is added to the library.")