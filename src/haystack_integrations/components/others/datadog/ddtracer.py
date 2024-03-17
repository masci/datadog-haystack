from haystack import component
from haystack.tracing.datadog import DatadogTracer
import haystack.tracing
import ddtrace


@component
class DDTracerComponent:
    def __init__(self, service: str):
        tracer = ddtrace.tracer
        ddtrace.config.service = service
        haystack.tracing.enable_tracing(DatadogTracer(tracer))
        haystack.tracing.tracer.is_content_tracing_enabled = True

        self.service = service

    @component.output_types(service=str)
    def run(self):
        return {"service": self.service}
