#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/**
 * Recursively defined function from CS3052 notes on decidability
 */
int f(int i)
{
    printf("%d\n", i);
    if (i == 1)
    {
	return i;
    }
    else if (i % 2 == 1 && i >= 3)
    {
	return f(3*i + 1);
    }
    else if (i % 2 == 0)
    {
	return f(i/2);
    }
    else
    {
	return 0;
    }
}



int main(int argc, char* argv[])
{
    srand(time(NULL));
    int count = rand();

    int result = f(count);
    printf("result: %d\n", result);
    
    return 0;
}


