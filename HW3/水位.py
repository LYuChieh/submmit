x=list(input("Input seqence of seats: "))
s=[]
for i in x:
    s.append(int(i))
n = len(s)
if n <= 2:
    print("No water can be trapped.")
else:
    left = 0
    right = n - 1
    left_max = 0
    right_max = 0
    water_units = 0
    while left < right:
        if s[left] < s[right]:
            if s[left] >= left_max:
                left_max = s[left]
            else:
                water_units += left_max - s[left]
            left += 1
        else:
            if s[right] >= right_max:
                right_max = s[right]
            else:
                water_units += right_max - s[right]
            right -= 1
print("Maximum units of water that can be trapped:", water_units)

