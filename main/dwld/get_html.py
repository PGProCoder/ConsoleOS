import requests

def get_html_code(url):
    response = requests.get(url)

    if response.status_code == 200:
        html_code = response.text
        with open("html_code.html", "w", encoding="utf-8") as f:
            f.write(html_code)
        print("HTML code saved to html_code.html")
    else:
        print("Failed to retrieve HTML code")

url = "https://www.example.com"
get_html_code(url)