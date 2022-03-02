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
