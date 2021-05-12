import itertools
import tkinter

# constants
width_window = 500
height_window = 500
x_up_right = 100
y_up_right = 50
width_traffic = 300
height_traffic = 400
# Нужно доработать, фргументы передавaть ars and kwars

class TrafficLight:
    def __init__(self, x=x_up_right, y=y_up_right, a=width_traffic, b=height_traffic):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.color = 'black'
        self.id_oval = None  # идетификатор фонаря
        self.colors = itertools.cycle(['red', 'yellow', 'green'])
        self.time_work = 2000  # время работы

    def count_coordinates(self):
        """Координаты светофора"""
        coordinates = [self.x, self.y]
        right_down = [self.x + self.a, self.y + self.b]
        coordinates.extend(right_down)
        return coordinates

    def draw_light(self):
        """Отрисовываем фонарь"""
        self.id_oval = canvas.create_oval(150, 150, 350, 350, fill=str(next(self.colors)))

    def draw_ground(self):
        """Отрисовываем корпус светофора"""
        canvas.create_rectangle(*(self.count_coordinates()), fill=self.color)

    def main(self):
        self.draw_ground()
        if self.id_oval is globals():
            canvas.itemconfig(self.id_oval, fill=str(next(self.colors)))
        else:
            self.draw_light()
        canvas.after(self.time_work, self.main)


root = tkinter.Tk()
root.title('TrafficLight')
canvas = tkinter.Canvas(root, width=width_window, height=height_window)
canvas.pack()
unit_1 = TrafficLight()
unit_1.main()
root.mainloop()
