//queues are frequently used in computer programming and a topical example is the creation of a job queues by an operating system if the operating system does nit use prorities then the job are processed in the order they enter the system.
// write c++ program for simulating job queue.write function to add job and delete job from queue.

#include<iostream>
#include<queue>
using namespace std;
queue<int>s1;
int add_data(){
    int x;
    cout<<"Add new job"<<endl;
    cin>>x;
    s1.push(x);
}

void delect(){
    if(s1.empty()){
        cout<<"queue is already deleted"<<endl;
    }
    else{
        s1.pop();
    }
}
void display(queue<int>s1){
    if(s1.empty()){
        cout<<"jobs in the queue is empty:"<<endl;
    }
        while(!s1.empty()){      // jevha parayant empty hot nahi toprayant print ! means not
            cout<<s1.front()<<endl;
            s1.pop();
        } 
}
int main(){
    int ch;
    do{
        cout<<"hello sir"<<endl;
        cout<<"\n1.add job\n2.delete job\n3.display job\n4.exit"<<endl;
        cin>>ch;
        switch (ch){
            case 1:
            add_data();
            break;

            case 2:
            delect();
            break;

            case 3:
            display(s1);
            break;

            case 4:
            break;

        }
}while(ch!=4);
return 0;
}

// 1.sarvat pahile queue<int>pizza decleared karayche int madhe integer number stored karayche.
// 2.decleare int x and take order using push operation push means insert the element.
// 3.jae s1 empty asel tar print queue is already deleted.nahitar pop operation use karayche means kadun takayche.