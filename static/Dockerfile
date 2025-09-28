# Build stage
FROM node:18 AS build
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json .     

# Install dependencies
RUN npm install --legacy-peer-deps

# Copy all React app files
COPY . .                 

# Build React app
RUN npm run build

# Production stage with Nginx
FROM nginx:alpine

# Copy React build
COPY --from=build /app/build /usr/share/nginx/html

# Copy custom Nginx config to enable API proxying
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
