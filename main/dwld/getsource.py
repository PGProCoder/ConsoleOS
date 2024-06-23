import requests
def get():
    url = "https://github.com/PrathamGhaywat/ConsoleOS/archive/refs/heads/main.zip" #github repository
    response = requests.get(url)

    try:
        response.raise_for_status()
        with open("ConsoleOS.zip", "wb") as f:
            f.write(response.content)
        print("File downloaded and saved as ConsoleOS.zip")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download file: {e}")