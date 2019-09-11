// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

// Represents number of buckets in a hash table
#define N 26

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Represents a hash table
node *hashtable[N];     //ハッシュテーブルの数：26個

//単語数
int wordNum = 0;

// Hashes word to a number between 0 and 25, inclusive, based on its first letter
unsigned int hash(const char *word)
{
    return tolower(word[0]) - 'a';      //アルファベットに応じて、0~25の数字を返す。
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Initialize hash table
    for (int i = 0; i < N; i++)
    {
        hashtable[i] = NULL;
    }

    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];

    // Insert words into hash table
    while (fscanf(file, "%s", word) != EOF)     //EOFに到達するまで、fileの文字列をwordに格納
    {
        // TODO　※まだハッシュテーブルに格納されてない。
        int index = hash(word);         //ハッシュ値(インデックス)
        word[strlen(word)] = '\0';      //wordの終端文字をNULL

        //wordをnewNodeへ格納
        node *newNode = malloc(sizeof(node));
        if (newNode == NULL)
        {
            unload();
            return false;
        }

        //newNodeにワードを格納
        strcpy(newNode->word, word);

        //wordをハッシュテーブルに格納＋wordを先頭ポインタに指定
        newNode->next = hashtable[index];
        hashtable[index] = newNode;

        //wordNumを更新
        wordNum++;

        //ファイルの終端に到着したら、
        if (feof(file))
        {
            // hit end of file
            free(newNode);
            break;
        }
    }

    // Close dictionary
    fclose(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return wordNum;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    //ハッシュテーブルのインデックスを保存
    int index = hash(word);

    //テキスト内のワードを全て小文字に変換
    char lower[strlen(word) + 1];
    for (int i = 0; i < strlen(word); i++)
    {
        lower[i] = tolower(word[i]);
    }
    lower[strlen(word)] = '\0';


    //ハッシュテーブルから、文字を探索
    node *cursor = hashtable[index];
    while (cursor != NULL)
    {
        if (strcmp(cursor->word, lower) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}


// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *cursor = hashtable[i];
        while (cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
        free(cursor);
    }
    return true;
}