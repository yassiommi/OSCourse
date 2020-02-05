//
//  multithreading.c
//  C
//
//  Created by Yassaman Ommi on 2019-11-13.
//  Copyright © 2019 Yassaman Ommi. All rights reserved.
//

#include <stdio.h>
#include <pthread.h>
#include <math.h>

int array[50], n;

void avg()
{
    float sum = 0, average;
    
    for(int i = 0; i < n; i++)
    {
        sum = sum + array[i];
    }
    average = sum / n;
    printf("The Average Value is: %f" ,average);
}

void min()
{
    int minimum = array[0];
    
    for(int i = 1; i < n; i++)
    {
        if(minimum > array[i])
        {
            minimum = array[i];
        }
    }
    printf("\nThe Minimum Value is: %d" ,minimum);
    
}

void max()
{
    
    int maximum = array[0];
    for(int i = 1; i < n; i++)
    {
        if(maximum < array[i])
        {
            maximum = array[i];
        }
    }
    printf("\nThe Maximum Value is: %d", maximum);
}

void devi()
{
    int sum = 0, habib = 0;
    float variance, deviation, average;
    
    for(int i = 0; i < n; i++)
    {
        sum = sum + array[i];
    }
    average = sum / n;
    
    for (int i = 0; i < n; i++)
    {
        habib = habib + pow((array[i] - average), 2);
    }
    variance = habib / n;
    deviation = sqrt(variance);
    printf("\nThe Standard Deviation is: %f", deviation);
    printf("\n");
    
}

int main()
{
    printf("enter the number of your numbers: ");
    scanf("%d" ,&n);
    
    for(int i = 0; i < n; i++)
    {
        scanf("%d" ,&array[i]);
    }
    
    pthread_t t1;
    pthread_t t2;
    pthread_t t3;
    pthread_t t4;
    
    pthread_create(&t1,NULL,&avg,NULL);
    pthread_join(t1,NULL);
    
    pthread_create(&t2,NULL,&min,NULL);
    pthread_join(t2,NULL);
    
    pthread_create(&t3,NULL,&max,NULL);
    pthread_join(t3,NULL);
    
    pthread_create(&t4,NULL,&devi,NULL);
    pthread_join(t4,NULL);


}
