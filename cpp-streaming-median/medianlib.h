//
// Created by Pekka on 30.9.2019.
//
#include <vector>

#ifndef MEDIANLIB_H
#define MEDIANLIB_H

class StreamingMedian {

    std::vector<int> lows;
    std::vector<int> highs;

public:
    StreamingMedian();
    explicit StreamingMedian(std::vector<int>);


    float get();
    void add(int);
};

#endif //MEDIANLIB_H
