
# Pawfect Playdates

Pawfect Playdates aims to help dog parents schedule playdates for their pets. Dog parents can create a profile for their dog and browse through other dog profiles. If they find a profile they like, they can add it to their favorites. Each dog profile will have the email information for the owner so that the owners can contact each other to schedule play dates.

### Features

* users can browse dogs and view details about them
* users can favorite dog profiles and view a list of their favorites
* users can unfavorite a dog to remove them from their favorites list
* users can add a profile for their own dog
* users can update and delete their dogs profile, but are unable to update/delete a dog profile that does not belong to them
* users can update their profile information

## Technologies Used

![html](https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white)
![Bulma](https://img.shields.io/badge/Bulma-00D1B2?style=for-the-badge&logo=Bulma&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Django Rest Framework](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)







## Running The Application

#### To deploy this project you will first need to set up the API. 

1. Open a terminal window.

2. Clone the server side repository and navigate to that directory in the terminal.
```bash
git clone git@github.com:rachel-kendricks/pawfect-playdates.git
cd pawfect-playdates-api
```
3. Open in Visual Studio Code by running:
```bash
code .
```
4. Install Dependencies: Inside the project directory, you need to install the project dependencies. Since this project uses pipenv, you'll need to have it installed. Run:
```
pipenv install
```
5. Activate Virtual Environment: Once the dependencies are installed, you need to activate the virtual environment created by pipenv. Run:
```
pipenv shell
```
6. Database Setup: If the Django app uses a database, you may need to set it up. Typically, this involves running migrations to create the database schema. You can do this by running:
```
./seed_database.sh
```
7. Start the debugger by holding down these keys: shift + alt + d



#### Now, you can clone the client side and start the app.

1. Open a new tab in the termainal (cmd t).

2. Clone the client side repository and navigate to that directory in the terminal.
```bash
git clone git@github.com:rachel-kendricks/pawfect-playdates-client.git
cd pawfect-playdates-client
```
3. Install Dependencies: Inside the project directory, you need to install the project dependencies. Run:
```bash
npm install
```
4. Open in Visual Studio Code by running:
```bash
code .
```
5. Start the Development Server: Once Visual Studio Code is open, you can start the development server. Open a new terminal within VS Code (Terminal > New Terminal) and run:
```bash
npm run dev
```
This command starts the Vite development server. Once it's running, you can access your app in the browser by command clicking on localhost url http://localhost:XXXX.



## Authors

- [@rachel-kendricks](https://github.com/rachel-kendricks)

