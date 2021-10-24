import math
class MathFormula:
    import math
    def __init__(self):
        pass

    def areaOfcircle(self,radius):
        a=math.pi*radius*radius
        return f" Area of this circle is {a} "
    
    def perimeterOfcircle(self,radius):
        perimeter=2*math.pi*radius
        return f"Perimeter of this circle is {perimeter}"

    def areaOfrectangle(self,length,breadth):
        '"Enter length and breadth of rectangle "'
        area=length*breadth
        return f"Area of rectangle is {area}"

    def perimeterOfrectangle(self,length,breadth):
        '"Enter length and breadth of rectangle "'
        peri=2*(length+breadth)
        return f"perimeter of rectangle is {peri}"

obj=MathFormula()  
a=int(input("Enetr length"))
print(obj.perimeterOfcircle(a))

        