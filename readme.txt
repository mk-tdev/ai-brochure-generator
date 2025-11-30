// source into venv
# To activate your virtual environment, use the following command:

# On Unix or MacOS:
source .venv/bin/activate

# On Windows:
venv\Scripts\activate


You're using `uv.lock`, so you may have `uv` available. Here are options for creating a virtual environment and running Python:

## Option 1: Using Python's built-in venv (standard method)

1. Create the virtual environment:
   ```bash
   cd /Users/mk/Desktop/workspace/ai-stuff/brochure-maker
   python3 -m venv venv
   ```
   Or if you have Python 3.11+ specifically:
   ```bash
   python3.11 -m venv venv
   ```

2. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
   Your prompt should show `(venv)`.

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Or if you're using `pyproject.toml`:
   ```bash
   pip install -e .
   ```

4. Run your Python script:
   ```bash
   python test.py
   ```

## Option 2: Using uv (if you have it installed)

If you have `uv` installed (you have `uv.lock`), you can use it:

1. Create and activate venv with uv:
   ```bash
   cd /Users/mk/Desktop/workspace/ai-stuff/brochure-maker
   uv venv
   source .venv/bin/activate
   ```

2. Install dependencies from the lock file:
   ```bash
   uv pip install -r requirements.txt
   ```
   Or sync from the lock file:
   ```bash
   uv sync
   ```

3. Run your script:
   ```bash
   python test.py
   ```

## Deactivating the virtual environment

When you're done, deactivate with:
```bash
deactivate
```

## Quick check

To verify it's working:
```bash
python --version  # Should show Python 3.11+
which python      # Should point to your venv directory
```

Since your `pyproject.toml` requires Python >=3.11, make sure you're using Python 3.11 or newer. If you want, I can help check your Python version or troubleshoot any issues.
