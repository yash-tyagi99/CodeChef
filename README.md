# CodeChef

Some CodeChef Question are.

## Question 1

### Life, the Universe, and Everything .

#### Input => Your program is to use the brute-force approach in order to find the Answer to Life, the Universe, and Everything.More precisely... rewrite small numbers from input to output. Stop processing input after reading in the number 42. All numbers at input are integers of one or two digits.
         
 
## Solution
(https://www.codechef.com/viewsolution/36199951)


## Question 2

### Reverse The Number.

#### Input => The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.

## Solution
(https://www.codechef.com/viewsolution/35852327)

## Question 3

### Smart Phone

##### Theory => You are developing a smartphone app. You have a list of potential customers for your app. Each customer has a budget and will buy the app at your declared price if and only if the price is less than or equal to the customer's budget.You want to fix a price so that the revenue you earn from the app is maximized. Find this maximum possible revenue.For instance, suppose you have 4 potential customers and their budgets are 30, 20, 53 and 14. In this case, the maximum revenue you can get is 60.

#### Input => Line 1 : N, the total number of potential customers. Lines 2 to N+1: Each line has the budget of a potential customer.

## Solution
(https://www.codechef.com/viewsolution/36318750)
## Question 4

### Factorial

##### Theory => The most important part of a GSM network is so called Base Transceiver Station (BTS). These transceivers form the areas called cells (this term gave the name to the cellular phone) and every phone connects to the BTS with the strongest signal (in a little simplified view). Of course, BTSes need some attention and technicians need to check their function periodically.The technicians faced a very interesting problem recently. Given a set of BTSes to visit, they needed to find the shortest path to visit all of the given points and return back to the central company building. Programmers have spent several months studying this problem but with no results. They were unable to find the solution fast enough. After a long time, one of the programmers found this problem in a conference article. Unfortunately, he found that the problem is so called "Traveling Salesman Problem" and it is very hard to solve. If we have N BTSes to be visited, we can visit them in any order, giving us N! possibilities to examine. The function expressing that number is called factorial and can be computed as a product1.2.3.4....N. The number is very high even for a relatively small N.The programmers understood they had no chance to solve the problem. But because they have already received the research grant from the government, they needed to continue with their studies and produce at least some results. So they started to study behavior of the factorial function.For example, they defined the function Z. For any positive integer N, Z(N) is the number of zeros at the end of the decimal form of number N!. They noticed that this function never decreases. If we have two numbers N1<N2, then Z(N1) <= Z(N2). It is because we can never "lose" any trailing zero by multiplying by any positive number. We can only get new and new zeros. The function Z is very interesting, so we need a computer program that can determine its value efficiently.

#### Input => There is a single positive integer T on the first line of input (equal to about 100000). It stands for the number of numbers to follow. Then there are T lines, each containing exactly one positive integer number N, 1 <= N <= 1000000000.

## Solution
(https://www.codechef.com/viewsolution/36313988)
## Question 5

### Coin Flip

##### Theory => Little Elephant was fond of inventing new games. After a lot of research, Little Elephant came to know that most of the animals in the forest were showing less interest to play the multi-player games.Little Elephant had started to invent single player games, and succeeded in inventing the new single player game named COIN FLIP.In this game the player will use N coins numbered from 1 to N, and all the coins will be facing in "Same direction" (Either Head or Tail),which will be decided by the player before starting of the game.The player needs to play N rounds.In the k-th round the player will flip the face of the all coins whose number is less than or equal to k. That is, the face of coin i will be reversed, from Head to Tail, or, from Tail to Head, for i ≤ k.Elephant needs to guess the total number of coins showing a particular face after playing N rounds. Elephant really becomes quite fond of this game COIN FLIP, so Elephant plays G times. Please help the Elephant to find out the answer.

#### Input => The first line of input contains an integer T, denoting the number of test cases. Then T test cases follow.The first line of each test contains an integer G, denoting the number of games played by Elephant. Each of the following G lines denotes a single game, and contains 3 space separeted integers I, N, Q, where I denotes the initial state of the coins, N denotes the number of coins and rounds, and Q, which is either 1, or 2 as explained below.Here I=1 means all coins are showing Head in the start of the game, and I=2 means all coins are showing Tail in the start of the game. Q=1 means Elephant needs to guess the total number of coins showing Head in the end of the game, and Q=2 means Elephant needs to guess the total number of coins showing Tail in the end of the game.
## Solution
(https://www.codechef.com/viewsolution/36317895)

## Question 6

### Laddu .

##### Theory => You might have heard about our new goodie distribution program aka the "Laddu Accrual System". This problem is designed to give you a glimpse of its rules. You can read the page once before attempting the problem if you wish, nonetheless we will be providing all the information needed here itself.Laddu Accrual System is our new goodie distribution program. In this program, we will be distributing Laddus in place of goodies for your winnings and various other activities (described below), that you perform on our system. Once you collect enough number of Laddus, you can then redeem them to get yourself anything from a wide range of CodeChef goodies.Let us know about various activities and amount of laddus you get corresponding to them.Contest Win (CodeChef’s Long, Cook-Off, LTIME, or any contest hosted with us) : 300 + Bonus (Bonus = 20 - contest rank). Note that if your rank is > 20, then you won't get any bonus.Top Contributor on Discuss : 300Bug Finder : 50 - 1000 (depending on the bug severity). It may also fetch you a CodeChef internship!Contest Hosting : 50You can do a checkout for redeeming laddus once a month. The minimum laddus redeemable at Check Out are 200 for Indians and 400 for the rest of the world.You are given history of various activities of a user. The user has not redeemed any of the its laddus accrued.. Now the user just wants to redeem as less amount of laddus he/she can, so that the laddus can last for as long as possible. Find out for how many maximum number of months he can redeem the laddus.

#### Input => The first line of input contains a single integer T denoting number of test cases
#### For each test case:
#### First line contains an integer followed by a string denoting activities, origin respectively, where activities denotes number of activities of the user, origin denotes whether the user is Indian or the rest of the world. origin can be "INDIAN" or "NON_INDIAN".
#### For each of the next activities lines, each line contains an activity.
#### An activity can be of four types as defined above.
#### Contest Win : Input will be of form of CONTEST_WON rank, where rank denotes the rank of the user.
#### Top Contributor : Input will be of form of TOP_CONTRIBUTOR.
#### Bug Finder : Input will be of form of BUG_FOUND severity, where severity denotes the severity of the bug.
#### Contest Hosting : Input will be of form of CONTEST_HOSTED.

## Solution
(https://www.codechef.com/viewsolution/36199504)

## Question 7

### Chef and Street Food

##### Theory => in Chefland, there is a very famous street where N types of street food (numbered 1 through N) are offered. For each valid i, there are Si stores that offer food of the i-th type, the price of one piece of food of this type is Vi (the same in each of these stores) and each day, Pi people come to buy it; each of these people wants to buy one piece of food of the i-th type.Chef is planning to open a new store at this street, where he would offer food of one of these N types. Chef assumes that the people who want to buy the type of food he'd offer will split equally among all stores that offer it, and if this is impossible, i.e. the number of these people p is not divisible by the number of these stores s, then only ⌊ps⌋ people will buy food from Chef.Chef wants to maximise his daily profit. Help Chef choose which type of food to offer and find the maximum daily profit he can make.

#### Input => The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
#### The first line of each test case contains a single integer N.
#### N lines follow. For each i (1≤i≤N), the i-th of these lines contains three space-separated integers Si, Pi and Vi.

## Solution
(https://www.codechef.com/viewsolution/36200324)

## Question 8

### Zack And The Handkerchieves

##### Theory => Zack is a tailor by profession. He is famous for making square-shaped beautifully-cut and sewed handkerchieves.The customers demand large-sized handkerchieves. So, now Zack is determined to get the maximum size out of the cloth. He has a rectangular piece of cloth of length 'L' and breadth 'B'.His task is to divide it into 'N' square-shaped cloth pieces each of side length ‘S’. So he can make handkerchieves out of them of the maximum size.

#### Input => The first line of the input contains T- the number of test cases. T lines follow. Each line of the test case contains L followed by B.

## Solution
(https://www.codechef.com/viewsolution/36314630)
