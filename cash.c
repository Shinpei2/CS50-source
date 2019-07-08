#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    float dollars;
    do
    {
        dollars = get_float("Change:");
    }
    while (dollars <= 0);
    int cents = round(dollars * 100);
    //printf("%i\n",cents);

    int coinNum = 0;
    while (cents >= 25)
    {
        cents -= 25;
        coinNum += 1;
        //printf("cents:%i\n",cents);
        //printf("coinNum:%i\n",coinNum);
    }
    
    while (cents >= 10)
    {
        cents -= 10;
        coinNum += 1;
        //printf("cents:%i\n",cents);
        //printf("coinNum:%i\n",coinNum);
    }
    
    while (cents >= 5)
    {
        cents -= 5;
        coinNum += 1;
        //printf("cents:%i\n",cents);
        //printf("coinNum:%i\n",coinNum);
    }
    
    while (cents >= 1)
    {
        cents -= 1;
        coinNum += 1;
        //printf("cents:%i\n",cents);
        //printf("coinNum:%i\n",coinNum);
    }
    printf("%i\n", coinNum);
}
