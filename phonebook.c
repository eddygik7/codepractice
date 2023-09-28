#include<stdio.h>
#include<cs50.h>
#include<string.h>

typedef struct
{
    string name;
    string number;
}
person;
int main(void)
{
    person people[2];
    people[0].name = "eddy";
    people[0].number ="+254707035002";

    people[1].name = "steve";
    people[1].number ="+254779351916";

    string name = get_string("Name: ");
    for (int i=0; i<2; i++)
    {
        if(strcmp(people[i].name,name)==0)
        {
            printf("found %s %s\n",people[i].name, people[i].number);
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}