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

knowledge_base = {
    "intents": [
        {
            "tag": "greetings",
            "patterns": ["hi", "hello", "hey", "good morning", "good evening", "is anyone there"],
            "responses": ["Hello! I am the IIITD chatbot. Ask me about courses, fees, placements, or campus facilities!"]
        },
        {
            "tag": "location",
            "patterns": ["where is the campus", "location of university", "address", "how to reach", "location"],
            "responses": ["IIIT-Delhi is located in Okhla Industrial Estate, Phase III, New Delhi - 110020, near the Govindpuri Metro Station and Nehru Place."]
        },
        {
            "tag": "affiliation",
            "patterns": ["is iiitd affiliated to ugc", "aicte approval", "university status", "is it a state university", "affiliation"],
            "responses": ["IIIT-Delhi is a State University established by the Delhi Government. It is recognized by the UGC under section 2(f) and 12(B) of the UGC Act and is approved by AICTE."]
        },
        {
            "tag": "courses",
            "patterns": ["courses running in university", "what programs are offered", "btech branches", "mtech specializations", "courses offered", "courses"],
            "responses": ["The university offers B.Tech programs in CSE, ECE, CSAM, CSD, CSSS, CSB, CSAI, EVE, and CSEcon. It also offers M.Tech programs in CSE, ECE, and CB, alongside Ph.D. and PG Diploma programs."]
        },
        {
            "tag": "highest_placement",
            "patterns": ["courses giving highest placement", "highest package branch", "top placement stats", "highest placement", "placement"],
            "responses": ["For the 2025 season, B.Tech CSE and CSAM branches yielded the highest placements. The highest domestic package was ₹51.31 LPA and the highest overseas package was ₹107 LPA. CSAM had a 98.28% placement rate."]
        },
        {
            "tag": "fees",
            "patterns": ["fees of all courses", "what is the tuition fee", "btech cost", "mtech fees", "fees structure", "fees"],
            "responses": [f"For the 2025-2026 academic year, the total B.Tech tuition fee is approximately ₹19.55 Lakhs. M.Tech tuition ranges between ₹3.7 Lakhs to ₹6 Lakhs. Scraped data states: {fees_info}"]
        },
        {
            "tag": "industry_partners",
            "patterns": ["industry partners", "top recruiters", "companies visiting campus", "who hires from iiitd"],
            "responses": ["Top industry partners and recruiters include Google, Microsoft, Amazon, Goldman Sachs, Uber, Adobe, Oracle, Qualcomm, Samsung, and TCS."]
        },
        {
            "tag": "timings",
            "patterns": ["college timings", "when do classes start", "institute hours", "timings of classes", "timings", "time"],
            "responses": ["Academic classes generally commence at 9:00 AM. Specific lecture timings depend on the individual student's course schedule."]
        },
        {
            "tag": "attendance",
            "patterns": ["attendance criteria", "minimum attendance rule", "what happens if attendance is low", "attendance"],
            "responses": ["Attendance is mandatory for core courses. Students who fall below the 75% attendance threshold in core courses are issued a formal warning."]
        },
        {
            "tag": "facilities",
            "patterns": ["campus facilities", "what amenities are there", "is there a gym or library", "facilities in the campus", "facilities"],
            "responses": ["The campus features separate hostels for boys and girls, a common mess, cafeterias, a 24x7 library with reading rooms, an infirmary, a gym, an HDFC ATM, and various sports courts."]
        },
        {
            "tag": "advanced_labs",
            "patterns": ["advanced labs queries", "research centers", "what labs are available", "tell me about the labs", "labs"],
            "responses": ["IIIT-Delhi houses over 30 advanced research centers and labs, including the Centre for Quantum Technology, Infosys Centre for AI, Human-Machine Interaction Lab, Creative Interfaces Lab, and the Advanced Multicore Systems Lab."]
        }
    ]
}

with open('intents.json', 'w') as file:
    json.dump(knowledge_base, file, indent=4)