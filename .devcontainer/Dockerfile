# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the primary working directory for the application code inside the container
WORKDIR /usr/src/app

# ----------------------------------------------------------------------
# SECTION 1: Install OS Dependencies and Tools (Highly Cachable Layer)
# ----------------------------------------------------------------------
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    build-essential \
    python3-venv && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry Globally
RUN pip install --upgrade pip && \
    pip install poetry

# Set the PATH environment variable so the 'poetry' command is recognized
ENV PATH="/root/.local/bin:$PATH"

# ----------------------------------------------------------------------
# SECTION 2: Install Python Dependencies (The Corrected Step)
# ----------------------------------------------------------------------
# 1. Copy essential files needed for dependency installation.
#    We use the confirmed path 'openbb_platform/' relative to the build context.
COPY openbb_platform/pyproject.toml openbb_platform/dev_install.py ./

# 2. Run the full installation and build. This command is now inside the Dockerfile,
#    so it will run once and be fully cached until pyproject.toml changes.
#    This step will execute the 'poetry install' logic that you mentioned.
RUN python dev_install.py && \
    openbb-build

# ----------------------------------------------------------------------
# SECTION 3: Final Application Code
# ----------------------------------------------------------------------
# Copy the rest of the application code last.
# This layer only runs when your source code (excluding dependencies) changes.
# Note: The source files must also be under 'openbb_platform' to be copied here
COPY . .

# Expose a default development port if your application uses one
EXPOSE 8000

# Environment variables
ENV PYTHONUNBUFFERED 1