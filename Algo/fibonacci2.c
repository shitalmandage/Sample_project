
// bottom-up aparoach.
#include<stdio.h>
int fibo(int n, int a[]){
  int k;
  if(a[n]!=-1)
    return a[n];
  if(n==0)
    return 0;
  if(n==1)
    return 1;
  else{
    k=fibo(n-1, a)+fibo(n-2, a);
    a[n]=k;
  }
}
int main(){
  int a[100],n,i;
    printf("enter n");
    scanf("%d",&n);
    for(i=0;i<=n;i++)
      a[i]=-1;
    printf("\n%d",fibo(n,a));
  return 0;
}
