#include<stdio.h>
#include<cs50.h>
#include<stdint.h>
int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Improper usage.\n");
        return 1;
    }
    //open file
    string filename = argv[1];
    FILE *file = fopen(filename, "r");
    //check if file exists
    if (file == NULL)
    {
        printf("No such file exists.\n");
        return 1;
    }
    uint8_t buffer[4];
    uint8_t signature []={37,80,68,70};
    fread(buffer, 1, 4, file);
    for(int i = 0; i<4; i++)
    {
       if (buffer[i] != signature[i])
       {
        printf("likely not a pdf.\n");
        return 0;
       }
    }
    printf("likely a pdf.\n");
    fclose(file);
    return 0;
}