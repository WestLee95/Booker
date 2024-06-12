ng Started

### Prerequisites

- Python 3.x
- Node.js
- npm
- MySQL

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/booker.git
    cd booker
    ```

2. **Set up the virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install Python dependencies**:
    ```bash
    pip install django djangorestframework mysqlclient
    ```

4. **Install Tailwind CSS**:
    ```bash
    npm install -D tailwindcss
    npx tailwindcss init
    ```

5. **Configure Tailwind CSS**:
    - Edit `tailwind.config.js`:
      ```javascript
      module.exports = {
        content: [
          './templates/**/*.html',
          './static/js/**/*.js',
        ],
        theme: {
          extend: {},
        },
        plugins: [],
      }
      ```
    - Create a `static/css/tailwind.css` file:
      ```css
      @tailwind base;
      @tailwind components;
      @tailwind utilities;
      ```

6. **Build Tailwind CSS**:
    ```bash
    npx tailwindcss -i ./static/css/tailwind.css -o ./static/css/main.css --watch
    ```

7. **Configure MySQL database**:
    - Update `booker/settings.py` with your database credentials:
      ```python
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.mysql',
              'NAME': 'booker',
              'USER': 'yourusername',
              'PASSWORD': 'yourpassword',
              'HOST': 'localhost',
              'PORT': '3306',
          }
      }
      ```

8. **Run migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

9. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

10. **Start the Django development server**:
    ```bash
    python manage.py runserver
    ```

### Running the React Frontend

1. **Navigate to the frontend directory**:
    ```bash
    cd frontend
    ```

2. **Install React dependencies**:
    ```bash
    npm install
    ```

3. **Start the React development server**:
    ```bash
    npm start
    ```

### Build React for Production

1. **Build the React app**:
    ```bash
    npm run build
    ```

2. **Move the build files to Django static directory**:
    ```bash
    cp -r build/* ../static/
    ```

### Project Structure Details

- **main/models.py**: Contains the database models for students, rooms, etc.
- **main/serializers.py**: Contains the serializers for the REST API.
- **main/views.py**: Contains the viewsets for the REST API and the main view for serving the React app.
- **main/urls.py**: Contains the URL routing for the API and main view.
- **templates/**: Contains the Django templates.
- **static/**: Contains the static files including the compiled CSS from Tailwind and the React build.

### Acknowledgments

- Thanks to the Django, Tailwind CSS, and React communities for their fantastic tools and documentation.
