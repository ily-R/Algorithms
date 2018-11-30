# Algorithms

- **closet_pair_of_points.py**:
An optimized algorithm that calculates the smallest distance between a pair of points among the given 𝑛 points. This is a basic primitive in computational geometry having applications in,for example, graphics, computer vision, traffic-control systems. A naive algorithm with quadratic running time iterates through all pairs of points to find the closest pair. Here I designed an 𝑂(𝑛 log 𝑛) time divide and conquer_approach algorithm. To solve this problem in time 𝑂(𝑛 log 𝑛), we first split the given 𝑛 points by an appropriately chosen vertical line into two halves 𝑆1 and 𝑆2 of size 𝑛/2. Make two recursive calls for the sets 𝑆1 and 𝑆2 and merge the result on both sides( See the code for more details). Here are the plots for the naive and the divide&conquer approach . We see clearly that the naive approach is too exhaustive and take too much time on a relatively small sets in the order of thousands.
- **randomized-quick_sort.py**: 
Detailed algorithm for randomized quick-sort that adapts to a sequence containing many equal elements, with O(n log(n) ) runningtime. Using only 2 partitions will lead to a quadratic runningtimeO(n²). [runningtime plot](https://github.com/ilyasAr/Algorithms/blob/master/quick_sort.png)


