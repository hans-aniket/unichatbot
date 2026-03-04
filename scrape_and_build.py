import requests
from bs4 import BeautifulSoup
import json

def scrape_text(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        text = " ".join([p.get_text(strip=True) for p in paragraphs])
        return text[:500]
    except:
        return "Information currently unavailable."

fees_info = scrape_text("https://www.iiitd.ac.in/admission/fees")
placement_info = scrape_text("https://www.iiitd.ac.in/placement")

knowledge_base = {
    "intents": [
        {
            "tag": "greetings",
            "patterns": ["hi", "hello", "hey", "good morning", "good evening", "is anyone there"],
            "responses": ["Hello! I am the IIITD chatbot. Ask me about courses, fees, placements, or campus facilities!"]
        },
        {
            "tag": "location",
            "patterns": ["where is the campus", "iiitd address", "how to reach college", "location"],
            "responses": ["The campus is located in Okhla Phase-III, near Nehru Place and the Govindpuri Metro Station."]
        },
        {
            "tag": "fees",
            "patterns": ["what is the fee", "how much does btech cost", "tuition structure", "hostel fees", "btech"],
            "responses": [f"Website data states: {fees_info}"]
        },
        {
            "tag": "placements",
            "patterns": ["highest placement", "placement stats", "average package", "placement"],
            "responses": [f"Recent placement info: {placement_info}"]
        },
        {
            "tag": "facilities",
            "patterns": ["what facilities are there", "is there a gym", "campus amenities"],
            "responses": ["The campus has separate hostels, a common mess, cafeterias, a 24x7 library, a gym, an infirmary, an HDFC ATM, and sports courts."]
        },
        {
            "tag": "attendance",
            "patterns": ["attendance criteria", "what is the attendance rule", "minimum attendance"],
            "responses": ["Attendance is taken in all core courses. Students having less than 75% attendance in core courses are issued a warning."]
        },
        {
            "tag": "courses",
            "patterns": ["what courses are running", "programmes offered", "courses", "programme"],
            "responses": ["IIITD offers B.Tech programs in CSE and ECE, M.Tech programs in CSE and ECE, and PhD programs."]
        }
    ]
}

with open('intents.json', 'w') as file:
    json.dump(knowledge_base, file, indent=4)