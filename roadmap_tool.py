# roadmap_tool.py
from agents import function_tool

@function_tool
def get_career_roadmap(field: str) -> str:
    maps = {
        "software engineer": "Learn Python, DSA, Web Dev, GitHub, Projects.",
        "data science": "Master Python, Pandas, ML, and real-world datasets.",
        "graphic designer": "Learn Figma, Photoshop, UI/UX, Portfolio.",
        "ai": "Study Python, deep Learning, Ytansformers, and AI tools."
    }
    return maps.get(field.lower(), "No roadmap found for that field.")