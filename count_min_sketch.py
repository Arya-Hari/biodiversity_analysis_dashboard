from hashfactory import hash_function
from countminsketch import CountMinSketch
import pandas as pd

def process_data(sketch,data):
    for i, row in data.iterrows():
        use = row['kingdom']
        sketch.add(use,1)
    

def load_data(filename):
    # read in the CSV data
    df = pd.read_csv(filename, encoding='utf-8')
    
    return df

def output(sketch):
   outputs = []
   outputs.append(["Animalia",sketch.query("Animalia")])
   outputs.append(["Plantae",sketch.query("Plantae")])
   outputs.append(["incertae sedis",sketch.query("incertae sedis")])
   outputs.append(["Fungi",sketch.query("Fungi")])
   outputs.append(["Bacteria",sketch.query("Bacteria")])
   return outputs

  