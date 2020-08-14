# CodeChef

Some CodeChef Question are.

## Question 1

### Life, the Universe, and Everything .

#### Input => Your program is to use the brute-force approach in order to find the Answer to Life, the Universe, and Everything.More precisely... rewrite small numbers from input to output. Stop processing input after reading in the number 42. All numbers at input are integers of one or two digits.
         
 
## Solution
```bash
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
