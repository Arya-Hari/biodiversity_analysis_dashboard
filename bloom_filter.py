from bloomfilter import BloomFilter
import pandas as pd

def main():
    bloom_filter = BloomFilter(100000, 0.001)
    data = load_data('modified_biodiversity_dataset.csv')
    process_data(bloom_filter,data)
    print("Ursus maritimus" in bloom_filter)
    print("Spalgis epius" in bloom_filter)

def process_data(bloom_filter,data):
    for i, row in data.iterrows():
        species = row['species']
        bloom_filter.add(str(species))
    
def load_data(filename):
    # read in the CSV data
    df = pd.read_csv(filename, encoding='utf-8')
    
    return df

if __name__ == '__main__':
    main()
