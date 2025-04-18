# Note-Taking App Backend

This is the backend of a **Note-Taking Application** built with Django and Django REST Framework (DRF). It provides a RESTful API for managing notes and tags, supporting all CRUD operations and tagging functionality.

---

## Features

- **CRUD Operations**: Easily create, read, update, and delete notes.
- **Tagging System**: Add tags to notes for enhanced organization.
- **Environment-Specific Configuration**: Uses SQLite for development and PostgreSQL for production environments.
- **Pagination**: Efficiently handles large datasets with paginated API responses.
- **RESTful API**: Built with Django REST Framework for seamless integration with frontend applications.
- **Security**: Implements CSRF protection, secure handling of sensitive data, and environment-based security settings.

---

## Technologies Used

- **Backend Framework**: Django
- **API Framework**: Django REST Framework (DRF)
- **Database**: SQLite (Development), PostgreSQL (Production)
- **Tagging**: Django-Taggit
- **Environment Management**: Python `dotenv`

---

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- `pip` (Python package manager)
- PostgreSQL (for production environment)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd note_taking_app_backend
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:

   - Create `.env.development` for local development:
     ```ini
     DJANGO_ENV=development
     DEBUG=True
     DJANGO_SECRET_KEY=your_development_secret_key
     ALLOWED_HOSTS=localhost,127.0.0.1
     CSRF_TRUSTED_ORIGINS=http://localhost,http://127.0.0.1
     ```

   - Create `.env.production` for production:
     ```ini
     DJANGO_ENV=production
     DEBUG=False
     DJANGO_SECRET_KEY=your_production_secret_key
     DATABASE_URL=postgres://<user>:<password>@<host>:<port>/<database>
     ALLOWED_HOSTS=your-production-domain.com
     CSRF_TRUSTED_ORIGINS=https://your-production-domain.com
     ```

5. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

---

## API Endpoints

### Notes Endpoints

| Method | Endpoint        | Description                      |
|--------|-----------------|----------------------------------|
| GET    | `/notes/`       | List all notes                  |
| POST   | `/notes/`       | Create a new note               |
| GET    | `/notes/<id>/`  | Retrieve a specific note        |
| PUT    | `/notes/<id>/`  | Update a specific note          |
| DELETE | `/notes/<id>/`  | Delete a specific note          |

### Tags Endpoints

| Method | Endpoint         | Description                      |
|--------|------------------|----------------------------------|
| GET    | `/tags/`         | List all tags                   |
| POST   | `/tags/`         | Create a new tag                |
| GET    | `/tags/<id>/`    | Retrieve a specific tag         |
| PUT    | `/tags/<id>/`    | Update a specific tag           |
| DELETE | `/tags/<id>/`    | Delete a specific tag           |

---

## Project Structure

```plaintext
note_taking_app_backend/
├── Notes/                           # Application for note-taking functionality
│   ├── migrations/                  # Database migrations
│   ├── models.py                    # Database models
│   ├── serializers.py               # API serializers
│   ├── views.py                     # API views
│   ├── urls.py                      # App-specific URLs
├── note_taking_app/                 # Project settings and configurations
│   ├── settings.py                  # Django settings
│   ├── urls.py                      # Project-wide URLs
│   ├── wsgi.py                      # WSGI configuration
├── staticfiles/                     # Static files for the app
├── templates/                       # HTML templates (if any)
├── manage.py                        # Django management script
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```

---

## Deployment

### Using Gunicorn and Nginx

1. Install Gunicorn:
   ```bash
   pip install gunicorn
   ```

2. Run Gunicorn:
   ```bash
   gunicorn note_taking_app.wsgi:application --bind 0.0.0.0:8000
   ```

3. Set up Nginx to proxy requests to Gunicorn.

### Using Render or Heroku

1. Add the necessary environment variables (e.g., `DATABASE_URL`) to your hosting platform.
2. Deploy using the provided `requirements.txt` and `Procfile`.

---

## Security Best Practices

- **Disable Debug Mode in Production**: Ensure `DEBUG=False` in production.
- **Use Strong Secret Keys**: Never use default or weak `DJANGO_SECRET_KEY`.
- **Restrict Allowed Hosts**: Only allow trusted domains in `ALLOWED_HOSTS`.
- **Use HTTPS**: Always use `https://` for production environments and configure `CSRF_TRUSTED_ORIGINS`.

---

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Commit your changes:
   ```bash
   git commit -m "Add your commit message"
   ```

4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```

5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Django**: A high-level Python Web framework.
- **Django REST Framework**: A powerful and flexible toolkit for building Web APIs.
- **Django-Taggit**: A simple tagging system for Django.

---

## Contact

For questions or support, feel free to reach out to [adeniyijohn2002@gmail.com].