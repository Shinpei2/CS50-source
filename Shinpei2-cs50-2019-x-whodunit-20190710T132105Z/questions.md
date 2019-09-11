# Questions

## What's `stdint.h`?

TODO
指定幅を持つint型を宣言するためのC言語の標準ライブラリ

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

・各データに対して、対応したバイト数を指定するため(BYTE：符号なし8ビット、DWORD：符号なし32ビット、LONG：符号あり32ビット、WORD：符号なし16ビット)

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

BYTE：1byte, DWORD：4byte, LONG：4byte, WORD：2byte

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

"BM"

## What's the difference between `bfSize` and `biSize`?

bfsize：ファイル全体のサイズ
bisize：構造体"BITMAPINFOHEADER"のサイズ

## What does it mean if `biHeight` is negative?

画素の格納順が上から下である

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCounte

## Why might `fopen` return `NULL` in `copy.c`?

ファイル名を正しくしていないため。


## Why is the third argument to `fread` always `1` in our code?

本プログラムでは、各ファイル全体を１つの要素として読み取るため。

## What value does `copy.c` assign to `padding` if `bi.biWidth` is `3`?

3　(9%4=1 1%4=1→4-1=3)

## What does `fseek` do?

ファイル位置表示子を変更する

## What is `SEEK_CUR`?

ファイル・ポインターの現在位置
