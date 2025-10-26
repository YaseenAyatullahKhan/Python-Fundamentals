#works with pythonProject2 folder

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

for i in range(7):
    if i == 0:
        url = 'http://py4e-data.dr-chuck.net/known_by_Rohma.html'
    else:
        url = link
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    count = 0
    for tag in tags:
        link = tag.get('href', None)
        content = tag.contents[0]
        count = count + 1
        if count == 18:
            break

print("Answer: ", content)