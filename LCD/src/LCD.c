#include "LCD.h"

#define LCDBroke "uwu *is broken*"

/************************************
Initializes LCD
Must be run for each instance of LCD struct
*************************************/
void fridge_init(fridgeDisplay* p){
    // p.currentText = malloc(sizeof(char)*32);
    //p = malloc(sizeof(fridgeDisplay));
    wiringPiSetup();        
    p->lcd = lcdInit (2, 16, 4, LCD_RS, LCD_E, LCD_D4, LCD_D5, LCD_D6, LCD_D7, 0, 0, 0, 0);
    lcdClear(p->lcd);
}

/************************************
Displays string that is passed
Uses default formatting for now
*************************************/
void fridge_display(fridgeDisplay* p, char* str){
    lcdPuts(p->lcd,str);
}

/************************************
Clears LCD
*************************************/
void fridge_clear(fridgeDisplay* p){
    lcdClear(p->lcd);
}

/************************************
UWU
*************************************/
void uwuTFOutOfIt(fridgeDisplay* p){
    lcdClear(p->lcd);
    lcdPuts(p->lcd, LCDBroke);   
    exit(-1);
}
