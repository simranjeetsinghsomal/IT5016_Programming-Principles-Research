# Inheritance in Object-Oriented Programming (OOP)

Inheritance is a fundamental concept in Object-Oriented Programming (OOP), allowing a class to inherit attributes and methods from another class. This promotes code reuse and facilitates the creation of a hierarchy of classes.

## Example
- The Circle class inherits attributes and methods from the Shape class.
## Best Practices for Inheritance:
1. Use Inheritance for "Is-A" Relationships
Inheritance should be used when a subclass "is-a" type of its superclass. For example, a Circle "is-a" Shape.
2. Favor Composition Over Inheritance When in Doubt
Sometimes using composition (having an instance of another class as an attribute) can be more flexible than inheritance. This avoids deep class hierarchies.
3. Follow the Liskov Substitution Principle (LSP)
Subclasses should be substitutable for their base classes. This means that wherever the base class is expected, the subclass should be usable without any surprises or errors.
4. Keep Classes and Methods Small and Cohesive
Large classes or methods with multiple responsibilities can lead to confusion. Aim for single responsibility and small, focused classes.
5. Avoid Deep Inheritance Hierarchies
Deep hierarchies can become difficult to manage and understand. Consider refactoring if you find your hierarchy becoming too deep.
## Advantages of Inheritance:
Code Reusability: Inheritance allows for the reuse of code defined in a superclass, reducing redundancy.
Promotes Hierarchy: Inheritance creates a hierarchy of classes, making the code structure more organized and understandable.
Polymorphism: Subclasses can be treated as instances of their superclass, allowing for polymorphic behavior. This means that a method can behave differently based on the object it is called with.

## Disadvantages of Inheritance:
Tight Coupling: Subclasses become tightly coupled with their superclasses. Changes in the superclass can affect subclasses.
Overuse: Overusing inheritance can lead to a complex and rigid class structure, making it harder to maintain and extend the code.
Inappropriate Use: Using inheritance where it is not suitable can lead to incorrect design and potential bugs.
