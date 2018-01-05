print '\n1. feladat\n'
st = 'Print only the words that start with s in this sentence'
for i in st.split(" "):
    if i.startswith("s"):
           print i

print '\n2. feladat\n'
paros = [p for p in range(0,11) if p % 2 ==0]
print paros

print '\n3. feladat\n'
div3 = [p for p in range(1,50) if p % 3 ==0]
print div3

print '\n4. feladat\n'
for i in st.split(" "):
    if len(i) % 2 == 0:
           print i + " Paros"
print '\n5. feladat'
sor = range(1,101)
for i in sor:
     if i % 3 == 0 and i % 5 == 0:
             print 'FizzBuzz'
     elif i % 5 == 0:
             print 'Buzz'
     elif i % 3 == 0:
             print 'Fizz'
     else:
             print i


print '\n6. feladat\n'
st = 'Create a list of the first letters of every word in this string'
elsob = [e[0] for e in st.split(" ")]
print elsob