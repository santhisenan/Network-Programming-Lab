#include<stdio.h>
#include<iostream>

using namespace std;                                            

struct node
{
    unsigned dist[6];
    unsigned from[6];
} DVR[10];

int main()
{
int costmat[6][6];
int nodes, i, j, k;
int graph1[3][3]={{0 ,1, 2 },{1, 0, 4 },{ 2 ,4 ,0 }};

for(i = 0; i < 3; i++)
 {
    for(j = 0; j < 3; j++)
    {
        graph1[i][j];
        costmat[i][i] = 0;
        DVR[i].dist[j] = graph1[i][j]; 
        DVR[i].from[j] = j;
    }
}
        for(i = 0; i < 3; i++) 
        for(j = i+1; j < 3; j++)
        for(k = 0; k < 3; k++)
            if(DVR[i].dist[j] > graph1[i][k] + DVR[k].dist[j])
            {   
                DVR[i].dist[j] = DVR[i].dist[k] + DVR[k].dist[j];
                DVR[j].dist[i] = DVR[i].dist[j];
                DVR[i].from[j] = k;
                DVR[j].from[i] = k;
            }
    for(i = 0; i < 3; i++)
    {
        cout<<"\n\n For router: "<<i+1;
        for(j = 0; j < 3; j++)
            cout<<"\t\n node "<<j+1<<" via "<<DVR[i].from[j]+1<<" Distance "<<DVR[i].dist[j];
    }
cout<<" \n\n ";
return 0;
}