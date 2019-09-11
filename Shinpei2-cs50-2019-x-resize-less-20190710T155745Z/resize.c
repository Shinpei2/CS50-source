// Copies a BMP file

#include <stdio.h>
#include <stdlib.h>

#include "bmp.h"

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        fprintf(stderr, "Usage: copy infile outfile\n");
        return 1;
    }

    //argv[1]が1以上の整数でなければ強制終了
    int num = atoi(argv[1]);
    if (num < 1)
    {
        fprintf(stderr, "Usage: copy infile outfile\n");
        return 2;
    }

    // ファイル名を格納
    char *infile = argv[2];
    char *outfile = argv[3];

    // インプットファイルを開く
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 3;
    }

    // 書込みファイルを開く(用意)
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 4;
    }

    // 読み込みファイルのBITMAPFILEHEADERを読み込む
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // 読み込みファイルBITMAPINFOHEADERを読み込む
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // 読み込みファイルが24ビットのBMPファイルか確認
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 5;
    }

    /***　BITMAPINFOHEADERのサイズ変更　***/
    //リサイズ前後のpaddingの計算
    int prePadding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    int padding = (4 - (bi.biWidth * num * sizeof(RGBTRIPLE)) % 4) % 4;
    // temporary storage
    RGBTRIPLE triple;

    bi.biHeight *= num;
    bi.biWidth *= num;
    bi.biSizeImage = ((sizeof(triple) * bi.biWidth) + padding) * abs(bi.biHeight);
    bf.bfSize = bi.biSizeImage + sizeof(bf) + sizeof(bi);

    // 書込みファイルのBITMAPFILEHEADERに書込み
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);
    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);


    /***************　　以下がcopyとの変更点　　***************/


    /*****　全リサイズ　*****/
    //読み込みファイルの高さ分だけ繰返し
    for (int i = 0, biHeight = abs(bi.biHeight / num); i < biHeight; i++)
    {
        /***　一行分のリサイズ　***/
        // 縦のリサイズ
        for (int j = 0; j < num; j++)
        {
            //横のリサイズ
            for (int k = 0; k < bi.biWidth / num; k++)
            {
                // read RGB triple from infile(1ピクセル読み取り)
                fread(&triple, sizeof(RGBTRIPLE), 1, inptr);
                // write RGB triple to outfile(num個貼り付け)
                for (int l = 0; l < num; l++)
                {
                    fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
                }
            }

            // then add it back (to demonstrate how)
            for (int k = 0; k < padding; k++)
            {
                fputc(0x00, outptr);
            }

            //同じ行のリサイズを継続する場合は、ファイルの位置表示子を行の先頭に戻す
            if (j < num - 1)
            {
                fseek(inptr, -(sizeof(RGBTRIPLE) * bi.biWidth / num), SEEK_CUR);
            }
            // 次の行のコピーに移る場合は、行を進める
            else
            {

                fseek(inptr, prePadding, SEEK_CUR);
            }

        }

    }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}
