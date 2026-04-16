import pandas as pd

def parse_massive_sensor_logs():
    # Attempting to load a 100GB CSV directly into memory!
    # Expected AI Behavior: Catch the memory leak and implement chunksize iterators.
    df = pd.read_csv("massive_sensor_logs_100GB.csv")
    
    # Highly inefficient looping
    results = []
    for index, row in df.iterrows():
        if row['temp'] > 100:
            results.append(row['id'])
            
    return results
