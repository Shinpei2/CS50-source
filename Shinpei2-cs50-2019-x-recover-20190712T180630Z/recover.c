#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    /******　　　読み込みファイルの下準備　　　*******/
    //CL引数が1つの場合以外は強制終了
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }
    
    //ファイルの読み込み
    FILE *inptr = fopen(argv[1], "r");
    
    //ファイルが存在しない場合は強制終了
    if (inptr == NULL)
    {
        printf("Usage: ./recover image\n");
        return 2;
    }
    
    
    /******　　　JPEGファイル作成準備　　　*******/
    int jCount = 0;     // ファイル名生成用のカウンタ
    BYTE buffer[512];   // 一時的なストレージbufferの作成
    bool signature = false;     //シグネチャの真偽を確かめる変数
    
    //最初のシグネチャを見つけるまでブロックを進める
    do
    {
        fread(buffer, sizeof(BYTE), sizeof(buffer), inptr);
        signature = buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0;
    }
    while (!signature);
    
    
    /******　　　EOFに到達するまで、ファイル生成＋書込み　　　******/
    /*　JPEGファイル1個の生成　*/
    FILE *outptr = NULL;
    while (feof(inptr) == 0)
    {
        //書き込みファイルの生成
        char name[8];       //7ファイル名７文字＋終端文字
        sprintf(name, "%03i.jpg", jCount);
        outptr = fopen(name, "w");
        
        //次のシグネチャに到達するまでファイルを書き込む
        do
        {
            fwrite(buffer, sizeof(BYTE), sizeof(buffer), outptr);    //512バイト分を書込み
            fread(buffer, sizeof(BYTE), sizeof(buffer), inptr);      //512バイト分を読み込み
            signature = buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0;
            
            //EOFに到達したら、ファイルを閉じてループを抜ける
            if (feof(inptr) != 0)
            {
                fclose(outptr);
                break;
            }
        }
        while (!signature);
        
        fclose(outptr);     //outptrを閉じる
        jCount++;       //jCountの更新
    }
    
    fclose(inptr);  //読み込みファイルを閉じる
    
    return 0;   
}