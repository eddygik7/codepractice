#include<cs50.h>
#include<stdio.h>
#include <string.h>
int main(void)
{
    int number[] = {20,500,10,30,23,33,72};
    int n = get_int("Number: ");
    for (int i = 0; i<n; i++)
    {
        if (number[i] == n)
        {
            printf("found\n");
            return 0;
        }
    }
        printf("Not found\n");
    return 1;
}
