import pandas as pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def get_dataframe():
    # Create a simple DataFrame
    data = {'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35],
            'City': ['New York', 'Los Angeles', 'Chicago']}
    
    df = pd.DataFrame(data)
    
    # Convert the DataFrame to HTML
    html = df.to_html()

    return html