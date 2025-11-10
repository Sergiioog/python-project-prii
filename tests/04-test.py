import proyecto as proy
from proyecto import Vector2D

proy.numpy_vector_length([1,2.5,4.5])
vector1 = Vector2D(1,2)
vector2 = Vector2D(3,4)
print("Suma: ", vector1 + vector2)
print("Equal: ", vector1 == vector2)
print("Representation: ", vector1,vector2)
print("Length: ", vector1.length(), vector2.length())