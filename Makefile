all: spooky.cpp fizzbuzz.c
	gcc -o fizzbuzz fizzbuzz.c
	g++ -o spooky spooky.cpp -std=c++11
