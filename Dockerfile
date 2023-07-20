FROM nvidia/cuda:12.2.0-runtime-ubuntu22.04

# Install Python 3.11, pip, YOLO
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        python3.11 python3-pip \
        libgl1-mesa-glx \
        libglib2.0-0 \
    && pip3 install ultralytics \
    && pip3 install Flask \
    && apt-get clean \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the app code
COPY . ./

# Start the app
CMD ["python3", "app.py"]