from flask import Flask, render_template
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/run_selenium')
def run_selenium():
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://google.com")
    time.sleep(999999999999999999999999999999999999999999999999999999999999999999)
if __name__ == '__main__':
    app.run(debug=True)
