# Brochure Maker

An AI-powered tool that automatically generates brochures by scraping websites, extracting relevant content, and using AI models to select the most important pages and information for creating company brochures.

## Features

- 🔗 **Web Scraping**: Automatically fetches links and content from websites
- 🤖 **AI-Powered Link Selection**: Uses AI models (OpenAI/Ollama) to intelligently select relevant pages for brochures
- 📄 **Content Extraction**: Extracts clean text content from web pages
- 📓 **Jupyter Notebook Support**: Interactive development environment for experimentation
- ⚡ **Modern Python Tooling**: Uses `uv` for fast dependency management and `pyproject.toml` for project configuration

## Prerequisites

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer and resolver

### Installing uv

If you don't have `uv` installed, you can install it using one of the following methods:

**macOS/Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Or using pip:**

```bash
pip install uv
```

## Project Setup

This project uses `uv` for dependency management and `pyproject.toml` for project configuration.

### About pyproject.toml

The `pyproject.toml` file is the modern standard for Python project configuration. It defines:

- Project metadata (name, version)
- Python version requirements
- Project dependencies
- Build system configuration

This project uses PEP 621 standard format with `uv` for dependency resolution and installation.

### Initial Setup Steps

1. **Clone the repository** (if applicable):

   ```bash
   git clone <repository-url>
   cd brochure-maker
   ```

2. **Create a virtual environment using uv**:

   ```bash
   uv venv
   ```

   This creates a `.venv` directory with an isolated Python environment.

3. **Activate the virtual environment**:

   **macOS/Linux:**

   ```bash
   source .venv/bin/activate
   ```

   **Windows:**

   ```powershell
   .venv\Scripts\activate
   ```

4. **Install project dependencies**:

   ```bash
   uv pip install -e .
   ```

   The `-e` flag installs the project in "editable" mode, meaning changes to your source code are immediately reflected without reinstalling.

   Alternatively, you can sync from the lock file:

   ```bash
   uv sync
   ```

### Environment Variables

Create a `.env` file in the project root with your API keys:

```env
OPENAI_API_KEY=your_openai_api_key_here
OLLAMA_BASE_URL=http://localhost:11434  # If using local Ollama instance
```

**Note:** The `.env` file is already included in `.gitignore` to keep your secrets safe.

## Project Structure

```
brochure-maker/
├── app.ipynb              # Main Jupyter notebook for interactive development
├── scraper.py             # Web scraping utilities
├── test.py                # Test file
├── pyproject.toml         # Project configuration and dependencies
├── uv.lock                # Lock file for reproducible builds
├── requirements.txt       # Alternative dependency list (for compatibility)
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Usage

### Running the Jupyter Notebook

1. **Start Jupyter Lab or Jupyter Notebook**:

   ```bash
   jupyter lab
   # or
   jupyter notebook
   ```

2. **Open `app.ipynb`** and start experimenting!

### Using the Scraper Module

The `scraper.py` module provides two main functions:

- `fetch_website_links(url)`: Returns all links found on a webpage
- `fetch_website_contents(url)`: Returns the title and text content of a webpage (truncated to 2,000 characters)

Example usage:

```python
from scraper import fetch_website_links, fetch_website_contents

# Get all links from a website
links = fetch_website_links("http://example.com")

# Get website content
title, content = fetch_website_contents("http://example.com")
```

### Running Python Scripts

You can run Python scripts directly:

```bash
python test.py
python scraper.py
```

## Dependency Management with uv

### Adding New Dependencies

To add a new dependency to the project:

1. **Add it to `pyproject.toml`** under `[project.dependencies]`:

   ```toml
   dependencies = [
       "existing-package>=1.0.0",
       "new-package>=2.0.0",  # Add your new package here
   ]
   ```

2. **Install and update the lock file**:
   ```bash
   uv pip install -e .
   uv lock
   ```

### Updating Dependencies

To update all dependencies:

```bash
uv lock --upgrade
uv pip install -e .
```

### Removing Dependencies

1. Remove the package from `pyproject.toml`
2. Run `uv lock` to update the lock file
3. Reinstall: `uv pip install -e .`

## About uv.lock

The `uv.lock` file is automatically generated and contains:

- Exact versions of all dependencies and their sub-dependencies
- Platform-specific dependencies
- Hash verification for security

**Important:** Commit `uv.lock` to version control to ensure all developers use the same dependency versions, providing reproducible builds.

## Development

### Virtual Environment Management

**Activate:**

```bash
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

**Deactivate:**

```bash
deactivate
```

### Verifying Setup

Check that everything is set up correctly:

```bash
python --version  # Should show Python 3.11+
which python      # Should point to .venv/bin/python (macOS/Linux)
```

## Troubleshooting

### Python Version Issues

This project requires Python 3.11 or higher. If you encounter version errors:

1. Check your Python version: `python3 --version`
2. If needed, use a specific version: `uv venv --python 3.11`

### Dependency Installation Issues

If you encounter issues installing dependencies:

1. Make sure you're in the virtual environment
2. Update uv: `pip install --upgrade uv`
3. Clear the cache and reinstall:
   ```bash
   uv cache clean
   uv pip install -e . --refresh
   ```

### Environment Variables Not Loading

Ensure:

1. The `.env` file exists in the project root
2. `python-dotenv` is installed (it's in the dependencies)
3. You're calling `load_dotenv()` in your scripts

## Technologies Used

- **Python 3.11+**: Modern Python features
- **uv**: Fast Python package installer
- **BeautifulSoup4**: Web scraping and HTML parsing
- **OpenAI API**: AI-powered content selection
- **Ollama**: Local LLM support
- **Jupyter**: Interactive development environment
- **python-dotenv**: Environment variable management
- **LangChain**: AI/LLM integration framework

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]

## Support

[Add support information here]
