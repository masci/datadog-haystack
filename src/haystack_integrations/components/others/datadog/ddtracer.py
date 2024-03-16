from haystack import component
from haystack.tracing.datadog import DatadogTracer
import haystack.tracing
import ddtrace


@component
class DDTracerComponent:
    def __init__(self, service: str):
        tracer = ddtrace.tracer
        tracer.service = service
        haystack.tracing.enable_tracing(DatadogTracer(tracer))

        self.service = service

    @component.output_types(dummy=str)
    def run(self):
        return {"dummy": ""}
