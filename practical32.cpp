//*********added one end means rear removed from other end is front***********
//practical 32- pizza parlor accepting maximum m order,order are served in first come first served basis.order once placed can not be cancelled.
//write c++ program to simulate the system using circular queue using array.

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
        while(!pizza.empty()){ // jevha payant empty hot nahi tevha patyant served karar rahayche
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

// we put queue<int>pizza beause in int we enter integers number just like we go pizza shop and ordered n type of pizza just like we ordered pizza those name is 1 means integer number.
// 1. it is a queue program therefore quue header file included.
// 2. decleare int x and take order using push operation push means insert the element.
// 3. if order is empty so two possibilatity is created 1st one is all ordered are already sarved or other is ordered served ata zale.
// 4 considerd two person are ordered pizza in those who ordered first he gets pizza first because queue follow first in first out approach and those who ordered second he must wait beause he's order remaining to served.
// 5 next we put while condition, condition indicates until all ordered are served you dont stop,we perform pop operation because we removed element means perform front operation.
// 6 then decleared int and enter choice and end with return 0.
// 7. while(!pizza.empty) means jevha paryant not equal to pizza ha empty hot nahi tevha paryant print karat rahayche