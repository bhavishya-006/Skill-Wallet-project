import requests

def fact_check(query: str):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}"

    try:
        response = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=5
        )

        print("Status Code:", response.status_code)
        print("Response:", response.text[:300])

        if response.status_code == 200:
            data = response.json()
            return data.get("extract", "No summary available.")

        return f"Wikipedia returned status code {response.status_code}"

    except Exception as e:
        return f"Error: {e}"