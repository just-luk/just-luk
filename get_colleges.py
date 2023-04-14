from bs4 import BeautifulSoup
import requests, zipfile, io
with open('IPEDS Data Center.html', 'r') as r:
    raw_html = r.read()

def get_zip(path):
    url = 'https://nces.ed.gov/ipeds/datacenter/' + path
    zip_data = requests.get(url).content
    z = zipfile.ZipFile(io.BytesIO(zip_data))
    z.extractall('data')
    print(f'saved {path}')

soup = BeautifulSoup(raw_html, 'html.parser')
rows = soup.findAll("tr", {"class": "idc_gridviewrow"})
for row in rows:
    cols = row.findAll("td")
    get_zip(cols[3].a["href"])
    get_zip(cols[-1].a["href"])
    