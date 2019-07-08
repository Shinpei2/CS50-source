#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //値を入力
    int Height;
    do
    {
        Height = get_int("Height: ");
    }
    while (Height < 1 || 8 < Height);
    
    //Heightと同じ段数の階段を表示
    for (int i = 1; i <= Height; i++)
    {
        //スペースを表示
        for (int j = 1; j <= Height - i; j++)
        {
            printf(" ");
        }

        //ブロックを表示
        for (int j = 1; j <= i; j++)
        {
            printf("#");
        }

        //改行
        printf("\n");
    }   
}
