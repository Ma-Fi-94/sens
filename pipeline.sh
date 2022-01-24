yapf -i sens.py
yapf -i test_sens.py
mypy sens.py
mypy test_sens.py
py.test --cov=. --cov-report term-missing  -v
