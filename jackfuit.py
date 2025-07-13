'''
Chackochan is preparing for the grand Chakka Mahotsavam (Jackfruit Festival) in his village in Kerala! As part of the festivities, he wants to make as much jackfruit jam as possible to win the hearts of the judges.
Luckily, Chackochan owns a lush jackfruit farm and has just finished harvesting the fruits. Being incredibly skilled, he has managed to collect N jackfruits, each with a different weight. A jackfruit weighing W kg can be turned into exactly W kg of jackfruit jam.
However, the festival is only D days away, and he can process only one jackfruit per day.
Given the weights of the jackfruits he has collected, help Chackochan calculate the maximum amount of jackfruit jam (in kg) he can prepare before the festival.
Input:
The first line contains two integers: N and D. The second line contains N integers, where the i-th integer represents the weight of the i-th jackfruit.
Output:
Print a single integer — the maximum amount of jackfruit jam Chackochan can prepare.
'''

n,d=map(int,input().split())
l=list(map(int,input().split(" ")))
l.sort()
print(sum(l[n-d:n]))
    
    
        
    
