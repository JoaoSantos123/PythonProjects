#include <stdio.h>
#include <math.h>

double attackerSuccessProbability(double q, int z){
    double p = 1.0 - q;
    double lambda = z * (q/p);
    double sum = 1.0;
    int i,k;

    for(k=0;k<=z;k++){
        double poisson = exp(-lambda);
        for(i=1;i<=k;i++){
            poisson *= lambda/i;
        }
        sum -= poisson * (1-pow(q/p,z-k));
        printf("\nBlock %d -> %lf",k,sum);
    }
    return sum;
}

int main(){
    
    double q;
    int z;

    printf("Probability of the attacker finds the next block ");
    scanf("%lf",&q);
    printf("How many blocks is the attacker behind ");
    scanf("%i",&z);

    double result = attackerSuccessProbability(q,z);
    printf("\n\nResult is %lf\n", result);
    
    return 0;
}

