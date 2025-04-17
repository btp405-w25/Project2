# Use an official Nginx image
FROM nginx:alpine

# Set the working directory
WORKDIR /usr/share/nginx/html

# Copy the Vite build output
COPY dist/ /usr/share/nginx/html/

# Copy custom nginx config
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf

# Expose the web server port
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
