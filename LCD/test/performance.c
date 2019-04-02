#include <stdio.h>
#include <time.h>
#include "LCD.h"

int main(){
    fridgeDisplay p;
    fridgeDisplay *disp = &p;
    double time_taken = 0;
    clock_t t;
    t = clock();
    fridge_init(disp);
    t = clock() - t;
    time_taken = ((double)t)/CLOCKS_PER_SEC;
    printf("\nInit finished in %f seconds",time_taken);
    t = clock();
    fridge_display(disp,"ripipipipipipipipipipipipipipipipip");
    t = clock() - t;
    time_taken = ((double)t)/CLOCKS_PER_SEC;
    printf("\nDisplay finished in %f seconds",time_taken);
    return 0;

}