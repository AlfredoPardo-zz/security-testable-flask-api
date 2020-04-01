# Security-testable Flask API

I will start from scratch using the example in the [Flask Restplus Website](https://flask-restplus.readthedocs.io/en/stable/example.html)

1. Assuming you're using linun and python 3, create a virtual environment:

> $ python3 -m venv venv

2. Activate the virtual environment

> $ source venv/bin/activate

3. Install the requirements

> $ pip install -r requirements.txt

**Note**: You should use Werkzeug==0.16.1, otherwise flask-restplus fails

4. Run the app

> $ python main.py

This starts the API in http://127.0.0.1:5000/api/1/