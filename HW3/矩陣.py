m=input("Enter index x,y,k (separated by whitespace): ")
print("Enter the matrix by mutiple lines: ")
matrix=[]
while True:#輸入者用矩陣方式輸入然後停止輸入就打q就會停止，然後把q從matrix中pop掉
    row=input()
    a=row.split(" ")
    matrix.append(a)#創建一個矩陣
    if a==["q"]:
        matrix.pop()
        break
x,y,k=m.split(" ")
x,y,k=int(x),int(y),k
z=matrix[x][y]
def replace_pixel(matrix,x,y,z,k):#這裡是一個遞迴函式，他會將座標像素以及與其相鄰的可轉變像素的相鄰像素都轉換成指定像素
    if x<0 or x>=len(matrix) or y<0 or y>=len(matrix[0]):
        return
    if matrix[x][y]!=z:
        return
    matrix[x][y]=k
    replace_pixel(matrix,x+1,y,z,k)
    replace_pixel(matrix,x,y+1,z,k)
    replace_pixel(matrix,x,y-1,z,k)
    replace_pixel(matrix,x-1,y,z,k)
replace_pixel(matrix,x,y,z,k)#呼叫該函式
for row in matrix:#一行一行列印才有辦法換行
    print(" ".join(row))#將串列中元素組成字串
