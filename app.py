from flask import *
import os
import image_scraper
import requests
import json

# Configuration

app = Flask(__name__)

# Routes 

@app.route('/')
def root():
    return render_template("main.j2") 

@app.route('/scraper', methods=['POST'])
def scraper():
    input_json = request.get_json(force=True)
    if not request.json or not 'PageURL' in request.json:
        abort(400, "This is a bad request!")
    
    page_url = request.json['PageURL']
    return image_scraper.find_images(page_url)

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 64234))
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(host='0.0.0.0', port=port, debug=True) 