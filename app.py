from flask import Flask, request, render_template
import requests
import google.generativeai as genai
from mistletoe import markdown
app = Flask(__name__)

API_KEY = 'AIzaSyBLiYtc53Kr3uP0e7r6-Pgh4QfoP8YyBv4'

# Endpoint to render the form
@app.route('/')
def index():
    return render_template('index.html')

def callAPI(prompt="there is no prompt"):
   genai.configure(api_key=API_KEY)
   model = genai.GenerativeModel('gemini-pro')
   response = model.generate_content(prompt)
   return response
 

def get_mdHTML(mdContent):

  # Convert markdown to HTML
  html_content = markdown(mdContent)
#   context = {'api_content': html_content}
  return html_content


# Endpoint to handle form submission
@app.route('/generate', methods=['POST'])
def generate_blog():
    user_input = request.form['prompt']
    
    # Make a request to the Gemini API
    # response = requests.post(
    #     'https://api.openai.com/v1/text-davinci-003/completions',
    #     headers={'Authorization': f'Bearer {API_KEY}'},
    #     json={'prompt': user_input, 'max_tokens': 200}
    # )
    
    response = callAPI("write a blog on " + user_input)
   # print(response)
    #to_markdown(response.text)
        
    #generated_text = response.json()['choices'][0]['text']
    # generated_text=response.text
    mdHtml = get_mdHTML(response.text)
    return render_template('blog.html', mdHtml=mdHtml)
    


if __name__ == '__main__':
    app.run(debug=True)
