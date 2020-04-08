from bs4 import BeautifulSoup
import csv
import requests

 
source = requests.get('https://www.brainpickings.org/').text
soup = BeautifulSoup(source, 'lxml')

file = open('BrainPickingsMain.csv', 'w')
writer = csv.writer(file)
writer.writerow(['Headline', 'Quote', 'Body'])

for article in soup.find_all('div', id='posts'):
    
    headline = article.find('h1', class_='entry-title').text
    print(headline)
    
    quote = article.h2.text
    print(quote)
    
    summary = article.find('div', class_='entry_content').text
    print(summary)
    print()
    
    writer.writerow([headline.encode('utf8'), quote.encode('utf8'), summary.encode('utf8')])
file.close()    
    
    
   
  