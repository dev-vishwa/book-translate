import zipfile
import os
import glob
from bs4 import BeautifulSoup
import re

def extractfile():
    if (os.path.isdir("temp")): os.remove('temp')
    with zipfile.ZipFile("test.epub","r") as zip_ref:
        zip_ref.extractall("temp")

def getAllHtmlFiles():
    files = glob.glob("./temp/*.html")
    return files

def getHtmlObjectFromFile(file):
    with open(file, encoding="utf-8") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    return soup

#extractfile()
files = getAllHtmlFiles()
soup = getHtmlObjectFromFile(files[0])

#print(soup.prettify())
test = soup.prettify()

re.compile(r"\#T\#(.*?)\#T\#")

print(test)