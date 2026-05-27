import tkinter as tk
from datetime import datetime

# Main Window
root = tk.Tk()
root.title("🌦️ Creative Weather Chatbot")
root.geometry("600x700")
root.configure(bg="#0f172a")

# Weather Data
weather_data = {
    "bangalore": "🌤️ 28°C - Partly Cloudy",
    "delhi": "☀️ 35°C - Sunny",
    "mumbai": "🌧️ 30°C - Rainy",
    "chennai": "🌦️ 32°C - Humid",
    "hyderabad": "🌩️ 29°C - Thunderstorm"
}

# Function
def send_message():

    user_message = entry_box.get()

    if user_message == "":
        return

    # Show user message
    chat_area.insert(tk.END, "🧑 You: " + user_message + "\n\n")

    message = user_message.lower()

    # Bot replies
    if "hi" in message or "hello" in message:
        response = "🤖 Hello! Welcome to Smart Weather Bot"

    elif "time" in message:
        current_time = datetime.now().strftime("%I:%M %p")
        response = "⏰ Current Time: " + current_time

    elif "date" in message:
        current_date = datetime.now().strftime("%d-%m-%Y")
        response = "📅 Today's Date: " + current_date

    elif message in weather_data:
        response = "🌍 Weather in " + message.title() + "\n" + weather_data[message]

    elif "cities" in message:
        response = "🏙️ Available Cities:\n"

        for city in weather_data:
            response += "• " + city.title() + "\n"

    elif "bye" in message:
        response = "👋 Bye! Have a Nice Day"

    else:
        response = "❌ Sorry, City Not Found"

    # Show bot response
    chat_area.insert(tk.END, "🌦️ Bot: " + response + "\n\n")

    # Auto scroll
    chat_area.see(tk.END)

    # Clear box
    entry_box.delete(0, tk.END)

# Title
title = tk.Label(
    root,
    text="🌦️ SMART WEATHER CHATBOT 🌦️",
    font=("Arial", 20, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)

title.pack(pady=15)

# Chat Frame
frame = tk.Frame(root, bg="#0f172a")
frame.pack()

# Chat Area
chat_area = tk.Text(
    frame,
    width=60,
    height=25,
    font=("Arial", 12),
    bg="#1e293b",
    fg="white",
    insertbackground="white",
    bd=5,
    relief="ridge"
)

chat_area.pack(pady=10)

# Entry Box
entry_box = tk.Entry(
    root,
    width=35,
    font=("Arial", 15),
    bg="#e2e8f0",
    fg="black",
    bd=3
)

entry_box.pack(pady=15)

# Send Button
send_button = tk.Button(
    root,
    text="SEND 🚀",
    font=("Arial", 14, "bold"),
    bg="#38bdf8",
    fg="white",
    activebackground="#0ea5e9",
    width=12,
    height=1,
    command=send_message
)

send_button.pack(pady=10)

# Footer
footer = tk.Label(
    root,
    text="Created with Python Tkinter",
    font=("Arial", 10),
    bg="#0f172a",
    fg="lightgray"
)

footer.pack(side="bottom", pady=10)

# Run Window
root.mainloop()