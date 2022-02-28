from collections import OrderedDict
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, LoginManager, UserMixin

db = SQLAlchemy()


class UserPool(db.Model):
    __tablename__ = 'user_pool'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    survey_rec_id = db.Column(db.String(150), nullable=False)

    def to_dict(self):
        return OrderedDict(
            id=self.id,
            created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            survey_rec_id=self.survey_rec_id
        )


class SurveyRecord(db.Model):
    __tablename__ = 'survey_record'
    id = db.Column(db.String(150), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    identifier_key = db.Column(db.String(500), nullable=False)
    data_consent = db.relationship('DataConsent', backref="survey_record", lazy=False)
    demographics = db.relationship('Demographics', backref="survey_record", lazy=False)
    ideologies = db.relationship('Ideologies', backref="survey_record", lazy=False)
    tool = db.relationship('ToolRating', backref="survey_record", lazy=False)
    quality_control = db.relationship('QualityControl', backref="survey_record", lazy=False)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                           identifier_key=self.identifier_key,
                           data_consent=[data_consent.to_dict() for data_consent in self.data_consent],
                           demographics=[demographic.to_dict() for demographic in self.demographics],
                           ideologies=[ideology.to_dict() for ideology in self.ideologies],
                           quality_control=[qc.to_dict() for qc in self.quality_control])


class DataConsent(db.Model):
    __tablename__ = 'data_consent'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    survey_record_id = db.Column(db.String(150), db.ForeignKey('survey_record.id'))
    consent = db.Column(db.Boolean, nullable=False)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                           survey_record_id=self.survey_record_id,
                           consent=self.consent)


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

class Debriefing(db.Model):
    __tablename__ = 'debriefing'
    id = db.Column(db.Integer, primary_key=True)
    survey_record_id = db.Column(db.String(150), db.ForeignKey('survey_record.id'))
    chart = db.Column(db.Integer, nullable=False)
    video = db.Column(db.Integer, nullable=False)
    annotation = db.Column(db.Integer, nullable=False)
    extended_annotation = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           survey_record_id=self.survey_record_id,
                           chart=self.chart,
                           video=self.video,
                           annotation=self.annotation,
                           extended_annotation=self.extended_annotation)

class ScientificResearch(db.Model):
    __tablename__ = 'scientific_research'
    id = db.Column(db.Integer, primary_key=True)
    survey_record_id = db.Column(db.String(150), db.ForeignKey('survey_record.id'))
    scientific_research = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           survey_record_id=self.survey_record_id,
                           scientific_research=self.scientific_research)

class ToolRating(db.Model):
    __tablename__ = 'tool'
    id = db.Column(db.Integer, primary_key=True)
    survey_record_id = db.Column(db.String(150), db.ForeignKey('survey_record.id'))
    group_id = db.Column(db.Integer, nullable=False)
    quiz_first = db.Column(db.Text, nullable=True)
    quiz_second = db.Column(db.Text, nullable=True)
    biased_article = db.Column(db.Integer, nullable=False)
    bias_detection = db.Column(db.Integer, nullable=False)
    bias_facts = db.Column(db.Integer, nullable=False)
    tool_article_ideology = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           survey_record_id=self.survey_record_id,
                           group_id=self.group_id,
                           quiz_first=self.quiz_first,
                           quiz_second=self.quiz_second,
                           biased_article=self.biased_article,
                           bias_detection=self.bias_detection,
                           bias_facts=self.bias_facts,
                           tool_article_ideology=self.tool_article_ideology)

class Ideologies(db.Model):
    __tablename__ = 'ideologies'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    survey_record_id = db.Column(db.String(150), db.ForeignKey('survey_record.id'))
    political_ideology = db.Column(db.Integer, nullable=True)
    followed_news_outlets = db.Column(db.Text, nullable=True)
    news_check_frequency = db.Column(db.Integer, nullable=True)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                           survey_record_id=self.survey_record_id,
                           political_ideology=self.political_ideology,
                           followed_news_outlets=self.followed_news_outlets,
                           news_check_frequency=self.news_check_frequency)


class QualityControl(db.Model):
    __tablename__ = 'quality_control'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    survey_record_id = db.Column(db.String(150), db.ForeignKey('survey_record.id'))
    passed = db.Column(db.Boolean, nullable=False)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                           survey_record_id=self.survey_record_id,
                           passed=self.passed)


class ToolGroups(db.Model):
    __tablename__ = 'tool_groups'
    id = db.Column(db.Integer, primary_key=True)
    max_quota = db.Column(db.Integer, nullable=False)
    remaining_quota = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           max_quota=self.max_quota,
                           remaining_quota=self.remaining_quota,
                           created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'))

class AnnotationGroups(db.Model):
    __tablename__ = 'annotation_groups'
    id = db.Column(db.Integer, primary_key=True)
    max_quota = db.Column(db.Integer, nullable=False)
    remaining_quota = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           max_quota=self.max_quota,
                           remaining_quota=self.remaining_quota,
                           created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'))

class TestQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    test_question = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           test_question=self.test_question,
                           created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'))

class Groups(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    survey_record_id = db.Column(db.String(150), db.ForeignKey('survey_record.id'))
    group = db.Column(db.Integer)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           group=self.group)

class AGroups(db.Model):
    __tablename__ = 'aGroups'
    id = db.Column(db.Integer, primary_key=True)
    survey_record_id = db.Column(db.String(150), db.ForeignKey('survey_record.id'))
    group = db.Column(db.Integer)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           group=self.group)

class FirstGroup(db.Model):
    __tablename__ = '1Group'
    id = db.Column(db.Integer, primary_key=True)
    survey_record_id = db.Column(db.String(150), db.ForeignKey('survey_record.id'))
    group = db.Column(db.Integer)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           group=self.group)

class SecondGroup(db.Model):
    __tablename__ = '2Group'
    id = db.Column(db.Integer, primary_key=True)
    survey_record_id = db.Column(db.String(150), db.ForeignKey('survey_record.id'))
    group = db.Column(db.Integer)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           group=self.group)

class ThirdGroup(db.Model):
    __tablename__ = '3Group'
    id = db.Column(db.Integer, primary_key=True)
    survey_record_id = db.Column(db.String(150), db.ForeignKey('survey_record.id'))
    group = db.Column(db.Integer)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           group=self.group)

class FourthGroup(db.Model):
    __tablename__ = '4Group'
    id = db.Column(db.Integer, primary_key=True)
    survey_record_id = db.Column(db.String(150), db.ForeignKey('survey_record.id'))
    group = db.Column(db.Integer)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           group=self.group)

class FifthGroup(db.Model):
    __tablename__ = '5Group'
    id = db.Column(db.Integer, primary_key=True)
    survey_record_id = db.Column(db.String(150), db.ForeignKey('survey_record.id'))
    group = db.Column(db.Integer)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           group=self.group)

class SixthGroup(db.Model):
    __tablename__ = '6Group'
    id = db.Column(db.Integer, primary_key=True)
    survey_record_id = db.Column(db.String(150), db.ForeignKey('survey_record.id'))
    group = db.Column(db.Integer)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           group=self.group)

class SeventhGroup(db.Model):
    __tablename__ = '7Group'
    id = db.Column(db.Integer, primary_key=True)
    survey_record_id = db.Column(db.String(150), db.ForeignKey('survey_record.id'))
    group = db.Column(db.Integer)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           group=self.group)

class EighthGroup(db.Model):
    __tablename__ = '8Group'
    id = db.Column(db.Integer, primary_key=True)
    survey_record_id = db.Column(db.String(150), db.ForeignKey('survey_record.id'))
    group = db.Column(db.Integer)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           group=self.group)

class NinthGroup(db.Model):
    __tablename__ = '9Group'
    id = db.Column(db.Integer, primary_key=True)
    survey_record_id = db.Column(db.String(150), db.ForeignKey('survey_record.id'))
    group = db.Column(db.Integer)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           group=self.group)

class TenthGroup(db.Model):
    __tablename__ = '10Group'
    id = db.Column(db.Integer, primary_key=True)
    survey_record_id = db.Column(db.String(150), db.ForeignKey('survey_record.id'))
    group = db.Column(db.Integer)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           group=self.group)

class TestSurveyGroups(db.Model):
    __tablename__ = 'test_survey_groups'
    id = db.Column(db.Integer, primary_key=True)
    max_quota = db.Column(db.Integer, nullable=False)
    remaining_quota = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           max_quota=self.max_quota,
                           remaining_quota=self.remaining_quota,
                           created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'))

class AnnotationSentences(db.Model):
    __tablename__ = 'annotation_sentences'
    id = db.Column(db.String(150), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    headline = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)
    tool = db.Column(db.Text, nullable=False)
    extra= db.Column(db.Text, nullable=True)
    quiz_id = db.Column(db.Text, nullable=False)
    group_id = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                           headline=self.headline,
                           text=self.text,
                           tool=self.tool,
                           extra=self.extra,
                           quiz_id=self.quiz_id,
                           group_id=self.group_id)

class Articles(db.Model):
    __tablename__ = 'annotation'
    id = db.Column(db.String(150), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    headline = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)
    political = db.Column(db.Text, nullable=False)
    quiz_id = db.Column(db.Text, nullable=False)
    group_id = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                           text=self.text,
                           headline=self.headline,
                           quiz_id=self.quiz_id,
                           political=self.political,
                           group_id=self.group_id)

class Annotations(db.Model):
    __tablename__ = 'survey_annotations'
    id = db.Column(db.String(150), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    survey_record_id = db.Column(db.String(150), db.ForeignKey('survey_record.id'))
    quiz_left_high = db.Column(db.Text, nullable=True)
    quiz_left_middle = db.Column(db.Text, nullable=True)
    quiz_left_low = db.Column(db.Text, nullable=True)
    quiz_right_high = db.Column(db.Text, nullable=True)
    quiz_right_middle = db.Column(db.Text, nullable=True)
    quiz_right_low = db.Column(db.Text, nullable=True)
    quiz_center_high = db.Column(db.Text, nullable=True)
    quiz_center_middle = db.Column(db.Text, nullable=True)
    quiz_center_low = db.Column(db.Text, nullable=True)
    annotation_biased_article = db.Column(db.Integer, nullable=False)
    annotation_bias_detection = db.Column(db.Integer, nullable=False)
    annotation_bias_facts = db.Column(db.Integer, nullable=False)
    annotation_tool_article_ideology = db.Column(db.Integer, nullable=False)
    words = db.Column(db.Text, nullable=False)
    political = db.Column(db.Text, nullable=False)
    group_id = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                           survey_record_id=self.survey_record_id,
                           quiz_left_high=self.quiz_left_high,
                           quiz_left_middle=self.quiz_left_middle,
                           quiz_left_low=self.quiz_left_low,
                           quiz_right_high=self.quiz_right_high,
                           quiz_right_middle=self.quiz_right_middle,
                           quiz_right_low=self.quiz_right_low,
                           quiz_center_high=self.quiz_center_high,
                           quiz_center_middle=self.quiz_center_middle,
                           quiz_center_low=self.quiz_center_low,
                           annotation_biased_article=self.annotation_biased_article,
                           annotation_bias_detection=self.annotation_bias_detection,
                           annotation_bias_facts=self.annotation_bias_facts,
                           annotation_tool_article_ideology=self.annotation_tool_article_ideology,
                           words=self.words,
                           political = self.political,
                           group_id=self.group_id)

class Survey(db.Model):
    __tablename__ = 'surveys'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    questions = db.relationship('Question', backref="survey", lazy=False)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           name=self.name,
                           created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                           questions=[question.to_dict() for question in self.questions])


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    name = db.Column(db.String(500), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    survey_id = db.Column(db.Integer, db.ForeignKey('surveys.id'))
    simple_choices = db.relationship('SimpleChoice', backref='question', lazy=False)
    range_slider_choices = db.relationship('RangeSliderChoice', backref='question', lazy=False)

    def to_dict(self):
        return OrderedDict(id=self.id,
                           text=self.text,
                           name=self.name,
                           type=self.type,
                           created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                           survey_id=self.survey_id,
                           simple_choices=[simple_choice.to_dict() for simple_choice in self.simple_choices],
                           range_slider_choices=[range_slider_choice.to_dict() for range_slider_choice in
                                                 self.range_slider_choices])


class SimpleChoice(db.Model):
    __tablename__ = 'simple_choices'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(250), nullable=False)
    selected = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))

    def to_dict(self):
        return OrderedDict(id=self.id,
                           text=self.text,
                           created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                           question_id=self.question_id)


class RangeSliderChoice(db.Model):
    __tablename__ = 'range_slider_choices'
    id = db.Column(db.Integer, primary_key=True)
    min_range = db.Column(db.Integer, nullable=False)
    max_range = db.Column(db.Integer, nullable=False)
    label_left_side = db.Column(db.String(100), nullable=False)
    label_right_side = db.Column(db.String(100), nullable=False)
    selected = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))

    def to_dict(self):
        return OrderedDict(id=self.id,
                           min_range=self.min_range,
                           max_range=self.max_range,
                           label_left_side=self.label_left_side,
                           label_right_side=self.label_right_side,
                           created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                           question_id=self.question_id)

