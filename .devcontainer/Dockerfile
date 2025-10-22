# Use an official Python runtime as a parent image
# We choose 3.11-slim for a smaller image size
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install necessary packages for development tools (like git and build tools)
# 'python3-venv' is included which is crucial for creating virtual environments.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    build-essential \
    python3-venv && \
    rm -rf /var/lib/apt/lists/*

# --- New: Install Poetry Globally ---
# Upgrade pip to the latest version and then install Poetry
RUN pip install --upgrade pip && \
    pip install poetry

# Set the PATH environment variable so the 'poetry' command is recognized
# The global 'pip install' puts executables in this location for root user
ENV PATH="/root/.local/bin:$PATH"

# Set the working directory to the OpenBB platform subdirectory
# Setting the WORKDIR here ensures all subsequent shell commands start in the right place
WORKDIR /workspaces/OpenBBTerminal/openbb_platform
# --- End of new additions ---


# Expose a default development port if your app uses one
EXPOSE 8000


# Environment variables
ENV PYTHONUNBUFFERED 1