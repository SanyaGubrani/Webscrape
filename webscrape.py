#Web scraping practice code to extract data from website geeksforgeeks, specifically 
#the article titled: "What is Web Scraping and How to Use It?" written by harkiran78.
#Website: https://www.geeksforgeeks.org/  ;
#https://www.geeksforgeeks.org/what-is-web-scraping-and-how-to-use-it/



import requests
from bs4 import BeautifulSoup

url = "https://www.geeksforgeeks.org/what-is-web-scraping-and-how-to-use-it/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

title = soup.select('h1')[0].text  #Title of the page (in H1)
print(title)


headings = []  

for element in soup.select('h3'):
    headings.append(element.text)  #Adding all the Headings (H3 element's text)


para_content = []

for para in soup.select('p'):
    para_content.append(para.text)  #Adding all the paragraph's content


#Scraping out the required data :---


print(headings[0])
output0 = '\n'.join(para_content[5:7])
print(output0)


print(headings[1])
output1 = '\n'.join(para_content[7:9])
print(output1)


print(headings[2])
output2 = '\n'.join(para_content[9:13])
print(output2)

    
print(headings[3])
output3 = (para_content[13])
print(output3)


print(headings[4])
output4 = (para_content[14])
print(output4)
subheadings = []  

for element in soup.select('h4'):
    subheadings.append(element.text)

print('\n'.join(subheadings[0:5]))



