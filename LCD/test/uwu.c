#include <stdio.h>
#include <time.h>
#include "LCD.h"

void uwuTFOutOfIt(fridgeDisplay* p);
int main(){
    fridgeDisplay p;
    fridgeDisplay *disp = &p;

    fridge_init(disp);
    uwuTFOutOfIt(disp);

}