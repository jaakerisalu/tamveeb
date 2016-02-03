#bind = "0.0.0.0:8000"
bind = "unix:/tmp/gunicorn_tamveeb.sock"

workers = 2
proc_name = "tamveeb"
#loglevel = 'debug'
