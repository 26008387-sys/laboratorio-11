import turtle

height = 400
width = 500

screen = turtle.Screen()
screen.setup(width, height)
                                        # Agregue aca su codigo

                                        # Configuración inicial del cursor (turtle)
t = turtle.Turtle()
t.speed(0)                              # Máxima velocidad de dibujo
t.hideturtle()                           # Oculta la flecha para que se vea más limpio
t.penup()
t.goto(-250, 0)
t.pendown()
t.goto(250, 0)

t.penup()
t.goto(0, 200)
t.pendown()
t.goto(0, -200)

# 1. PINTAR LOS CUADRANTES
# Función para dibujar y rellenar un rectángulo indicando una esquina y el color
def dibujar_cuadrante(x, y, ancho_c, alto_c, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(ancho_c)
        t.left(90)
        t.forward(alto_c)
        t.left(90)
    t.end_fill()

# Cuadrante Superior Derecho (Color Azul)
dibujar_cuadrante(0, 0, 250, 200, "blue")

# Cuadrante Superior Izquierdo (Color Rojo)
dibujar_cuadrante(-250, 0, 250, 200, "red")

# Cuadrante Inferior Izquierdo (Color Verde)
dibujar_cuadrante(-250, -200, 250, 200, "green")

# Cuadrante Inferior Derecho (Color Naranja)
dibujar_cuadrante(0, -200, 250, 200, "orange")

# Mantener la ventana abierta al finalizar
turtle.done()
