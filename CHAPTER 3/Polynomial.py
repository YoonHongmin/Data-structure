class Polynomial :
    def __init__(self) :
        self.coef = []  

    def degree(self) :
        return len(self.coef) - 1 
    
    def display(self, msg ="f(x) =") :
        print(" ",msg, end = '')
        if not self.coef[self.degree()] == 0 :
            print("%.1f x^%d" % (self.coef[self.degree()], self.degree()), end ='  ')

        for i in range(self.degree() , 1 , -1) :
            if self.coef[i-1] > 0 :
                print('+',end='')
            print("%.1f x^%d " % (self.coef[i-1], i-1), end ='')
        if self.coef[0] > 0 :
            print("+ %4.1f" % self.coef[0])
        elif self.coef[0] < 0 :
            print("%5.1f" % self.coef[0])    

    def add(self, b) :
        p = Polynomial()
        if self.degree() > b.degree() :
            p.coef = list(self.coef)
            for i in range(b.degree() + 1) :
                p.coef[i] += b.coef[i]

        else :
            p.coef = list(b.coef)
            for i in range(self.degree()+1) :
                p.coef[i] += self.coef[i]
            return p

    def minus(self, b): 
        p = Polynomial()
        if self.degree() > b.degree():
            p.coef = list(self.coef) 
            for i in range(b.degree()+1):
                p.coef[i] -= b.coef[i]

        elif self.degree() < b.degree(): 
            p.coef = list(b.coef) 
            for i in range(self.degree()+1):
                p.coef[i] -= self.coef[i]
        else: 
            if self.coef[-1] > b.coef[-1]:
                p.coef = list(self.coef)
                for i in range(b.degree() +1):
                    p.coef[i] -= b.coef[i]
            else:
                p.coef = list(b.coef)
                for i in range(self.degree()+1):
                    p.coef[i] -= self.coef[i]
        return p

    def mul(self, b): 
        p = Polynomial()
        if self.degree() > b.degree():
            p.coef = list(self.coef)
            for i in range(b.degree()+1):
                p.coef[i] *= b.coef[i]
        else:
            p.coef = list(b.coef)
            for i in range(self.degree()+1):
                p.coef[i] *= self.coef[i]
        return p

    def eval(self, b) :
        sum = 0
        p = Polynomial()
        b = 2
        for i in range(self.degree(), -1, -1) :
            re = self.coef[i] * b ** i
            sum += re
        return sum

    def read(self) :
        strlist = input("??????????????? ????????? ???????????? ???????????????: ").split()
        for coef in strlist :
            self.coef.append(float(coef))
        self.coef.reverse()
        

a = Polynomial()
b = Polynomial()

a.read()
b.read()

print("\n")
a.display("a(x) = ")
b.display("b(x) = ")

print("\n")
c = b.add(a) 
c.display("??????(x) = ") 
print("  ??????(2) =  ", c.eval(b)) 

print("\n")
d = b.minus(a)
d.display("??????(x) = ")
print("  ??????(2) =  ", d.eval(b))

print("\n")
e = b.mul(a)
e.display("??????(x) = ")
print("  ??????(2) =  ", e.eval(b))