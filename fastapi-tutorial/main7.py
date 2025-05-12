#Plotting

import io
import matplotlib.pyplot as plt
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.get("/plot")
async def get_plot():
    # Generate a plot
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [10, 20, 25, 30])

    # Save the plot to a BytesIO buffer
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)  # Rewind the buffer to the beginning

    # Return the image as a StreamingResponse
    return StreamingResponse(buf, media_type="image/png")