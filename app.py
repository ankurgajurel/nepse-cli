import typer
import requests
import json

def send_req(scrip: str) -> dict:
    BASE = "https://www.nepsealpha.com/trading-menu/top-stocks/"
    return json.loads(requests.get(BASE + scrip.upper()).text)

app = typer.Typer()

@app.command()
def company_profile(scrip):
    try:
        info = send_req(scrip)['info']
        for i in info:
            print(f'{i} --> {info[i]}')

    except Exception as e:
        print(f"could not fetch info because {e}")

@app.command()
def price(scrip: str, command='today_price'):
    try:
        price_info = send_req(scrip)['price']
        typer.echo(f"{command} = {price_info[command]}")
    except Exception as e:
        ...

if __name__ == "__main__":
    app()