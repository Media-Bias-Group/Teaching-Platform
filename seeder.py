import csv
import uuid

# from flask.cli import with_appcontext
from surveyapi.models import db, Survey, Question, AnnotationSentences, Articles, SimpleChoice, RangeSliderChoice, ToolGroups, AnnotationGroups
from surveyapi.create_app import create_app

# VERY IMPORTANT
MAX_QUOTA = 100
REMAINING_QUOTA = 100
NUM_OF_GROUPS_TOOL = 10
NUM_OF_GROUPS_ANNOTATION= 9

def seed_personal_questions():
    app = create_app()
    ctx = app.app_context()
    ctx.push()
    db.init_app(app)
    survey = Survey(name="demographic_questions")
    questions = []

    # 1
    question_1 = Question(text='What gender do you identify with?', type='radio', name='gender')
    question_1.simple_choices = [
        SimpleChoice(text='Female'),
        SimpleChoice(text='Male'),
        SimpleChoice(text='Other'),
        SimpleChoice(text='Prefer not to say')
    ]
    questions.append(question_1)

    # 2
    question_2 = Question(text='What is your age?', type='text_field', name='age')
    questions.append(question_2)

    # 3
    question_3 = Question(text='What is the highest level of education you have completed?', type='radio', name='education')
    question_3.simple_choices = [
        SimpleChoice(text='8th grade'),
        SimpleChoice(text='Some high school'),
        SimpleChoice(text='High school graduate'),
        SimpleChoice(text='Vocational or technical school'),
        SimpleChoice(text='Some college'),
        SimpleChoice(text='Associate degree'),
        SimpleChoice(text='Bachelor’s degree'),
        SimpleChoice(text='Graduate work'),
        SimpleChoice(text='I prefer not to say')
    ]
    questions.append(question_3)

    # 4
    question_4 = Question(text='What is the level of your English proficiency?', type='radio', name='native_english_speaker')
    question_4.simple_choices = [
        SimpleChoice(text='Proficient'),
        SimpleChoice(text='Independent'),
        SimpleChoice(text='Basic'),
    ]
    questions.append(question_4)

    survey.questions = questions
    db.session.add(survey)
    db.session.commit()

def seed_ideology_questions():
    app = create_app()
    ctx = app.app_context()
    ctx.push()
    db.init_app(app)
    survey = Survey(name="ideology_questions")
    ideology_questions = []

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

    # 2
    question_2 = Question(
        text='How often on an average do you check the news?',
        type='radio',
        name='news_check_frequency'
    )
    question_2.simple_choices = [
        SimpleChoice(text='Never'),
        SimpleChoice(text='Very rarely'),
        SimpleChoice(text='Several times per month'),
        SimpleChoice(text='Several times per week'),
        SimpleChoice(text='Every day'),
        SimpleChoice(text='Several times per day')
    ]
    ideology_questions.append(question_2)


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

    survey.questions = ideology_questions
    db.session.add(survey)
    db.session.commit()

def seed_iqc_questions():
    app = create_app()
    ctx = app.app_context()
    ctx.push()

    db.init_app(app)
    survey = Survey(name="info_quality_control")
    questions = []

    # 1
    question_1 = Question(text='How is bias connected to sentiment?', type='radio', name='bias_sentiment')
    question_1.simple_choices = [
        SimpleChoice(text='Bias is the same as negative sentiment'),
        SimpleChoice(text='Bias can be both positive, negative or even not have particular sentiment'),
        SimpleChoice(text='Bias is the same as positive sentiment'),
        SimpleChoice(text='Bias is not connected to sentiment at all')
    ]
    questions.append(question_1)

    survey.questions = questions
    db.session.add(survey)
    db.session.commit()

def seed_tool_rating():
    app = create_app()
    ctx = app.app_context()
    ctx.push()
    db.init_app(app)

    survey = Survey(name="tool_rating_questions")
    questions = []

    # 1
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

    # 2
    question_2 = Question(
        text='This article speaks out...',
        type='quiz_second',
        name='quiz_second'
    )
    question_2.simple_choices = [
        SimpleChoice(text='...against the NRA.'),
        SimpleChoice(text='...in favor of NRA.')
    ]
    questions.append(question_2)

    # 3
    question_3 = Question(
        text='Please tell us what you think about following sentence: In my opinion, this article is biased.',
        type='radio',
        name='biased_article'
    )
    question_3.simple_choices = [
        SimpleChoice(text='Strongly disagree'),
        SimpleChoice(text='Disagree'),
        SimpleChoice(text='Somewhat disagree'),
        SimpleChoice(text='Somewhat agree'),
        SimpleChoice(text='Agree'),
        SimpleChoice(text='Stronlgy agree')
    ]
    questions.append(question_3)

    # 4
    question_4 = Question(
        text='This article is...',
        type='radio',
        name='bias_facts'
    )
    question_4.simple_choices = [
        SimpleChoice(text='Very factual'),
        SimpleChoice(text='Factual'),
        SimpleChoice(text='Somewhat factual'),
        SimpleChoice(text='Somewhat fictious'),
        SimpleChoice(text='Fictious'),
        SimpleChoice(text='Very fictious')
    ]
    questions.append(question_4)

    # 5
    question_5 = Question(
        text='How easy was it for you to detect potentially biased language in this article?',
        type='radio',
        name='bias_detection'
    )
    question_5.simple_choices = [
        SimpleChoice(text='Very easy'),
        SimpleChoice(text='Easy'),
        SimpleChoice(text='Somewhat easy'),
        SimpleChoice(text='Somewhat difficult'),
        SimpleChoice(text='Difficult'),
        SimpleChoice(text='Very difficult')
    ]
    questions.append(question_5)

    # 6
    question_6 = Question(
        text='Do you consider this article to be liberal, conservative or somewhere in between?',
        type='range_slider',
        name='tool_article_ideology'
    )
    question_6.range_slider_choices = [
        RangeSliderChoice(
            min_range=-10,
            max_range=10,
            label_left_side='Very liberal',
            label_right_side='Very conservative'
        )
    ]
    questions.append(question_6)

    survey.questions = questions
    db.session.add(survey)
    db.session.commit()

def seed_knowledge_test():
    app = create_app()
    ctx = app.app_context()
    ctx.push()
    db.init_app(app)

    survey = Survey(name="knowledge_test")
    questions = []

    # 1
    question_1 = Question(
        text='The article states that...',
        type='quiz_left_high',
        name='quiz_left_high'
    )
    question_1.simple_choices = [
        SimpleChoice(text="...the country already has an outsized problem with vigilante 'justice'."),
        SimpleChoice(text="...the country didn't have an outsized problem with vigilante 'justice' until now.")
    ]
    questions.append(question_1)

    # 2
    question_2 = Question(
        text='The article states that...',
        type='quiz_left_middle',
        name='quiz_left_middle'
    )
    question_2.simple_choices = [
        SimpleChoice(text='...Rittenhouse shot and killed Anthony Huber, who hit him several times with a skateboard.'),
        SimpleChoice(text='...Rittenhouse shot and killed Anthony Huber, who hit him several times with a hard object.')
    ]
    questions.append(question_2)

    # 3
    question_3 = Question(
        text='The article states that...',
        type='quiz_left_low',
        name='quiz_left_low'
    )
    question_3.simple_choices = [
        SimpleChoice(text='...Rittenhouse was patrolling the streets, staying out after curfew, with no apparent approval of some of the police officers on duty at the time.'),
        SimpleChoice(text='...Rittenhouse was patrolling the streets, staying out after curfew, with the apparent approval of some of the police officers on duty at the time.')
    ]
    questions.append(question_3)

    # 4
    question_4 = Question(
        text='The article states that...',
        type='quiz_right_high',
        name='quiz_right_high'
    )
    question_4.simple_choices = [
        SimpleChoice(text="...as the trial unfolded, legal experts began characterizing the prosecution's bid as an downhill climb."),
        SimpleChoice(text="...as the trial unfolded, legal experts began characterizing the prosecution's bid as an uphill climb.")
    ]
    questions.append(question_4)

    # 5
    question_5 = Question(
        text='The article states that...',
        type='quiz_right_middle',
        name='quiz_right_middle'
    )
    question_5.simple_choices = [
        SimpleChoice(text='...the shots also nearly hit Daily Caller journalist Richi McGinniss, who was covering the riots.'),
        SimpleChoice(text='...the shots also nearly hit Washington Post journalist Richi McGinnis who was covering the riots.')
    ]
    questions.append(question_5)

    # 6
    question_6 = Question(
        text='The article states that...',
        type='quiz_right_low',
        name='quiz_right_low'
    )
    question_6.simple_choices = [
        SimpleChoice(text="...Rittenhouse attorney Marc Richards says that he represents 'clients' not 'cause'"),
        SimpleChoice(text="...Rittenhouse attorney Marc Richards says that it is always hard to present 'clients' and not 'causes'")
    ]
    questions.append(question_6)

    # 7
    question_7 = Question(
        text='The article states that...',
        type='quiz_center_high',
        name='quiz_center_high'
    )
    question_7.simple_choices = [
        SimpleChoice(text='...the bloodshed in Kenosha took place during a summer of mostly-violent protests.'),
        SimpleChoice(text='...the bloodshed in Kenosha took place during a summer of sometimes-violent protests.')
    ]
    questions.append(question_7)

    # 8
    question_8 = Question(
        text='The article states that...',
        type='quiz_center_middle',
        name='quiz_center_middle'
    )
    question_8.simple_choices = [
        SimpleChoice(text='...with so much of that night in Kenosha caught on cellphone and surveillance video, many basic facts were in dispute.'),
        SimpleChoice(text='...with so much of that night in Kenosha caught on cellphone and surveillance video, few basic facts were in dispute.')
    ]
    questions.append(question_8)

    # 9
    question_9 = Question(
        text='The article states that...',
        type='quiz_center_low',
        name='quiz_center_low'
    )
    question_9.simple_choices = [
        SimpleChoice(text="...Huber’s parents told the Washington Post they’re 'heartbroken and angry'"),
        SimpleChoice(text="...Huber’s parents told the Washington Post they’re 'devastated and angry'")
    ]
    questions.append(question_9)

    # 10
    question_10 = Question(text='The list of annotations that you highlighted in the text above:', type='highlight', name='sentence_bias_annotation')
    questions.append(question_10)


    # 11
    question_11 = Question(
        text='Please tell us what you think about following sentence: In my opinion, this article is biased.',
        type='radio',
        name='annotation_biased_article'
    )
    question_11.simple_choices = [
        SimpleChoice(text='Strongly disagree'),
        SimpleChoice(text='Disagree'),
        SimpleChoice(text='Somewhat disagree'),
        SimpleChoice(text='Somewhat agree'),
        SimpleChoice(text='Agree'),
        SimpleChoice(text='Stronlgy agree')
    ]
    questions.append(question_11)

    # 12
    question_12 = Question(
        text='This article is...',
        type='radio',
        name='annotation_bias_facts'
    )
    question_12.simple_choices = [
        SimpleChoice(text='Very factual'),
        SimpleChoice(text='Factual'),
        SimpleChoice(text='Somewhat factual'),
        SimpleChoice(text='Somewhat fictious'),
        SimpleChoice(text='Fictious'),
        SimpleChoice(text='Very fictious')
    ]
    questions.append(question_12)

    # 13
    question_13 = Question(
        text='How easy was it for you to detect potentially biased language in this article?',
        type='radio',
        name='annotation_bias_detection'
    )
    question_13.simple_choices = [
        SimpleChoice(text='Very easy'),
        SimpleChoice(text='Easy'),
        SimpleChoice(text='Somewhat easy'),
        SimpleChoice(text='Somewhat difficult'),
        SimpleChoice(text='Difficult'),
        SimpleChoice(text='Very difficult')
    ]
    questions.append(question_13)

    # 14
    question_14 = Question(
        text='Do you consider this article to be liberal, conservative or somewhere in between?',
        type='range_slider',
        name='annotation_tool_article_ideology'
    )
    question_14.range_slider_choices = [
        RangeSliderChoice(
            min_range=-10,
            max_range=10,
            label_left_side='Very liberal',
            label_right_side='Very conservative'
        )
    ]
    questions.append(question_14)

    survey.questions = questions
    db.session.add(survey)
    db.session.commit()

def seed_scientific_research():
    app = create_app()
    ctx = app.app_context()
    ctx.push()

    db.init_app(app)
    survey = Survey(name="scientific_research")
    questions = []

    # 1
    question_1 = Question(text='Can we trust your data for scientific research?', type='radio', name='scientific_research')
    question_1.simple_choices = [
        SimpleChoice(text='Yes, you can trust my data for scientific research.'),
        SimpleChoice(text='No, you may not want to trust my data for scientifc research.')
    ]
    questions.append(question_1)

    survey.questions = questions
    db.session.add(survey)
    db.session.commit()

def seed_debriefing():
    app = create_app()
    ctx = app.app_context()
    ctx.push()

    db.init_app(app)
    survey = Survey(name="debriefing")
    questions = []

    # 1
    question_1 = Question(text='Please rate how much you liked option 1 (icon array)?', type='radio', name='chart')
    question_1.simple_choices = [
        SimpleChoice(text='✩✩✩✩✩'),
        SimpleChoice(text='✩✩✩✩'),
        SimpleChoice(text='✩✩✩'),
        SimpleChoice(text='✩✩'),
        SimpleChoice(text='✩')
    ]
    questions.append(question_1)

    # 2
    question_2 = Question(text='Please rate how much you liked option 2 (annotations with explanations)?', type='radio', name='extended_annotation')
    question_2.simple_choices = [
        SimpleChoice(text='✩✩✩✩✩'),
        SimpleChoice(text='✩✩✩✩'),
        SimpleChoice(text='✩✩✩'),
        SimpleChoice(text='✩✩'),
        SimpleChoice(text='✩')
    ]
    questions.append(question_2)

    # 3
    question_3 = Question(text='Please rate how much you liked option 3 (annotations)?', type='radio', name='annotation')
    question_3.simple_choices = [
        SimpleChoice(text='✩✩✩✩✩'),
        SimpleChoice(text='✩✩✩✩'),
        SimpleChoice(text='✩✩✩'),
        SimpleChoice(text='✩✩'),
        SimpleChoice(text='✩')
    ]
    questions.append(question_3)

    # 4
    question_4 = Question(text='Please rate how much you liked option 4 (explanation video)?', type='radio', name='video')
    question_4.simple_choices = [
        SimpleChoice(text='✩✩✩✩✩'),
        SimpleChoice(text='✩✩✩✩'),
        SimpleChoice(text='✩✩✩'),
        SimpleChoice(text='✩✩'),
        SimpleChoice(text='✩')
    ]
    questions.append(question_4)

    # 5
    question_5 = Question(text='', type='dict', name='dict')
    question_5.simple_choices = [
        SimpleChoice(text='No')
    ]
    questions.append(question_5)

    survey.questions = questions
    db.session.add(survey)
    db.session.commit()

def create_groups_for_tool():
    app = create_app()
    ctx = app.app_context()
    ctx.push()
    db.init_app(app)
    for i in range(1, NUM_OF_GROUPS_TOOL+1):
        group = ToolGroups(id=i, max_quota=MAX_QUOTA, remaining_quota=REMAINING_QUOTA)
        db.session.add(group)
        db.session.commit()
    ctx.pop()

def create_groups_for_annotation():
    app = create_app()
    ctx = app.app_context()
    ctx.push()
    db.init_app(app)
    for i in range(1, NUM_OF_GROUPS_ANNOTATION+1):
        group = AnnotationGroups(id=i, max_quota=MAX_QUOTA, remaining_quota=REMAINING_QUOTA)
        db.session.add(group)
        db.session.commit()
    ctx.pop()


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

def seed_annotation_articles():
    app = create_app()
    ctx = app.app_context()
    ctx.push()
    db.init_app(app)
    with open('annotation.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            annotation = Articles(
                id=uuid.uuid4().hex,
                headline=row['headline'],
                text=row['text'],
                political=row['political'],
                group_id=int(row['group_id']),
                quiz_id=row['quiz_id']
            )
            db.session.add(annotation)
            db.session.commit()
    ctx.pop()


if __name__ == '__main__':
    # seed_personal_questions()
    # seed_ideology_questions()
    # seed_iqc_questions()
    # seed_tool_rating()
    # seed_knowledge_test()
    # seed_scientific_research()
    # seed_debriefing()
    # create_groups_for_tool()
    # create_groups_for_annotation()
    # seed_tool_articles()
     seed_annotation_articles()
