#include <cs50.h>
#include <stdio.h>

int main(void)
{   
    //高さを入力
    int height;
    do
    {
        height = get_int("Height: ");
    } 
    while (height < 1 || 8 < height);
    
    //ブロックを階段で表示
    for (int i = 1; i <= height ; i++)
    {
        //スペースの表示
        for (int j = 1; j <= height - i ; j++)
        {
            printf(" ");
        }
        
        //ブロックの表示
        for (int j = 1; j <= i; j++)
        {
            printf("#");
        }
        
        //空白の表示
        printf("  ");
        
        ////ブロックの表示
        for (int j = 1; j <= i; j++)
        {
            printf("#");
        }
        
        //改行
        printf("\n");
    }
}
