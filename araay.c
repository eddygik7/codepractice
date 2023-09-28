#include<cs50.h>
#include<stdio.h>
int main(void)
{
    int length;
    do
    {
        length = get_int("length: ");
    }

    while (length >=  1);
}