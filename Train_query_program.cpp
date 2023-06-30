#include<bits/stdc++.h>
#include<unistd.h>   
#include<fstream>
using namespace std;
vector<string> week = {"Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday","Sunday"};

// This struct is for storing information about train.
struct details
{
    string train_no,train_name,Arrival_Time,Destination_Junction,Depature_Time,Duration,WeekSchedule;
};

// It is a class that provides likage to train information txt file and provide functions for getting various functionalities with the trains.
class query
{
    private:
    vector<details> train;
    public:
    query()
    {
        ifstream file;          //This link our txt file.
        file.open("trains.txt");
        if(file.is_open())
        {
            string p;
            int cnt=0;
            while(file>>p)
            {
                vector<string> lstr;
                lstr.push_back(p);
                while(cnt<6)
                {
                    file>>p;
                    lstr.push_back(p);
                    cnt++;
                }
                cnt=0;
                train.push_back({lstr[0],lstr[1],lstr[2],lstr[3],lstr[4],lstr[5],lstr[6]});
            }
            file.close();
        }
        else
        {
            cout<<"File NOT Found !!";
        }
    }
    void find_detail_through_train_number(string k)        // This is use for finding the train with train name.
    {
        bool flag=0;
        for(auto x:train)
        {
            if(x.train_no==k)
            {
                flag=1;
                vector<string> days;
                for(int i=0;i<7;i++)
                {
                    if(x.WeekSchedule[i]=='1')days.push_back(week[i]);
                }
                cout<<"Train Name:                "<<x.train_name<<endl;
                cout<<"Arrival Time:              "<<x.Arrival_Time<<endl;
                cout<<"Destination Junction:      "<<x.Destination_Junction<<endl;
                cout<<"Destination Reaching Time: "<<x.Depature_Time<<endl;
                cout<<"Train Duration:            "<<x.Duration<<endl;
                cout<<"Days on Which it runs:     ";
                for(auto x:days)cout<<x<<' ';
                break;
            }
        }
        if(!flag)
        {
            cout<<"SORRY NO SUCH TRAIN FOUND !!"<<endl;
        }
    }
    void find_detail_through_train_name(string k)       // This is use for finding the train with train number.
    {
        bool flag=0;
        for(auto x:train)
        {
            if(x.train_name==k)
            {
                flag=1;
                vector<string> days;
                for(int i=0;i<7;i++)
                {
                    if(x.WeekSchedule[i]=='1')days.push_back(week[i]);
                }
                cout<<"Train Number:              "<<x.train_no<<endl;
                cout<<"Arrival Time:              "<<x.Arrival_Time<<endl;
                cout<<"Destination Junction:      "<<x.Destination_Junction<<endl;
                cout<<"Destination Reaching Time: "<<x.Depature_Time<<endl;
                cout<<"Train Duration:            "<<x.Duration<<endl;
                cout<<"Days on Which it runs:     ";
                for(auto x:days)cout<<x<<' ';
                break;
            }
        }
        if(!flag)
        {
            cout<<"SORRY NO SUCH TRAIN FOUND !!"<<endl;
        }
    }
    void find_train_to_a_specificdestination(string k)      // This is use for finding train on basis of destination of train.
    {
        bool flag=0;
        for(auto x:train)
        {
            if(x.Destination_Junction==k)
            {
                flag=1;
                vector<string> days;
                for(int i=0;i<7;i++)
                {
                    if(x.WeekSchedule[i]=='1')days.push_back(week[i]);
                }
                cout<<"Train Number:              "<<x.train_no<<endl;
                cout<<"Train Name:                "<<x.train_name<<endl;
                cout<<"Arrival Time:              "<<x.Arrival_Time<<endl;
                cout<<"Destination Reaching Time: "<<x.Depature_Time<<endl;
                cout<<"Train Duration:            "<<x.Duration<<endl;
                cout<<"Days on Which it runs:     ";
                for(auto x:days)cout<<x<<' ';cout<<endl<<endl;
            }
        }
        if(!flag)
        {
            cout<<"SORRY NO TRAINS TO THIS DESTINATION!!"<<endl;
        }
    }
    void find_train_to_a_destination_on_specific_day(string k,string l)             // This is use for finding train on basis of destination and boarding date
    {
        bool flag=0;
        int id;
        for(int i=0;i<7;i++)
        {
            if(l==week[i])
            {
                id=i;
            }
        }
        for(auto x:train)
        {
            if(x.Destination_Junction==k and x.WeekSchedule[id]=='1')
            {
                flag=1;
                cout<<"Train Number:              "<<x.train_no<<endl;
                cout<<"Train Name:                "<<x.train_name<<endl;
                cout<<"Arrival Time:              "<<x.Arrival_Time<<endl;
                cout<<"Train Duration:            "<<x.Duration<<endl;
                cout<<endl;
            }
        }
        if(!flag)
        {
            cout<<"NO TRAIN TO THIS DESTINATION ON THIS DAY"<<endl;
        }
    }   
};

// This is a login class that connect to txt file that has information about the users.This class doen't provide any print function so information about users can be kept private.
class login
{
    map<string,string> users;
    public:
    login()     // This part connect to txt file.
    {
        ifstream file_1;
        file_1.open("user detail.txt");
        if(file_1.is_open())
        {
            string x;
            while (file_1>>x)
            {
                string y;
                file_1>>y;
                users.insert({x,y});
            }
            file_1.close();
        }
        else
        {
            cout<<"NO SUCH FILE FOUND !!";
        }
    }
    bool check_details(string a,string b)   // This part check the crediantiality of the user.
    {
        if(users.find(a)==users.end() or users[a]!=b)
        {
            cout<<"INVALID CREDENTIALS !!"<<endl;
            return false;
        }
        else
        {
            cout<<"LOGIN SUCCESFULL !!";
            return true;
        }
    }
    void update()       // This function add new users to the user detail file .
    {
        string u,v,w;
        while(1)
        {
            sleep(2);system("cls");
            cout<<"Enter Your Username:   "<<endl;
            cin>>u;
            cout<<"Enter Your Password:   "<<endl;
            cin>>v;
            cout<<"Renter Your Password:  "<<endl;
            cin>>w;
            if(v!=w)
            {
                cout<<"Passwords doesnot match  !!"<<endl;
            }
            else break;
        }
        ofstream file_2;
        file_2.open("user detail.txt",ios::app);
        if(file_2.is_open())
        {
            file_2<<endl<<u<<' '<<v;
            file_2.close();
        }
        cout<<"Thanks For registering."<<endl;
        cout<<"Now you can procced for querying"<<endl;
    }
};

// This program gives the intro message.
void intro()
{
    cout<<"----------------------------------------------Welcome---------------------------------------------------"<<endl;
}

string quer1()  // This is query for asking login and status of user.
{
    cout<<"Please Login"<<endl;
    string p;
    cout<<"Are you a new User?"<<endl;
    cin>>p;
    return p;
}

void get_detail(string &a,string &b)    // This is for asking details to current users.
{
    sleep(2);system("cls");
    cout<<"Enter Your Name:     ";
    cin>>a;cout<<endl;
    cout<<"Enter Your Password: ";
    cin>>b;
}

int main()
{
    bool any=0;                 // this is defined so that when a new user register so get directly procced further without again logining.
    string name,password;
    query q;
    login lg;

    intro();

    if(quer1()=="YES")lg.update(),any=1;   // This part decides wether user is new or current.
    else get_detail(name,password);        // This part ask current user for name and password.

    // This part is for quering.
    if(any or lg.check_details(name,password))
    {
        sleep(2);system("cls");
        while(1)
        {
            sleep(2);system("cls");
            cout<<"Welcome you can ask queries related to trains from kharagpur junction here."<<endl;
            cout<<"query type                                                          id"<<endl;
            cout<<"search train by train name                                          1"<<endl;
            cout<<"search train by train number                                        2"<<endl;
            cout<<"search train by final destination on any day                        3"<<endl;
            cout<<"search train by final destination on a particular day               4"<<endl;
            int id;
            cout<<"\n Type id of query that you want to do: ";
            cin>>id;
            cout<<endl;
            string x;
            if(id==1)
            {
                cout<<"Enter the train name: ";cin>>x;cout<<endl;
                q.find_detail_through_train_name(x);
            }   
            else if(id==2)
            {
                cout<<"Enter the train number: ";cin>>x;cout<<endl;
                q.find_detail_through_train_number(x);
            }
            else if(id==3)
            {
                cout<<"Enter the destination: ";cin>>x;cout<<endl;
                q.find_train_to_a_specificdestination(x);
            }
            else
            {
                string z;
                cout<<"Enter the destination:  ";cin>>x;cout<<endl;
                cout<<"Enter the day of abord: ";cin>>z;cout<<endl;
                q.find_train_to_a_destination_on_specific_day(x,z);
            }
            cout<<"\n Do You Have any Other query?"<<endl;
            cin>>x;
            if(x=="NO")
            {
                cout<<"Visit again Have a nice day";break;
            }
        }
    }

    return 0;
}
