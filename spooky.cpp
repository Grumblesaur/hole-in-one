#include<iostream>
#include<sstream>
#include<string>
int main(){
int y;std::cin>>y;
std::cout<<[](int x){std::stringstream q;q<<x<<"spooky"<<x+2<<"me";
return q.str();}(y)<<std::endl;
return 0;
}

