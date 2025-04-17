# Stage 1: Build the frontend using Node
FROM node:18-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Serve using a simple HTTP server (since you're using Vite)
FROM node:18-alpine

WORKDIR /app
COPY --from=builder /app/dist ./dist

# Install serve package
RUN npm install -g serve

EXPOSE 5173
CMD ["serve", "-s", "dist", "-l", "5173"]