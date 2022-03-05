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
    
![Seeder File](https://github.com/Media-Bias-Group/Teaching-Platform/blob/main/readme-assets/Seeder%20File.png)  
  
Run the file, exit the console, comment on the first two functions by adding a # and delete the # from the following two functions. After that run the code again and follow these steps until the each function was covered.

### 5. Last steps

The last step will be to navigate back to your web app and click on reload to start the teaching platform. Then you should be able to acces the survey on the link of your webapp.

## Modify the texts and questions in each section

Because the system lives from the different surveys that can be made with it, it is important to have a manual on how to change the questions and texts. Thus, this section will explain which changes can be made and where they will need to be made. Firstly the general structure of how questions work and what changes need to be applied will be described. Secondly, each section of the teaching platform will be shortly described.

### General question setup

All questions that are loaded in the teaching platform are stored in the seeder.py. The teaching platform can contain single-choice and multiple-choice questions, text fields, range sliders and attention checks (depends on the implementation of the section). The first thing that can be adjusted in this file is the number of groups for the tool and annotation section. This cann be changed in the NUM_OF_GROUPS_TOOL and NUM_OF_GROUPS_ANNOTATION variable which are currently set to ten for the tool and nine for the annotation group. To also enable the correct drawing of the groups the needed groups must have a database in the models.py where the id can be stored. The api.py must also be altered. The api call that posts to /article/ contains an if query that puts the records into the correct database. the *_get_available_groups_for_annotation* function also contains this query that needs to be adjusted if more ore less groups will be implemented. In line 437 of the api.py the number from length % must be altered to the number the annotation groups contain. Generally this means that for each group of the tool section a database like the FirstGroup database needs to be added to the models.py and the if queries of the api.py must be lenghtend or shortend according to the amount of available groups.  
  
![First Group](https://github.com/Media-Bias-Group/Teaching-Platform/blob/main/readme-assets/First.png)  
  
Lengthening can be achieved by simply copying the elif sections underneath the last elif part and adjusting the last else section that will be used if no query is correct.  
  
![Copy Section](https://github.com/Media-Bias-Group/Teaching-Platform/blob/main/readme-assets/Copy.png)  
  
Shortening can be achieved by deleting one of the elif parts and again adjusting the last query to get a default that will be triggered.  
 
![Delete Section](https://github.com/Media-Bias-Group/Teaching-Platform/blob/main/readme-assets/Delete.png)  
  
 Each section of the teaching platform is covered by a unique python function which contains the questions. The questions are always stored with the text, type and the internal name as well as the possible answers that can be given and are later stored in connected databases. To get these databases the models.py in the surveyapi folder contains the setup for the storage where each answer and internal name gets mapped for further use. In order to fill these databases the previously mentioned JavaScript file contains the code that filles the internal values with content and sends them to the api.py that works as the router and manages the dispatch to the databases. The internal values must also be added to the db_helper.py in order to extract the information correctly afterward. This setup will be explained with an example when analysing the sections.

### 1. Briefing

To change the contents of the briefing and therefore the first two panels of the teaching platform the JavaScript file is the way to go. Thus, navigate there, open the file and search for the term *e._v("Welcome")*. The code representated there resembles the text of the welcome page.  
  
![Welcome Page](https://github.com/Media-Bias-Group/Teaching-Platform/blob/main/readme-assets/Welcome.png)

The structure of the texts in this section looks similar to this `n("h2", { staticClass: "font-weight-black", staticStyle: { "margin-top": "20px" } }, [e._v("Welcome")]), e._v(" "), n("br"), e._v(" ")`. Therefore each part of the text is frammed in a n-Element. This n-Element stands for one section of text that in this example contains an h2 element. The h2-Element is styled with the help of the staticClass *"font-weight-black"* and the staticStyle of *"margin-top": "20px"*. The classes are CSS classes that are already defined by vuetify and can be used in combination of other elements like other headings (e.g. h1, h3 etc.) or textelements (e.g. p, span etc.). Then the actual content follows and with *n("br")* a line break is realized. On the hand, the way to go would be to alter already existing texts by searching them and overrides the contents (both on the welcome page and the short briefing over the use of data). On the other hand it is possible to simply copy these n-Elements and therefore add new and more elements that could contain text. When copying an element just make sure that you really use the whole element and at leat one *e._v(" ")* behind it and also don't add it anywhere in the code but where the other texts elements are already stored.

### 2. Demographics

The demographics section is the first section where the editing of questions will be described. Firstly the questions can be found in the seeder.py under the function *seed_personal_questions()*. Generally, one can again work with simply searching for the wording of the questions in this file to get the correct position. Every function for the questions of a section start with the following code:  
  
```
app = create_app()
ctx = app.app_context()
ctx.push()
db.init_app(app)
survey = Survey(name="demographic_questions")
questions = []
```  
  
This part of the function implements the connection to the database where the questions will be stored. All questions are stored in the questions array that will later be uploaded to the survey database that stores the questions whereas this specific section gets stored as entry called *demographic_questions*.
Following this initialisation is the setup for the question which starts with a simple choice questions about the gender of the user. Simple choice questions look like this:  
  
```
question_1 = Question(text='What gender do you identify with?', type='radio', name='gender')
question_1.simple_choices = [
    SimpleChoice(text='Female'),
    SimpleChoice(text='Male'),
    SimpleChoice(text='Other'),
    SimpleChoice(text='Prefer not to say')
]
questions.append(question_1)
```  
  
The first line of code initialisese the text of the question, its type and the internal value. As you can see in the code simple questions use the *radio* type. The text of the question can be changed without any problems while the internal value is important for the database that will store the answers and will be explained later on. Following the question an array with the SimpleChoice answers is implemented. Again the text of these answers can be alterd without any problems. The last section of the code appends the initialised question to the questions array.  
The next element of this section is the question about age which resembles a text input field. This type is implemented by the following code:  
  
```
question_2 = Question(text='What is your age?', type='text_field', name='age')
questions.append(question_2)
```  

This short code element is similar to the simple choice question element on the first line of code. Only the type of the question differs and possible answers don't have to be implemented.  
The other two questions don't need to analysed further because they again show how simple choice questions are implemented. The last part of each function comit the questions array to the database with the following needed code:  
  
```
survey.questions = questions
db.session.add(survey)
db.session.commit()
```  
  
If new questions need to be implemented or if the name given in the code changes further steps need to be made. Firstly, new questions can be simply added by coping already existing code snippets, alter the content and append the question to the *seed_personal_questions()* function. The positioning describes the order that the questions will appear so make sure to implement them on the correct place. Also numerate your questions and don't forget to append the question to the array. Secondly, the api.py, the models.py, the javascript file and the db_helper.py need to be altered in order to ensure correct storage and retrieval of the data. Navigate to the models.py and alter the  database of the section that was just altered with your questions. In case of the demographics section the database set up could look like:  
  
```
class Demographics(db.Model):
    __tablename__ = 'demographics'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    survey_record_id = db.Column(db.String(150), db.ForeignKey('survey_record.id'))
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    education = db.Column(db.Integer, nullable=False)
    native_english_speaker = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                           survey_record_id=self.survey_record_id,
                           age=self.age,
                           gender=self.gender,
                           education=self.education,
                           native_english_speaker=self.native_english_speaker)
```  
  
The name of the class and the tablename (in this case Demographics and demographics) can be chosen by you but as a best practice it is recommended to use the same word (one time capitalized). The next lines that contain the id and the survey_record_id should always stay the same and should always be added when setting up a database. The created_at element is currently not implemented in each database but can be added if needed. After the ids and the created_at element all questions that were implemented in the seeder.py for this section need to be added in separate columns. This means that the interal value will be combined with the information whethere the answer is a text or an integer. For the question about the age for example a db.Column is created that stores db.Integer and that can not be null. Because the age question is generally implemented as text input field the answers there could also contain a text which would then result in the following code:  
  
```
age = db.Column(db.Text, nuallble=False)
``` 
  
After all internal values are combined with the columns of the database the possible answers will also be stored in a dictonary to make retrieving the data more simple. In the *def to_dict(self):* function therefore the names of the questions need to be combined with the self value which looks like this:  

```
age = self.age
```  
  
After setting up the database in the models.py the api.py needs to be adjusted in order to safe the correct data. In case of the demographic questions the following api route has already been set up:  
  
```
@api.route('/survey_record/update_demographic_info/', methods=['POST'])
def update_demographic_info():
    data = request.json
    if request.method == 'POST':
        survey_record_id = data.get('body').get('survey_record_id')
        age = data.get('body').get('age')
        gender = data.get('body').get('gender')
        education = data.get('body').get('education')
        native_english_speaker = data.get('body').get('native_english_speaker')
        new_record = Demographics(
            survey_record_id=survey_record_id,
            age=age,
            gender=gender,
            education=education,
            native_english_speaker=native_english_speaker
        )
        print(new_record)
        db.session.add(new_record)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
        return jsonify(new_record.to_dict()), 201
```  
  
Again most of the aspects here will stay the same but the internal names of the questions again need to be added on several spots. Firstly, you will see that the age for example is again added two times. With *age = data.get('body').get('age')* the code gets the sent data from the json file sent from the frontend (that will be explained later). With *age=age* in the new_record section the value stored in the age component beforehand gets now associated with the column in the Demographics database (you can see here that the api.py uses the name of the class that was created in the models.py). If you added new questions then you would again need to add the name of the questions twice as described in this section.  
The next step would be to make sure that the frontend really sends the data correctly. To ensure this step navigate to the javascript file and firstly search for the name *update_demographic_info* which is the same as the function in the api.py. There you will find a code that looks like this:   
  
```
this.$store.dispatch("update_demographic_info", { survey_record_id: localStorage.media_bias_lexica_annotator_survey_record_id_key, age: this.responses.age, gender: this.responses.gender, education: this.responses.education, native_english_speaker: this.responses.native_english_speaker })
```
  
As you already will know by now the information about your questions also needs to be implemented inbetween the curly brackets in the same way the other questions are already implemented. Therefore age is for example added by programming *age: this.responses.age*. The code above does not only map the data that was retrieged from the frontend to certain names but also calls the *update_demographic_info* function that creates a json with the help of this data. To find the position of this function just search for *update_demographic_info* again until you find code that looks like this:  
  
```
update_demographic_info: function (e, t) { e.commit, e.state; return new ce.a(function (e, s) { h.a.post(ue + "/survey_record/update_demographic_info/", { body: { survey_record_id: t.survey_record_id, age: t.age, gender: t.gender, education: t.education, native_english_speaker: t.native_english_speaker }, headers: { "Content-Type": "application/json" } }).then(function (t) { return e(t) }).catch(function (e) { return s(e) }) }) },
```  
  
This function produces the json file that is needed to fill the database correctly. As you can see the body there again contains the name of the questions and your task will again be to add it the same way shown here *age: t.age*.  
After completing this three files the data will be stored correctly. To retrieve the data afterwards the db_helper.py also needs to be modified. To show how this works you will now firstly see the code that would extract all information given in the survey withouth the annotations:  

```
def to_csv_survey_worker_records(db, ctx, after_date='2000-10-10 00:00:00'):
    ctx.push()
    with open('detailed_user_record_mturk_{}.csv'.format(after_date), mode='w') as csv_file:
        fieldnames = ['id', 'prolific_id', 'created_at', 'age', 'gender', 'education', 'native_english_speaker', 'political_ideology', 'followed_news_outlets', 'news_check_frequency', 'group_id', 'quiz_first', 'quiz_second', 'biased_article', 'bias_facts', 'bias_detection', 'tool_article_ideology', 'scientific_research', 'chart', 'video', 'annotation', 'extended_annotation']
        t = PrettyTable(fieldnames)
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        # First, get all worker status
        sql_str = """
            SELECT identifier_key, survey_record_id, survey_record.created_at, COUNT(*) as count
            FROM survey_annotations
            INNER JOIN survey_record ON survey_record.id = survey_annotations.survey_record_id
            WHERE survey_record.created_at > '""" + after_date + """'
            GROUP BY survey_record_id
            ORDER BY survey_record.created_at;
            """
        sql = text(sql_str)
        for row in db.session.execute(sql):
            survey_record_id = dict(row)['survey_record_id']

            # Then, get the detailed records for each id
            sql_str_2 = """
                SELECT identifier_key, demographics.created_at, age, gender, education, political_ideology, native_english_speaker, followed_news_outlets, news_check_frequency, group_id, quiz_first, quiz_second, biased_article, bias_facts, bias_detection, tool_article_ideology, scientific_research, chart, video, annotation, extended_annotation, demographics.survey_record_id
                FROM demographics
                INNER JOIN ideologies on demographics.survey_record_id = ideologies.survey_record_id
                INNER JOIN survey_record on survey_record.id=ideologies.survey_record_id
                INNER JOIN tool on demographics.survey_record_id = tool.survey_record_id
                INNER JOIN scientific_research on demographics.survey_record_id = scientific_research.survey_record_id
                INNER JOIN debriefing on demographics.survey_record_id = debriefing.survey_record_id
                WHERE survey_record.id = '""" + survey_record_id + """'
                ;
                """
            sql_2 = text(sql_str_2)

            result_2 = db.session.execute(sql_2)
            for row_2 in result_2:
                record = dict(row_2)
                prolific_id = record['identifier_key']
                created_at = record['created_at']
                age = record['age']
                gender = SimpleChoice.query.get(record['gender']).to_dict()['text']
                education = SimpleChoice.query.get(record['education']).to_dict()['text']
                native_english_speaker = SimpleChoice.query.get(record['native_english_speaker']).to_dict()['text']
                group_id = record['group_id']
                quiz_first = SimpleChoice.query.get(record['quiz_first']).to_dict()['text']
                quiz_second = SimpleChoice.query.get(record['quiz_second']).to_dict()['text']
                biased_article = SimpleChoice.query.get(record['biased_article']).to_dict()['text']
                bias_facts = SimpleChoice.query.get(record['bias_facts']).to_dict()['text']
                bias_detection = SimpleChoice.query.get(record['bias_detection']).to_dict()['text']
                tool_article_ideology = record['tool_article_ideology']
                scientific_research = SimpleChoice.query.get(record['scientific_research']).to_dict()['text']
                chart = SimpleChoice.query.get(record['chart']).to_dict()['text']
                video = SimpleChoice.query.get(record['video']).to_dict()['text']
                annotation = SimpleChoice.query.get(record['annotation']).to_dict()['text']
                extended_annotation = SimpleChoice.query.get(record['extended_annotation']).to_dict()['text']
                political_ideology = record['political_ideology']
                followed_news_outlets = record['followed_news_outlets'].split(',')
                converted_news_outlets = []
                for outlet in followed_news_outlets:
                    if (outlet.isdigit()):
                        ot = SimpleChoice.query.get(outlet).to_dict()['text']
                        converted_news_outlets.append(ot)
                    else:
                        converted_news_outlets.append(outlet)
                news_check_frequency = SimpleChoice.query.get(record['news_check_frequency']).to_dict()['text']

                t.add_row([survey_record_id, prolific_id, created_at, age, gender, education, native_english_speaker, political_ideology, converted_news_outlets, news_check_frequency, group_id, quiz_first, quiz_second, biased_article, bias_facts, bias_detection, tool_article_ideology, scientific_research, chart, video, annotation, extended_annotation])

                writer.writerow({
                    'id': survey_record_id,
                    'prolific_id': prolific_id,
                    'created_at' : created_at,
                    'age': age,
                    'gender': gender,
                    'education': education,
                    'native_english_speaker': native_english_speaker,
                    'political_ideology': political_ideology,
                    'followed_news_outlets': converted_news_outlets,
                    'news_check_frequency': news_check_frequency,
                    'group_id': group_id,
                    'biased_article': biased_article,
                    'bias_facts': bias_facts,
                    'bias_detection': bias_detection,
                    'tool_article_ideology': tool_article_ideology,
                    'quiz_first': quiz_first,
                    'quiz_second': quiz_second,
                    'scientific_research': scientific_research,
                    'chart': chart,
                    'video': video,
                    'annotation': annotation,
                    'extended_annotation': extended_annotation
                })

        print('csv generated...')
        # print(t)
        ctx.pop()
```  
  
When reading through this code you will again see a lot of appearances of the name age. Therefore it will be the same task here to add your altered name or your new questions name into this section in the same way all other names have already been added. In this case there isn't only one appearance of the debriefing information because it will not only be extracted in this main function but also in the *to_csv_briefing* section where the altered names therefore also need to be added. Other elements don't need to be changed here.  
Summarizing, one can say that the general setup of the section is already implemented and that the four files only need to be altered if the name of a question changes or if a new questions is added. Altering in this case means looking for the appearance of already existing questions and functions and add the new questions name into the correct positions in the same way each other element is already implemented. This section did not only cover the simple choice questions, text input fields and altering of the different files but also works as a how to guide for each following section were questions can be added. The following sections will therefore only show different questions that can possibly be implemented as well as the name of the functions one needs to look for.

### 3. Political questions

Similar to the demographic questions the political questions can be found under the seed_ideology questions in the seeder.py. There a new type of question is implemented. The political orientation question uses a range slider that would be implemented by using the following code:  
  
```
    # 1
    question_1 = Question(
        text='Do you consider yourself to be liberal, conservative or somewhere in between?',
        type='range_slider',
        name='political_ideology'
    )
    question_1.range_slider_choices = [
        RangeSliderChoice(
            min_range=-10,
            max_range=10,
            label_left_side='Very liberal',
            label_right_side='Very conservative'
        )
    ]
    ideology_questions.append(question_1)
```  
  
The type is therefore called *range-slider* and the choices only contain the min and max range as well as the labels that should appear next to the slider. These element (not the name!) can be alter without the need to change anything in the other files.  
Another new element in this section is the possibility of multiple choice questions. The structure reminds of the simple choice questions because only the type, which is called *checkbox* is different here.  
  
```
# 3
question_3 = Question(text="Please select AT LEAST one news outlet that you follow or select 'I'dont follow any news outlets'.", type='checkbox', name='followed_news_outlets')
question_3.simple_choices = [
    SimpleChoice(text='Fox News'),
    SimpleChoice(text='New York Times'),
    SimpleChoice(text='CNN'),
    SimpleChoice(text='MSNBC'),
    SimpleChoice(text='Reuters'),
    SimpleChoice(text='Breitbart'),
    SimpleChoice(text='The Federalist'),
    SimpleChoice(text='Huffington Post'),
    SimpleChoice(text='New York Post'),
    SimpleChoice(text='Alternet'),
    SimpleChoice(text='USA Today'),
    SimpleChoice(text='ABC News'),
    SimpleChoice(text='CBS News'),
    SimpleChoice(text='Univision'),
    SimpleChoice(text='The Washington Post'),
    SimpleChoice(text='The Wall Street Journal'),
    SimpleChoice(text='The Guardian'),
    SimpleChoice(text='BuzzFeed'),
    SimpleChoice(text='Vice'),
    SimpleChoice(text='Time magazine'),
    SimpleChoice(text='Business Insider'),
    SimpleChoice(text="I don't follow any news outlets.")
]
ideology_questions.append(question_3)
```  
  
If you alter anything in this section the database in the models.py would be called *Ideologies*, the api route in the api.py and also the functions in the javascript file would be called *update_idology_info* and the db_helper.py extracts this information in the *to_csv_survey_worker_records* and in the *to_csv_briefing* function. 

### 4. Knowledge test section

The text of the knowledge test section is structured similar to the text of the briefing part. Therefore again search for the text in the javascript file and edit it as explained above. Attention with the letter that describes the section because in this case no n but a s is used as you can see here:  
  
```
s("h4", { staticClass: "text-justify font-weight-regular" }, [e._v("\n              You will now be shown ")
```  
  
The question for the knowledge test can be altered in the *seed_iqc_questions* section of the seeder.py. If you have altered the number of questions before this part it could be that you would also need to alter the *QUALITY_CONTROL_BIAS_SENTIMENT_CORRECT_OPTION_ID* in the api.py because this is the number of the question that then triggers the pop up if the question has been answered wrongly. The answer of this question will not be stored in a database. Hence, the models.py, the javascript file and the db_helper.py don't need to be altered.

### 5. Tool presentation section

With the *seed_tool_rating* function in the seeder.py the questions of the tool presentation section are implemented. While this follows the same procedure as editing every question section (also altering *ToolRating* in models.py, *update_tool_rating* in api.py and the javascript file and *to_csv_tool* and *to_csv_survey_worker_records* in db_helper.py) this section contains a new kind of questions called the quiz questions.  
  
```
question_1 = Question(
    text='The Austrian MEP Harald Vilimsky speaks out...',
    type='quiz_first',
    name='quiz_first'
)
question_1.simple_choices = [
    SimpleChoice(text='...against firearms.'),
    SimpleChoice(text='...in favor of firearms.')
]
questions.append(question_1)
```  
  
While these questions look like simple choice questions the type and the name are always the same and are always similar to the quiz_ids that are stored in the .csv file that stores the texts. The name and type should always look like this. If you therefore would like to add a third text, the type and the name in this section would be *quiz_third*.
This id would also be needed to be added to the *articles.csv*. In order to add texts combined with visualisations this file needs to be filled with headline, text, tool, extra, group_id and quiz_id. The tool can be video, html, image or none while depending on this choice the extra needs to be filled with a relative path or html code. The group_id is simply the group that should get this text and tool combination and the quiz_id must be the quiz that should be presented with the text.  
To get this text into the database the following code needs to be called:  

```
def seed_tool_articles():
    app = create_app()
    ctx = app.app_context()
    ctx.push()
    db.init_app(app)
    with open('articles.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            annotation_sentence = AnnotationSentences(
                id=uuid.uuid4().hex,
                headline=row['headline'],
                text=row['text'],
                tool=row['tool'],
                extra=row['extra'],
                group_id=int(row['group_id']),
                quiz_id=row['quiz_id']
            )
            db.session.add(annotation_sentence)
            db.session.commit()
    ctx.pop()
```
  
Similar to the questions before the elements here can also be altered in order to have more columns in the database and the .csv file. If anything is altered here, again the other files need to be adjusted (*article* in api.py, *survey_sentences* in models.py, *loadRandomSurveySentences* in the javascript file)

### 6. Annotation Task

The annotation task also works with a file called annotation.csv where the texts and group ids can be stored. The quiz_ids and the corresponding questions are similar to the tool section as well. One aspect that differes from all previous sections is the highlight type of question in the seeder.py that lists all highlighted annotations and only works in this section:  
  
```
question_10 = Question(text='The list of annotations that you highlighted in the text above:', type='highlight', name='sentence_bias_annotation')
questions.append(question_10)
```  
  
The text that gets shown before the actual annotation task can again be changed similar to the text in the knowledge test section. Any changes in the structure again need to be also changed in the .csv file and the other parts (*article* in api.py, *annotations* in models.py, *loadAnnotationArticle* in the javascript file)

### 7. Debriefing

The debriefing section again combines the changing of the questions in the seeder.py and all other files while this time two functions are used separately. The question about the usage of the data is stored in the *seed_scientific_research* function in the seeder.py while the questions about the rating of the other tools is implemented in the *seed_debriefing* part of the file. Therefore changes in both of these questions lead to changes that need be made in multiple functions in the models.py, the api.py, the javascript file and the db_helper.py (*scientific_research* and *debriefing* in api.py, *ScientificResearch* and *Debriefing* in models.py, *scientific_research* and *debriefing* in the javascript file and *to_csv_debriefing* and *to_csv_survey_worker_records* in db_helper.py). The text shown above the rating and in the last section where the id is shown can again be altered by looking for the text in the javascript file just like known from the knowledge test section.


## Extracting the survey output

To extract the data from the databases navigate to the consoles tab of pythonanywhere and open a bash console. With the command `cd api` you need to navigate to the api folder where you can then add the command `python3.8 -i db_helper.py` to open the db_helper file with python. Get the db by using `db, ctx = create_db_client()` and extract the content of all survey worker records and therefore the information about each section of the teaching platform without the annotations by `to_csv_survey_worker_records(db, ctx)`. The data of the annotations can be extracted by `to_csv_all_annotations(db, ctx)`.
It is also possible to extract only the information of certain sections of the survey with `to_csv_briefing(db, ctx)`, `to_csv_tool(db, ctx)` and `to_csv_debriefing(db, ctx)`. 

---

Feel free to come forward with any questions or extend/improve the tool. Just contact us.
