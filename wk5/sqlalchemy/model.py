"""Models and database functions for cars db."""

from flask_sqlalchemy import SQLAlchemy

# Here's where we create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library. On db, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Brand(db.Model):
    """Car brand."""

    __tablename__ = 'brands'

    brand_id = db.Column(db.String(5), primary_key=True)
    name = db.Column(db.String(50))
    founded = db.Column(db.Integer, nullable=True)
    headquarters = db.Column(db.String(50), nullable=True)
    discontinued = db.Column(db.Integer, nullable=True)

    models = db.relationship('Model')

    def __repr__(self):
        """Console representation of Brand object."""

        return '<Brand brand_id={} name={}>'.format(self.brand_id, self.name)


class Model(db.Model):
    """Car model."""

    __tablename__ = 'models'

    model_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer)
    name = db.Column(db.String(50))

    brand_id = db.Column(db.String(5),
                         db.ForeignKey('brands.brand_id'),
                         )

    brand = db.relationship('Brand')

    def __repr__(self):
        """Console representation of Model object."""

        return """<Model model_id={} name={} year={}
               brand_id={}>""".format(self.model_id,
                                      self.name,
                                      self.year,
                                      self.brand_id,
                                      )

# End Part 1


##############################################################################
# Helper functions

def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app.
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print 'Connected to DB.'


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///cars'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app.
    from flask import Flask

    app = Flask(__name__)

    connect_to_db(app)
    print 'Connected to DB.'
