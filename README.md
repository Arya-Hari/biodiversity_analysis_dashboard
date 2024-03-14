# biodiversity_analysis_dashboard

Biodiversity analysis of data from the Indian Biodiversity Portal was done to understand the variety and variability of flora and fauna in Indian forests and demonstrate the use of probabilistic data structures in data analysis.

The data structures used and the reason for use have been expanded below - 
* Bloom Filters - Bloom filters were used to implement a search feature for users to search for the presence/absence of a particular species in Indian forests.
* Count Min-Sketch - It was used to count the frequency of species in distinct families, genera, etc. The top three most recurring items were identified by implementing a heavy keeper algorithm using a min-heap.
* HyperLogLog - It was used to find the number of distinct kingdoms, species, genera, etc., as present in the dataset

The implementation is entirely in Python.

References -
* https://github.com/svpcom/hyperloglog
* https://github.com/21zhouyun/CountMinSketch
* https://techtonics.medium.com/implementing-bloom-filters-in-python-and-understanding-its-error-probability-a-step-by-step-guide-13c6cb2e05b7
* https://www.geeksforgeeks.org/min-heap-in-python/
