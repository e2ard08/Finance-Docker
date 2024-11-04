from flask import Flask, render_template_string
import yfinance as yf
from datetime import datetime

app = Flask(__name__)

# Diccionario con los símbolos de las acciones y nombres completos
stocks = {
    "JNJ": "Johnson & Johnson", "PG": "Procter & Gamble", "KO": "Coca-Cola",
    "PEP": "PepsiCo", "MMM": "3M Company", "ABBV": "AbbVie", "CL": "Colgate-Palmolive",
    "T": "AT&T Inc.", "VZ": "Verizon Communications", "MCD": "McDonald’s",
    "KMB": "Kimberly-Clark", "XOM": "Exxon Mobil", "CVX": "Chevron Corporation",
    "IBM": "IBM", "INTC": "Intel Corporation", "MRK": "Merck & Co.",
    "PFE": "Pfizer Inc.", "TXN": "Texas Instruments", "CAT": "Caterpillar",
    "NEE": "NextEra Energy", "WBA": "Walgreens Boots Alliance", "GIS": "General Mills",
    "O": "Realty Income", "AMGN": "Amgen Inc.", "DUK": "Duke Energy",
    "SO": "Southern Company", "LMT": "Lockheed Martin", "MO": "Altria Group",
    "PM": "Philip Morris International", "BLK": "BlackRock Inc.",
    "TGT": "Target Corporation", "ITW": "Illinois Tool Works", "ED": "Consolidated Edison",
    "SYY": "Sysco Corporation", "WM": "Waste Management", "D": "Dominion Energy",
    "ALL": "Allstate Corporation", "AEP": "American Electric Power", "UNP": "Union Pacific",
    "CB": "Chubb Ltd", "WMT": "Walmart Inc.", "MDT": "Medtronic plc",
    "HON": "Honeywell International", "UPS": "United Parcel Service", "LOW": "Lowe’s Companies",
    "CLX": "Clorox Company", "TROW": "T. Rowe Price Group", "LLY": "Eli Lilly and Company",
    "GE": "General Electric", "TRV": "Travelers Companies", "AMT": "American Tower Corporation",
    "JCI": "Johnson Controls", "AMAT": "Applied Materials", "BMY": "Bristol-Myers Squibb",
    "DE": "Deere & Company", "BAC": "Bank of America", "JPM": "JPMorgan Chase & Co.",
    "ORCL": "Oracle Corporation", "QCOM": "Qualcomm", "AVGO": "Broadcom Inc.",
    "COST": "Costco Wholesale", "BBY": "Best Buy Co.", "DG": "Dollar General",
    "DFS": "Discover Financial Services", "GS": "Goldman Sachs", "PFG": "Principal Financial Group",
    "PRU": "Prudential Financial", "KEY": "KeyCorp", "FITB": "Fifth Third Bancorp",
    "KMI": "Kinder Morgan", "MPC": "Marathon Petroleum", "VLO": "Valero Energy Corporation",
    "OKE": "Oneok Inc.", "COP": "ConocoPhillips", "OXY": "Occidental Petroleum",
    "EOG": "EOG Resources", "RTX": "Raytheon Technologies", "NOC": "Northrop Grumman",
    "LHX": "L3Harris Technologies", "PNC": "PNC Financial Services", "WFC": "Wells Fargo & Company",
    "C": "Citigroup", "MS": "Morgan Stanley", "USB": "U.S. Bancorp", "TFC": "Truist Financial",
    "FE": "FirstEnergy Corp", "PEG": "Public Service Enterprise Group", "NRG": "NRG Energy",
    "NEM": "Newmont Corporation", "GOLD": "Barrick Gold Corporation", "DOW": "Dow Inc.",
    "CTVA": "Corteva Inc.", "CF": "CF Industries Holdings", "ADM": "Archer Daniels Midland",
    "DRI": "Darden Restaurants", "SBUX": "Starbucks Corporation", "YUM": "Yum! Brands, Inc.",
    "MKC": "McCormick & Company", "HSY": "Hershey Company", "CPB": "Campbell Soup Company"
}

@app.route("/")
def index():
    # Obtener precios y dividendos
    data = {}
    for symbol, name in stocks.items():
        ticker = yf.Ticker(symbol)
        price = ticker.history(period="1d")['Close'].iloc[-1]
        dividend_yield = ticker.info.get('dividendYield')
        
        if dividend_yield is not None:
            dividend_yield = dividend_yield * 100  # Convertir a porcentaje
        else:
            dividend_yield = 0  # Si no hay datos, asignar 0

        data[name] = {'price': price, 'dividend_yield': dividend_yield}

    # Ordenar por precios de menor a mayor
    sorted_data = dict(sorted(data.items(), key=lambda item: item[1]['price']))

    # Fecha de la cotización
    quote_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Plantilla HTML con la fecha de cotización y los datos en una tabla
    html_template = """
    <html>
    <head>
        <title>Stock Prices and Dividend Yields</title>
        <style>
            table { width: 80%; margin: auto; border-collapse: collapse; }
            th, td { padding: 10px; border: 1px solid #ddd; text-align: center; }
            th { background-color: #f2f2f2; }
            body { font-family: Arial, sans-serif; }
            .header { text-align: right; font-size: small; padding: 20px; }
        </style>
    </head>
    <body>
        <div class="header">Fecha de cotización: {{ quote_date }}</div>
        <h1 style="text-align: center;">Stock Prices and Dividend Yields</h1>
        <table>
            <tr>
                <th>Company</th>
                <th>Price (USD)</th>
                <th>Dividend Yield (%)</th>
            </tr>
            {% for name, info in sorted_data.items() %}
            <tr>
                <td>{{ name }}</td>
                <td>${{ "{:.2f}".format(info['price']) }}</td>
                <td>{{ "{:.2f}".format(info['dividend_yield']) }}%</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """
    return render_template_string(html_template, quote_date=quote_date, sorted_data=sorted_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
