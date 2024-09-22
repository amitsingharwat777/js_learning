#evenOrOdd.sh
echo "enter the number"
read n
r=$(expr $n % 2)  # Fixed spacing and syntax for assignment
if [ $r -eq 0 ]  # Fixed spacing in the if condition
then 
echo "the number is even"
else 
echo "the number is odd"
fi