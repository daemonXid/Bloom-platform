# Bloom Platform

AI-powered learning community for university students with RAG system

## 🎯 Project Overview

A Django-based platform designed for university students featuring:
- Custom user authentication with student profiles
- AI-powered tools using Ollama
- Community features
- News feed system
- PostgreSQL database
- Redis caching

## 🚀 What We Accomplished Today (2025-10-05)

### ✅ Docker Environment Setup
1. **PostgreSQL Database** - Running in Docker container
   - Port: 5432
   - Database: `bloom_db`
   - User: `bloom`
   - All Django tables created successfully

2. **Redis Cache** - Running in Docker container
   - Port: 16379 (changed from 6379 due to Windows port restrictions)

3. **Ollama AI Server** - Running in Docker container
   - Port: 11434

4. **Django Application** - Dockerized and running
   - Port: 8000
   - Successfully running inside Docker container
   - All migrations completed

5. **pgAdmin** - Web-based PostgreSQL management tool
   - Port: 5050
   - Login: admin@bloom.com / admin123

### ✅ Key Issues Resolved
- **Windows Encoding Issue**: Encountered Korean locale encoding errors with psycopg2/psycopg3 on Windows
  - **Solution**: Moved Django entirely into Docker container, eliminating all encoding issues
- **Port Conflicts**: Windows reserved ports 6379-6380
  - **Solution**: Moved Redis to port 16379
- **Database Connection**: Python libraries couldn't connect from Windows host
  - **Solution**: Docker networking with service names (postgres, redis, ollama)

### ✅ Files Created/Modified
- `Dockerfile` - Django application container
- `docker-compose.yml` - Multi-container orchestration (Django, PostgreSQL, Redis, Ollama, pgAdmin)
- `accounts/migrations/0001_initial.py` - User model migrations
- `config/settings.py` - Updated to use Docker service names
- `.env` - Environment variables (not committed to git)

## 📋 Current Setup

### Running Services
```bash
docker ps
```

You should see:
- `bloom_web` - Django (port 8000)
- `bloom_postgres` - PostgreSQL (port 5432)
- `bloom_redis` - Redis (port 16379)
- `bloom_ollama` - Ollama AI (port 11434)
- `bloom_pgadmin` - pgAdmin (port 5050)

### Access Points
- **Django App**: http://localhost:8000
- **Django Admin**: http://localhost:8000/admin
- **pgAdmin**: http://localhost:5050

## 🛠️ Common Commands

### Start All Services
```bash
docker-compose up -d
```

### Stop All Services
```bash
docker-compose down
```

### View Django Logs
```bash
docker logs bloom_web -f
```

### Run Django Management Commands
```bash
# Create superuser
docker exec -it bloom_web python manage.py createsuperuser

# Make migrations
docker exec bloom_web python manage.py makemigrations

# Apply migrations
docker exec bloom_web python manage.py migrate

# Django shell
docker exec -it bloom_web python manage.py shell

# Collect static files
docker exec bloom_web python manage.py collectstatic
```

### Database Access
```bash
# Access PostgreSQL via psql
docker exec -it bloom_postgres psql -U bloom -d bloom_db

# View tables
docker exec bloom_postgres psql -U bloom -d bloom_db -c "\dt"
```

### Rebuild After Code Changes
```bash
# Rebuild Django container
docker-compose build web

# Restart with new build
docker-compose up -d web
```

## 🗄️ Database Management

### Option 1: pgAdmin (Recommended - Web UI)
1. Open http://localhost:5050
2. Login: `admin@bloom.com` / `admin123`
3. Register new server:
   - Name: `Bloom Database`
   - Host: `postgres` (important: use service name, not localhost)
   - Port: `5432`
   - Database: `bloom_db`
   - Username: `bloom`
   - Password: `bloom123`

### Option 2: VS Code PostgreSQL Extension
- **Status**: Has encoding issues on Windows
- **Alternative**: Use pgAdmin instead

### Option 3: Command Line
```bash
docker exec -it bloom_postgres psql -U bloom -d bloom_db
```

Common psql commands:
- `\l` - List databases
- `\dt` - List tables
- `\d table_name` - Describe table
- `\q` - Quit

## 📁 Project Structure

```
Bloom-platform/
├── accounts/          # Custom user authentication
├── ai_tools/          # AI-powered tools
├── community/         # Community features
├── config/            # Django settings
├── news_feed/         # News feed functionality
├── staticfiles/       # Collected static files
├── media/             # User-uploaded files
├── Dockerfile         # Django container definition
├── docker-compose.yml # Multi-container setup
├── manage.py          # Django management script
├── pyproject.toml     # Python dependencies (uv)
└── .env              # Environment variables
```

## 🔐 Environment Variables

Located in `.env` file:
```env
DEBUG=True
SECRET_KEY=django-insecure-change-this-in-production-12345

# Database (Docker service name)
DATABASE_URL=postgresql://bloom:bloom123@postgres:5432/bloom_db

# Redis (Docker service name)
REDIS_URL=redis://redis:16379/0

# Ollama (Docker service name)
OLLAMA_BASE_URL=http://ollama:11434
OLLAMA_MODEL=llama3.2:3b

# ChromaDB
CHROMA_DB_PATH=./chroma_db
```

## 👤 Custom User Model

Located in `accounts/models.py`

**Fields:**
- `email` - Login identifier (instead of username)
- `name` - Full name
- `university` - University name
- `department` - Department/major
- `student_id` - Student ID number
- `grade` - Year/grade level
- `bio` - Profile bio
- `avatar` - Profile picture

**Create Superuser:**
```bash
docker exec -it bloom_web python manage.py createsuperuser
```

**Change Password:**
```bash
# Method 1: Django shell
docker exec bloom_web python manage.py shell
>>> from accounts.models import User
>>> user = User.objects.get(email='your@email.com')
>>> user.set_password('newpassword')
>>> user.save()
>>> exit()

# Method 2: Via admin panel
# Go to http://localhost:8000/admin and click "Change Password"
```

## 📦 Dependencies

Managed with `uv` (faster than pip):

**Main Dependencies:**
- Django 5.2.7
- djangorestframework
- psycopg[binary] - PostgreSQL adapter
- dj-database-url
- python-decouple
- django-cors-headers
- Pillow (image handling)

**Dev Dependencies:**
- pytest
- pytest-django
- ruff (linter)
- pre-commit

## 🔄 Next Steps

### Immediate Tasks
1. **View Database with pgAdmin**
   - Access http://localhost:5050
   - Connect to PostgreSQL server
   - Explore tables and data

2. **Create Admin User**
   - Run `docker exec -it bloom_web python manage.py createsuperuser`
   - Login to http://localhost:8000/admin

3. **Test Django Application**
   - Visit http://localhost:8000
   - Test admin panel
   - Create test users

### Development Tasks
1. **Implement Community Features**
   - Create views for community app
   - Add URL patterns
   - Design templates

2. **Implement AI Tools**
   - Connect to Ollama
   - Implement RAG system with ChromaDB
   - Create AI-powered learning features

3. **News Feed Implementation**
   - Design news feed models
   - Create feed views
   - Implement real-time updates

4. **Frontend Development**
   - Create templates
   - Add CSS/JavaScript
   - Implement responsive design

5. **API Development**
   - Design REST API endpoints
   - Add authentication (JWT/Token)
   - Document API with Swagger/OpenAPI

### Production Preparation
1. **Security**
   - Change SECRET_KEY
   - Set DEBUG=False
   - Configure ALLOWED_HOSTS
   - Set up HTTPS

2. **Performance**
   - Configure Redis caching strategy
   - Optimize database queries
   - Set up CDN for static files

3. **Deployment**
   - Choose hosting platform (AWS, DigitalOcean, etc.)
   - Set up CI/CD pipeline
   - Configure production database backups

## 🐛 Known Issues

1. **PostgreSQL VS Code Extension**: Cannot connect due to Windows Korean locale encoding issue
   - **Workaround**: Use pgAdmin web interface instead

2. **Windows Port Restrictions**: Ports 6379-6380 are reserved
   - **Solution**: Redis runs on port 16379

## 📚 Resources

- Django Documentation: https://docs.djangoproject.com/
- Docker Documentation: https://docs.docker.com/
- Ollama Documentation: https://ollama.ai/
- pgAdmin Documentation: https://www.pgadmin.org/docs/

## 🤝 Contributing

This is a student learning project. Feel free to experiment and learn!

## 📝 License

MIT License

---

**Last Updated**: 2025-10-05
**Status**: ✅ Development Environment Ready


----

 Perfect! I've created a comprehensive README that documents:

  ✅ What's Documented:

  1. What We Accomplished Today
    - All Docker services setup
    - Issues we encountered and solutions
    - Files created/modified
  2. Current Setup
    - All running services and ports
    - Access points for each service
  3. Common Commands
    - How to start/stop services
    - Django management commands
    - Database access methods
  4. Database Management
    - pgAdmin setup instructions
    - VS Code extension issue note
    - Command-line access
  5. Next Steps
    - Immediate tasks (view database, create admin user)
    - Development tasks (implement features)
    - Production preparation
  6. Known Issues
    - Windows encoding issue with VS Code extension
    - Port conflicts and solutions

  Everything is documented so when you come back, you can easily:
  - See what we did today
  - Know how to start/stop services
  - Access pgAdmin at http://localhost:5050


- mcp connect
- function calling
- github actions and renderh to deploy