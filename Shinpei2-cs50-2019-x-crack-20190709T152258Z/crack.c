#include <cs50.h>
#include <stdio.h>
#include <crypt.h>
#include <string.h>

bool saltCheck(char *hash);

int main(int argc, string argv[])
{
    //コマンドライン引数が1以外の場合は強制終了
    if (argc != 2)
    {
        printf("Usage: ./crack hash\n");
        return 1;
    }
    
    //salt桁(最上位2桁)が64種類の文字以外の場合、強制終了
    if (!(saltCheck(argv[1])))
    {
        printf("LOL\n");
        return 1;
    }
    
    //ハッシュの長さが13以外の場合は強制終了
    if (strlen(argv[1]) != 13)
    {
        printf("LOL\n");
        return 1;
    }
    
    //配列soltにsolt値を格納
    char salt[2] = {argv[1][0], argv[1][1]};
    
    
    /***  配列alpha[53]に英字52種類とNullを格納 ***/
    char alpha[53]; 
    
    //配列alpha[0]~[25]に大文字英字を格納
    for (int i = 0; i < 26; i++)
    {
        int asciiNum = 65 + i;
        alpha[i] = (char)asciiNum;
    }
    
    //配列alpha[26]~[51]に小文字英字を格納
    for (int i = 0; i < 26; i++)
    {
        int asciiNum = 97 + i;
        alpha[i + 26] = (char)asciiNum;
    }
    
    //alpha[52]にNullを格納
    alpha[52] = '\0';
    
    
    /***   全数探索　  ***/
    
    //password格納用配列の用意　※6番目は終端文字
    char passward[6] = {'\0', '\0', '\0', '\0', '\0', '\0'};
    
    //全数探索
    for (int i = 0; i < 53; i++)
    {
        passward[0] = alpha[i];
        for (int j = 0; j < 53; j++)
        {
            passward[1] = alpha[j];
            for (int k = 0; k < 53; k++)
            {
                passward[2] = alpha[k];
                for (int l = 0; l < 53; l++)
                {
                    passward[3] = alpha[l];
                    for (int m = 0; m < 53; m++)
                    {
                        passward[4] = alpha[m];
                        //printf("%s\n",passward);
                        if (argv[1] == crypt(passward, salt))
                        {
                            //見つかった場合は、パスワードを表示し、プログラムを終了。
                            printf("passward: %s", passward);
                            return 0;
                        }
                    }
                }
            }
        }       
    }
    
    
    //パスワードが探索できなかった場合、"LOL"とプリント表示
    printf("LOL");
    return 0;
}



//saltが有効な値かどうかを調べる関数saltCheck()
bool saltCheck(char *hash)
{
    int asciiNum1 = (int)hash[0];
    int asciiNum2 = (int)hash[1];
    
    //最上位桁目が64種類の文字に該当するか調べる
    if (('A' <= asciiNum1 && asciiNum1 <= 'Z') || ('a' <= asciiNum1 && asciiNum1 <= 'z') || ('.' <= asciiNum1 && asciiNum1 <= '9'))
    {
        //最上位2桁目が64種類の文字に該当するか調べる
        if (('A' <= asciiNum2 && asciiNum2 <= 'Z') || ('a' <= asciiNum2 && asciiNum2 <= 'z') || ('.' <= asciiNum2 && asciiNum2 <= '9'))
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }
}
