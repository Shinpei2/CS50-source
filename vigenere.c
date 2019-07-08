#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int shift(char c);

int main(int argc, string argv[])
{
    //コマンドライン引数の個数が2つ以外の場合、強制終了
    if (argc != 2)
    {
        printf("Usage: ./vigenere keyword\n");
        return 1;
    }
    
    //コマンドライン引数の全ての文字がアルファベット以外の場合、強制終了
    for (int i = 0, len = strlen(argv[1]); i < len; i++)
    {
        if (!(isalpha(argv[1][i])))
        {
            printf("Usage: ./vigenere keyword\n");
            return 1;
        }
    }
    
    //暗号鍵の1文字目から順に配列shiftNumに格納する。
    int shiftNum[strlen(argv[1])];
    for (int i = 0, len = strlen(argv[1]); i < len ; i++)
    {
        shiftNum[i] = shift(argv[1][i]);
    }
    
    //平文の入力および表示
    printf("plaintext: ");
    string plainText = get_string("");
    
    //暗号文の表示
    printf("ciphertext: ");
    
    int key;
    int keyCount = 0;
    for (int i = 0, len = strlen(plainText); i < len; i++)
    {
        //暗号鍵を変数keyに格納(平文のi番目文字列÷暗号文字列の余剰)
        key =  shiftNum[keyCount % strlen(argv[1])];
        
        int asciiNum = plainText[i];
            
        //大文字の変換
        if ('A' <= asciiNum && asciiNum <= 'Z')
        {
            asciiNum = (asciiNum + key - 'A') % 26 + 'A';
            keyCount += 1;
        }
        
        //小文字の変換
        else if ('a' <= asciiNum && asciiNum <= 'z')
        {
            asciiNum = (asciiNum + key - 'a') % 26 + 'a';
            keyCount += 1;
        }
        printf("%c", asciiNum);
    }
    
    printf("\n");     
}

//文字をシフト
int shift(char c)
{
    int shiftNum = 0;
    if ('A' <= c && c <= 'Z')
    {
        shiftNum = (int)(c - 'A');
    }
    else if ('a' <= c && c <= 'z')
    {
        shiftNum = (int)(c - 'a');
    }
    return shiftNum;
}
