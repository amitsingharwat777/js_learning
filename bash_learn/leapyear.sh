#leapyear.sh
echo "enter the number : "
read n
a=$(expr $n % 4)  # Fixed spacing and syntax for assignment
b=$(expr $n % 100)  # Fixed spacing and syntax for assignment
c=$(expr $n % 400)  # Fixed spacing and syntax for assignment
if [ $a -eq 0 ] && [ $b -ne 0 ] || [ $c -eq 0 ]  # Fixed spacing in the if condition
then
echo "$n is a leap year"
else
echo "$n is not a leap year"
fi