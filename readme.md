### What is rfm python model

The RFM stand for Recency, frequency, monetary value (RFM) is a marketing analysis tool used to identify a firm's best clients based on the nature of their spending habits.

### Key Takeaways

    Recency, frequency, monetary value (RFM) is a marketing analysis tool used to identify a firm's best clients based on the nature of their spending habits.
    An RFM analysis evaluates clients and customers by scoring them in three categories: how recently they've made a purchase, how often they buy, and the size of their purchases.
    RFM analysis helps firms reasonably predict which customers are likely to purchase their products again, how much revenue comes from new (versus repeat) clients, and how to turn occasional buyers into habitual ones.

Understanding Recency, Frequency, Monetary Value

The RFM model is based on three quantitative factors:

    Recency: How recently a customer has made a purchase
    Frequency: How often a customer makes a purchase
    Monetary Value: How much money a customer spends on purchases

RFM analysis numerically ranks a customer in each of these three categories, generally on a scale of 1 to 5 (the higher the number, the better the result). The "best" customer would receive a top score in every category.

These three RFM factors can be used to reasonably predict how likely (or unlikely) it is that a customer will do business again with a firm or, in the case of a charitable organization, make another donation. 

You can read more about RFM from here https://www.investopedia.com/terms/r/rfm-recency-frequency-monetary-value.asp

### HOW TO WORK WITH THI MODEL

### required modules
```
pip install -r modules.txt
```

or use

pip install 
```
numpy
pandas
plotly
python_dateutil
streamlit
```

### Datasets

* Make sure you follow the structure of the input.csv file,
  If you have data in spreadsheet file, don't change the extension with .csv, "instead save the spreadsheet as .csv" 

## The Model

You can find the code in the model.py 
 
### Review the Output of the model

When you run the model.py, the new csv file with name output.csv will be generated in the
output folder,
You can also use a basic streamlit app file included in the project folder, it has the
name app.py.
The app will allow you to do analyse and review RFM scores in the output data,
the score includes all churn types

NB
You havr to run the model first and then the app with the following command:  

```
python model.py 

streamlit run app.py

```
Access the app via the localhost link provided via cmd/powershell.
