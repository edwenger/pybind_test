class Cohort {

public:
    Cohort(int count);
    const int getCount() const;
    void setCount(const int count_);
    int drawFraction(const float fraction_);

private:
    int count;
};
