# Algorithms

- **closet_pair_of_points.py**:
This is a basic primitive in computational geometry having applications in,for example, graphics, computer vision, traffic-control systems. A naive algorithm with quadratic running time iterates through all pairs of points to find the closest pair. Here I designed an 𝑂(𝑛 log 𝑛) time divide and conquer_approach algorithm. To solve this problem in time 𝑂(𝑛 log 𝑛), we first split the given 𝑛 points by an appropriately chosen vertical line into two halves 𝑆1 and 𝑆2 of size 𝑛/2. Make two recursive calls for the sets 𝑆1 and 𝑆2 find d1 and d2, create a strip of points around the splitting axis with size 2* min(d1, d2) and return the minum distance found in this strip( See the code for more details). Here are the plots for the naive and the divide&conquer approach . We see clearly that the naive approach is too exhaustive and take too much time on a relatively small sets in the order of thousands. 
![runningtime plot1](https://github.com/ilyasAr/Algorithms/blob/master/naive_approach.png) 
![runningtime plot2](https://github.com/ilyasAr/Algorithms/blob/master/divide%26conquer_approach.png)

*remarque* : The more the data have same coordinates on a certain dimension the more it takes less time to find the closest distance, as it take less recursive calls.

- **randomized-quick_sort.py**: 
Detailed algorithm for randomized quick-sort that adapts to a sequence containing many equal elements, with O(n log(n) ) runningtime. Using only 2 partitions will lead to a quadratic runningtimeO(n²). 
![runningtime plot3](https://github.com/ilyasAr/Algorithms/blob/master/quick_sort.png)

- **editDistance_2_sequences.py**:
The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions of symbols) to transform one string into another. It is a measure of similarity of two strings. Edit distance has applications, for example, in computational biology, natural language processing, and spell checking. For instance, given two sequences of a DNA, we can quantify the similarity between the two sequences and the optimal transformation from sequence 1 to sequence 2 which can be viewd as strings of the letters A, C, G and T. The straightforward, recursive way of evaluating this recurrence takes exponential time. Given a string A of length n and B of length m and using Dynamic programming, we will construct a matrix D of size (n+1)x(m+1), such that D(i, j) is the minimal editing distance between A(0:i) and B(0:j). Consequently, the algorithm return D(n, m) as the minimal editing distance between A and B. The complexity is that of constructing the matrix D, so O(nm) and finding the transformation afterwards is done in O(m +n).


