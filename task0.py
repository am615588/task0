n=100
counter = NULL
counter.output = NULL
counter = seq(1, n, by=1)

# Generalize for any varaible a & b
a=3
b=5

for (i in 1:n){
  if(counter[i] %% a == 0 & counter[i] %% b == 0) {
  counter.output[i] = "FizzBuzz"     
        }  
    else if (counter[i] %% a == 0) {
         counter.output[i] = "Fizz"
      }
    else if (counter[i] %% b == 0) {
        counter.output[i] = "Buzz"
      }
    else counter.output[i] = counter[i]
}
