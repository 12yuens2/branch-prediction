#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    int count = atoi(argv[1]);
    while (count > 0)
    {
	printf("hello\n");
	count--;
    }
    return 0;
}
