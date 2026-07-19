#!/usr/bin/env python
"""
Database Initialization Script (with SQLite fallback for testing)
For production, use PostgreSQL with Docker

Role: Database Team - Schema Setup
"""

import os
from app import create_app, db


def init_db():
    """Initialize database with all tables"""

    # Try with the configured database first
    app = create_app()

    with app.app_context():
        print(f"🔧 Creating database tables...")
        db_uri = app.config.get('SQLALCHEMY_DATABASE_URI', 'Unknown')
        print(f"   Attempting: {db_uri}")

        try:
            # Create all tables defined in models
            db.create_all()

            print("✅ Database initialized successfully!")
            print("   - users table created")
            print("\n📝 Configuration:")

            if 'sqlite' in str(db_uri).lower():
                print("   ⚠️  Using SQLite (development/testing only)")
                print("   - For PostgreSQL production:")
                print("     1. Install & start Docker")
                print("     2. Run: docker-compose up -d")
                print("     3. Verify .env has DATABASE_URL set")
                print("     4. Run: python init_db.py")
            else:
                print("   ✅ Using PostgreSQL (production)")
                print("   - Auth team: implement password hashing")
                print("   - Backend team: create user routes")

        except Exception as e:
            print(f"❌ Error: {e}")

            # Try fallback to SQLite
            print("\n⚠️  PostgreSQL connection failed. Trying SQLite fallback...")
            os.environ['DATABASE_URL'] = ''

            try:
                from importlib import reload
                import config
                reload(config)

                app2 = create_app()
                with app2.app_context():
                    print("   Attempting: sqlite:///test.db")
                    db.create_all()
                    print("✅ Database initialized with SQLite!")
                    print("   - users table created")
                    print("   - Use PostgreSQL in production")

            except Exception as e2:
                print(f"❌ SQLite fallback also failed: {e2}")
                print("\n🔧 Manual Setup:")
                print("   1. Check schema.sql file")
                print("   2. Run SQL directly in your database")


if __name__ == '__main__':
    init_db()
