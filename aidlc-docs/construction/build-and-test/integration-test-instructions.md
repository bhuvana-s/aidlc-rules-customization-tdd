# Integration Test Instructions - Calculator Desktop App

## Purpose

Test the integration between the calculator logic and the PyQt5 GUI to ensure they work together correctly.

**TDD Note**: Unit tests verified the calculator logic independently. Integration tests verify the GUI correctly uses the calculator logic.

---

## Test Environment Setup

### Prerequisites

- Build completed successfully
- Unit tests passing (15/15)
- PyQt5 installed
- macOS environment

### Start the Application

```bash
python calculator.py
```

The calculator window should appear with:
- Display showing "0"
- Number buttons (0-9)
- Operator buttons (+, -, *, /)
- Equals button (=)
- Clear button (C)
- Decimal point button (.)

---

## Manual Integration Test Scenarios

### Scenario 1: Basic Arithmetic Operations

**Purpose**: Verify GUI buttons correctly trigger calculator logic

#### Test 1.1: Addition
1. Click: `5`
2. Click: `+`
3. Click: `3`
4. Click: `=`
5. **Expected**: Display shows `8`

#### Test 1.2: Subtraction
1. Click: `C` (clear)
2. Click: `1`, `0`
3. Click: `-`
4. Click: `4`
5. Click: `=`
6. **Expected**: Display shows `6`

#### Test 1.3: Multiplication
1. Click: `C` (clear)
2. Click: `6`
3. Click: `*`
4. Click: `7`
5. Click: `=`
6. **Expected**: Display shows `42`

#### Test 1.4: Division
1. Click: `C` (clear)
2. Click: `1`, `5`
3. Click: `/`
4. Click: `3`
5. Click: `=`
6. **Expected**: Display shows `5`

**Status**: [ ] Pass / [ ] Fail

---

### Scenario 2: Decimal Number Handling

**Purpose**: Verify decimal point functionality integrates with calculator logic

#### Test 2.1: Decimal Addition
1. Click: `C` (clear)
2. Click: `2`, `.`, `5`
3. Click: `+`
4. Click: `3`, `.`, `7`
5. Click: `=`
6. **Expected**: Display shows `6.2`

#### Test 2.2: Decimal Division
1. Click: `C` (clear)
2. Click: `7`
3. Click: `/`
4. Click: `2`
5. Click: `=`
6. **Expected**: Display shows `3.5`

#### Test 2.3: Multiple Decimal Points (Error Case)
1. Click: `C` (clear)
2. Click: `1`, `.`, `2`, `.`, `3`
3. **Expected**: Only one decimal point appears (display shows `1.23`)

**Status**: [ ] Pass / [ ] Fail

---

### Scenario 3: Error Handling Integration

**Purpose**: Verify GUI displays errors from calculator logic

#### Test 3.1: Division by Zero
1. Click: `C` (clear)
2. Click: `1`, `0`
3. Click: `/`
4. Click: `0`
5. Click: `=`
6. **Expected**: Display shows `Error: Cannot divide by zero`

#### Test 3.2: Recovery After Error
1. (After division by zero error)
2. Click: `C` (clear)
3. Click: `5`, `+`, `3`, `=`
4. **Expected**: Display shows `8` (calculator recovered)

**Status**: [ ] Pass / [ ] Fail

---

### Scenario 4: Sequential Operations

**Purpose**: Verify state management between GUI and calculator logic

#### Test 4.1: Chained Operations
1. Click: `C` (clear)
2. Click: `5`, `+`, `3`, `=`
3. **Expected**: Display shows `8`
4. Click: `*`, `2`, `=`
5. **Expected**: Display shows `16`

#### Test 4.2: Operation Without Equals
1. Click: `C` (clear)
2. Click: `5`, `+`, `3`, `+`
3. **Expected**: Display shows `8` (auto-calculates before new operator)
4. Click: `2`, `=`
5. **Expected**: Display shows `10`

**Status**: [ ] Pass / [ ] Fail

---

### Scenario 5: Clear Functionality

**Purpose**: Verify clear button resets both GUI and calculator state

#### Test 5.1: Clear During Input
1. Click: `5`, `+`, `3`
2. Click: `C` (clear)
3. **Expected**: Display shows `0`
4. Click: `2`, `+`, `2`, `=`
5. **Expected**: Display shows `4` (previous operation cleared)

#### Test 5.2: Clear After Result
1. Click: `5`, `+`, `3`, `=`
2. **Expected**: Display shows `8`
3. Click: `C` (clear)
4. **Expected**: Display shows `0`

**Status**: [ ] Pass / [ ] Fail

---

### Scenario 6: Edge Cases

**Purpose**: Verify GUI handles edge cases correctly

#### Test 6.1: Zero Operations
1. Click: `C` (clear)
2. Click: `0`, `+`, `5`, `=`
3. **Expected**: Display shows `5`

#### Test 6.2: Negative Results
1. Click: `C` (clear)
2. Click: `5`, `-`, `1`, `0`, `=`
3. **Expected**: Display shows `-5`

#### Test 6.3: Large Numbers
1. Click: `C` (clear)
2. Click: `9`, `9`, `9`, `9`, `9`, `9`, `+`, `1`, `=`
3. **Expected**: Display shows `1000000`

**Status**: [ ] Pass / [ ] Fail

---

## Visual and Usability Testing

### Visual Design Verification

- [ ] Display is clearly readable
- [ ] Buttons are appropriately sized
- [ ] Layout is clean and minimalist
- [ ] Button labels are clear
- [ ] Color scheme is consistent
- [ ] Window size is appropriate (300x400)

### Usability Verification

- [ ] Buttons respond to clicks (visual feedback)
- [ ] Display updates immediately after button clicks
- [ ] Error messages are user-friendly
- [ ] Clear button is easily accessible
- [ ] Number pad layout is intuitive
- [ ] Operators are clearly distinguished from numbers

---

## Integration Test Results

### Test Summary

| Scenario | Tests | Passed | Failed | Status |
|----------|-------|--------|--------|--------|
| Basic Arithmetic | 4 | | | |
| Decimal Numbers | 3 | | | |
| Error Handling | 2 | | | |
| Sequential Operations | 2 | | | |
| Clear Functionality | 2 | | | |
| Edge Cases | 3 | | | |
| Visual/Usability | 12 | | | |
| **TOTAL** | **28** | | | |

### Overall Status

- [ ] All integration tests passed
- [ ] Some tests failed (document failures below)

### Failed Tests (if any)

Document any failed tests here:

1. **Test Name**: 
   - **Expected**: 
   - **Actual**: 
   - **Issue**: 

---

## Known Issues

Document any known issues or limitations:

1. **Issue**: 
   - **Impact**: 
   - **Workaround**: 

---

## Integration Test Checklist

- [ ] Calculator logic integrates correctly with GUI
- [ ] All button clicks trigger correct logic operations
- [ ] Display updates correctly after operations
- [ ] Error messages display correctly in GUI
- [ ] Clear button resets both GUI and logic state
- [ ] Sequential operations maintain correct state
- [ ] Decimal point handling works correctly
- [ ] Edge cases handled properly
- [ ] Visual design meets requirements
- [ ] Usability is intuitive

---

## Next Steps

After successful integration testing:
1. Review build-and-test-summary.md
2. Document any issues found
3. Proceed to deployment preparation (if all tests pass)
