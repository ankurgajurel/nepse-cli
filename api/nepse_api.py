import all_data

from flask import Flask, jsonify

app = Flask(__name__)

link_to_git = "https://github.com/ankurgajurel/nepse-cli"
@app.route('/')
def index():
    return f"<div style=\"font-size: 700%;overflow:hidden;\">this api will serve all data used in the nepse-cli app. <br> check more at: <a href=\"https:\/\/github.com\/ankurgajurel\/nepse-cli\">https://github.com/ankurgajurel/nepse-cli</a></div>"

@app.route('/scrip/<scrip>')
def stocks(scrip):
    data = all_data.send_req_scrip_data(scrip)
    json_data = {
        "last_transaction_price": data[0],
        "percentage_change": data[1],
        "highest_transaction_price": data[2],
        "lowest_transaction_price": data[3], 
    }
    return json_data

if __name__ == "__main__":
    app.run(debug=True, port=3322)