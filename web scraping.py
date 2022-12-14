from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
import phonenumbers
from phonenumbers import geocoder, carrier

print("Welcome to webin \n")
print("ENSANITY_el \n")
url_reciever = input("enter ur url \n")
page = requests.get(url_reciever)
soup = BeautifulSoup(page.content, "html.parser")
titl = soup.titl
para = soup.find_all('p')


def https():
    anchor = soup.find_all('a')

    all_links = set()
    for link in anchor:
        if (link.get('href') != "#"):
            link = url_reciever + link.get('href')
            all_links.add(link)
            print(link)


def contentpage():
    print(soup.find('p'))
    print(soup.find('p')['class'])
    print(soup.find_all("p", class_="lead"))
    print(soup.find('p').get_text())  # text from tags
    print(soup.get_text())


def parentchild():
    wordid = input("enter ur word search id")
    wordsearch = soup.find(id=wordid)
    store = wordsearch.parent
    store2 = wordsearch.next_sibling
    store3 = wordsearch.previous_sibling
    print("Enter ur choice")
    print("1.Parent")
    print("2.next_sibling")
    print("3.previous_sibling")
    while True:
        choices = input("enter ur choice 1/2/3 \n")
        if choices in ('1', '2', '3'):
            if choices == '1':
                print(store.prettify())
            if choices == '2':
                print(store2.prettify())
            if choices == '3':
                print(store3.prettify())


def phnum():
    newnum = input("enter ur phone number")
    phoneNumber = phonenumbers.parse(newnum)
    Carrier = carrier.name_for_number(phoneNumber, 'en')
    Region = geocoder.description_for_number(phoneNumber, 'en')
    print(Carrier)
    print(Region)


print("select operations")
print("1.https")
print("2.contentpage")
print("3.parentchild")
print("4.phone number")

while True:
    choice = input("enter your choice(1/2/3/4) \n")
    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            https()
        if choice == '2':
            contentpage()
        if choice == '3':
            parentchild()
        if choice == '4':
            phnum()
