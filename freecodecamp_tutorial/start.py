from bs4 import BeautifulSoup
import requests

with open("home.html", "r") as file:
    content = file.read()

    soup = BeautifulSoup(content, 'html.parser')

    courses_cards = soup.find_all("div", class_="card")
    for course in courses_cards:
        course_name = course.h5.text
        price = course.a.text.split()[-1]

        print(f"{course_name}: {price}")