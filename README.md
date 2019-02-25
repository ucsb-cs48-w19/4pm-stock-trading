# 4pm-stock-trading

URL to current app: https://stocktrading-4pm-mvp.herokuapp.com/

Travis CI to the master branch
<a href="https://travis-ci.org/ucsb-cs48-w19/4pm-stock-trading">
<img src="https://travis-ci.org/ucsb-cs48-w19/4pm-stock-trading?branch=master" alt="Build Status">
</a>

## Project summary

### An app that displays information about stocks and provides recommendations to the user.

### One-sentence description of the project

A simple easy to use app that helps you make more informed stock-related decisions.

### Additional information about the project

This app displays a list of popular stocks and allows you to choose which ones you want to learn more about. Once you choose a stock, you will be able to see important information about it such as its current price per unit and a graph of its recent price history. In addition, the app will recommend stocks for you to buy based on your interests and specifications.

## Installation

### Prerequisites

* Flask version 1.0.2
* Python version 3.6 and above
* iexfinance version 0.3.5
* plotly version 3.6.1
* matplotlib version 3.0.2
* numpy version 1.16.1
* pandas version 0.24.1
* ipython version 7.2.0

### Installation Steps

This assumes that Python 3.6 and above is installed.

Install all the required Python modules using this command:
`$ pip install -r requirements.txt`

## Functionality

Deploy your `StockApp.py` script by executing the command

`$ FLASK_APP=StockApp.py flask run`

The site is deployed locally at http://localhost:5000/.

## Known Problems

We are currently using Plotly to construct our graphs. However, every free account has a limit of 25 public graphs available. So, we must create a new account and input the new information into the top of 'graph.py' every time we run out of graphs for that account.

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License

Licensed under MIT License.
