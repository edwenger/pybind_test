from flask import Flask
import emod

app = Flask(__name__)

@app.route('/')
def hello_cohort():
    c = emod.Cohort(10)
    return 'A cohort with count = %d' % c.count
