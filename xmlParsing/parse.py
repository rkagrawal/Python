import xml.etree.ElementTree as ET

mytree = ET.parse("books.xml")
myroot = mytree.getroot()
books = myroot.findall('book')
for b in books:
    d = b.attrib
    for i in b:
        print(i.tag)
