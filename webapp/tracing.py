"""Optional Langfuse tracing for student workflows and Anthropic calls."""
import os
from pathlib import Path

from dotenv import load_dotenv
from langfuse import get_client, observe as langfuse_observe
from opentelemetry.instrumentation.anthropic import AnthropicInstrumentor

load_dotenv(Path(__file__).resolve().parent.parent / '.env')

langfuse = None
if (os.getenv('LANGFUSE_PUBLIC_KEY') and os.getenv('LANGFUSE_SECRET_KEY')
        and os.getenv('LANGFUSE_TRACING_ENABLED', 'true').lower() != 'false'):
    langfuse = get_client()
    AnthropicInstrumentor().instrument()


def observe(**options):
    # Missing keys or an explicit opt-out must not initialize telemetry clients.
    return langfuse_observe(**options) if langfuse else lambda function: function
