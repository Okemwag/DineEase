FROM node:18-alpine

WORKDIR /usr/src/app

COPY package*.json ./

# Update npm
RUN npm install -g npm@10.2.0


RUN npm install

COPY . .

EXPOSE 3000

CMD npm run dev