from hashfactory import hash_function
from countminsketch import CountMinSketch
from count_min_sketch import load_data, process_data,output
from minheap import MinHeap
import pandas as pd

def main():
    depth = 8
    width = 2**22
    hash_functions = [hash_function(i) for i in range(depth)]
    sketch = CountMinSketch(depth, width, hash_functions)
    data = load_data('modified_biodiversity_dataset.csv')
    process_data(sketch,data)
    minHeap = MinHeap(3)
    outputs = output(sketch)
    print(outputs)
    for i in outputs:
       minHeap.insert(i)
    ls = minHeap.Print()
    for i in outputs:
       if i[1] in ls:
          print(i[0]," : ",i[1])
    


if __name__ == '__main__':
  main()
  