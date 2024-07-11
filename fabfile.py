#!/usr/bin/python3
from fabric import Connection
connection = Connection(host="ubuntu@35.175.132.56")
connection.run("whoami")
