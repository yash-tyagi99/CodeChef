# CodeChef

Some CodeChef Question are.

## Question 1

### Life, the Universe, and Everything .

#### Input => Your program is to use the brute-force approach in order to find the Answer to Life, the Universe, and Everything.More precisely... rewrite small numbers from input to output. Stop processing input after reading in the number 42. All numbers at input are integers of one or two digits.
         
 
## Solution
```
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int n;
	while(1)
	{
	    cin>>n;
	    if(n==42)
	     {break;}
	    else{
	        cout<<n<<endl;
	}}
	return 0;
}
````


## Question 2

### Reverse The Number.

#### Input => The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.

## Solution
```
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{   int n;
	    cin>>n;
	    int rev=0;
	    while(n>0)
	    {
	       rev=(rev*10)+(n%10);
	       n=n/10;
	    }
	   cout<<rev<<"\n"; 
	    
	}
	return 0;
}
````

## Question 3

### Smart Phone

##### Theory => You are developing a smartphone app. You have a list of potential customers for your app. Each customer has a budget and will buy the app at your declared price if and only if the price is less than or equal to the customer's budget.You want to fix a price so that the revenue you earn from the app is maximized. Find this maximum possible revenue.For instance, suppose you have 4 potential customers and their budgets are 30, 20, 53 and 14. In this case, the maximum revenue you can get is 60.

#### Input => Line 1 : N, the total number of potential customers. Lines 2 to N+1: Each line has the budget of a potential customer.

## Solution
```
try:
    n = int(input())
    x = []
    for i in range(n):
        x.append(int(input()))
    x.sort()
    y = 0
    z = 0
    for i in range(n):
        y = (n-i)*x[i]
        if y > z:
            z = y
    print(z)
except EOFError:
    pass
````
## Question 4

### Factorial

##### Theory => The most important part of a GSM network is so called Base Transceiver Station (BTS). These transceivers form the areas called cells (this term gave the name to the cellular phone) and every phone connects to the BTS with the strongest signal (in a little simplified view). Of course, BTSes need some attention and technicians need to check their function periodically.The technicians faced a very interesting problem recently. Given a set of BTSes to visit, they needed to find the shortest path to visit all of the given points and return back to the central company building. Programmers have spent several months studying this problem but with no results. They were unable to find the solution fast enough. After a long time, one of the programmers found this problem in a conference article. Unfortunately, he found that the problem is so called "Traveling Salesman Problem" and it is very hard to solve. If we have N BTSes to be visited, we can visit them in any order, giving us N! possibilities to examine. The function expressing that number is called factorial and can be computed as a product1.2.3.4....N. The number is very high even for a relatively small N.The programmers understood they had no chance to solve the problem. But because they have already received the research grant from the government, they needed to continue with their studies and produce at least some results. So they started to study behavior of the factorial function.For example, they defined the function Z. For any positive integer N, Z(N) is the number of zeros at the end of the decimal form of number N!. They noticed that this function never decreases. If we have two numbers N1<N2, then Z(N1) <= Z(N2). It is because we can never "lose" any trailing zero by multiplying by any positive number. We can only get new and new zeros. The function Z is very interesting, so we need a computer program that can determine its value efficiently.

#### Input => There is a single positive integer T on the first line of input (equal to about 100000). It stands for the number of numbers to follow. Then there are T lines, each containing exactly one positive integer number N, 1 <= N <= 1000000000.

## Solution
```
try:
    T=int(input())
    for i in range(T):
        N=int(input())
        q=int(N)
        s=0
        while q>=5:
            r=q//5
            s=s+r
            q=r
        print(s)
except EOFError:
    pass
````
## Question 5

### Coin Flip

##### Theory => Little Elephant was fond of inventing new games. After a lot of research, Little Elephant came to know that most of the animals in the forest were showing less interest to play the multi-player games.Little Elephant had started to invent single player games, and succeeded in inventing the new single player game named COIN FLIP.In this game the player will use N coins numbered from 1 to N, and all the coins will be facing in "Same direction" (Either Head or Tail),which will be decided by the player before starting of the game.The player needs to play N rounds.In the k-th round the player will flip the face of the all coins whose number is less than or equal to k. That is, the face of coin i will be reversed, from Head to Tail, or, from Tail to Head, for i ≤ k.Elephant needs to guess the total number of coins showing a particular face after playing N rounds. Elephant really becomes quite fond of this game COIN FLIP, so Elephant plays G times. Please help the Elephant to find out the answer.

#### Input => The first line of input contains an integer T, denoting the number of test cases. Then T test cases follow.The first line of each test contains an integer G, denoting the number of games played by Elephant. Each of the following G lines denotes a single game, and contains 3 space separeted integers I, N, Q, where I denotes the initial state of the coins, N denotes the number of coins and rounds, and Q, which is either 1, or 2 as explained below.Here I=1 means all coins are showing Head in the start of the game, and I=2 means all coins are showing Tail in the start of the game. Q=1 means Elephant needs to guess the total number of coins showing Head in the end of the game, and Q=2 means Elephant needs to guess the total number of coins showing Tail in the end of the game.
## Solution
```
try:
    for j in range(int(input())):
       for i in range(int(input())):
              a,b,c = map(int,input().split())
              if b%2 == 0 or a==c:
                 print(int(b/2))
              else:
                 
                     print(int(b/2)+1)
except EOFError:
    pass
 ````
