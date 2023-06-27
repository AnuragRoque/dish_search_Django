# Dish Search Application

The Dish Search Application is a Django-based web application that allows users to search for dishes and get recommendations based on their names.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your/repo.git

2. Navigate to the project directory:
   ```shell
   cd dish-search-app
   
4. Install the required dependencies:
   ```shell
   pip install -r requirements.txt

6. Install the required dependencies:
   ```shell
   pip install Django

## Usage
1. Start the Django development server:
   ```shell
   python manage.py runserver

  Access the application in your web browser at http://localhost:8000/.

  Use the search form to enter a dish name and click the "Search" button to get recommendations.
  
  The search results will be displayed, showing the matching dish names.

## Technologies Used

  Django: Python web framework for building the application.
  SQLite: File-based database for storing and retrieving dish data.

## File Structure


      dish-search-app/
    ├── db.sqlite3
    ├── manage.py
    ├── dish_search/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── dish_search_app/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── restaurants_small.csv
    └── README.md
