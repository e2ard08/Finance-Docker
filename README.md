# Finance App

## Description

Finance App is a web application built with Flask that allows users to query information about the stock prices of various companies that pay dividends. The application displays a table with the following data:

- Company name
- Current stock price
- Percentage of dividends generated
- Quote date

Users can filter results by stock price and dividend percentage.

## Requirements

- Python 3.x
- Docker installed on your machine.
- Internet access to download images and access stock data.

## Steps to Run the Environment with Docker

1. **Clone the Repository**

   Open your terminal and clone the GitHub repository (replace `<your-repo-url>` with the URL of your repository):

   ```bash
   git clone <your-repo-url>
   cd repo-name

2. **Run the Application: Once the image is built, run the following command to start the application:**

   ```bash
   docker run -p 5000:5000 finance-app

Access the Application: Open your browser and navigate to http://localhost:5000 to see the application in action.

#Code Structure
The main file of the application is app.py

#Contributions
If you want to contribute to this project, feel free to submit a pull request or open an issue on GitHub.
