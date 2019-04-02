#include <wiringPi.h>          
#include <lcd.h>               
 
//USE WIRINGPI PIN NUMBERS
#define LCD_RS  25               //Register select pin
#define LCD_E   24               //Enable Pin
#define LCD_D4  23               //Data pin 4
#define LCD_D5  22               //Data pin 5
#define LCD_D6  21               //Data pin 6
#define LCD_D7  14               //Data pin 7
#define LCDBroke "uwu *is broken*"
 
typedef struct fridgeDisplay{
    // char[32] currentText;
    int lcd;
} fridgeDisplay;

// Initializes LCD
void init(fridgeDisplay* p){
    // p.currentText = malloc(sizeof(char)*32);
    wiringPiSetup();        
    p.lcd = lcdInit (2, 16, 4, LCD_RS, LCD_E, LCD_D4, LCD_D5, LCD_D6, LCD_D7, 0, 0, 0, 0);
    lcdClear(p.lcd);
}

//***************************
//display
//Struct: fridgeDisplay
//Input: struct fridgeDisplay *p
//
void display(fridgeDisplay *p, char[] string){
    lcdputs(p.lcd,string);
}



//uwu
static void uwuTFOutOfIt(){
    lcdClear(lcd);
    lcdPuts(lcd, LCDBroke);   
    exit(-1);
}