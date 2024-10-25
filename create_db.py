from application import app, db

# Create the database and the tables
with app.app_context():
    db.create_all()
    print("Database and tables created!")
