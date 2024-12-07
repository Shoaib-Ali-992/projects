import tkinter as tk
from tkinter import scrolledtext, END
from nltk.chat.util import Chat, reflections

class ChatBot:
    def __init__(self, master):
        self.master = master
        master.title("ChatBot")

        self.chat_log = scrolledtext.ScrolledText(master, width=50, height=20)
        self.chat_log.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.user_input = tk.Entry(master, width=40)
        self.user_input.grid(row=1, column=0, padx=10, pady=10)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        self.bot = Chat(self.pairs, reflections)

    def send_message(self):
        user_input = self.user_input.get()
        self.user_input.delete(0, END)
        self.update_chat_log("You: " + user_input)
        response = self.bot.respond(user_input)
        self.update_chat_log("ChatBot: " + response)

    def update_chat_log(self, message):
        self.chat_log.configure(state='normal')
        self.chat_log.insert(tk.END, message + '/n')
        self.chat_log.configure(state='disabled')

    # Define chat patterns and responses
    pairs = [
    (r'what is Pakistan\?', ['Pakistan, officially the Islamic Republic of Pakistan is a country in South Asia. It is the fifth most populous country, with a population of over 241.5 million having the second-largest Muslim population as of 2023']),
    (r'where is Pakistan located\?', ['Pakistan is located in Southern Asia bordering the Arabian Sea, between India to the east and Iran and Afghanistan to the west and China to the north. Pakistan covers an area of 803,943 sq.']),
    (r'what is the capital of Pakistan\?', ['The capital of Pakistan is Islamabad.']),
    (r'what are the major cities in Pakistan\?', ['Some of the major cities in Pakistan include Karachi, Lahore, Islamabad, Rawalpindi, Faisalabad, and Multan.']),
    (r'what languages are spoken in Pakistan\?', ['The official language of Pakistan is Urdu, but other languages spoken include Punjabi, Pashto, Sindhi, Balochi, and Saraiki. English is also widely used in business and government.']),
    (r'what is the currency of Pakistan\?', ['The currency of Pakistan is the Pakistani Rupee, abbreviated as PKR.']),
    (r'what is the population of Pakistan\?', ['As of the latest estimates, Pakistan has a population of over 225 million people, making it the fifth-most populous country in the world.']),
    (r'what is the climate like in Pakistan\?', ['Pakistan has a varied climate, ranging from arid and semi-arid in the southern and central regions to temperate in the north. The country experiences four seasons: winter, spring, summer, and autumn.']),
    (r'what is the national animal of Pakistan\?', ['The national animal of Pakistan is the Markhor, a species of wild goat native to the mountainous regions of Central Asia.']),
    (r'what is the national bird of Pakistan\?', ['The national bird of Pakistan is the Chukar Partridge, a gamebird native to South Asia and the Middle East.']),
    (r'what is the national flower of Pakistan\?', ['The national flower of Pakistan is the Jasmine, specifically the Jasminum officinale variety.']),
    (r'what is the national tree of Pakistan\?', ['The national tree of Pakistan is the Deodar Cedar, a coniferous tree native to the Himalayas and other mountainous regions of South Asia.']),
    (r'what is the national sport of Pakistan\?', ['The national sport of Pakistan is field hockey.']),
    (r'what is the history of Pakistan\?', ['Pakistan has a rich history that dates back thousands of years, with civilizations such as the Indus Valley Civilization flourishing in the region.']),
    (r'what is the political system of Pakistan\?', ['Pakistan is a federal parliamentary democratic republic, with a President as the head of state and a Prime Minister as the head of government.']),
    (r'who is the founder of Pakistan\?', ['Muhammad Ali Jinnah, also known as Quaid-e-Azam (Great Leader), is considered the founder of Pakistan.']),
    (r'what is the national anthem of Pakistan\?', ['The national anthem of Pakistan is "Qaumi Taranah", which was written by Hafeez Jalandhari and composed by Ahmed Ghulamali Chagla.']),
    (r'what is the national flag of Pakistan\?', ['The national flag of Pakistan consists of a dark green field with a white vertical stripe on the left side, a white crescent moon, and a five-pointed star in the middle.']),
    (r'what is the national day of Pakistan\?', ['The national day of Pakistan is celebrated on March 23rd each year, commemorating the Lahore Resolution passed on March 23, 1940, which laid the groundwork for the creation of Pakistan.']),
    (r'what is the significance of the Lahore Resolution\?', ['The Lahore Resolution, also known as the Pakistan Resolution, called for the creation of independent states for Muslims in British India, leading to the eventual formation of Pakistan.']),
    (r'what is the significance of Pakistan Day\?', ['Pakistan Day commemorates the Lahore Resolution of 1940, which laid the foundation for the creation of Pakistan as a separate nation for Muslims of the Indian subcontinent.']),
    (r'what is the significance of Independence Day in Pakistan\?', ['Independence Day in Pakistan, celebrated on August 14th, marks the day when Pakistan gained independence from British rule in 1947.']),
    (r'what is the role of Pakistan in the world\?', ['Pakistan plays a significant role in regional and global affairs, particularly in South Asia and the Muslim world. It is known for its strategic location, nuclear capabilities, and contributions to peacekeeping missions.']),
    (r'what is the relationship between Pakistan and India\?', ['Pakistan and India have a complex relationship, characterized by historical conflicts, territorial disputes, and occasional attempts at peace and reconciliation. The two countries have fought several wars and continue to engage in diplomatic negotiations to address their differences.']),
    (r'what is the relationship between Pakistan and China\?', ['Pakistan and China enjoy a close and strategic relationship, often described as an "all-weather friendship". The two countries collaborate on various economic, military, and infrastructure projects through initiatives such as the China-Pakistan Economic Corridor (CPEC).']),
    (r'what is the relationship between Pakistan and the United States\?', ['The relationship between Pakistan and the United States has been characterized by periods of cooperation and tension, particularly in the context of counterterrorism efforts and regional stability in South Asia.']),
    
    ]

if __name__ == "__main__":
    root = tk.Tk()
    chatbot_app = ChatBot(root)
    root.mainloop()
