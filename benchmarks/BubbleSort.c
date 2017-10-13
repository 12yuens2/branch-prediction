#include <time.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    int arrsize = atoi(argv[1]);

    int array[arrsize];

    srand(time(NULL));
    for (int i = 0; i < arrsize; i++)
    {
	int r = rand();
	array[i] = r;
    }

    for (int i = 0; i < arrsize - 1; i++)
    {
	for (int j = 0; j < arrsize - i - 1; j++)
	{
	    if (array[j] > array[j+1])
	    {
		int temp = array[j];
		array[j] = array[j+1];
		array[j+1] = temp;
	    }
   	}
    }

    for (int i = 0; i < arrsize; i++)
    {
	printf("%d, ", array[i]);
    }

    printf("\n");

    return 0;
}
