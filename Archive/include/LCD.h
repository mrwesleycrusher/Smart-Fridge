#ifndef LCD_H
#define LCD_H

#include <stdlib.h>

#include <wiringPi.h>          
#include <lcd.h>

 
//USE WIRINGPI PIN NUMBERS
#define LCD_RS  25               //Register select pin
#define LCD_E   24               //Enable Pin
#define LCD_D4  23               //Data pin 4
#define LCD_D5  22               //Data pin 5
#define LCD_D6  21               //Data pin 6
#define LCD_D7  14               //Data pin 7


/************************************
Holds data for LCD display
TODO - make static? only allowed one instance??
*************************************/ 
typedef struct fridgeDisplay{
    // char[32] currentText;
    int lcd;
} fridgeDisplay;

/************************************
Initializes LCD
Must be run for each instance of LCD struct
*************************************/
void fridge_init(fridgeDisplay* p);

/************************************
Displays string that is passed
Uses default formatting
*************************************/
void fridge_display(fridgeDisplay* p, char* str);

/************************************
Clears LCD
*************************************/
void fridge_clear(fridgeDisplay* p);
#endif