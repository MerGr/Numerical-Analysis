#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compte_mots(char* c){
    int n = (int)strlen(c);
    int count = 0;
    for(int i = 0; i < n; i++){ // use < instead of <= to avoid going beyond the end of the string
        if(c[i] == ' '){
            count++; // increment count only when a space is found
        }
    }
    count++; // add one to count for the last word
    return count;
}


int main() { // use int main() instead of void main()
    char* c;
    c = (char*)malloc(20*sizeof(char));
    strcpy(c, "reda lahlali"); // use strcpy to copy the string into c
    printf("%d\n", compte_mots(c));
    free(c); // free the memory allocated with malloc
    return 0; // return a value to indicate success
}
