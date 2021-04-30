"""Seed file to make sample data for users db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()


# Add users
vin = Pet(name="vin", species="dog",
          photo_url="https://media1.popsugar-assets.com/files/thumbor/Xqi0W8lbQkX_boK4ZNCAUsLQ6cg/220x77:2725x2582/fit-in/500x500/filters:format_auto-!!-:strip_icc-!!-/2020/06/30/762/n/1922398/abb19e095efb73c3ee1500.23266776_/i/Vin-Diesel.jpg",
          age="young")

diesal = Pet(name="Diesal", species="cat",
             photo_url="https://media.tegna-media.com/assets/WQAD/images/b9252759-f297-4959-9fc6-2da602565e83/b9252759-f297-4959-9fc6-2da602565e83_1920x1080.png",
             age="old")

# Add new objects to session, so they'll persist
db.session.add(vin)
db.session.add(diesal)

# add users to temp DB with flush so we can add some sample posts
db.session.commit()
