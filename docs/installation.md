# Installation Guide

## Prerequisites

Before installing DJ CRM, ensure you have the following prerequisites:

- Python 3.13+
- PostgreSQL 15+
- Node.js and npm (for frontend assets)
- Git

## Local Development Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/djcrm.git
cd djcrm
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
# Install production dependencies
pip install -r requirements.txt

# Install development dependencies (optional)
pip install -r requirements-dev.txt
```

4. Set up environment variables:
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your settings
# Make sure to update DATABASE_URL and EMAIL settings
```

5. Initialize the database:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## Docker Setup

1. Build and start the containers:
```bash
docker-compose up --build
```

2. Run migrations:
```bash
docker-compose exec web python manage.py migrate
```

3. Create a superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```

## Production Deployment

For production deployment, make sure to:

1. Set `DEBUG=False` in your environment
2. Configure proper email settings
3. Set up proper database credentials
4. Enable SSL/TLS
5. Configure proper static file serving
6. Set up proper caching

## Environment Variables

See `.env.example` for all available configuration options. Key variables include:

- `DEBUG`: Enable/disable debug mode
- `SECRET_KEY`: Django secret key
- `DATABASE_URL`: Database connection string
- `EMAIL_*`: Email configuration
- `ALLOWED_HOSTS`: List of allowed hosts

## Development Tools

- `make install`: Install production dependencies
- `make install-dev`: Install development dependencies
- `make migrate`: Run database migrations
- `make test`: Run tests
- `make lint`: Run linting tools
- `make format`: Format code
- `make clean`: Clean temporary files
