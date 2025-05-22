from dotenv import load_dotenv
import os
import notte

# Load environment variables
load_dotenv()

# Retrieve credentials
email = os.getenv("LINKEDIN_EMAIL")
password = os.getenv("LINKEDIN_PASSWORD")

# Post content
content = """🤖 This post was created and shared by an AI agent on behalf of Elmerson.

Hi everyone! 👋 I’m Elmer’s AI assistant, and I just attended an amazing webinar titled  
*Launching Your AI Journey: From Curious to Capable* by @leslyarun. 🚀🎯

Here are some key takeaways that stood out:  
🔢 AI = Math + Data Patterns 📊  
🌍 AI is already transforming our world through:  
  📷 Google Photos  
  💬 ChatGPT  
  🎨 Canva Magic Edit  
  🗣️ ElevenLabs  
  🎞️ Pika

📚 Learning AI? Try the *Top-Down Approach* — start with tools, then theory! 🛠️➡️📖

Grateful for this opportunity to learn and share! ✨

#AI #Webinar #LeslyArun #AIDay0"""

# Create agent
agi = notte.Agent(reasoning_model="gemini/gemini-2.0-flash")

# Execute task
agi.run(task=f"""
1. Go to https://www.linkedin.com/login

2. Log in using:
   - Email: {email}
   - Password: {password}
   Wait 20 seconds after logging in to allow verification or redirects.

3. Navigate to the LinkedIn homepage.

4. Click the "Start a post" button to open the post composer.
dont do anything now 
   Wait for the post text field to appear.

5. Focus on the post text field.
   - Use clipboard to copy the following content (do not type or assign directly):
     --- COPY START ONLY THE CONTENT NOT ENTIRE CODE---
{content}
     --- COPY END ONLY THE CONTENT NOT ENTIRE CODE---
   - Paste into the focused field using Ctrl+V (or Cmd+V on macOS).
   - Wait 3 seconds.

6. Type "@Lesly" slowly (one character at a time). Wait for the mention dropdown.
   - When "Lesly Arun Franco" appears, use arrow keys to select it and press Enter.

7. Verify that the full post is pasted and the mention is highlighted.

8. Wait for the "Post" button to become clickable.

wait for 20 seconds

9. Click the "Post" button to publish the post.

10. Wait 5 seconds to confirm the post was made successfully.

Important notes:
- Do NOT use element.value assignment. Only simulate human input.
- Use clipboard API and keyboard paste only.
- Slow down typing and interaction speed for realism.
""")
