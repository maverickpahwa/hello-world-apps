# Use official Node.js image
FROM node:latest

# Set working directory
WORKDIR /app

# Copy package files and install dependencies
COPY package.json .
RUN npm install

# Copy the rest of the app
COPY . .

# Start the React app
CMD ["npm", "start"]
