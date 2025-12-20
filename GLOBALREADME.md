# Co-op Interview Questions: Foundational Skills for DLL/Flask/Python Work

## Overview
These questions assess the foundational skills needed to work with DLLs, Flask, and Python without requiring prior DLL experience. They test problem-solving, APIs, data structures, and debugging skills that transfer directly to DLL integration work.

---

## Question 4: Error Handling & Debugging (20 minutes)

### Scenario
You're working with a function that sometimes fails:

```python
def unreliable_operation(device_id, data):
    """
    This function sometimes works, sometimes fails
    - Returns: (success: bool, result: any, error_code: int)
    - error_code: 0=success, 1=invalid device, 2=timeout, 3=data error
    """
    # Simulates unreliable hardware
    pass
```

### Task
Write a wrapper that:
1. Retries failed operations (with a max retry count)
2. Logs all attempts
3. Raises clear exceptions with helpful messages
4. Has a timeout mechanism

### What This Tests
- **Error handling** - critical for DLL work where failures are common
- **Retry logic** - needed for unreliable hardware
- **Logging** - essential for debugging DLL issues
- **Exception design** - creating helpful error messages
- **Timeout handling** - preventing hangs

### Good Answer Example
```python
import logging
import time
from typing import Any, Tuple

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DeviceError(Exception):
    """Custom exception for device operations"""
    pass

class DeviceTimeoutError(DeviceError):
    """Raised when device operation times out"""
    pass

def reliable_operation(device_id: int, data: Any, max_retries: int = 3, timeout: float = 5.0) -> Any:
    """
    Wrapper that adds retry logic and better error handling
    
    Args:
        device_id: Device identifier
        data: Data to send
        max_retries: Maximum number of retry attempts
        timeout: Max time to wait (seconds)
        
    Returns:
        Result from the operation
        
    Raises:
        DeviceError: If operation fails after all retries
        DeviceTimeoutError: If operation times out
    """
    start_time = time.time()
    
    for attempt in range(max_retries):
        # Check timeout
        if time.time() - start_time > timeout:
            logger.error(f"Operation timed out after {timeout}s")
            raise DeviceTimeoutError(f"Operation timed out after {timeout}s")
        
        try:
            logger.info(f"Attempt {attempt + 1}/{max_retries} for device {device_id}")
            
            success, result, error_code = unreliable_operation(device_id, data)
            
            if success:
                logger.info(f"Operation succeeded on attempt {attempt + 1}")
                return result
            else:
                # Map error codes to messages
                error_messages = {
                    1: "Invalid device ID",
                    2: "Device timeout",
                    3: "Data format error"
                }
                error_msg = error_messages.get(error_code, f"Unknown error code {error_code}")
                
                logger.warning(f"Attempt {attempt + 1} failed: {error_msg}")
                
                # Don't retry on invalid device
                if error_code == 1:
                    raise DeviceError(f"Invalid device ID: {device_id}")
                
                # Wait before retry (exponential backoff)
                if attempt < max_retries - 1:
                    wait_time = 0.5 * (2 ** attempt)  # 0.5s, 1s, 2s
                    logger.info(f"Waiting {wait_time}s before retry")
                    time.sleep(wait_time)
        
        except Exception as e:
            logger.error(f"Unexpected error on attempt {attempt + 1}: {e}")
            if attempt == max_retries - 1:
                raise DeviceError(f"Operation failed after {max_retries} attempts: {e}")
    
    raise DeviceError(f"Operation failed after {max_retries} attempts")

# Usage example
try:
    result = reliable_operation(device_id=1, data="test", max_retries=3, timeout=10.0)
    print(f"Success: {result}")
except DeviceTimeoutError as e:
    print(f"Timeout: {e}")
except DeviceError as e:
    print(f"Error: {e}")
```

### Follow-up Questions
- "Should all errors be retried? Which ones shouldn't?"
- "How would you decide the retry delay?"
- "What information would be most helpful in error messages?"
- "How would you test this retry logic?"

### Red Flags
- No retry logic
- Retries errors that shouldn't be retried
- No logging
- Generic error messages that don't help debug
- Doesn't consider timeout

### Green Flags
- Implements exponential backoff
- Distinguishes retryable vs non-retryable errors
- Adds comprehensive logging
- Creates custom exception types
- Considers timeout scenarios
- Error messages contain useful context

---

## Question 5: Callback Pattern (15 minutes)

### Scenario
You're working with an asynchronous system that notifies you when events happen:

```python
class EventSystem:
    def register_callback(self, event_type, callback_func):
        """Register a function to be called when event occurs"""
        pass
    
    def trigger_event(self, event_type, data):
        """Triggers all callbacks for this event type"""
        pass
```

### Task
1. Implement a simple version of this EventSystem
2. Create an example that shows how to use it
3. Handle the case where a callback raises an exception

### What This Tests
- **Callback patterns** - used heavily with DLLs for async operations
- **Function references** - understanding how to store and call functions
- **Error isolation** - one callback failing shouldn't break others
- **Data passing** - how data flows through callbacks

### Good Answer Example
```python
from typing import Callable, Dict, List, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EventSystem:
    def __init__(self):
        # Store callbacks: {event_type: [callback_functions]}
        self._callbacks: Dict[str, List[Callable]] = {}
    
    def register_callback(self, event_type: str, callback_func: Callable):
        """Register a callback for an event type"""
        if event_type not in self._callbacks:
            self._callbacks[event_type] = []
        
        self._callbacks[event_type].append(callback_func)
        logger.info(f"Registered callback for '{event_type}'")
    
    def trigger_event(self, event_type: str, data: Any):
        """Trigger all callbacks for this event type"""
        if event_type not in self._callbacks:
            logger.warning(f"No callbacks registered for '{event_type}'")
            return
        
        logger.info(f"Triggering event '{event_type}' with data: {data}")
        
        # Call all callbacks, isolating errors
        for callback in self._callbacks[event_type]:
            try:
                callback(data)
            except Exception as e:
                # Log error but continue to other callbacks
                logger.error(f"Callback {callback.__name__} failed: {e}")

# Example usage
def on_data_received(data):
    """Handle data received event"""
    print(f"Data received: {data}")

def on_data_received_logger(data):
    """Log received data"""
    logger.info(f"Logging data: {data}")

def broken_callback(data):
    """This callback will fail"""
    raise ValueError("Something went wrong!")

# Setup
event_system = EventSystem()

# Register callbacks
event_system.register_callback('data_received', on_data_received)
event_system.register_callback('data_received', on_data_received_logger)
event_system.register_callback('data_received', broken_callback)

# Trigger event
event_system.trigger_event('data_received', {'temperature': 25.5, 'humidity': 60})
```

### Follow-up Questions
- "How would you unregister a callback?"
- "What if callbacks need to be called in a specific order?"
- "How would you make this thread-safe?"
- "What if you need to pass additional context to callbacks?"

### Red Flags
- Can't implement basic callback storage
- Doesn't handle callback exceptions (lets them propagate)
- Doesn't understand function references
- Can't explain when you'd use callbacks

### Green Flags
- Implements error isolation (one callback failing doesn't affect others)
- Logs errors appropriately
- Clean API design
- Understands when callbacks are useful
- Mentions thread safety concerns

---

## Question 6: State Management (15 minutes)

### Scenario
You're building a connection manager that needs to track multiple device connections:

```python
# Each device has an ID and needs to maintain connection state
# States: "disconnected", "connecting", "connected", "error"
```

### Task
Design a class that:
1. Can connect/disconnect devices by ID
2. Tracks the state of each device
3. Prevents invalid state transitions (e.g., can't disconnect if not connected)
4. Returns information about all devices

### What This Tests
- **State management** - critical for DLL handles and resources
- **Resource tracking** - keeping track of what's open/closed
- **State machine logic** - valid transitions between states
- **Dictionary usage** - mapping IDs to state

### Good Answer Example
```python
from enum import Enum
from typing import Dict, Optional

class DeviceState(Enum):
    DISCONNECTED = "disconnected"
    CONNECTING = "connecting"
    CONNECTED = "connected"
    ERROR = "error"

class ConnectionManager:
    def __init__(self):
        self._devices: Dict[int, DeviceState] = {}
    
    def connect(self, device_id: int) -> bool:
        """Connect to a device"""
        current_state = self._devices.get(device_id, DeviceState.DISCONNECTED)
        
        # Validate state transition
        if current_state in [DeviceState.CONNECTING, DeviceState.CONNECTED]:
            print(f"Device {device_id} already {current_state.value}")
            return False
        
        # Transition to connecting
        self._devices[device_id] = DeviceState.CONNECTING
        
        try:
            # Simulate connection (in real code, call DLL here)
            print(f"Connecting to device {device_id}...")
            # ... connection logic ...
            
            # Success - transition to connected
            self._devices[device_id] = DeviceState.CONNECTED
            print(f"Device {device_id} connected")
            return True
            
        except Exception as e:
            # Error - transition to error state
            self._devices[device_id] = DeviceState.ERROR
            print(f"Failed to connect to device {device_id}: {e}")
            return False
    
    def disconnect(self, device_id: int) -> bool:
        """Disconnect from a device"""
        current_state = self._devices.get(device_id)
        
        # Validate device exists and is connected
        if current_state is None:
            print(f"Device {device_id} not found")
            return False
        
        if current_state != DeviceState.CONNECTED:
            print(f"Device {device_id} not connected (state: {current_state.value})")
            return False
        
        try:
            # Simulate disconnection
            print(f"Disconnecting device {device_id}...")
            # ... disconnection logic ...
            
            self._devices[device_id] = DeviceState.DISCONNECTED
            print(f"Device {device_id} disconnected")
            return True
            
        except Exception as e:
            self._devices[device_id] = DeviceState.ERROR
            print(f"Error disconnecting device {device_id}: {e}")
            return False
    
    def get_state(self, device_id: int) -> Optional[DeviceState]:
        """Get current state of a device"""
        return self._devices.get(device_id)
    
    def get_all_devices(self) -> Dict[int, str]:
        """Get all devices and their states"""
        return {dev_id: state.value for dev_id, state in self._devices.items()}
    
    def get_connected_devices(self) -> list[int]:
        """Get list of connected device IDs"""
        return [dev_id for dev_id, state in self._devices.items() 
                if state == DeviceState.CONNECTED]

# Usage
manager = ConnectionManager()
manager.connect(1)
manager.connect(2)
print(manager.get_all_devices())
manager.disconnect(1)
print(manager.get_connected_devices())
```

### Follow-up Questions
- "How would you handle cleanup if the program crashes?"
- "What if multiple threads try to connect the same device?"
- "How would you add timeouts for stuck connections?"
- "What data would you store beyond just the state?"

### Red Flags
- Doesn't validate state transitions
- No error handling
- Can't track multiple devices
- Uses strings instead of enums for states
- Doesn't consider concurrent access

### Green Flags
- Uses enums for states
- Validates state transitions
- Handles errors and moves to error state
- Provides query methods for state
- Mentions thread safety
- Thinks about resource cleanup

---

## Practical Coding Exercise (30 minutes)

### The Challenge
Build a simple HTTP API that wraps this "device simulator":

```python
class DeviceSimulator:
    """Simulates a hardware device (pretend this is a DLL)"""
    
    def __init__(self):
        self._connected = False
        self._data = []
    
    def connect(self) -> bool:
        """Connect to device. Returns True on success."""
        import random
        if random.random() > 0.2:  # 80% success rate
            self._connected = True
            return True
        return False
    
    def disconnect(self):
        """Disconnect from device"""
        self._connected = False
        self._data = []
    
    def is_connected(self) -> bool:
        """Check if connected"""
        return self._connected
    
    def read_data(self) -> dict:
        """Read data from device. Must be connected."""
        if not self._connected:
            raise RuntimeError("Not connected")
        
        import random
        return {
            'temperature': round(20 + random.random() * 10, 2),
            'humidity': round(40 + random.random() * 20, 2),
            'timestamp': time.time()
        }
```

### Requirements
Create a Flask API with these endpoints:
1. `POST /device/connect` - Connect to device (with retry logic)
2. `DELETE /device/disconnect` - Disconnect from device
3. `GET /device/status` - Get connection status
4. `GET /device/data` - Read current data from device
5. All endpoints should return appropriate status codes and error messages

### What This Tests (All Together)
- Flask API design
- State management
- Error handling
- Retry logic
- Input validation
- Real-world problem solving

### Evaluation Criteria
**Must Have:**
- ✓ All endpoints work
- ✓ Proper HTTP status codes
- ✓ Error handling for "not connected" state
- ✓ Can handle connection failures

**Nice to Have:**
- ✓ Retry logic for connection
- ✓ Proper state management
- ✓ Logging
- ✓ Input validation
- ✓ Documentation/comments

**Bonus Points:**
- ✓ Thread safety consideration
- ✓ Automatic disconnection on errors
- ✓ Health check endpoint
- ✓ Metrics (successful/failed operations)

---

## Overall Assessment Framework

### Junior Co-op (1st/2nd year) - Should be able to:
- ✓ Write basic Python functions and classes
- ✓ Understand basic error handling (try/except)
- ✓ Work with dictionaries and lists
- ✓ Create simple Flask endpoints
- ✓ Follow instructions and ask clarifying questions
- ✓ Show willingness to learn

### Intermediate Co-op (2nd/3rd year) - Should be able to:
- ✓ Design clean APIs
- ✓ Implement proper error handling with custom exceptions
- ✓ Understand state management
- ✓ Work with binary data (struct module)
- ✓ Create REST APIs with proper status codes
- ✓ Think about edge cases
- ✓ Write testable code

### Advanced Co-op (3rd/4th year) - Should be able to:
- ✓ Design production-ready APIs
- ✓ Handle concurrency concerns
- ✓ Implement retry logic with backoff
- ✓ Use callbacks and async patterns
- ✓ Comprehensive error handling and logging
- ✓ Consider performance implications
- ✓ Write maintainable, documented code
- ✓ Make good architectural decisions

### Key Qualities to Look For (All Levels):
1. **Problem-solving approach** - Do they break down problems systematically?
2. **Communication** - Do they explain their thinking?
3. **Error handling** - Do they consider what can go wrong?
4. **Code quality** - Is their code readable and organized?
5. **Learning attitude** - Do they ask good questions?
6. **Pragmatism** - Do they focus on what matters?

---

## Red Flags for All Levels:
- ❌ Can't explain their code
- ❌ No error handling whatsoever
- ❌ Gives up when stuck
- ❌ Doesn't ask clarifying questions
- ❌ Can't debug their own code
- ❌ Rigid thinking / can't adapt approach

## Green Flags for All Levels:
- ✅ Thinks out loud
- ✅ Asks good questions
- ✅ Considers edge cases
- ✅ Tests their code mentally
- ✅ Admits when they don't know something
- ✅ Shows genuine interest in the problem
- ✅ Can explain trade-offs in their decisions