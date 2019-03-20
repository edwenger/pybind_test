A test project using pybind11 and CMake on EMOD-relevant objects.

This project is build by running: `python3 setup.py develop`

As currently configured in the make file, the `pybind11` directory (or a symlink to it) should exist at the same level as the setup and make files.

After installing the C++ extension package, you can make sure that `import emod` is possible by running the test script.

If you have installed Flask (and dependencies), `pip install Flask`, you can additionally check out the simple flask app, by navigating to `app/hello.py`, running `export FLASK_APP=hello.py`, and then `flask run`.  The localhost URL will print to the terminal screen.
