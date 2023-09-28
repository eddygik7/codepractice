#include<cs50.h>
#include<stdio.h>
#include <string.h>
int main(void)
{
    string strings[]= {"chicken", "rat", "dollars", "dog"};
    string s = get_string("string: ");
    int length = strlen(s);
    for (int i = 0; i<length; i++)
    {
     if (strcmp(strings[i], s)==0)
        {
            printf("string found\n");
            return 0;
        }
}
printf("string Not found\n");
return 1;
}