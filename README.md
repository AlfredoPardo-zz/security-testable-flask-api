# Security-testable Flask API

## Switching to an Scalable Model

Following the scalable [example](https://flask-restplus.readthedocs.io/en/stable/scaling.html) of flask-restplus, and using the [previous base](https://github.com/AlfredoPardo/security-testable-flask-api-pv/tree/01-Flask-Restplus-example) I created a small API with customers, cloud_providers, and cloud_accounts.

1. Assuming you're using linux and python 3, create a virtual environment:

> $ python3 -m venv venv

2. Activate the virtual environment

> $ source venv/bin/activate

3. Install the requirements

> $ pip install -r requirements.txt

4. Run the app

> $ python app.py

This is now available at: http://127.0.0.1:5000/