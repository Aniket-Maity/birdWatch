#problem statement
-----------------------------------------------------------------------



You have been asked to help study the population of birds migrating across the continent. Each type of bird you are interested in will be identified by an integer value. Each time a particular kind of bird is spotted, its id number will be added to your array of sightings. You would like to be able to find out which type of bird is most common given a list of sightings. Your task is to print the type number of that bird and if two or more types of birds are equally common, choose the type with the smallest ID number.



For example, assume your bird sightings are of types arr = [1,1,2,2,3] . There are two each of types 1 and 2 , and one sighting of type 3. Pick the lower of the two types seen twice: type 1 .



Write a program which will output the lowest type number of the most frequently sighted bird.

Extra Info


Input Format
The first line contains an integer n denoting , the number of birds sighted and reported in the array arr.

The second line describes arr as  space-separated integers representing the type numbers of each bird sighted.

Output Format
Print the type number of the most common bird; if two or more types of birds are equally common, choose the type with the smallest ID number.

Constraints
5 <= n <= 2* 10^5

It is guaranteed that each type is 1 or 2 or 3 or 4 or 5 .

Time Limit
2s
Each test case should pass in 2s.
Sample Input
6 
1 4 4 4 5 3
Sample Output
4
