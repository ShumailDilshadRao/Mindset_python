
#type:ignore

import streamlit as st
import datetime

def ramadan_growth_mindset_challenge():
    st.title("🌙 Ramadan Growth Mindset Challenge 🌟")

    # Define the challenge tasks for each week
    challenge_tasks = {
        "Week 1: Intention & Reflection 💭": [
            "🙏 Set daily intentions for your fast and spiritual growth.",
            "🧐 Reflect on your daily actions and identify areas for improvement.",
            "✍️ Practice gratitude journaling before Suhoor or after Iftar.",
            "📖 Read a chapter of the Quran with contemplation.",
            "💪 Identify and list your strengths and weaknesses."
        ],
        "Week 2: Patience & Perseverance ⏳": [
            "🧘 Practice patience in challenging situations (e.g., traffic, long lines).",
            "📅 Stick to your daily schedule, even when you feel tired.",
            "🧗 Complete a challenging task, breaking it into smaller steps.",
            "🍽️ Practice mindful eating during Iftar.",
            "🤲 Learn a new dua and try to memorize it."
        ],
        "Week 3: Empathy & Compassion ❤️": [
            "🤝 Perform an act of kindness for someone in need.",
            "👂 Listen actively to others without judgment.",
            "🎁 Donate to a charity or volunteer your time.",
            "🕊️ Practice forgiveness and let go of grudges.",
            "✨ Reflect on the blessings in your life and share them with others."
        ],
        "Week 4: Growth & Gratitude 🌱": [
            "📈 Review your progress and identify areas of growth.",
            "💌 Express gratitude to those who have supported you during Ramadan.",
            "📝 Plan how you will maintain your positive habits after Ramadan.",
            "📚 Reflect on the spiritual lessons learned during the month.",
            "🎯 Write down your future goals and how you will achieve them."
        ],
    }

    # Get the current date and calculate the week of Ramadan
    today = datetime.date.today()
    ramadan_start = datetime.date(2025, 3, 2) # Example Ramadan Start Date. Adjust as needed.
    days_since_start = (today-ramadan_start).days

    if days_since_start < 0:
        st.write("Ramadan has not started yet. Check back during Ramadan! 🌙")
        return

    week_number = (days_since_start // 7) + 1
    week_number = min(week_number, 2)
    week_number = max(week_number, 1)

    st.subheader(f" Week {week_number}: {list(challenge_tasks.keys())[week_number - 1]} 🗓️")

    # Display the challenge tasks for the current week
    for task in challenge_tasks[list(challenge_tasks.keys())[week_number - 1]]:
        st.write(f"- {task}")

    # Checkbox for completed tasks
    completed_tasks = []
    for task in challenge_tasks[list(challenge_tasks.keys())[week_number - 1]]:
        if st.checkbox(f"✅ Completed: {task}"):
            completed_tasks.append(task)

    if completed_tasks:
        st.success(f"🎉 You have completed {len(completed_tasks)} tasks this week! 🎉")

    # Reflection area
    st.subheader("Daily Reflection 📝")
    reflection = st.text_area("Write your thoughts and reflections here:", height=200)

    #Additional fields
    saher_time = st.time_input("Saheri Time ⏰", datetime.time(5, 30))
    iftar_time = st.time_input("Iftar Time 🍽️", datetime.time(18, 36))
    daily_dua = st.text_input("Daily Dua 🙏", "")
    daily_quran_verse = st.text_input("Daily Quran Verse 📖", "")

    if st.button("Save Reflection & Daily Entries 💾"):
        # Here you can add logic to save the reflection (e.g., to a file or database)
        st.success("Reflection and Daily Entries saved! 🌟")

    st.subheader("Resources 📚")
    st.markdown("- [Quran recitation 🎧](https://www.youtube.com/watch?v=hCGVXMFVHCA&list=PLXLJ0Tsrz9yCFDhWVo2Bap9khiOQIdjSA)")
    st.markdown("- [Islamic lectures 🎙️](https://www.youtube.com/watch?v=573891181)")
    st.markdown("- [Dua collection 🤲](https://youtu.be/eREZ1WAsl-Q?si=3Xlqo7RoE2Snxq2m)")

    st.markdown("---") # Add a horizontal line for visual separation
    st.markdown("<style>body { background-color: #f8f8f8; }</style>", unsafe_allow_html=True) #light background
    st.markdown("<style>div.stButton > button:first-child { background-color: #4CAF50; color: white; }</style>", unsafe_allow_html=True) #style button
    st.markdown("<style> .stTextArea textarea {background-color: #e8f5e9;}</style>", unsafe_allow_html=True) #style text area.
    st.balloons()
    
if __name__ == "__main__":
    ramadan_growth_mindset_challenge()