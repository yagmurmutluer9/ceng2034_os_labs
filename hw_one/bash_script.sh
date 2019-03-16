#!/bin/bash


echo "You are  in the jail!!!!" 

echo "Tell me your name."
read name
echo "Hi, $name. Do you want to escape?"
echo "If you want to escape, write exit."
echo "If you want to play a game, let's play! 
write 'play'"
read answer
(( number = RANDOM % 10 +1 ))
guess=-1

if [ $answer == "exit" ] ; then
	exit 1
fi

if [ $answer == "play" ] ; then
echo "This is a guess game,
enter a number between 0-10.
good luck!"
 while (( guess != number)); do	 
   (( num=num+1 ))
   read -p "Enter your guess" guess   
	  if (( guess < number)); then
	     echo "Higher!!"
	   elif ((guess > number)); then
	     echo "Lower..."
	     fi
	done
fi

echo -e "Correct! That took $num guesses. \n"

exit 1
