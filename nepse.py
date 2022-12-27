import typer
import typing
import all_data as data

app = typer.Typer()

@app.command()
def nepse(live=None, status=None, percent_change=None):
    """
        This command works with the basic data about NEPSE as a whole for that day. Options like market status, percentage change and all are included.
    """
    if live:
        typer.echo(data.send_req_nepse("live"))
    if status:
        my_bool = data.send_req_nepse("status")
        if my_bool:
            typer.echo("The market is OPEN right now.")
        else:
            typer.echo("The market is CLOSED right now.")
    if percent_change:
        typer.echo(f"{data.send_req_nepse('percent_change')}%")
    if live==None and status==None and percent_change==None:
        typer.echo(data.send_req_nepse("live"))

@app.command()
def company_profile(scrip):
    """
        This command will print the company profile of the argument symbol.
        There are no extra options for this command
    """
    try:
        info = data.send_req_basic(scrip)['info']
        for i in info:
            print(f'{i} --> {info[i]}')
    except Exception as get_exception:
        print(f"could not fetch info because {get_exception}")

@app.command()
def price(scrip: str):
    """
        This command will print the price of the argument symbol.
        There are no extra options for this command.
    """
    last_price, per_change, high, low = data.send_req_scrip_data(scrip)
    try:
        typer.echo(f"Last Price        = Rs. {last_price}")
        typer.echo(f"Percentage Change = {per_change}%")
        typer.echo(f"Highest Today     = Rs. {high}")
        typer.echo(f"Lowest Today      = Rs. {low}")

    except Exception as what_exception:
        print(f"Could not process price because {what_exception}")

@app.command()
def news(n: int = 3):
    """
        This command will print the top 3 news of the argument symbol.
        There is one extra optional "option" which the number of news.
    """
    news_list = list(data.send_req_news())
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
            typer.echo(f"{data.send_req_top_stocks(i, field)}")
        except Exception as what_exception:
            print(f"Could not process because {what_exception}")


if __name__ == "__main__":
    app()  