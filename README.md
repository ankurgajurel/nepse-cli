# Change into the git directory
```bash
cd nepse-cli
```


# Install the required dependencies
## For Windows,
```bash
pip install -r ./requirements.txt
```
## For Linux / UNIX,
```bash
pip3 install -r ./requirements.txt
```

Or, if you do not want the hassle, you can also run the req.py file. This will install the dependencies for you.
```bash
python3 req.py
```

For help, use the command:
```bash
python3 nepse.py --help
```

# Usage of 'nepse' command
```bash
python3 nepse.py nepse 
```
This command will get you the recent data about the NEPSE Index. For example, the above command will return the latest index of the market.

## Options
```bash
Options:
    --live [True / False / 1 / 0]: Live NEPSE Index
    --status [True / False / 1 / 0]: Market Open or Closed
    --percent-change: Percentage Change in NEPSE Index
```


# Usage of 'all-scrips' command 
This will print out all the scrips
```bash
python3 nepse.py all-scrips
```

# Usage of 'company-profile' command
```bash
python3 nepse.py company-profile [script]
```
This command will print the company profile of the scrip "ADBL". The company profile at the moment only includes the full name of the company and the type of the scrip, if it is a stock or a mutual fund or a debenture, etc


# Usage of 'price' command
```bash
python3 nepse.py price [scrip]
```
The price command will give return you the Last Transaction Price, Percentage Change in the price, highest price for that transaction day and lowest price for that transaction day. The command will only take one argument which is the scrip symbol of the desired company. 


# Usage of 'news' command
```bash
python3 nepse.py news
```
You can also extract the latest breaking news related to NEPSE. There might not be many news beacuse this command will extract only important ones.

## Options
Base: 
```bash
python3 nepse.py news [option]
```
--options
```bash
    --n [int]: Prints out specific number of news.
```

# Usage of 'top' command
```bash
python3 nepse.py top [options]
```
You can also view the top gainers, loosers and the top turnover using the "top" command. The top command has one required argument. The argument might either be "gainer" or "looser" or "turnover". It will print a tuple of the symbol and the value of the property.

## Options
```bash
    gainer: Prints out the top gainer companies of the day
    looser: Prints out the top loser companies of the day
    turnover: Prints out the top turnover companies of the day
```

--multi-option
Base: 
```bash
python3 nepse.py top [option1] [option2]
```

Option2s:
```bash
    --n [int]: specific number of companies in the top
```

# Usage of 'index' command
```bash
python3 nepse.py index [options]
```
You can check the data of every index like total gainers, losers of that index, value of that index, percent change of that index from the index command.

## Options
```bash
    Banking, 
    Tourism, 
    Hotels, 
    Devbanks, 
    Hydropower, 
    Finance, 
    NonLifeInsu, 
    Manufacture, 
    Others, 
    Microfinance, 
    LifeInsu, 
    Investment
```
Note: the index options are not case sensitive.

# NEPSE_API FLASK

I have also started developing a flask api for the data I am using for this app. To use the API, follow these steps.
Note: You should have already setup the app and installed the required dependencies as mentioned in the top of this README.

## Run the Flask App

```bash
python3 ./api/nepse_api.py 
```

This will serve on the 127.0.0.1 port 3322.

## Open the browser and go to this URL

``` http://127.0.0.1:3322 ```

## Company Names

``` https://127.0.0.1:3322/companies ```

## Scrip Data

``` https://127.0.0.3322/scrip/adbl ```

# Contributing

<p>
    If you're willing to contribute to this project, please go through the project yourself or contact me on any of my socials and I'll expalin all about the project to you. The projet is fairly simple and anyone with basic understanding of Python, APIs and CLIs can contribute.
</p>