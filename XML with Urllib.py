import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

comments = tree.findall('.//comment')
nums = list()
for count in comments:
    num = count.find('count').text
    nums.append(int(num))

print('Count:', len(nums))
print('Sum:', sum(nums))