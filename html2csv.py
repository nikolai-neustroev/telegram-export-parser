import glob
import csv
from bs4 import BeautifulSoup

files = glob.glob('messages*.html')
data = [["name", "created", "text"]]

for i in files:
    with open(i, "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        bodies = soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['body'])
        for body in bodies:
            try:
                name = body.find(attrs={"class": "from_name"}).get_text()
                dt_info = body.find(attrs={"class": "pull_right date details"})['title']
                txt = body.find(attrs={"class": "text"}).get_text()
                row = [name[1:-8], dt_info, txt[1:-8]]
                data.append(row)
            except AttributeError:
                pass

with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
