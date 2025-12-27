# SOLID Principles

## S — Single Responsibility Principle
- A class should have **one reason to change**.
- It's about responsibility to an **actor/stakeholder**, not just "doing one thing".

---

## O — Open/Closed Principle
- **Open for extension, closed for modification**
- You should be able to add behavior without changing existing code
- Achieved via polymorphism, interfaces, composition, strategy pattern, etc.
- Inheritance is just one way, not the definition

---

## L — Liskov Substitution Principle
- Subtypes must be substitutable for their base types without breaking correctness

**In practice:**
- No stronger preconditions
- No weaker postconditions
- No breaking expectations of the base class

---

## I — Interface Segregation Principle
- Clients should not be forced to depend on interfaces they do not use

**In practice:**
- Prefer many small, focused interfaces
- Avoid "fat" interfaces

---

## D — Dependency Inversion Principle
- High-level modules should not depend on low-level modules.
- Both should depend on abstractions.

**Key points:**
- Depend on interfaces, not concrete implementations
- Dependency Injection is a technique that helps achieve this principle