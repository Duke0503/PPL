import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_401(self):
        input = """
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_402(self):  
        input = """
            func main()
            func main() begin
                number main
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 402))
    
    def test_403(self):
        input = """
            func main(number a) begin
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_404(self): 
        input = """
            func main() return 1   
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 404))        

    def test_405(self):
        input="""
        func Minh()
        func Duc(number a, number b)
        func main()
        return 0
        func Duc(number c, number d)
        begin
        end
        
        """
        expect="No Function Definition: Minh"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_406(self):
        input = """
            func foo(number a)
            func foo(number a) return     
        
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_407(self):
        input = """
            func foo(number a) return   
        
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_408(self):      
        input = """
            func foo(number a) 
        
            func main() return
        """
        expect = "No Function Definition: foo"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_409(self):  
        input="""
        func happy()
        return 2
        func happy()
        return 1
        func main()
        return 0
        """
        expect="Redeclared Function: happy"
        self.assertTrue(TestChecker.test(input, expect, 409))   
        
    def test_410(self):
        input = """
            number a
            string a 
            
            func main() return
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_411(self):    
        input = """
            func a()
            number a
            
            func main() return
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_412(self):    
        input = """
            func foo() return
            func foo()
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_413(self):     
        input = """
            func foo()
            func foo()
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_414(self):    
        input = """
            func foo() return
            func foo() return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_415(self):    
        input = """
            number foo
            func foo()
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_416(self):    
        input = """
            number a
            func Duc() return
            func main()begin
                number a
                number c
                string Duc
                begin
                    number c
                    string Duc
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_417(self):     
        input = """
            number a
            func Duc() return
            func main()begin
                number a
                string a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_418(self):     
        input = """
            number a
            func Duc() return
            func main()begin
                number a
                begin
                    number a
                end
                string a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_419(self):     
        input = """
            number a
            func Duc() return
            func main()begin
                number a
                begin
                    number a
                    string a
                end
                
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_420(self):     
        input = """
            number a
            func Duc(number a, number Duc, number c)
            begin
                string c
            end
            
            func main() return
        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_421(self):      
        input = """
            number a
            func Duc(number a, number Duc, number c, string c)
            begin
            end
            
            func main() return
        """
        expect = "Redeclared Parameter: c"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_422(self):     
        input = """
            number a
            func Duc(number a, number Duc, number c)
            begin
                begin
                    number a
                end
                number a
            end
            
            func main() return
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_423(self):     
        input = """
            func foo(number a) 
            func foo(number b) return
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_424(self):      
        input = """
            func foo(number a) 
            func foo(string a) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_425(self):    
        input = """
            func foo(number a) 
            func foo(number a, string c) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_426(self):    
        input = """
            func foo(number a, string c) 
            func foo(number a) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 426))
        
    def test_427(self): 
        input = """
            number a <- a
            func main() begin
                number b <- a
                number c <- e
            end
        """
        expect = "Undeclared Identifier: e"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_428(self):     
        input = """
            func a() return 1
            func main() begin
                number b <- a
            end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_429(self):     
        input = """
            func a() return 1
            func main() begin
                number a
                begin 
                    number d
                end
                number b <- a
                number c <- d
            end
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_430(self):     
        input = """
            func a() begin
                a()
            end
            func main() begin
                a()
                b()
            end
        """
        expect = "Undeclared Function: b"
        self.assertTrue(TestChecker.test(input, expect, 430))
        
    def test_431(self):     
        input = """
            func a()
            func main() begin
                a()
            end
            func a() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 431))


    def test_432(self): 
        input = """
            func main() begin
                var i <- 2
                for i until true by 1
                begin
                    break
                    continue
                    begin
                        break
                        continue
                    end
                    
                    for i until true by 1
                    begin
                        break
                        continue
                    end
                    break
                    continue
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_433(self):     
        input = """
            func main() begin
                break
            end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_434(self):     
        input = """
            func main() begin
                continue
            end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 434))
        
    def test_435(self): 
        input = """
            dynamic Duc
            var a <- Duc

            func main() return
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, Id(Duc))"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_436(self):     
        input = """
            number Duc
            var a <- Duc
            number b <- a

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_437(self):     
        input = """
            dynamic Duc
            number a <- Duc
            number b <- Duc

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 437))
        
    def test_438(self):     
        input = """
            func foo() begin
                return 1
                dynamic a
                return a
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_439(self):     
        input = """
            func foo() begin
                number a
                return a
                return 1
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_440(self):     
        input = """
            func foo() begin
                dynamic a
                dynamic b
                a <- b
            end

            func main() return
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_441(self):     
        input = """
            func foo() begin
                number a
                dynamic b
                a <- b
                b <- 1
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_442(self):     
        input = """
            func foo() begin
                number a
                dynamic b
                b <- a
                b <- 1
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 442))
        
    def test_443(self):
        input="""
        func main(number a, number b)
        begin
            dynamic d
            dynamic c
            bool e <- (d...c == c ) and (a > b) or (a < b)
        end
        func main()
        """
        expect="Type Mismatch In Expression: BinaryOp(..., Id(d), BinaryOp(==, Id(c), Id(c)))"
        self.assertTrue(TestChecker.test(input, expect, 443))    

    def test_444(self):
        input = """
            number a <- "1"

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_445(self):    
        input = """
            number a[1,2] <- [[1,2]]

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 445))
        
    def test_446(self):
        input = """
            number a[1,2,3] <- [[1,2]]

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0, 2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))))"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_447(self):
        input = """
            number a[1] <- [[1,2]]

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))))"
        self.assertTrue(TestChecker.test(input, expect, 447))       

    def test_448(self):
        input = """
            func foo() return

            func main()begin
                foo()
                foo(1)
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 448))    

    def test_449(self):    
        input = """
            func foo(number a) return

            func main()begin
                foo()
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 449))     

    def test_450(self):    
        input = """
            func foo(number a) return

            func main()begin
                foo("1")
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 450))    

    def test_451(self):    
        input = """
            func foo(number a) return

            func main()begin
                dynamic a
                foo(a)
                number c <- a
                
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 451))                

    def test_452(self):
        input = """
            func main()begin
                dynamic a
                if (a) return
                a <- true
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 452))     

    def test_453(self):    
        input = """
            func main()begin
                dynamic a <- 1
                if (a) return
            end
        """
        expect = "Type Mismatch In Statement: If((Id(a), Return()), [], None)"
        self.assertTrue(TestChecker.test(input, expect, 453))                 

    def test_454(self):
        input = """
            func main()begin
                dynamic a
                if (a) number a
                elif (a)  return
                else number a
                
                if(true) number a
                elif (1) number a
            end
        """
        expect = "Type Mismatch In Statement: If((BooleanLit(True), VarDecl(Id(a), NumberType, None, None)), [(NumLit(1.0), VarDecl(Id(a), NumberType, None, None))], None)"
        self.assertTrue(TestChecker.test(input, expect, 454)) 

    def test_455(self):    
        input = """
            func foo() begin
                dynamic a
                dynamic b
                dynamic c
                for a until b by c return
                a <- 1
                b <- true
                c <- 1
            end
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 455))   

    def test_456(self):    
        input = """
            func foo() begin
                dynamic a <- true
                dynamic b
                dynamic c
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 456))    

    def test_457(self):    
        input = """
            func foo() begin
                dynamic a 
                dynamic b <- 2
                dynamic c
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 457))  

    def test_458(self):
        input = """
            func foo() begin
                dynamic a 
                dynamic b
                dynamic c <- "1"
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 458))    

    def test_459(self):    
        input = """
            func foo() begin
                number a
                return 1
                return a
                return "!"
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: Return(StringLit(!))"
        self.assertTrue(TestChecker.test(input, expect, 459))  
        
    def test_460(self):    
        input = """
            func foo() begin
                number a
                a <- 1
                a <- true
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 460))  


    def test_461(self):
        input = """
            func foo() return 1

            func main() begin
                var a <- foo()
                var b <- foo(1)
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_462(self):     
        input = """
            func foo(number a) return 1

            func main() begin
                var a <- foo()
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_463(self):    
        input = """
            func foo(number a) return 1

            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_464(self):    
        input = """
            func foo(number a) return
            
            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_465(self):    
        input = """
            func foo(number a) return
            
            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_466(self):    
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- left + right
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_467(self):    
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- left + 1
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_468(self):    
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- 1 + right
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 468))
        
    def test_469(self): 
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- - left
                left <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_470(self):     
        input = """
            func main() begin
                number a[1,2]
                number b
                var c <- b[1]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_471(self):     
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- b[1]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_472(self):     
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[b, 1]
                b <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_473(self):     
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a["1"]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_474(self):     
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1,2,3]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0), NumLit(3.0)])"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_475(self):     
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1,3]
                c <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_476(self):
        input="""
        func main()
        begin
            number a <- 1
            number b <- 2
            bool c <- a > b
            bool d <- a < b
            bool e <- a == b
            bool f <- a != b
            bool g <- a >= b
            bool h <- a <= b
        end
        """
        expect="Type Mismatch In Expression: BinaryOp(==, Id(a), Id(b))"

        self.assertTrue(TestChecker.test(input, expect, 476))   

    def test_477(self): 
        input = """
func f(number x)
begin
    return f(x)
end

func main()
begin
    dynamic d <- f(10)
end
"""
        expect = "Type Cannot Be Inferred: Return(CallExpr(Id(f), [Id(x)]))"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_478(self): 
        input = """
            func areDivisors(number num1, number num2)
            return ((num1 % num2 = 0) or (num2 % num1 = 0))
            func main()
            begin
            var num1 <- readNumber()
            var num2 <- readNumber()
            if (areDivisors(num1, num2)) writeString("Yes")
            else writeString("No")
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_479(self):         
        input = """
func isPrime(number x)
func main()
begin
number x <- readNumber()
if (isPrime(x)) writeString("Yes")
else writeString("No")
end
func isPrime(number x)
begin
if (x <= 1) return false
var i <- 2
for i until i > x / 2 by 1
begin
if (x % i = 0) return false
end
return true
end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_480(self):
        input = """
dynamic x <- f(2)
func f(number x)

func main()
begin

end
"""
        expect = "Undeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_481(self):
        input = """
func add(number x, number y)

func main()
begin
    number x <- readNumber()
    number y <- readNumber()
    writeNumber(pow(x, y))
end

func add(number a, number b)
begin
    return a + b
end
"""
        expect = "Undeclared Function: pow"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_482(self):
        input = """
func f(number x)

func main()
begin
    number x <- 10
    number y <- f(x)
    writeNumber(y)
end

func f(string x)
begin
    return x == "Hello"
end
"""
        expect = "Redeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 482))  

    def test_483(self):
        input = """
func f()

func main()
begin
    number x <- g(1, 2, 3)
end
"""
        expect = "Undeclared Function: g"
        self.assertTrue(TestChecker.test(input, expect, 483)) 

    def test_484(self):
        input = """
func main()

func main()

func main()
begin
    if (1) writeBool(true)
    else writeBool(false)
end
"""
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_485(self):
        input = """
func test(number x)
begin
    var y <- test
    test(2018)
end
"""
        expect = "Undeclared Identifier: test"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_486(self):
        input = """
func main()
begin
    number x <- readNumber()
    if (x <= 10) writeString("Number is less than or equal to 10")
    elif ((x > 10) and (x <= 20)) writeString("Number is between 11 and 20")
    else writeString("Invalid number!")
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_487(self):
        input = """
func main()
begin
    dynamic x <- readBool()
    dynamic y <- not readBool()
    if (x and y) writeNumber(1)
    else writeNumber(0)
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 487)) 

    def test_488(self):
        input = """
func main()
begin
    dynamic x <- "Hello"
    if (x == "Hello") writeString(x)
    else writeString("Something weird!")
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_489(self):
        input = """
func isPrime(number x)

func main()
begin
    number x <- readNumber()
    if (isPrime(x)) writeString("x is a prime number")
    else writeString("x is not a prime number")
end

func isPrime(number x)
begin
    if (x <= 1) return false
    var i <- 2
    for i until i > x / 2 by 1
    begin
        if (x % i = 0) return false
    end
    return true
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 489))
    
    def test_490(self):
        input = """
func areDivisors(number num1, number num2)
    return ((num1 % num2 = 0) or (num2 % num1 = 0))

func main()
begin
    var num1 <- readNumber()
    var num2 <- readNumber()
    if (areDivisors(num1, num2)) writeString("Yes")
    else writeString("No")
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_491(self):
        input = """
func add(number x, number y)

func main()
begin
    var i <- 0
    for i until i > 10 by 0
    begin
        i <- add(i, 1)
        writeNumber(i)
    end
end

func add(number a, number b)
begin
    number x <- a + b
    return x
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_492(self):
        input = """
number x
number y
func add()
    return x + y

func main()
begin
    x <- readNumber()
    y <- readNumber()
    writeNumber(add())
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_493(self):
        input = """
        func areDivisors(number num1, number num2) 
            return ((num1 % num2 = 0) or (num2 % num1 = 0))
            
        func main()
        begin
            var num1 <- readNumber()
            var num2 <- readNumber()
            if (areDivisors(num1, num2)) writeString("Nope")
            else writeString("What?")
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_494(self):
        input = """
        func main()
        begin
            number x <- readNumber()
            if (x <= 5) writeString("Number is smaller or equal 5")
            elif ((x < 5) and (x <= 10)) writeString("Number between 5 and 10")
            else writeString("Number greater than 10")
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_495(self):
        input = """
func f()
begin
    var i <- 0
    for i until i > 10 by 1
    begin

    end
    continue
end

func main()
begin
    f()
end
"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_496(self):
        input = """
func main()
begin
    var i <- 0
    for i until i < 0 by 1
    begin
        string x <- readString()
        if (x == "Hello") 
        begin
            x <- x ... ", world!"
            writeString(x)
        end
        else writeString("Try again")
    end
    break
end
"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_497(self):
        input = """
func main()
begin
    continue
end
"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_498(self):
        input = """
func main()
begin
    break
end
"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_499(self):
        input = """
func max(number x, number y)
begin
    if (x <= y) return y
    return x
end

func main()
begin
    number x <- readNumber()
    number y <- readNumber()
    number z <- readNumber()
    writeNumber(max(max(x, y), z))
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_500(self):
        input = """
func f(number n)

func main()
begin
    var i <- f(2, 3)
end

func f(number a)
    return a
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [NumLit(2.0), NumLit(3.0)])"
        self.assertTrue(TestChecker.test(input, expect, 500))