import requests
from bs4 import BeautifulSoup

class Movies:
    def __init__(self):

        self.url = "https://www.imdb.com/chart/top/" # Top 250 Movies
        self.url2 = "https://www.imdb.com/chart/moviemeter/?ref_=nv_td_mpm" # Most Popular Movies

    def topList(self,limit=1):

        html = requests.get(self.url).content
        bs_soup = BeautifulSoup(html,"html.parser")
        list = bs_soup.find("tbody",{"class":"lister-list"}).find_all("tr",limit=limit)
        return list

    def mostPopular(self,limit=1):
        
        html = requests.get(self.url2).content
        bs_soup = BeautifulSoup(html,"html.parser")
        list = bs_soup.find("tbody",{"class":"lister-list"}).find_all("tr",limit=limit)
        return list

movies = Movies()


while True:
    
    enter = int(input("1-Top 250 Movies\n2-Most Popular Movies\n3-Exit\nSeçim:"))

    if enter == 1:

        top250 = int(input("Top 250 Kaç Film Sıralansın: "))

        list = movies.topList(top250)
        
        for tr in list:
            title = tr.find("td",{"class":"titleColumn"}).find("a").text
            year = tr.find("td",{"class":"titleColumn"}).find("span").text
            rating = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
            print(f"Film Adı : {title}\nFilm Tarihi: {year}\nİMDB Puanı: {rating}")
        print("*"*50)

    elif enter == 2:

        most_popular = int(input("En Popüler Kaç Film Sıralansın: "))

        list = movies.mostPopular(most_popular)

        for tr in list:
            title = tr.find("td",{"class":"titleColumn"}).find("a").text
            year = tr.find("td",{"class":"titleColumn"}).find("span").text
            rating = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
            print(f"Film Adı : {title}\nFilm Tarihi: {year}\nİMDB Puanı: {rating}")
        print("*"*50)
    elif enter == 3:
        exit(0)
    else:
        print("HATA")

# Coded By Onurhocaoglu
# http://www.onurhocaoglu.com






