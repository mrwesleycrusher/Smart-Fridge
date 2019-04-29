#include "scanInput.h"


int scanForCode(char* code){
    printf("\nWaiting for Code\n");
    scanf("%s",code);
    printf("Code: %s received", code);
    return 0;
}

//for usb hid code scanning
// int scanForCode(BarcodeScanner* scanner){
    
//     printf("Waiting for code\n");
//     //FILE* fptr;
//     int ptr;
//     FILE* wfptr;
//     unsigned char cod[64];
//     for(int i = 0; i<40;i++){
//         ptr = open("/dev/hidraw0", 'r');
//         read(ptr,cod,sizeof(cod));
               
//     }
//     wfptr = fopen("test.txt","wb");
//     fwrite(cod,sizeof(cod),1,wfptr);
//     return 0;
        
    

// }