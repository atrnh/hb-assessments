"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

# A BaseQuery object.



# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

# An association table helps to bind a many-to-many relationship between other
# tables. Otherwise, it does not contain meaningful information.




# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the brand_id of ``ram``.
q1 = Brand.query.filter_by(brand_id='ram').one()

# Get all models with the name ``Corvette`` and the brand_id ``che``.
q2 = Model.query.filter_by(name='Corvette', brand_id='che').all()

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with ``Cor``.
q5 = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter(Brand.founded == 1903 and
                        Brand.discontinued is None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter(Brand.discontinued is not None or
                        Brand.founded < 1950).all()

# Get all models whose brand_id is not ``for``.
q8 = Model.query.filter(Model.brand_id != 'for').all()



# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    models = Model.query.options(db.joinedload('brand')).filter_by(
        year=year).all()

    if models:
        print '\nModels from the year {}:\n'.format(year)

        for model in models:
            print ('Model Name: {model_name}\n' +
                   'Brand: {brand_name}\n' +
                   'Brand HQ: {brand_hq}\n'
                   ).format(model_name=model.name,
                            brand_name=model.brand.name,
                            brand_hq=model.brand.headquarters,
                            )
    else:
        print '\nThere were no models created that year.'


def get_brands_summary():
    """Prints out each brand name (once) and all of that brand's models,
    including their year, using only ONE database query."""

    brands_with_models = Brand.query.options(db.joinedload('models')).all()

    # Here's the first way I did it:

    # for brand in brands_with_models:
    #     print '\n{}:'.format(brand.name.upper())
    #
    #     for model in brand.models:
    #         print ('\tModel: {model_name}\n' +
    #                '\tYear: {model_year}\n'
    #                ).format(model_name=model.name, model_year=model.year)

    # Here's an interesting way of doing it:

    # # A dictionary of all brands' summaries.
    # # Key is brand name and value is a list of strings that represent the name
    # # and year for each model of that brand.
    # models_by_brand = {brand.name:
    #                    [('\tModel: {model_name}\n' +
    #                      '\tYear: {model_year}\n'
    #                      ).format(model_name=model.name, model_year=model.year)
    #                     for model in brand.models]
    #                    for brand in brands_with_models}
    #
    # for brand_name, model_info in sorted(models_by_brand.items()):
    #     print '\n{}:'.format(brand_name.upper())
    #     print '\n'.join(model_info)

    # Here's a more readable way of doing the same thing (see above):
    def make_summaries(dictionary, brand):
        """Make a dictionary of all brands' summaries.

        For use with reduce()
        Key is brand name and value is a string of all models' names and years,
        delimited by a new line.
        """

        # Each item is an individual model's name and year as a string
        # Each string looks like this:
        #   Model: Mini Cooper
        #   Year: 1959
        model_info = [('\tModel: {model_name}\n' +
                       '\tYear: {model_year}\n'
                       ).format(model_name=model.name,
                                model_year=model.year)
                      for model in brand.models]
        summary = '\n'.join(model_info)  # Make the summary pretty

        dictionary[brand.name] = summary

        return dictionary

    models_by_brand = reduce(make_summaries, brands_with_models, {})

    for brand_name, summary in sorted(models_by_brand.items()):
        print '\n{}'.format(brand_name.upper())
        print summary


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    return Brand.query.filter(Brand.name.like('%' + mystr + '%')).all()


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    return Model.query.filter(Model.year >= start_year, Model.year < end_year).all()
