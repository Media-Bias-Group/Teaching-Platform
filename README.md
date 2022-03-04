# Teaching platform

The teaching platform is an extension of the text annotation survey system called TASSY. The system allows to combine surveys with a tool testing and annotation section in order to get information about the effictivness of visualising bias. Therefore this tool can be used to test different visual aids within news articles and afterward test the ability of the useres to detect the bias in blank texts.

## Demo

A demo can be looked up via https://mediabias.pythonanywhere.com/

## Setup the system

The system is optimized to run on the hosting service pythonanywhere.com. In the following the setup of the teaching platform on pythonanywhere will be explained.

### 1. Upload to pythonanywhere

The first step to setup the teaching platform on pythonanyhwere is to open the hosting system and navigate to the web tab. Click on "Add a new web app" and follow the setup guide. As python web framework you will need to choose flask and as python version use 3.8. The path where your flask project is stored should follow this structure: /home/youraccountname/api/flask_app.py.
After setting up the web app in your account navigate to the files tab and open your newly created api folder. Upload the whole system code that you can retrieve from the github project inside of this folder. Make sure to override the existing flask_app.py with the flask_app.py from the teaching platform and stick with the prefabricated folder system.

### 2. Install the requirements

To run the system certain requriements need to be installed. To do so open the consoles tab on pythonanyhwere and start a bash console. Navigate to your api folder using the command cd api and install all requirements by using the command pip3.8 install -r requirements.txt. After each requirements is installed you can close the bash console via the command exit;.

### 3. Setup and connect the database

Next, navigate to the databases tab. For the teaching platform you will need a MySQL database. Make sure that this kind of storage is highlighted with blue background. To initialize the database you need to add a password. This password will later be needed for the connection to your flask app. Therefore remember it carefully. After adding your password the page for your MySQL settings will appear. Navigate to create a database and add the name of the storage for example survey. The survey will then appear under the list of databases. Next step will be to connect the database to the teaching platform. For this step you will need to navigate back to your files, inside your api and then inside your surveyapi folder. There you need to open the confiq.py by clicking on it. Pythonanywhere will now show you the contents of this data where you need to change the username, password, hostname and databasename to your database settings. The username is the name of your pythonanywhereaccount, the password is the password you remebered from setting up the MySQL database, the hostname can be found in the MySQL settings under the informations for connecting and the databasename can be found in the your database section. These informations also need to be added to the db_helper.py stored in the api folder. Subsequently click through the folders dist, static and js until you find the app.375fa0041d42e39ea28f.js data. Open this JavaScript file and search for pythonanyhwere. There should be three appearances where you will now need to change the url to the url that is used by your webapp.

### 4. Run your code

After setting up everything the flask app and the seeder.py can be run for the first time. To do so navigate back to your flask_app.py, open the file and click on run in the upper right corner. This will start a console that can again be closed after it finished. Then navigate to the seeder.py file that is also stored in your api folder. Scroll down to the last function on line 615. The # comment out the actual code that needs to be run. Therefore first run the seeder.py with the first two function and comment out all other as you can see in the following picture:
![Seeder File] (readme-assets\Seeder File.png).
Run the file, exit the console, comment on the first two functions by adding a # and delete the # from the following two functions. After that run the code again and follow these steps until the each function was covered.

### 5. Last steps

The last step will be to navigate back to your web app and click on reload to start the teaching platform. Then you should be able to acces the survey on the link of your webapp.

## Change the texts and questions in each section

Because the system lives from the different surveys that can be made with it, it is important to have a manual on how to change the questions and texts. Thus, this section will explain which changes can be made and where they will need to be made. Firstly the general structure of how questions work and what changes need to be applied will be described. Secondly, each section of the teaching platform will be shortly described.

### General question setup

All questions that are loaded in the teaching platform are stored in the seeder.py. The teaching platform can contain single-choice and multiple-choice questions, text fields, range sliders and attention checks (depends on the implementation of the section). The first thing that can be adjusted in this file is the number of groups for the tool and annotation section. This cann be changed in the NUM_OF_GROUPS_TOOL and NUM_OF_GROUPS_ANNOTATION variable which are currently set to ten for the tool and nine for the annotation group. To also enable the correct drawing of the groups the needed groups must have a database in the models.py where the id can be stored. The api.py must also be altered. The api call that posts to /article/ contains an if query that puts the records into the correct database. the *_get_available_groups_for_annotation* function also contains this query that needs to be adjusted if more ore less groups will be implemented. In line 437 of the api.py the number from length % must be altered to the number the annotation groups contain. Generally this means that for each group of the tool section a database like the FirstGroup database needs to be added to the models.py and the if queries of the api.py must be lenghtend or shortend according to the amount of available groups. 
![First Group] (readme-assets\First.png).
Lengthening can be achieved by simply copying the elif sections underneath the last elif part and adjusting the last else section that will be used if no query is correct.
![Copy Section] (readme-assets\Copy.png).
Shortening can be achieved by deleting one of the elif parts and again adjusting the last query to get a default that will be triggered.
![Delete Section] (readme-assets\Delete.png).
 Each section of the teaching platform is covered by a unique python function which contains the questions. The questions are always stored with the text, type and the internal name as well as the possible answers that can be given and are later stored in connected databases. To get these databases the models.py in the surveyapi folder contains the setup for the storage where each answer and internal name gets mapped for further use. In order to fill these databases the previously mentioned JavaScript file contains the code that filles the internal values with content and sends them to the api.py that works as the router and manages the dispatch to the databases. The internal values must also be added to the db_helper.py in order to extract the information correctly afterward. This setup will be explained with an example when analysing the sections.

### 1. Briefing
### 2. Demographics
### 3. Political questions
### 4. Knowledge test section
### 5. Tool presentation section
### 6. Annotation Task
### 7. Debriefing

## Extracting the survey output

To extract the data from the databases navigate to the consoles tab of pythonanywhere and open a bash console. With the command `cd api` you need to navigate to the api folder where you can then add the command `python3.8 -i db_helper.py` to open the db_helper file with python. Get the db by using `db, ctx = create_db_client()` and extract the content of all survey worker records and therefore the information about each section of the teaching platform without the annotations by `to_csv_survey_worker_records(db, ctx)`. The data of the annotations can be extracted by `to_csv_all_annotations(db, ctx)`.
It is also possible to extract only the information of certain sections of the survey with `to_csv_briefing(db, ctx)`, `to_csv_tool(db, ctx)` and `to_csv_debriefing(db, ctx)`. 

---

Feel free to come forward with any questions or extend/improve the tool. Just contact us.
