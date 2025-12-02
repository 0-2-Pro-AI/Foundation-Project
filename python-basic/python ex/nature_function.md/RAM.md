RAM is physic product and have a limit of memory(?GB)

when no applications run, RAM is empty

and when something runs, it will run by RAM and RAM will devide segment for each function

text segment: for def like def delete, main,...Each def have their own address and contain the functions in them, and the next def is in the next addresses

data segment: for global variables like "menu for today", the fixed info you declare from the first

stack: for local variables,where the code excute their function, basically, RAM is limit and it can´t create more "real" space when it´s full but operating system will create a virtual space above the stack room when the main( who always stay in the stack to run the application) call the function and another room above again if the function which is called call another function to do another task, and then when the fuction is finish, those above room is deleted

heap: where the big list(.append) is, it varies big or small depend on the elements

basically, stack doesn´t contain any "real" info, it just have the variables with the arrow that connects with the real info is in heap, and when we call the function to find an info, it will run to the heap by the arrow and take the connected info

and the ram is totally fresh whenever u use it cause it delete all the structure when you close the app and create all again when you run it, so there is no problem about address conflict when you want to add more function in def

RAM is clearly defined the area of hardware

1 GB = 1000 Bytes

1 Byte contains 8 bits(switch on/off )

1 bit has 2 modes (on/off) Binary System

computer use electric to count

it is exponential

if you arrange the switch lying to each other, the number of conditions (numbers) will increase with every bit that added

2^0 = 1 conditions (2 modes, 1 bit), max=0
2^1 = 2 conditions (2 modes, 2 bit), max=1
2^2 = 4 conditions (2 modes, 3 bit), max=2
2^3 = 8 conditions (2 modes, 4 bit), max=3
--> Computer universe, everything start with 0