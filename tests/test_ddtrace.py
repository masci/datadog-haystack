from haystack import Pipeline
from haystack_integrations.components.others.datadog import DDTracerComponent


def test_init():
    DDTracerComponent("datadog_haystack.tests")


def test_pipeline():
    with open(
        "/Users/massi/dev/datadog-haystack/pipelines/chat_with_website.yaml", "r"
    ) as f:
        Pipeline.loads(f.read())
