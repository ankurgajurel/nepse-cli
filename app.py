import json
import requests
import typer

def send_req_basic(scrip: str) -> dict:
    """This is the basic send request function that will get the basic info of a company"""
    base_url = "https://www.nepsealpha.com/trading-menu/top-stocks/"
    return json.loads(requests.get(base_url + scrip.upper()).text)

def send_req_news() -> dict:
    """
        This send req will requests data for latest day's breaking news. 
        The news might be less in number because they are special ones.
    """

    base_url = "https://www.nepsealpha.com/api/smx9841/get_breaking_news"
    return json.loads(requests.get(base_url).text)['breaking']
    
def send_req_price(scrip: str) -> float:
    """
        This function will request raw data for the price of the company
    """
    base_url = "https://www.nepsealpha.com/trading/1/history?symbol=" + scrip.upper() + "&resolution=1D&from=1638921600&to=99999999999"
    return float(json.loads(requests.get(base_url).text)['c'][-1])

def send_req_top_stocks(rank: int, field: str) -> tuple:
    """
        This function will request raw data about top gainer or looser or turnover.
    """
    base_url = "https://www.nepsealpha.com/trading-menu/top-stocks/"
    return json.loads(requests.get(base_url).text)['topStocks'][rank][field][0:2]

app = typer.Typer()

@app.command()
def company_profile(scrip):
    """
        This command will print the company profile of the argument symbol.
        There are no extra options for this command
    """
    try:
        info = send_req_basic(scrip)['info']
        for i in info:
            print(f'{i} --> {info[i]}')
    except Exception as get_exception:
        print(f"could not fetch info because {get_exception}")

@app.command()
def price(scrip: str) -> None:
    """
        This command will print the price of the argument symbol.
        There are no extra options for this command.
    """
    try:
        typer.echo(f"Today's price of {scrip.upper()} is {send_req_price(scrip)}")
    except Exception as what_exception:
        print(f"Could not process price because {what_exception}")

@app.command()
def news(n: int = 3):
    """
        This command will print the top 3 news of the argument symbol.
        There is one extra optional "option" which the number of news.
    """
    news_list = list(send_req_news())
    my_str = ""
    try:
        for news_ in news_list[0:n]:
            my_str = my_str + "\n" + news_['title']
        typer.echo(my_str)
    except Exception as what_exception:
        print(f"Could not process news because {what_exception}")

@app.command()
def top(field:str, n=5):
    """
        This command will print the top 5 stock of the argument symbol.
        There is one optional "option" for this commmand which is the total number of scrips to be prints.
    """
    for i in range(int(n)):
        try:
            typer.echo(f"{send_req_top_stocks(i, field)}")
        except Exception as what_exception:
            print(f"Could not process because {what_exception}")


if __name__ == "__main__":
    app()
