import requests

def test_health_check():
    """Test the health endpoint of the local LLM server."""
    local_url = "http://localhost:8501"
    
    try:
        response = requests.get(local_url)
        assert response.status_code == 200
        print(f"Health check successful at {local_url}")
    except requests.exceptions.RequestException as e:
        print("Health check failed : {e}")
        assert False,f"Error conencting to {local_url}"