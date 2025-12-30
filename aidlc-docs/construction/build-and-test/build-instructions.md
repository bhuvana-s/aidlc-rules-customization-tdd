# Build Instructions - Calculator Desktop App

## Prerequisites

### System Requirements
- **Operating System**: macOS (primary target)
- **Python Version**: Python 3.7 or higher
- **Memory**: 512 MB RAM minimum
- **Disk Space**: 100 MB free space

### Required Tools
- Python 3.7+
- pip (Python package manager)
- Virtual environment (recommended)

### Dependencies
- PyQt5 >= 5.15.0 (GUI framework)
- pytest >= 7.0.0 (testing framework)

---

## Build Steps

### 1. Set Up Virtual Environment (Recommended)

Create and activate a Python virtual environment:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment (macOS/Linux)
source venv/bin/activate

# Verify activation (should show venv path)
which python
```

### 2. Install Dependencies

Install all required packages from requirements.txt:

```bash
pip install -r requirements.txt
```

**Expected Output**:
```
Successfully installed PyQt5-5.15.x PyQt5-Qt5-5.15.x PyQt5-sip-12.x pytest-7.x
```

### 3. Verify Installation

Verify that all dependencies are installed correctly:

```bash
# Check PyQt5 installation
python -c "import PyQt5; print('PyQt5 version:', PyQt5.QtCore.PYQT_VERSION_STR)"

# Check pytest installation
pytest --version
```

**Expected Output**:
```
PyQt5 version: 5.15.x
pytest 7.x.x
```

### 4. Verify Build Success

The calculator app is a Python application and doesn't require compilation. Verify the project structure:

```bash
ls -la
```

**Expected Files**:
- `calculator.py` - Main GUI application
- `calculator_logic.py` - Calculator logic module
- `test_calculator.py` - Unit tests
- `requirements.txt` - Dependencies
- `README.md` - Documentation

---

## Build Artifacts

### Application Files
- **Main Application**: `calculator.py`
- **Logic Module**: `calculator_logic.py`
- **Test Suite**: `test_calculator.py`

### No Compilation Required
This is a Python application that runs directly from source code. No build artifacts are generated.

---

## Troubleshooting

### Issue: pip install fails with "command not found"

**Cause**: pip is not installed or not in PATH

**Solution**:
```bash
# Install pip
python3 -m ensurepip --upgrade

# Or use easy_install
sudo easy_install pip
```

### Issue: PyQt5 installation fails on macOS

**Cause**: Missing system dependencies or incompatible Python version

**Solution**:
```bash
# Update pip and setuptools
pip install --upgrade pip setuptools

# Try installing PyQt5 again
pip install PyQt5

# If still fails, try PyQt6 as alternative
pip install PyQt6
# (Note: Code uses PyQt5, may need minor adjustments for PyQt6)
```

### Issue: Permission denied during installation

**Cause**: Trying to install to system Python without sudo

**Solution**:
```bash
# Use virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# OR use --user flag
pip install --user -r requirements.txt
```

### Issue: "No module named 'PyQt5'" when running

**Cause**: Virtual environment not activated or PyQt5 not installed

**Solution**:
```bash
# Activate virtual environment
source venv/bin/activate

# Verify PyQt5 is installed
pip list | grep PyQt5

# If not installed, install it
pip install PyQt5
```

---

## Environment Variables

No environment variables are required for this application.

---

## Build Verification Checklist

- [ ] Python 3.7+ is installed
- [ ] Virtual environment created and activated
- [ ] All dependencies installed successfully
- [ ] PyQt5 imports without errors
- [ ] pytest is available
- [ ] All source files present
- [ ] No import errors when running `python -c "import calculator_logic"`

---

## Next Steps

After successful build:
1. Run unit tests (see unit-test-verification.md)
2. Run the application (see README.md)
3. Perform manual testing
