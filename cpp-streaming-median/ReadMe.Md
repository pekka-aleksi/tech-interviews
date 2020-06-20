Streaming Median: C++
===

The Streaming Median is the median number of a constantly updating datastream, and not of some fixed dataset.

C++ Implementation of a Streaming Median. I used two heaps to implement the calculation of the streaming median in a fast way.

This piece of code has this stupid bug I forgot to fix for the final submission (the code actually works) that makes the performance of the algorithm much worse than it needs to be. The algorithm rebuilds the heaps when it doesn't need to. I just used the `std::make_heap` function at first to make sure there was a heap in place.



