# Use an official Python runtime as a parent image
# We choose 3.11-slim for a smaller image size
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install necessary packages for development tools (like git and build tools)
# We also include 'python3-venv' which is crucial for creating virtual environments.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    build-essential \
    python3-venv && \
    rm -rf /var/lib/apt/lists/*

# The project-specific dependencies (Poetry, openbb-build, etc.)
# are intentionally left out here, as they are handled by the 
# .devcontainer.json's postCreateCommand for flexibility.

# Expose a default development port if your app uses one
EXPOSE 8000

# Environment variables
ENV PYTHONUNBUFFERED 1
