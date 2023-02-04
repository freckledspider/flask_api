## const express = require("express")
import flask

## Create flask all
app = flask.Flask(__name__)

## Run server
## app.listen (PORT, ...)
app.run(port=4000)