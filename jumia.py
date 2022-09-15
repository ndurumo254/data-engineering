
#start by importing libraries.
from bs4 import BeautifulSoup
import requests
from csv import writer
#create a variable and assign the url to it
site= "https://www.jumia.co.ke/mlp-portal/generic/?seller_score=4-5&shipped_from=country_local--jumia_global#catalog-listing"
#use requests library to get content from the site 
htmls= requests.get(site)
#create object to hold the content you have requested
objects= BeautifulSoup(htmls.text, 'html.parser')
#use find_all function to get everything in the page
prod= objects.find_all('a', class_="core")


with open('jumia.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['commodity','price','location','old_price','different_perc']
    thewriter.writerow(header)

    #use  for loop to write on the csv file
    for items in prod:
            location= items.find('div', class_="bdg _glb _xs").text.replace('\n', '  ')
            price= items.find('div', class_="prc").text.replace('\n', '  ')
            old_price=items.find('div',class_="old").text.replace('\n', '  ')
            different_perc=items.find('div',class_="bdg _dsct _sm").text.replace('\n', '  ')
            commodity=items.find('h3', class_="name").text.replace('\n', '  ')
            description=[commodity,price,location,old_price,different_perc]
            thewriter.writerow(description)