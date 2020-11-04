Pytest Workshop
===============

## Setup

Install dependencies by running

```
pipenv install
```

Enter a virtual environment with

```
pipenv shell
```

## Exercises

### 01-unittest

The tests here have been written with `unittest`: python's test framework available in the standard library.

Run the tests with

```
python -m unittest -k 01
```

This runs the `unittest` module on tests with `01` in its path.

Examine the output from the tests.

Let's make one of the assertions fail. How does `unittest` present the failure?

Now run the same tests with pytest

```
pytest -k 01
```

What differences do you see in the output? Try making the tests fail in different ways and compare how errors are reported for different data structures.

Create a new file and convert the tests to use `assert`.

### 02-fixtures

We have the same set of tests as in the first exercise, with the additions of `setUp` and `tearDown` methods.

Run the tests with pytest. Add the `-s` flag and rerun the tests. Any print output or logs will be displayed alongside test results.

Convert the `setUp` and `tearDown` methods in pytest fixtures.

Use the fixtures by adding them into each test's arguments.

Try using `autouse`.

### 03-sharing-fixtures

Create a new file called `conftext.py`. Move the fixtures into that file.

Run pytest.

### 04-scopes

Try setting different scopes on the fixtures. The default scope is `function`. Choose from

* `function`
* `class`
* `module`
* `package`
* `session`

What do you notice in the test output? (Be sure to run pytest with the `-s` flag)

### 05-marks

There are two useful marks: `parametrize` and `usefixtures`. Give them a try.

Can you think of examples where these might be useful?
