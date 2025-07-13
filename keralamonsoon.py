'''Kerala, blessed with the Western Ghats and abundant monsoon rains, also witnesses a high number of lightning strikes every year, especially during the pre-monsoon and monsoon seasons. On average, districts like Idukki and Wayanad can record intense lightning activity due to their elevation and cloud dynamics.

Appu, a young engineer from Kothamangalam, is designing lightning protection for a row of buildings in a hilly town in Kerala. He surveys N buildings arranged from west to east along a narrow road winding through the hills. The peak of building i has coordinates (Xi, Yi), where Xi is the horizontal distance from the western end and Yi is the height from sea level (in meters).

Appu wants to place lightning rods on top of some buildings. A rod on a building protects that building and all buildings that lie on or under the 45° line of depression both westward and eastward.

In mathematical terms, a lightning rod on building i protects building j if and only if |Xi − Xj| ≤ Yi − Yj.

Your task is to help Appu determine the minimum number of lightning rods he needs to install to protect all the buildings in the street.

Input Format

Your program must read from standard input.

The first line contains a single integer N, the number of buildings.
The next N lines contain two integers Xi and Yi, describing the position and height of the buildings.
The Xi values are guaranteed to be in increasing order (i.e., Xi ≤ Xi+1).
Output Format

Print a single integer: the minimum number of lightning rods needed to protect all buildings.

Input Format

5
1 3
2 2
3 1
5 2
6 1

Constraints

NA

Output Format

2

Sample Input 0'''
n=int(input())
stack=[]
l2=[]
for i in range(n):
    x1, y = map(int, input().split())
    l2.append([x1,y])
stack.append(l2[0])
for i in range(1,n):
    x=stack.pop()
    if (abs(x[0]-l2[i][0])<=x[1]-l2[i][1]):
        stack.append(x)
    elif abs(l2[i][0]-x[0])<=l2[i][1]-x[1]:
        stack.append(l2[i])
    else:
        stack.append(x)
        stack.append(l2[i])
print(len(stack))
    
    
    
