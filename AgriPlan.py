#include <iostream>
#include <iomanip>
using namespace std;

class currentBill {
public:
    virtual double amount() = 0; // Pure virtual function
    virtual ~currentBill() {}
};

class Fan : public currentBill {
public:
    double watts, hours;
    Fan(double w, double h) {
        watts = w;
        hours = h;
    }
    double amount() override {
        return (watts * hours) / 1000.0 * 2.4; // rate = ₹2.4 per kWh
    }
};

class Light : public currentBill {
public:
    double watts, hours;
    Light(double w, double h) {
        watts = w;
        hours = h;
    }
    double amount() override {
        return (watts * hours) / 1000.0 * 2.4;
    }
};

class TV : public currentBill {
public:
    double watts, hours;
    TV(double w, double h) {
        watts = w;
        hours = h;
    }
    double amount() override {
        return (watts * hours) / 1000.0 * 2.4;
    }
};

int main() {
    double fw, fh, lw, lh, tw, th;
    cin >> fw >> fh >> lw >> lh >> tw >> th;

    currentBill* fan = new Fan(fw, fh);
    currentBill* light = new Light(lw, lh);
    currentBill* tv = new TV(tw, th);

    double total = fan->amount() + light->amount() + tv->amount();

    cout << fixed << setprecision(2) << total;

    delete fan;
    delete light;
    delete tv;

    return 0;
}
