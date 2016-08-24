#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int N, i, N_number, e;
    long total_square, total_sum, total;
    scanf("%d", &N);
    for (i = 0; i < N; i++) {
        total_square = 0;
        total_sum = 0;
        scanf("%d", &N_number);
        for (e = 1; e <= N_number; e++) {
            total_square = pow(e, 2) + total_square;
            total_sum = e + total_sum;
        }
        total = (pow(total_sum, 2) - total_square);
        printf("%ld\n", total);
    }
    return 0;
}
