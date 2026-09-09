print("Hello world! ♥")

# integer - celo št
x = 13
y = -10

# operacije inta
print(x+y)
print(x-y)
print(x/y)
print(x*y)

# celošt deljenje (//)
print(x//y)
print(int(x/y))

# deljenje z ostankom
print(x%2)

print(type(x))

#spreminjanje tipa (parse)
x = "12"
x = int(x) #float(x), str(x)
print(x+1)
print([[255, 255, 255]] * 1080)

print(0.1 + 0.2 == 0.3)

s = [1,2,3]
print(s[0])

# string - nizi znakov
a = "abc"
b = "def"

print(a+b)

# indeksiranje
print(a[0])


#rezine/slice
#string[od:do:korak]
print(a[0:1])
print(a[::-1]) #obrnjen string
print(len(a))

#f-string
ime = "Anja"
print(f"pozdravljen {ime}")