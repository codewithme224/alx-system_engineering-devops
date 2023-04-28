#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - the beginning of the program
 *
 * Return: returns 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - The beginning of the program
 *
 * Return: returns 0
 */

int main(void)
{
	int i;
	pid_t pid;
	int status;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
		{
			exit(0);
		}
		else
		{
			printf("Zombie process created, PID: %d\n", pid);
		}
	}
	infinite_while();
	return (0);
}
