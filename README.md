# Change into the git directory
```cd nepse-cli```


# Install the required dependencies
## For Windows,
```pip install -r requirements.txt```
## For Linux / UNIX,
```pip3 install -r requirements.txt```

Or, if you don't want the hassle, you can also run the req.py file. This will install the dependencies for you.
```python3 req.py```

For help, use the command:
```python3 nepse.py --help```

# Usage of nepse command

```python3 nepse.py nepse```

This command will get you the recent data about the NEPSE Index. For example, the above command will return the latest index of the market. 

This command has three options: --live, --status, --percent-change. All these options will require one argument either be 1 or True. This just tells the program that we only need that particular information.

If you want to check weather the market is open or not, you can use the following command. 

``` python3 nepse.py nepse --status True ```

To check the percentage change in the NEPSE Index, you can use the following command:

``` python3 nepse.py nepse --percent-change 1 ```

# Usage of company-profile command
```python3 nepse.py company-profile adbl```

This command will print the company profile of the scrip "ADBL". The company profile at the moment only includes the full name of the company and the type of the scrip, if it is a stock or a mutual fund or a debenture, etc

# Usage of price command

The price command will give return you the Last Transaction Price, Percentage Change in the price, highest price for that transaction day and lowest price for that transaction day. The command will only take one argument which is the scrip symbol of the desired company. For example,

``` python3 nepse.py price nabil ```


# Usage of news command

You can also extract the latest breaking news related to NEPSE. There might not be many news beacuse this command will extract only important ones. 

```python3 nepse.py news```

If you want to extract certain amount of news,

```python3 nepse.py news --n 10```

# Usage of top command

You can also view the top gainers, loosers and the top turnover using the "top" command. The top command has one required argument. The argument might either be "gainer" or "looser" or "turnover". It will print a tuple of the symbol and the value of the property. 

```python3 nepse.py top gainer```

This will print the top 5 gainers.

```python3 nepse.py top looser```

```python3 nepse.py top turnover```

If you want to print a certain number of top scrips, you can use the option --n.

For example, 

```python3 nepse.py top gainer --n 10```

This command will print the top 10 gainers of the latest trading day.

Remember that the max value for --n is 10. So, app will throw an exception of list out of range

