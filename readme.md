
To start the app:
$ gunicorn wsgi:app -k gevent -w 2
-w 2 signifies the number of workers

Then you can send the POST requests.
To test how long it will take to process a 100 POST requests start the script:
$ python time_requests.py

