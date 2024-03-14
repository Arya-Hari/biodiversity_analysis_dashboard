import pandas as pd
import hyperloglog

def main():
    kingdomSketch = hyperloglog.HyperLogLog(0.01)
    phylumSketch = hyperloglog.HyperLogLog(0.01)
    classSketch = hyperloglog.HyperLogLog(0.01)
    orderSketch = hyperloglog.HyperLogLog(0.01)
    familySketch = hyperloglog.HyperLogLog(0.01)
    genusSketch = hyperloglog.HyperLogLog(0.01)
    speciesSketch = hyperloglog.HyperLogLog(0.01)
    sketch = [kingdomSketch,phylumSketch,classSketch,orderSketch,familySketch,genusSketch,speciesSketch]
    
    data = load_data('modified_biodiversity_dataset.csv')
    process_data(sketch,data)
    print("Kingdom Cardinality : ",len(kingdomSketch))
    print("Phylum Cardinality : ",len(phylumSketch))
    print("Class Cardinality : ",len(classSketch))
    print("Order Cardinality : ",len(orderSketch))
    print("Family Cardinality : ",len(familySketch))
    print("Genus Cardinality : ",len(genusSketch))
    print("Species Cardinality : ",len(speciesSketch))

def process_data(sketch,data):
    for i, row in data.iterrows():
        sketch[0].add(str(row['kingdom']))
        sketch[1].add(str(row['phylum']))
        sketch[2].add(str(row['class']))
        sketch[3].add(str(row['order']))
        sketch[4].add(str(row['family']))
        sketch[5].add(str(row['genus']))
        sketch[6].add(str(row['species']))

def load_data(filename):
    # read in the CSV data
    df = pd.read_csv(filename, encoding='utf-8')

    return df

if __name__ == '__main__':
  main()
  