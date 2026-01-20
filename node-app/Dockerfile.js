From node:18-alpine
WORKDIR /app
COPY package.json .
RUN npm isntall
COPY . .
CMD ["node", "index.js"]