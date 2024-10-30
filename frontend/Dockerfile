FROM node:20-alpine

# Create app directory
WORKDIR /app

# Install app dependencies
COPY package.json /app
RUN npm install

# Bundle app source
COPY . /app

# Build app
RUN npm run build

# Expose port
EXPOSE 3000

# Start app
CMD ["npm", "run", "serve"]