#include <stdio.h>
#include <string.h>
#define z 122
int main(){
  char f[]={70,105,z,z,0},b[]={66,117,z,z,0},i=1,B[z],g;
  for(i=1;i<=100;i++){
    g=0;if(i%3<1)strcpy(B,f),g=1;
    if(i%5<1){if(g>0)strcat(B,b);else if(g<1)strcpy(B,b),g=1;}
    if(g<1)printf("%d\n",i);
    else printf("%s\n",B);
  }
return 0;}
