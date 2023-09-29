import requests
from bs4 import BeautifulSoup
import time

unfamilliar_skill = input("Put some skill that you're not familiar with:\n> ")
print(f"Filtering out {unfamilliar_skill}")


def find_jobs():
    # Define the URL with the search parameters
    url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="

    # Send an HTTP GET request and retrieve the HTML content
    html_text = requests.get(url).text

    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_text, "html.parser")

    # Find all job listings
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    for i, job in enumerate(jobs):
        # Find the published date
        published_date = job.find("span", class_="sim-posted").span.text.strip()

        # Check if the job was posted "few days ago"
        if "few days ago" in published_date.lower():
            # Find the company name
            company_name = job.find("h3", class_="joblist-comp-name").text.strip().title()

            # Find and clean the skills
            skills = job.find("span", class_="srp-skills").text.strip()
            skills = ", ".join(map(str.strip, skills.split(",")))  # Clean up spaces and format

            # Find more info
            more_info = job.header.h2.a["href"]

            # Print job details after filtering
            if unfamilliar_skill not in skills:
                with open(f"posts/{i}.txt", "w") as file:
                    file.write(f"Company Name: {company_name}\n")
                    file.write(f"Required Skills: {skills}\n")
                    file.write(f"Published Date: {published_date}\n")
                    file.write(f"More Info: {more_info}\n")
                print(f"File {i} saved")

if __name__ == "__main__":
    while True:
        find_jobs()
        print("Waiting 10 minutes...")
        time.sleep(600)

