echo "enter the number"
read n 
i=$(expr $n - 1)  # Fixed spacing and syntax for assignment
while [ $i -ge 1 ]  # Fixed spacing in the while condition
do
n=$(expr $n \* $i)  # Fixed spacing and syntax for assignment
i=$(expr $i - 1)  # Fixed spacing and syntax for assignment
done
echo "the factorial of the given Number is $n"
