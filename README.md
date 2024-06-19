Blood Bank Application
This is a Django web application for managing a blood bank. It provides basic CRUD (Create, Read, Update, Delete) functionalities for handling donor information.
Features

List all registered donors
View details of a specific donor
Create a new donor record
Update an existing donor's information
Delete a donor record

Installation

Clone the repository:

Copygit clone https://github.com/your-username/blood-bank-app.git

Navigate to the project directory:

Copycd blood-bank-app

Create and activate a virtual environment (optional but recommended):

Copypython -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`

Install the required dependencies:

Copypip install -r requirements.txt

Run the database migrations:

Copypython manage.py migrate

Start the development server:

Copypython manage.py runserver
The application should now be running at http://localhost:8000.
Usage
The application provides the following URL paths for managing donors:

path('', views.welcome): Renders the welcome page.
path('person/show/', views.person_show, name='person_show'): Displays the details of a specific donor.
path('person/<int:pk>/delete/', views.delete_person, name='delete_person'): Deletes a donor record.
path('people/', views.person_list, name='person_list'): Lists all registered donors.
path('person/create/', views.person_create, name='person_create'): Renders a form to create a new donor record.
path('person/update/<int:pk>/', views.person_update, name='person_update'): Renders a form to update an existing donor's information.

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
License
This project is licensed under the MIT License.
