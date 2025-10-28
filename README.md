# Fitness Tracker API

A **Django REST Framework (DRF)** based backend API that allows users to manage and track their fitness activities — including logging workouts, viewing summaries, and managing user profiles.

---

## Features

### User Management
- Register new users  
- Login and obtain authentication tokens (JWT)  
- Manage user profiles (gender, height, weight, fitness level)

### Activity Tracking
- CRUD operations for activities (Create, Read, Update, Delete)
- Activity fields: type, duration, distance, calories burned, date, etc.
- Users can only manage their own activities
- Admin users can view all activities

### Analytics & Metrics
- View total distance, duration, and calories burned
- Filter by date range or activity type
- Sort, search, and paginate activity results

---

## Tech Stack

| Category | Technology |
|-----------|-------------|
| Framework | Django 5.x, Django REST Framework |
| Database | SQLite (default) / PostgreSQL (for production) |
| Authentication | JWT (via `djangorestframework-simplejwt`) |
| Filtering & Pagination | DRF filters + DjangoFilterBackend |

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Tech-it-with-Billy/Fitness_Tracker_API.git
cd fitness-tracker-api
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # on macOS/Linux
venv\Scripts\activate      # on Windows
```

### 3. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Run the Server
```bash
python manage.py runserver
```
---

## Authentication

The API uses JWT token authentication.

- Register a user:
POST /api/users/register/

- Login to obtain tokens:
POST /api/users/login/

- Use the token in headers:
Authorization: Bearer <access_token>
---

## API Endpoints
### User Endpoints
| Method    | Endpoint                   | Description                 |
| --------- | -------------------------- | --------------------------- |
| POST      | `/api/users/register/`     | Register new user           |
| POST      | `/api/users/login/`        | Obtain JWT tokens           |
| GET       | `/api/users/profile/`      | View logged-in user profile |
| PUT/PATCH | `/api/users/profile/{id}/` | Update profile              |
| POST      | `/api/users/logout/`       | Logout user                 |

### Activity Endpoints
| Method    | Endpoint                   | Description                                         |
| --------- | -------------------------- | --------------------------------------------------- |
| GET       | `/api/activities/`         | View user’s activities                              |
| POST      | `/api/activities/`         | Create new activity                                 |
| GET       | `/api/activities/{id}/`    | View a single activity                              |
| PUT/PATCH | `/api/activities/{id}/`    | Update activity                                     |
| DELETE    | `/api/activities/{id}/`    | Delete activity                                     |
| GET       | `/api/activities/summary/` | Get activity summary (distance, calories, duration) |

### Filters, Sorting & Pagination
| Feature                 | Example                                        |
| ----------------------- | ---------------------------------------------- |
| Filter by activity type | `/api/activities/?activity_type=Running`       |
| Filter by date          | `/api/activities/?date=2025-10-26`             |
| Sort by calories        | `/api/activities/?ordering=-calories_burned`   |
| Search                  | `/api/activities/?search=Running`              |
| Pagination              | Automatically enabled (10 per page by default) |
---

## Testing
Unit tests are included for both the User and Activity apps.
Run tests with:
```bash
python manage.py test
```

## API Testing (Postman)

You can test the API using:
- Postman VSCode Extension, or
- Postman Desktop App
Make sure to:
- Log in to get your JWT token.
- Add it to the Authorization header for protected requests.

### Example Requests (Postman)
#### Register a User
```bash
POST /api/users/register/
{
    "username": "newuser03",
    "email": "newuser03@fitness.com",
    "password": "NewUserPassword03"
}
```
#### Login User
```bash
POST /api/users/login/
{
    "username": "newuser001",
    "password": "NewUserPassword001"
}
```
#### View Current User Profile
```bash
GET /api/user/account/
Authorization: Bearer <access_token>
```
#### Create Activity
```bash
POST /api/activity/
Authorization: Bearer <access_token>
{ 
  "activity_type": "Running",
  "duration": "00:45:00",
  "distance": 5.2,
  "start_time": "2025-10-28T07:00:00Z",
  "end_time": "2025-10-28T07:45:00Z",
  "calories_burned": 450
}
```
#### Get All Activities
```bash
GET /api/activity/
Authorization: Bearer <access_token>
```
---

## Author
Billy Ochieng
Data Scientist & Software Engineer