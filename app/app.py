import json
import flask
import numpy as np
import emod


app = flask.Flask(__name__)

cohort_sizes = np.random.uniform(10, 100, size=10)
cohorts = [emod.Cohort(int(s)) for s in cohort_sizes]

@app.route("/")
def index():
    """
    When you request the root path, you'll get the index.html template.
    """
    return flask.render_template("index.html")


@app.route("/data")
@app.route("/data/<int:ndata>")
def data(ndata=100):
    """
    On request, this returns a list of ``ndata`` randomly made data points.
    :param ndata: (optional)
        The number of data points to return.
    :returns data:
        A JSON string of ``ndata`` data points.
    """

    print(cohorts)
    return json.dumps([{"_id": i, "x": np.random.rand(), "y": i, "area": c.count}
        for i, c in enumerate(cohorts)])


if __name__ == "__main__":
    import os

    port = 8000

    # Open a web browser pointing at the app.
    os.system("open http://localhost:{0}".format(port))

    # Set up the development server on port 8000.
    app.debug = True
    app.run(port=port)
