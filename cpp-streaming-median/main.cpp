//
// Created by Pekka on 30.9.2019.
//
#include "medianlib.h"
#include <iostream>
#include <exception>
#include <gtest/gtest.h>


TEST(StreamingMedian, EmptyGet) {
    std::vector<int> data = {};
    StreamingMedian x(data);
    EXPECT_THROW(x.get(), std::range_error);
}

TEST(StreamingMedian, OneGet) {
    std::vector<int> data = {1};
    StreamingMedian x(data);
    EXPECT_FLOAT_EQ(x.get(), 1);
}

TEST(StreamingMedian, TwoGet) {
    std::vector<int> data = {1, 2};
    StreamingMedian x(data);
    EXPECT_FLOAT_EQ((1+2)/2.0, x.get());
}

TEST(StreamingMedian, ThreeGet) {
    std::vector<int> data = {1, 2, 3};
    StreamingMedian x(data);
    EXPECT_FLOAT_EQ(2, x.get());
}

TEST(StreamingMedian, FourGet) {
    std::vector<int> data = {1, 2, 3, 4};
    StreamingMedian x(data);
    EXPECT_FLOAT_EQ((2+3)/2.0, x.get());
}



TEST(StreamingMedian, OneAddGet) {
    std::vector<int> data = {1};
    StreamingMedian x;

    for (auto v: data)
        x.add(v);

    EXPECT_FLOAT_EQ(x.get(), 1);
}

TEST(StreamingMedian, TwoAddGet) {
    std::vector<int> data = {77, -78};
    StreamingMedian x;

    for (auto v: data)
        x.add(v);

    EXPECT_FLOAT_EQ((77+(-78))/2.0, x.get());
}

TEST(StreamingMedian, ThreeAddGet) {
    std::vector<int> data = {33, -100, 100};
    StreamingMedian x;

    for (auto v: data)
        x.add(v);

    EXPECT_FLOAT_EQ(33, x.get());
}

TEST(StreamingMedian, FourAddGet) {
    std::vector<int> data = {4, -1, 0, 7};
    StreamingMedian x;

    for (auto v: data)
        x.add(v);
    EXPECT_FLOAT_EQ((0+4)/2.0, x.get());
}

int main (int argc, char ** argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}