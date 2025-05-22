from dotenv import load_dotenv
import os
import notte

# Load environment variables from .env file
load_dotenv()

# Retrieve credentials
email = os.getenv("LINKEDIN_EMAIL")
password = os.getenv("LINKEDIN_PASSWORD")

agi = notte.Agent(reasoning_model="gemini/gemini-2.0-flash")
agi.run(task=f"Log in to my LinkedIn account the mail id is {email} and password is {password} and then go to my profile. Create a new post and just type the following content as human in the text field in what do you want to talk about enter the below details :\n\n"
            "🤖 This post was created and shared by an AI agent on behalf of Elmerson.\n\n"
            "Hi everyone! 👋 I’m Elmerson’s AI assistant, and I just attended an amazing webinar titled "
            "*Launching Your AI Journey: From Curious to Capable* by @leslyarun. 🚀🎯\n\n"
            "Here are some key takeaways that stood out:\n"
            "🔢 AI = Math + Data Patterns 📊\n"
            "🌍 AI is already transforming our world through:\n"
            "   📷 Google Photos\n"
            "   💬 ChatGPT\n"
            "   🎨 Canva Magic Edit\n"
            "   🗣️ ElevenLabs\n"
            "   🎞️ Pika\n\n"
            "📚 Learning AI? Try the *Top-Down Approach* — start with tools, then theory! 🛠️➡️📖\n\n"
            "Grateful for this opportunity to learn and share! ✨\n\n"
            "#AI #Webinar #LeslyArun #AIDay0\"\n\n"
            "Make the post visible to 'Anyone'. Ensure @leslyarun is tagged properly in the post.")
