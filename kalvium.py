import requests
from bs4 import BeautifulSoup

# URL of the election results page
url = "https://results.eci.gov.in/PcResultGenJune2024/index.htm"

# Headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Sending a request to the webpage
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parsing the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Function to extract data from tables
    def extract_data(soup):
        tables = soup.find_all("table")
        if not tables:
            print("No tables found")
            return []

        data = []
        for table in tables:
            rows = table.find_all("tr")
            table_data = []
            for row in rows:
                cols = row.find_all("td")
                cols = [col.text.strip() for col in cols]
                table_data.append(cols)
            data.append(table_data)

        return data

    # Function to print the extracted data
    def print_data(data):
        for table in data:
            print("Table:")
            for row in table:
                print(" | ".join(row))
            print("\n")

    # Extracting and printing the data
    data = extract_data(soup)
    if data:
        print_data(data)
    else:
        print("No data extracted")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
