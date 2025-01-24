import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"../src")))

from tutor_ai.model_handler import LocalLLM

def test_model_handler_generate():
    """Test the generate function of LocalLLM with a simple prompt."""
    llm = LocalLLM()
    prompt = "Hello, how are you?"
    
    try:
        response = llm.generate(prompt)
        print(response)
        # Since the output is streamed, we verify it is iterable
        assert hasattr(response, "__iter__")
    except Exception as e:
        assert False, f"LLM generate failed: {str(e)}"
