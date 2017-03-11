from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route("/")
def index():
    """Returns the homepage."""

    return render_template("index.html")


@app.route("/application-form")
def application():
    """Returns application with a list of available jobs."""

    return render_template("application-response.html",
                           jobs=["Software Engineer",
                                 "QA Engineer",
                                 "Product Manager"])


@app.route("/application-success")
def application_success():
    """Displays info submitted from job application."""

    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")
    salary = float(request.args.get("salary"))
    job = request.args.get("job")

    return render_template("application-success.html",
                           first_name=first_name,
                           last_name=last_name,
                           salary=salary,
                           job=job)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
