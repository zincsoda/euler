#include <iostream>
#include <cmath>
#include <map>
#include <stdint.h>
#include <cstdlib>

/* The prime factors of 13195 are 5, 7, 13 and 29.
 *
 * What is the largest prime factor of the number 600851475143 ?
 */


struct PrimeInfo {
	PrimeInfo(uint64_t val):val(val),unity(false) {}
  std::map<long /* factor */, int /* count */>factors;
  uint64_t val;		  
  bool unity;		  
};

uint64_t getLowestMultiple(const uint64_t& val, PrimeInfo& info, const uint64_t& lowestPrime)
{
   uint64_t value(val);
   while (value % lowestPrime == 0)
   {
       info.factors[lowestPrime]++;
	   value /=lowestPrime;
   }
   return value;
}

void print100Primes()
{
  int num=0;
  std::cout<<"First 100 primes"<<std::endl;
  int value=2;
  uint64_t sumPrimes=0;
  while (num<1000001)
  {
     bool isPrime=true;
     for (int i=2;i<=sqrt(value);i++)
	 {
        if (value%i==0)
		{
			isPrime=false;
			break;
		}
	 }
	 if (isPrime)
	 {
		++num;
		if (value>2000000)
		{
				std::cout<<"sumPrimes="<<sumPrimes<<std::endl;
				exit(0);
		}
		sumPrimes +=value;
	   // std::cout<<value<<std::endl;
	 }
	 value++;

  }

}


void getFactors(uint64_t val)
{
   uint64_t max = sqrt(val);
   PrimeInfo pi600(val);
   uint64_t newVal=getLowestMultiple(pi600.val, pi600, 2);
   for (uint64_t i=3;i<max;i+=2)
   {
      newVal = getLowestMultiple(newVal, pi600,i);
   }
   // collect last number if its also prime
   if (newVal!=1)
       pi600.factors[newVal]++;



   typedef std::map<long, int >::const_iterator facIterator;
   std::cout<<"Factors of "<<pi600.val<<std::endl;
   for (facIterator iter = pi600.factors.begin(); iter != pi600.factors.end(); iter++)
		std::cout << iter->first <<"^"<< iter->second << std::endl;

}

int main()
{
   print100Primes();

   getFactors(600);
   //getFactors(13195);
   //getFactors(600851475143ULL);
   //getFactors(317584931803ULL);
 //  getFactors(60085147514397ULL);
 //  getFactors(160085147514397ULL);
   return 0;
}
