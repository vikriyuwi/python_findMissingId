def findMissingNumber(arr, diff, low, high):
    mid = low + (high - low) // 2
    
    if low == high:
        return 0
    
    if arr[mid] != arr[mid-1] + diff:
        return (arr[mid-1] + diff)
    
    leftdiff = (arr[mid] - arr[low]) / (mid-low)
    
    if leftdiff != diff:
        return findMissingNumber(arr, diff, low, mid)
    return findMissingNumber(arr, diff, mid, high)

n = int(input("Berapa banyak angka: "))
Numbers = []
print("");

print("Masukkan daftar angka:")
for i in range(n):
    Numbers.append(int(input()))

Numbers.sort()

high = n - 1
diff = (Numbers[high] - Numbers[0]) // n

missingID = findMissingNumber(Numbers, diff, 0, high)
print("\nSelisih angka:", diff)
print("Angka yang hilang yaitu:", missingID)