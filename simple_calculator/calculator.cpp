#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <sstream>
using namespace std;

string doubleToString(double a){
	ostringstream strs;
	strs << a;
	string str = strs.str();
	return str;
}

class calculator{
public:
	calculator() {};
	double simple_operations(double a, double b, int opNum);
	int factorial(int x);
	double power(double x, int pow);
	double Logarithm(double num);
};

double calculator::Logarithm(double num){
	return log(num);
}

double calculator::simple_operations(double a, double b, int opNum){
	double answer;
	switch(opNum){
		case 1: answer = a + b;
				break;
		case 2: answer = a - b;
				break;
		case 3: answer = a*b; 
				break;
		case 4: answer = a/b;
				break;
		default: answer = -1;
				break;
	}
	return answer;
}

int calc_factorial(int x){
	int answer=1;
	for(int i=1; i<=x; i++)
		answer *= i;
	return answer;
}

double cacl_neg_power(double num, int x){
	if(x==-1)
		return 1/num;
	int k = cacl_neg_power(num, x/2);
	if(x%2==0)
		return k*k;
	else 
		return (1/num)*k*k;
}

double calc_pos_power(double num,int x){
	if(x<=1)
		return num;
	int k = calc_pos_power(num, x/2);
	if(x%2==0)
		return k*k;
	else
		return num*k*k;
}

int calculator::factorial(int x){
	if(x<0)
		return -1;
	else if(x==0)
		return 1;
	else 
		return calc_factorial(x);
}

double calculator::power(double x, int pow){
	if(pow==0)
		return 1;
	else if(pow>=1)
		return calc_pos_power(x, pow);
	else if(pow <0)
		return cacl_neg_power(x, pow);
}



int main(){
	calculator calc;
	cout<<calc.factorial(5)<<endl;
	cout<<calc.simple_operations(10, 1, 1)<<endl;
	cout<<calc.power(10, 2)<<endl;
	cout<<calc.power(10, -1)<<endl;
	cout<<calc.Logarithm(10)<<endl;
	return 0;
}
