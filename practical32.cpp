
/*practical 32- pizza parlor accepting maximum m order,order are served in first come first served basis.order once placed can not be cancelled.
write c++ program to simulate the system using circular queue using array.*/

#include<iostream>
#include<queue>
using namespace std;
queue<int>pizza;
void accept_order(){
    int x;
    cout<<"Enter the order id: "<<endl;
    cin>>x;
    pizza.push(x);
}


void serve_order(){
    if(pizza.empty()){
        cout<<"All ordered are already served: "<<endl;
    }
    else{
    cout<<"Ordered served:"<<pizza.front()<<endl;
    pizza.pop();
}
}



void display(queue<int>pizza){
    cout<<"Order remaining to served: "<<endl;
        while(!pizza.empty()){ 
        cout<<pizza.front()<<" ";
        pizza.pop();

    }
}


int main(){
int ch;
cout<<"Welcome to pizza parlor:"<<endl;
do{
    cout<<"\n1.accept order.\n2.serve order.\n3.display all order.\n4.exit."<<endl;
    cout<<"Enter your choice"<<endl;
    cin>>ch;
        switch(ch){
            
            case 1:
                accept_order();
                break;

            case 2:
                serve_order();
                break;

            case 3:
                display(pizza);
                break;

            case 4:
                break;
        }
        }while(ch!=4);
return 0;
}

