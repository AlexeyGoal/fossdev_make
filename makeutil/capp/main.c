#include <stdio.h>
#include <time.h>

int main(void){
    time_t now = time(NULL);
    printf("Hello world\n");
    printf("run time: %ld\n", now);
    return 0;
}