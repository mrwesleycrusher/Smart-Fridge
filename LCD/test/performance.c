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
    char testc = ' ';
    double average = 0;
    char *c;
    int i = 0;
    printf("\nSingle Character Test\n-----------------------------s");
    for(i = 0; i!=0x7f; i++){
        t = clock();
        c = &testc;
        fridge_display(disp,c);
        t = clock() - t;
        time_taken = ((double)t)/CLOCKS_PER_SEC;
        average += time_taken;
        //printf("\n%f",time_taken);
        testc++;
    }
    average /= i;
    printf("\nSingle chars take %f seconds\n",average);

    printf("\n32 Character Test\n-----------------------------");
    for(i = 0; i < 100; i++){
        t = clock();
        fridge_display(disp,"12345678901234567890123456789012");
        t = clock() - t;
        time_taken = ((double)t)/CLOCKS_PER_SEC;
        average += time_taken;
        //printf("\n%f",time_taken);
    }
    average /= i;
    printf("\n32 Chars take %f seconds\n",average);
    
    printf("\n32 Character With Clear Test\n-----------------------------");
    for(i = 0; i < 100; i++){
        t = clock();
        fridge_display(disp,"12345678901234567890123456789012");
        fridge_clear(disp);
        t = clock() - t;
        time_taken = ((double)t)/CLOCKS_PER_SEC;
        average += time_taken;
        //printf("\n%f",time_taken);
    }
    average /= i;
    printf("\n32 Chars take %f seconds",average);

    fridge_clear(disp);
    fridge_display(disp,"god is dead");
    return 0;

}