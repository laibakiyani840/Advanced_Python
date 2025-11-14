class Shape:
    def area(self): pass
    def perimeter(self): pass
    def plot(self): pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def plot(self):
        circle = plt.Circle((0, 0), self.radius, fill=False)
        plt.gca().add_patch(circle)
        plt.axis('equal')

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def plot(self):
        rectangle = plt.Rectangle((0, 0), self.length, self.width, fill=False)
        plt.gca().add_patch(rectangle)
        plt.axis('equal')

# Input data
data = list(map(float, input("Enter numbers separated by space: ").split()))
series = pd.Series(data)



"""
Quadratic Equation Analyzer Tool
A modular tool to compute roots and plot parabolas for quadratic equations
"""

import math
import matplotlib.pyplot as plt
import numpy as np

class QuadraticAnalyzer:
    """A class to analyze quadratic equations and visualize their graphs"""
    
    def __init__(self, a, b, c):
        """
        Initialize quadratic equation coefficients
        
        Args:
            a (float): Coefficient of x²
            b (float): Coefficient of x
            c (float): Constant term
        """
        self.a = a
        self.b = b
        self.c = c
        self.nature = None
        self.roots = None
        self.discriminant = None
        self.vertex = None
        
        # Validate and compute
        self._validate_coefficients()
        self._compute_analysis()
    
    def _validate_coefficients(self):
        """Validate input coefficients"""
        if self.a == 0:
            raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation")
        
        if not all(isinstance(coef, (int, float)) for coef in [self.a, self.b, self.c]):
            raise TypeError("All coefficients must be numbers")
    
    def _compute_discriminant(self):
        """Compute the discriminant"""
        return self.b**2 - 4 * self.a * self.c
    
    def _determine_nature(self):
        """Determine the nature of roots based on discriminant"""
        if self.discriminant > 0:
            return "Real and Distinct"
        elif self.discriminant == 0:
            return "Real and Equal"
        else:
            return "Complex"
    
    def _compute_roots(self):
        """Compute the roots of the quadratic equation"""
        if self.nature == "Real and Distinct":
            root1 = (-self.b + math.sqrt(self.discriminant)) / (2 * self.a)
            root2 = (-self.b - math.sqrt(self.discriminant)) / (2 * self.a)
            return [root1, root2]
        
        elif self.nature == "Real and Equal":
            root = -self.b / (2 * self.a)
            return [root]
        
        else:  # Complex roots
            real_part = -self.b / (2 * self.a)
            imaginary_part = math.sqrt(-self.discriminant) / (2 * self.a)
            root1 = complex(real_part, imaginary_part)
            root2 = complex(real_part, -imaginary_part)
            return [root1, root2]
    
    def _compute_vertex(self):
        """Compute the vertex of the parabola"""
        x_vertex = -self.b / (2 * self.a)
        y_vertex = self.a * (x_vertex**2) + self.b * x_vertex + self.c
        return (x_vertex, y_vertex)
    
    def _compute_analysis(self):
        """Perform complete analysis of the quadratic equation"""
        self.discriminant = self._compute_discriminant()
        self.nature = self._determine_nature()
        self.roots = self._compute_roots()
        self.vertex = self._compute_vertex()
    
    def get_roots(self):
        """Get the computed roots"""
        return self.roots
    
    def get_nature(self):
        """Get the nature of roots"""
        return self.nature
    
    def get_discriminant(self):
        """Get the discriminant value"""
        return self.discriminant
    
    def get_vertex(self):
        """Get the vertex coordinates"""
        return self.vertex
    
    def get_equation_string(self):
        """Get the equation as a formatted string"""
        terms = []
        if self.a != 0:
            terms.append(f"{self.a}x²" if self.a != 1 else "x²")
        if self.b != 0:
            terms.append(f"{self.b:+}x")
        if self.c != 0:
            terms.append(f"{self.c:+}")
        
        equation = " ".join(terms).lstrip('+')
        return equation + " = 0"
    
    def plot_parabola(self, x_range=(-10, 10), figsize=(10, 6)):
        """
        Plot the quadratic equation parabola
        
        Args:
            x_range (tuple): Range of x values to plot
            figsize (tuple): Figure size
        """
        # Generate x values
        x = np.linspace(x_range[0], x_range[1], 400)
        y = self.a * x**2 + self.b * x + self.c
        
        # Create plot
        plt.figure(figsize=figsize)
        
        # Plot the parabola
        plt.plot(x, y, 'b-', linewidth=2, label=f'y = {self.get_equation_string()[:-3]}')
        
        # Plot roots if they are real
        if "Complex" not in self.nature:
            for i, root in enumerate(self.roots):
                plt.plot(root, 0, 'ro', markersize=8, label=f'Root {i+1}: {root:.2f}')
        
        # Plot vertex
        vertex_x, vertex_y = self.vertex
        plt.plot(vertex_x, vertex_y, 'g^', markersize=10, 
                label=f'Vertex: ({vertex_x:.2f}, {vertex_y:.2f})')
        
        # Add coordinate axes
        plt.axhline(y=0, color='k', linestyle='-', linewidth=0.8, alpha=0.7)
        plt.axvline(x=0, color='k', linestyle='-', linewidth=0.8, alpha=0.7)
        
        # Formatting
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.title(f'Quadratic Equation: {self.get_equation_string()}\nNature of Roots: {self.nature}')
        plt.xlabel('x')
        plt.ylabel('y')
        
        # Adjust y-axis limits for better visualization
        y_margin = (max(y) - min(y)) * 0.1
        plt.ylim(min(y) - y_margin, max(y) + y_margin)
        
        plt.tight_layout()
        plt.show()
    
    def display_analysis(self):
        """Display complete analysis of the quadratic equation"""
        print("\n" + "="*50)
        print("QUADRATIC EQUATION ANALYSIS")
        print("="*50)
        print(f"Equation: {self.get_equation_string()}")
        print(f"Discriminant (D): {self.discriminant:.2f}")
        print(f"Nature of Roots: {self.nature}")
        print(f"Roots: {self.roots}")
        print(f"Vertex: ({self.vertex[0]:.2f}, {self.vertex[1]:.2f})")
        print(f"Y-intercept: (0, {self.c})")
        print("="*50)


# Utility functions for quick analysis
def quick_analyze(a, b, c):
    """
    Quick function to analyze quadratic equation
    
    Args:
        a, b, c (float): Coefficients
        
    Returns:
        QuadraticAnalyzer: Analyzer object
    """
    return QuadraticAnalyzer(a, b, c)

def solve_quadratic(a, b, c):
    """
    Quick function to solve quadratic equation
    
    Returns:
        tuple: (nature, roots, discriminant)
    """
    analyzer = QuadraticAnalyzer(a, b, c)
    return analyzer.get_nature(), analyzer.get_roots(), analyzer.get_discriminant()