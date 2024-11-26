import base64
from requests import post
import urllib3
import skeleton as sk

# Disable SSL warnings (optional, if using self-signed certificates)
urllib3.disable_warnings()

# WordPress credentials and setup
username = "sohanpalabras"
pass_key = 'SFHe 9fV7 0jgo zAOQ RcYT lsrb'
wp_creden = f'{username}:{pass_key}'
wp_token = base64.b64encode(wp_creden.encode())
wp_headers = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}

# Specify the URL for posting
wp_post_url = 'https://bancodepalabras.com/wp-json/wp/v2/posts'

# Read the content from 'html_file.txt'
with open('html_file.txt', 'r', encoding='utf-8') as f:
    post_content = f.read()

# Read the recipe.json file to get the Title
keyword = sk.title

# Prepare data for the WordPress post
data = {
    'title': keyword,
    'content': post_content,
    'status': 'draft',  # Set to 'draft' to save as draft
    'categories': '24',  # Make sure '24' is the correct category ID
}

# Send the POST request with JSON data
res = post(wp_post_url, json=data, headers=wp_headers, verify=False)

# Check response status and output
if res.status_code == 201:  # 201 indicates success for creation
    print("Post created successfully!")
    print("Post ID:", res.json().get('id'))
else:
    print(f"Failed to create post. Status code: {res.status_code}")
    try:
        print(res.json())
    except Exception as e:
        print("Failed to parse JSON:", e)
        print("Response text:", res.text)
