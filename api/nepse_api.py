import sys
sys.path.append('../')
import all_data

from flask import Flask, jsonify

app = Flask(__name__)

link_to_git = "https://github.com/ankurgajurel/nepse-cli"
@app.route('/')
def index():
    return f"<div style=\"font-size: 700%;overflow:hidden;\">this api will serve all data used in the nepse-cli app. <br> check more at: <a href=\"https:\/\/github.com\/ankurgajurel\/nepse-cli\">https://github.com/ankurgajurel/nepse-cli</a></div>"

@app.route('/companies')
def stocks():
    return all_data.company_names()

if __name__ == "__main__":
    app.run(debug=True, port=3322)