# Create a class with an insert method to insert an int to a list. It should also support calculating the max, min, mean, and mode in O(1).

## Algorithm
* We'll init our max and min to None. Alternatively, we can init them to -sys.maxsize and sys.maxsize, respectively.
* For mean, we'll keep track of the number of items we have inserted so far, as well as the running sum.
* For mode, we'll keep track of the current mode and an array with the size of the given upper limit
    * Each element in the array will be init to 0
    * Each time we insert, we'll increment the element corresponding to the inserted item's value
* On each insert:
    * Update the max and min
    * Update the mean by calculating running_sum / num_items
    * Update the mode by comparing the mode array's value with the current mode

## Constraints
* Can we assume the inputs are valid?
    * No
* Is there a range of inputs?
    * 0 <= item <= 100
* Should mean return a float?
    * Yes
* Should the other results return an int?
    * Yes
* If there are multiple modes, what do we return?
    * Any of the modes
* Can we assume this fits memory?
    * Yes