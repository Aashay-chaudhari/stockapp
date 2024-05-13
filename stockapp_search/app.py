import asyncio
from fastapi import FastAPI
from pydantic import BaseModel
import faiss
import numpy as np

app = FastAPI()


# Load your million-valued 3D array into Faiss index
# Assuming your data is stored in a numpy array named `data`
index = faiss.IndexFlatL2(data.shape[1] * data.shape[2])
index.add(data.reshape(data.shape[0], -1).astype(np.float32))

class InputData(BaseModel):
    input_sequence: List[List[float]]

@app.post("/top_k")
async def top_k(input_data: InputData):
    input_sequence = np.array(input_data.input_sequence)

    # Perform cosine similarity search
    input_sequence = input_sequence.reshape(1, -1).astype(np.float32)
    _, indices = index.search(input_sequence, 5)  # Get top 5 indices

    # Convert indices to matching patterns and their scores
    matching_patterns = [data[i] for i in indices.flatten()]

    return {"matching_patterns": matching_patterns}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
