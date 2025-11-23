# 1. Use Node image
FROM node:18-alpine

# 2. Set working directory
WORKDIR /usr/src/app

# 3. Copy package files first (for caching)
COPY package*.json ./

# 4. Install dependencies
RUN npm install

# 5. Copy the REST of the application (including public/ and src/)
COPY . .

# 6. Expose port
EXPOSE 3000

# ADD THIS LINE - React needs to bind to 0.0.0.0 in Docker
ENV HOST=0.0.0.0

# 7. Start the app
# CI=true ensures it doesn't crash on warnings
ENV CI=true
CMD ["npm", "start"]