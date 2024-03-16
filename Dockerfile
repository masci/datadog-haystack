FROM deepset/hayhooks:main

COPY . /opt/datadog-haystack

RUN /opt/venv/bin/python -m pip install /opt/datadog-haystack
