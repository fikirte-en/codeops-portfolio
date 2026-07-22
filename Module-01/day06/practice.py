# %% spot SRP violations
class ReportBuilder:
   
    def __init__(self, title, data):
        self.title = title
        self.data = data
 
    def build(self):
        lines = [f"Report: {self.title}", "-" * 30]
        lines += [f"- {item}" for item in self.data]
        return "\n".join(lines)
 
 
class ReportSaver:
    
    def save(self, content, filepath):
        with open(filepath, "w") as f:
            f.write(content)
        return filepath
 
 
class ReportMailer:
    def send(self, content, recipient):
        print(f"[simulated email to {recipient}]")
        print(content)
 
 
def exercise_1():
    builder = ReportBuilder("Sales Q3", ["ETB 1200", "ETB 3400", "ETB 900"])
    content = builder.build()
 
    saver = ReportSaver()
    path = saver.save(content, "/tmp/report.txt")
    print(f"Saved to: {path}")
 
    mailer = ReportMailer()
    mailer.send(content, "manager@example.com")
# %% Refactor to OCP 
class Shape:
    def area(self):
        raise NotImplementedError
 
 
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
 
    def area(self):
        return 3.14159 * self.radius ** 2
 
 
class Square(Shape):
    def __init__(self, side):
        self.side = side
 
    def area(self):
        return self.side ** 2
 
 
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
 
    def area(self):
        return 0.5 * self.base * self.height
 
 
def print_area(shape: Shape):
    print(f"{shape.__class__.__name__} area: {shape.area():.2f}")
 
 
def exercise_2():
    shapes = [Circle(4), Square(3), Triangle(6, 2)]
    for shape in shapes:
        print_area(shape)

# %% Write a Singlton
class AppSettings:
    _instance = None
 
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.currency = "ETB"
        return cls._instance
settings1 = AppSettings()
settings2 = AppSettings()
print("settings1.currency:", settings1.currency)
print("settings2.currency:", settings2.currency)
print("Same object?", settings1 is settings2)
 

# %% Write a factory
class ShapeFactory:
    @staticmethod
    def create(kind, *args):
        kind = kind.lower()
        if kind == "circle":
            return Circle(*args)
        elif kind == "square":
            return Square(*args)
        elif kind == "triangle":
            return Triangle(*args)
        else:
            raise ValueError(f"Unknown shape kind: {kind}")
c = ShapeFactory.create("circle", 5)
s = ShapeFactory.create("square", 4)
t = ShapeFactory.create("triangle", 6, 3)
for shape in (c, s, t):
    print_area(shape)

# %% Write an observer pair

