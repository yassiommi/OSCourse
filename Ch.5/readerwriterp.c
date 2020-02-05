/////////////////////////////////////
////////    YASSAMAN OMMI (9613005)
/////////////////////////////////////

#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

sem_t mutex, writeblock;
int data = 0, rcount = 0;

int reader(int threadnum)
{
    sem_wait(&mutex);
    rcount = rcount + 1;
    if(rcount == 1)
        sem_wait(&writeblock);
    sem_post(&mutex);
    printf("reader%d reads %d\n", threadnum+1, data);
    sleep(2);
    sem_wait(&mutex);
    rcount = rcount - 1;
    
    if(rcount==0)
        sem_post(&writeblock);
    sem_post(&mutex);
    return 0;
}


int writer(int threadnum)
{
    sem_wait(&writeblock);
    data = pthread_self();
    printf("writer%d writes %d\n",threadnum+1, pthread_self());
    sleep(2);
    sem_post(&writeblock);
    return 0;
}

int main()
{
    int i;
    pthread_t rtid[4],wtid[2];
    sem_init(&mutex,0,1);
    sem_init(&writeblock,0,1);

    for(i=0;i<2;i++)
        pthread_create(&wtid[i],NULL,writer,i);
    
    for(i=0;i<4;i++)
        pthread_create(&rtid[i],NULL,reader,i);
    
    for(i=0;i<2;i++)
        pthread_join(wtid[i],NULL);
    
    for(i=0;i<4;i++)
        pthread_join(rtid[i],NULL);
    

  return 0;
}
