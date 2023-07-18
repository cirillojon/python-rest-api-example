# Flask Drink API

This is a simple Flask API built with Flask-SQLAlchemy to manage a list of drinks. It supports basic CRUD operations such as creating, reading, updating, and deleting drinks.

## Setup

1. Clone the repository.
2. Install required packages. The application requires Flask and Flask-SQLAlchemy. Install these packages using pip:

    ```
    pip install flask flask_sqlalchemy
    ```

3. Run the application:

    ```
    python app.py
    ```

The application runs on http://localhost:5000/.

## API Endpoints

1. **GET /** - Test endpoint to check if the API is running. Returns the message "Hello".
2. **GET /drinks** - Returns a list of all drinks.
3. **GET /drinks/<id>** - Returns the details of a specific drink by its id. If a drink with the specified id is not found, a 404 error is returned.
4. **POST /drinks** - Adds a new drink to the list. Requires a JSON body with 'name' and 'description' parameters. If a drink with the same name already exists, an error message is returned.
5. **DELETE /drinks/<id>** - Deletes a specific drink by its id. Returns a success message if the drink is deleted, and an error message if a drink with the specified id is not found.

## Database

The application uses an SQLite database to store drink data. The database name is "database.db". 

Each drink has an `id` (integer), `name` (string, unique, not null), and `description` (string). The `id` is the primary key.

## Model

The `Drink` model is defined as:

```python
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"
