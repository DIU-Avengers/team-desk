# Database Schema Documentation

**Role**: Database Team (PostgreSQL & Redis)  
**Status**: User table definition v1.0

---

## PostgreSQL User Table

### Table: `users`

**Purpose**: Store user identity, profile, and account status information.

| Column | Type | Constraints | Notes |
|--------|------|-------------|-------|
| `id` | INTEGER | PRIMARY KEY, AUTO-INCREMENT | Unique user identifier |
| `username` | VARCHAR(64) | NOT NULL, UNIQUE, INDEXED | Login identifier |
| `email` | VARCHAR(120) | NOT NULL, UNIQUE, INDEXED | Contact & recovery email |
| `first_name` | VARCHAR(64) | NULLABLE | User's first name |
| `last_name` | VARCHAR(64) | NULLABLE | User's last name |
| `password_hash` | VARCHAR(255) | NOT NULL | Hash only (auth team handles logic) |
| `is_active` | BOOLEAN | DEFAULT TRUE, INDEXED | Account status flag |
| `created_at` | DATETIME | NOT NULL, DEFAULT NOW() | Account creation timestamp |
| `updated_at` | DATETIME | NOT NULL, DEFAULT NOW() | Last update timestamp |

---

## Indexes

```sql
-- Automatically created by SQLAlchemy:
- users.id (PRIMARY KEY)
- users.username (UNIQUE)
- users.email (UNIQUE)
- users.is_active
```

---

## Redis Usage (Conceptual)

Redis will cache:
- **Session Data**: `session:{session_id}` → user info (TTL: session duration)
- **Auth Tokens**: `token:{token}` → user_id (TTL: token expiration)
- **User Cache**: `user:{user_id}` → full user object (TTL: 1 hour)

*Actual implementation is handled by Auth team (Tamzid)*

---

## Database Initialization

### 1. Create Database
```bash
createdb team_desk_db
```

### 2. Set Environment Variable
```env
DATABASE_URL=postgresql://username:password@localhost:5432/team_desk_db
```

### 3. Initialize Tables (from Flask shell)
```python
from app import create_app, db
app = create_app()
with app.app_context():
    db.create_all()
```

---



---

## Future Extensions (Do NOT implement yet)

- User roles/permissions table
- User profile extension table
- Login attempt logging
- OAuth integration table

*These will be added as requirements emerge.*
