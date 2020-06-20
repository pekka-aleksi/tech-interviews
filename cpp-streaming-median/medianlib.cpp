#include "medianlib.h"
#include <cmath>
#include <algorithm>
#include <tuple>
#include <iostream>

StreamingMedian::StreamingMedian() = default;


StreamingMedian::StreamingMedian(std::vector<int> y) {
    std::sort(y.begin(), y.end());

    // the algorithm will take a vector of numbers [0, 5, 10, 11] and split it into 2 heaps
    size_t const median_index = std::floor(y.size()/2);

    for (auto [it, index] = std::tuple{y.begin(), 0}; it != y.end(); it++, index++) {

        if (index < median_index) {
            std::cout << *it << " goes to lows!" << std::endl;

            this->lows.push_back(*it);
        }
        else {

            std::cout << *it << " goes to highs!" << std::endl;

            this->highs.push_back(*it);
        }
    }


    std::make_heap(this->lows.begin(), this->lows.end());
    std::make_heap(this->highs.begin(), this->highs.end(), std::greater<>{});

}



float StreamingMedian::get() {

    if (this->lows.empty() && this->highs.empty())
        throw std::range_error("Range error: The median data structure is empty! Cannot get from empty!");

    else if (this->lows.size() == this->highs.size()) {
        std::cout << "returning average of " << this->lows[0] << " and " << this->highs[0] << std::endl;

        return (this->lows[0] + this->highs[0]) / 2.0;
    }
    else if (this->lows.size() > this->highs.size()) {

        std::cout << "Lows are larger, returning " << this->lows[0] << std::endl;


        for (auto P: this->lows) {
            std::cout << "LOW " << P << std::endl;
        }

        for (auto P: this->highs) {
            std::cout << "HIGH " << P << std::endl;
        }
        return this->lows[0];

    }

    else {
        std::cout << "Highs are larger, returning " << this->highs[0] << std::endl;
        for (auto P: this->lows) {
            std::cout << "LOW " << P << std::endl;
        }

        for (auto P: this->highs) {
            std::cout << "HIGH " << P << std::endl;
        }
        return this->highs[0];

    }
}

void StreamingMedian::add(int n) {

    if (this->highs.empty() && this->lows.empty()) {
        this->lows.push_back(n);
    }
    else {
        float effectiveMedian = std::numeric_limits<float>::max();

        if (this->highs.size() < this->lows.size())
            effectiveMedian = this->lows[0];
        else if (this->highs.size() > this->lows.size())
            effectiveMedian = this->highs[0];
        else {
            if (!this->highs.empty() && !this->lows.empty()) {
                effectiveMedian = (this->highs[0] + this->lows[0]) / 2.0;
            }
        }

        if (n < effectiveMedian) {
            std::cout << n << " < " << effectiveMedian << std::endl;

            if (this->highs.size() < this->lows.size() && n <= this->lows[0]) {

                std::cout << "cleaning house since " << n << " <= " << this->lows[0] << std::endl;

                this->highs.push_back(this->lows[0]);
                this->lows.pop_back();
                this->lows.push_back(n);
                std::make_heap(this->highs.begin(), this->highs.end(), std::greater<>{});

            }
            else {
                this->lows.push_back(n);
            }
            std::make_heap(this->lows.begin(), this->lows.end());
        } else {
            std::cout << n << " >= " << effectiveMedian << std::endl;

            if (this->highs.size() > this->lows.size() && n >= this->highs[0]) {

                std::cout << "cleaning house since " << n << " >= " << this->highs[0] << std::endl;

                this->lows.push_back(this->highs[0]);
                this->highs.pop_back();
                this->highs.push_back(n);
                std::make_heap(this->lows.begin(), this->lows.end());

            } else {
                this->highs.push_back(n);
            }

            std::make_heap(this->highs.begin(), this->highs.end(), std::greater<>{});
        }

    }
}

