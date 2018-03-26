// top-down aparoach.
#include<stdio.h>
int main(){
  int i,n,n1=0,n2=1,n3;
    printf("enter n");
    scanf("%d",&n);
    for(i=1;i<n;i++){
      n3=n1+n2;
      n1=n2;
      n2=n3;
    }
    printf("\n%d",n3);
  return 0;
}

