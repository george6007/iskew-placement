'''You are designing a virtual machine for a new programming language called Lombok. The Lombok Virtual Machine (LVM) runs an assembler-like machine code. It operates on a stack and a single register.
In detail, the instructions work as follows:
PUSH x: This instruction pushes a given integer onto the stack. If the stack for example looks like this: [2, 3] and the machine executes the instruction PUSH -11,the stack looks like this afterwards: [-11, 2, 3]
STORE: This instruction takes the topmost integer from the stack and stores it in the register. If the stack for example looks like this: [3, 9, 4], the register contains any integer, and the machine executes the instruction STORE, the stack looks like this afterwards: [9, 4] and the register contains the integer 3.
LOAD: This instruction copies the content of the register and pushes it onto the stack. If the register for example contains the integer 6, the stack looks like this: [8, 7], and the machine executes the instruction LOAD, the stack looks like this afterwards: [6, 8, 7], and the register still contains the integer 6.
PLUS: This instruction takes the two topmost integers from the stack, adds them, and pushes the resulting integer back onto the stack. If the stack for example looks like this: [2, 3, 4], and the machine executes the instruction PLUS, the stack looks like this afterwards: [5, 4]
TIMES: This instruction takes the two topmost integers from the stack, multiplies them, and pushes the resulting integer back onto the stack. If the stack for example looks like this: [2, 3, 4], and the machine executes the instruction TIMES, the stack looks like this afterwards: [6, 4]
IFZERO n: This instruction removes the topmost integer from the stack, and checks if it is equal to 0. If that is the case, it jumps to the nth instruction (start counting at 0). If not, the machine continues as usual with the next instruction. See example below.
DONE: Finally, the DONE instruction prints out the integer on top of the stack, and terminates the program regardless of the following instructions.
Computation starts with the first instruction. Initially, the stack is empty and the register contains the number 0.
Input Format
14
PUSH 5
STORE
LOAD
LOAD
PUSH -1
PLUS
STORE
LOAD
IFZERO 13
LOAD
TIMES
PUSH 0
IFZERO 3
DONE
Constraint
NA
Output Format
120
'''
from collections import deque
n=int(input())
stack=deque()
l2=[]
for i in range(n):
    l1=input().split()
    l2.append(l1)
    

i=0
register=0
x=0
while(i<n):
    if l2[i][0]=="PUSH":
        stack.appendleft(int(l2[i][1]))
    elif l2[i][0]=="STORE":
        register=stack.popleft()
    elif l2[i][0]=="LOAD":
        stack.appendleft(register)
    elif l2[i][0]=="PLUS":
        x=stack.popleft()
        y=stack.popleft()
        s=x+y
        stack.appendleft(x+y)
    elif l2[i][0]=="TIMES":
        x1=stack.popleft()
        x2=stack.popleft()
        p=x1*x2
        stack.appendleft(p)
    elif l2[i][0]=="IFZERO":
        x=stack.popleft()
        if x==0:
            i=int(l2[i][1])-1
    elif l2[i][0]=="DONE":
        top=stack.popleft()
        print(top)
    
    i+=1
                         
                         
                         
        
    

    
