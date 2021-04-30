"""Models for adopt app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pet."""

    __tablename__ = "pets"

    # __table_args__ = (
    #     db.UniqueConstraint('first_name', 'last_name', 'image_url', name='unique_user'),)

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                    nullable=False)               
    species = db.Column(db.String(50),
                    nullable=False)
    photo_url = db.Column(db.String(), 
                    nullable=False, 
                    default='')
    age = db.Column(db.Text(10),
                    nullable=False)
    notes = db.Column(db.Text(50),
                    default='')  
    available = db.Column(db.Boolean,
                    nullable=False,
                    default=True) 
    
    #ask about creating uniqueness for full profile? (Add constraint)

    # posts = db.relationship('Post',backref='user')

    def __repr__(self):
        """Show info about user."""

        p = self
        return f"<Pet {p.id} {p.name} {p.species} {p.age} {p.available}>"
    


