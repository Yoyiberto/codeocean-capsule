FROM registry.codeocean.com/codeocean/ubuntu:20.04.2

ARG DEBIAN_FRONTEND=noninteractive

# Set working directory (Code Ocean uses /code as the default)
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3 \
    python3-pip \
    python3-dev \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Create symbolic links for python commands
RUN ln -s /usr/bin/python3 /usr/bin/python || true
RUN ln -s /usr/bin/pip3 /usr/bin/pip || true

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Code Ocean automatically mounts /data and /results
# But we'll create them just in case for local testing
RUN mkdir -p /data /results

# Set permissions for the run script
COPY run /code/
RUN chmod +x /code/run

# Default command (Code Ocean will use the run script)
CMD ["/bin/bash"] 