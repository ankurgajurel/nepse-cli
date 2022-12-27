import requests
import json

def send_req_basic(scrip: str) -> dict:
    """This is the basic send request function that will get the basic info of a company"""
    base_url = "https://www.nepsealpha.com/trading-menu/top-stocks/"
    return json.loads(requests.get(base_url + scrip.upper()).text)

def send_req_nepse(command: str = "live") -> float:
    """
        This function will extract a dictinary with data related to nepse as a whole
    """

    base_url = "https://www.nepsealpha.com/ajax/live-scan-nepse"
    live_data = json.loads(requests.get(base_url).text)

    if command == "live":
        return float(live_data["ltp"])
    if command == "percent_change":
        return float(live_data["percent_change"])
    if command == "status":
        return live_data["market_status"]['isOpen']

def send_req_news() -> dict:
    """
        This send req will requests data for latest day's breaking news. 
        The news might be less in number because they are special ones.
    """

    base_url = "https://www.nepsealpha.com/api/smx9841/get_breaking_news"
    return json.loads(requests.get(base_url).text)['breaking']
    
def send_req_scrip_data(scrip: str) -> tuple:
    """
        This function will request raw data for the price-related data of the company. We have used api from another website called merolagani.
    """
    base_url = "https://merolagani.com/handlers/webrequesthandler.ashx?type=market_summary"
    all_scrip = json.loads(requests.get(base_url).text)["turnover"]["detail"]
    
    for each_scrip in all_scrip:
        if each_scrip["s"] == scrip.upper():
            return float(each_scrip["lp"]), float(each_scrip["pc"]), float(each_scrip["h"]), float(each_scrip["l"])

def send_req_top_stocks(rank: int, field: str) -> tuple:
    """
        This function will request raw data about top gainer or looser or turnover.
    """
    base_url = "https://www.nepsealpha.com/trading-menu/top-stocks/"
    return json.loads(requests.get(base_url).text)['topStocks'][rank][field][0:2]
