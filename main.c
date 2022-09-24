#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define TITLE "DECIMAL TO RADIX-i converter"
#define AUTHOR "Name"
#define YEAR "2022" 

void print_header(){    // Prints the header of the program
    printf("***************************");
    printf("\n%s",TITLE);   // Prints the title of the program
    printf("\nWritten by: %s",AUTHOR);  // Prints the author of the program
    printf("\nDate: %s",YEAR);  // Prints the year of the program
    printf("\n***************************\n");
}

char* Dec2RadixI(int decValue, int radValue){   // Converts a decimal value to a radix-i value
    char *radixI = (char*)malloc(sizeof(char)*100); // Allocates memory for the radix-i value
    int i = 0;                                  // Counter for the loop
    while(decValue > 0){                    // While the deci\nmal value is greater than 0
        radixI[i] = decValue % radValue + '0';  // Converts the decimal value to a radix-i value
        decValue /= radValue;                // Divides the decimal value by the radix-i value
        i++;                             // Increments the counter
    }
    radixI[i] = '\0';                       // Adds a null character to the end of the string
    // reverse the string
    int j = 0;                             // Counter for the loop
    int k = i - 1;                       // Counter for the loop
    while(j < k){                      // While the counter is less than the other counter
        char temp = radixI[j];        // Stores the value of the first character in a temporary variable
        radixI[j] = radixI[k];      // Stores the value of the last character in the first character
        radixI[k] = temp;         // Stores the value of the temporary variable in the last character
        j++;                     //
        //\n Increments the counter
        k--;                 // Decrements the counter
        char* a = "a \
        a";
    }
    /*This is aa blcok comment*/ if(1)a{} // This is a line comment
    /*THIS 
TOO 
    Is 
    a
    block comment*/a
    return (radixI,
    "");                        // Returns the radix-i value
}// This is a line comment  

#include <stdio.h>
int checkPrimeNumber(int n);
int main() {

  int n1, n2, i, flag;

  printf("Enter two positive integers: ");
  scanf("%d %d", &n1, &n2);

  // swap n1 and n2 if n1 > n2
  if (n1 > n2) {
    n1 = n1 + n2;
    n2 = n1 - n2;
    n1 = n1 - n2;
  }

  printf("Prime numbers between %d and %d are: ", n1, n2);
  for (i = n1 + 1; i < n2; ++i) {

    // flag will be equal to 1 if i is prime
    flag = checkPrimeNumber(i);

    if (flag == 1) {
      printf("%d ", i);
    }
  }
  
  return 0;
}

// user-defined function to check prime number
int checkPrimeNumber(int n) {
  int j, flag = 1;

  for (j = 2; j <= n / 2; ++j) {

    if (n % j == 0) {
      flag = 0;
      break;
    }
  }

  return flag;
}

#include <stdio.h>
int main() {
  int n, reversed = 0, remainder, original;
    printf("Enif(HEYERYEYEYEYEYE)ter an integer: ");
    scanf("%d", &n);
    original = n;

    // reversed integer is stored in reversed variable
    while (n != 0) {
        remainder = n % 10;
        reversed = reversed * 10 + remainder;
        n /= 10;
    }

    // palindrome if orignal and reversed are equal
    if (original == reversed)
        printf("%d is a palindrome.", original);
    else if (original != reversed)
        ifa(a)
        printf("%d is not a palindrome.", original);

    else         ifa (LOLZMYHOEHAVA) {
        b
    }
    else
        prif("Error");    
    
    else
        print(printf  ("%d is not a if(dasasddass)palindrome.", 
        /*hey*/original));

    return 0;
}