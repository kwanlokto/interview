## Simple REST API (25 minutes)

### Scenario
You need to create a REST API to control a simple counter that can increment, decrement, reset, and return its current value.

### Task
Using Flask, create an API with these endpoints:
- `GET /counter` - Returns current count
- `POST /counter/increment` - Increases by 1, returns new value
- `POST /counter/decrement` - Decreases by 1, returns new value
- `DELETE /counter` - Resets to 0
- `POST /counter/set` - Sets to specific value (from JSON body)

Include proper HTTP status codes and error handling.

### What This Tests
- **Flask basics** - they'll be building Flask APIs over DLLs
- **RESTful design** - understanding HTTP methods and status codes
- **State management** - counters need state, like DLL handles
- **JSON handling** - needed for request/response with APIs
- **Error handling** - critical for production APIs

### Follow-up Questions
- "How would you make this thread-safe if multiple requests come in?"
- "What if you needed to persist the counter value across restarts?"
- "How would you add authentication?"
- "What if incrementing could fail sometimes?"

### Red Flags
- Doesn't use appropriate HTTP methods
- No error handling
- Returns wrong status codes (everything is 200)
- Doesn't validate input
- Can't explain REST principles

### Green Flags
- Uses correct HTTP methods and status codes
- Validates input thoroughly
- Returns consistent JSON structure
- Mentions thread safety concerns
- Thinks about edge cases

---
