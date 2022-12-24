# Change into the git directory
```cd nepse-api```


# Install the required dependencies
## For Windows,
```pip install -r requirements.txt```
## For Linux / UNIX,
```pip3 install -r requirements.txt```

Or, if you don't want the hassle, you can also run the req.py file. This will install the dependencies for you.
```python3 req.py```

For help, use the command:
```python3 app.py --help```

# Using the app
```python3 app.py company-profile adbl```

This command will print the company profile of the scrip "ADBL". The company profile at the moment only includes the full name of the company and the type of the scrip, if it is a stock or a mutual fund or a debenture, etc

```python3 app.py price adbl```

This command will print the latest price of the scrip "ADBL". The price will be in NRS and is not tested if it will update live whilst the NEPSE Market is open. 

You can also extract the latest breaking news related to NEPSE. There might not be many news beacuse this command will extract only important ones. 

```python3 app.py news```

If you want to extract certain amount of news,

```python3 app.py news --n 10```

You can also view the top gainers, loosers and the top turnover using the "top" command. The top command has one required argument. The argument might either be "gainer" or "looser" or "turnover". It will print a tuple of the symbol and the value of the property. 

```python3 app.py top gainer```

This will print the top 5 gainers.

```python3 app.py top looser```

```python3 app.py top turnover```

If you want to print a certain number of top scrips, you can use the option --n.

For example, 

```python3 app.py top gainer --n 10```

This command will print the top 10 gainers of the latest trading day.

Remember that the max value for --n is 10. So, app will throw an exception of list out of range