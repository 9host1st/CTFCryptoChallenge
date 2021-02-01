#include <stdio.h>
int main () {
	char *text[4];
	int v6;
	int v7;
	int v8;
	int v9;
	int v10;
	int v11;
	*text = 0x41424344;
	v6 = 0x45674567;
	v7 = 0x373bd62b;
	v8 = 0x77da5f29;
	v9 = 0xc46d7b5e;
	v10 = 0x74C02E0E;
	v11 = 0xB153FD7E;

	printf("%s", text[1]);
	/*
	for(int k = 0; k < 10; k++)
		*&text[4*k] ^= (unsigned int) 0x41;
	*/
}
