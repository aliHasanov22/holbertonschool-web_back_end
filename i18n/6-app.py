#!/usr/bin/env python3
"""Flask app with user locale preference."""
from flask import Flask, g, render_template, request
from flask_babel import Babel


class Config:
    """Application configuration."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()


def get_user():
    """Return the user indicated by the login_as URL parameter."""
    login_as = request.args.get("login_as", type=int)
    return users.get(login_as)


def get_locale():
    """Return the locale from the request, user, or headers."""
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale

    user = getattr(g, "user", None)
    if user and user.get("locale") in app.config["LANGUAGES"]:
        return user["locale"]

    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.before_request
def before_request():
    """Store the current user on flask.g before each request."""
    g.user = get_user()


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    """Render the home page."""
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
