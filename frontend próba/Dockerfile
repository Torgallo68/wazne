# Użycie obrazu Node.js jako podstawy
FROM node:18

# Ustawienie katalogu roboczego
WORKDIR /app

# Kopiowanie plików package.json i package-lock.json
COPY package.json package-lock.json ./

# Instalacja zależności
RUN npm install

# Instalacja dodatkowych pakietów
RUN npm install react-scripts react-router-dom react-dom

# Kopiowanie całej aplikacji
COPY . .

# Budowanie aplikacji
RUN npm run build

# Eksponowanie portu dla serwera development
EXPOSE 3000

# Uruchamianie aplikacji
CMD ["npm", "start"]
