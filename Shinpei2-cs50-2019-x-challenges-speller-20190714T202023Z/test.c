#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 26

int hashtable[N];

int main (void){
    int size = sizeof(hashtable[N]) / sizeof(int);
    printf("hashtable: %i\n", N);
}