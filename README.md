# Tasti - Recipe Sharing Platform

**Tasti** is a web application designed for food enthusiasts to share, explore, and comment on various recipes. Whether you're a home cook or a professional chef, Tasti offers a platform to share your unique culinary creations with others and discover new recipes from around the world.

## Features

- **Share Recipes**: Users can upload and share their own recipes, including ingredients and instructions.
- **Explore New Recipes**: Discover a wide variety of recipes uploaded by other users, categorized by cuisine, ingredients, and more.
- **Comment and Interact**: Comment on and like recipes to share your thoughts and feedback with the Tasti community.
- **User Accounts**: Sign up and create a profile to start sharing and interacting with others.

## Technologies Used

- **Flask**: A lightweight web framework for Python.
- **SQLAlchemy**: Database ORM used for managing user data and recipes.
- **Jinja2**: Templating engine for dynamic content rendering.
- **Flask-Login**: User authentication system.
- **MySQL**: Database to store user accounts, recipes, and comments.

## Installation and Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sroo9030/Tasti_portfolio_project
   cd tasti
   ```

2. **Create a virtual environment:**

```
python3 -m venv venv
source venv/bin/activate # On Windows use: venv\Scripts\activate
```

3. **Install the dependencies:**

```
pip install -r requirements.txt
```

4. **SETUP The DataBase:**

- you need to setup the database first to run the program correctly

4. **Run the application:**

```
flask run
```
