from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)
data = BeautifulSoup(response.content, 'lxml')

title_ = data.find("h2")
print("*************** " +title_.text + " ***************\n")
movies = data.find_all(name="h3", class_="title")

movies.reverse()
for h3 in movies:
    print(h3.text)