# 1. Use a modern, official Python image
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /usr/src/app

# 3. Copy requirements first (This leverages Docker caching)
COPY requirements.txt .

# 4. UPGRADE PIP (Crucial step to fix your error)
RUN pip install --upgrade pip

# 5. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of the application code
COPY . .

# 7. Command to run the app
CMD ["python", "app.py"]