#ifndef SCANINPUT
#define SCANINPUT

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int scanForCode(char* code);
#endif