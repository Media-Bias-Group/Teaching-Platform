"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

from flask import Blueprint, jsonify, request
import uuid
from sqlalchemy.sql.expression import func, select
from models import db, Debriefing, UserPool, Survey, SurveyRecord, AnnotationSentences, Annotations, Articles, ToolRating, Annotations, Demographics, Ideologies, DataConsent, QualityControl, ToolGroups, AnnotationGroups, Groups, FirstGroup, SecondGroup, ThirdGroup, FourthGroup, FifthGroup, SixthGroup, SeventhGroup, EighthGroup, NinthGroup, TenthGroup,AGroups, ScientificResearch
import random
import string
from sqlalchemy import text
import pandas as pd

# VERY IMPORTANT
QUALITY_CONTROL_BIAS_SENTIMENT_CORRECT_OPTION_ID = 45

MAX_QUOTA = 10
NUM_OF_GROUPS = 85
GROUP_SENTENCE_COUNT = 20

MAX_TEST_QUOTA = 15
NUM_OF_TEST_GROUPS = 3
TEST_GROUP_SENTENCE_COUNT = 10

QUALITY_CONTROL_BIAS_SENTIMENT_CORRECT_OPTION_ID = 46

api = Blueprint('api', __name__)



@api.route('/surveys/')
def surveys():
    surveys = Survey.query.all()
    return jsonify({
        'surveys': [s.to_dict() for s in surveys]
    })


@api.route('/surveys/<int:id>/')
def survey(id):
    survey = Survey.query.get(id)
    return jsonify({
        'survey': survey.to_dict()
    })


@api.route('/timeout/', methods=['POST'])
def remove_user_from_pool():
    data = request.json
    if request.method == 'POST':
        id = data.get('body').get('survey_record_id')
        record = UserPool.query.filter_by(survey_rec_id=id).first()
        if record is not None:
            db.session.delete(record)
            db.session.commit()
            return jsonify({
                'message': 'Your session has timed out. The survey has been closed now.'
            }), 201


@api.route('/survey_record/', methods=['GET', 'POST'])
def survey_record():
    data = request.json
    if request.method == 'GET':
        id = data.get('id', '')
        record = SurveyRecord.query.get(id)
        return jsonify({
            'survey_record': [s.to_dict() for s in record]
        })
    elif request.method == 'POST':
        print('------- START DEBUG ---------')
        print(data.get('body').get('identifier_key'), '')
        print('------- END DEBUG ------------')
        __id__ = uuid.uuid4().hex
        __key__ = data.get('body').get('identifier_key')
        user_p = UserPool(survey_rec_id=__id__)
        new_record = SurveyRecord(
            id=__id__,
            identifier_key=__key__
        )
        db.session.add(new_record)
        db.session.add(user_p)
        try:
            db.session.commit()
        except Exception as e:
            print('another exception')
            db.session.rollback()
            print('Renewing survey record...')
            user_p = UserPool(survey_rec_id=__id__)
            new_record = SurveyRecord(
                id=uuid.uuid4().hex,
                identifier_key=data.get('body').get('identifier_key')
            )
            db.session.add(new_record)
            db.session.add(user_p)
            db.session.commit()
        return jsonify(new_record.id), 201


@api.route('/survey_record/update_data_consent/', methods=['POST'])
def update_data_consent():
    data = request.json
    if request.method == 'POST':
        survey_record_id = data.get('body').get('survey_record_id')
        consent = data.get('body').get('data_consent')
        print('------- START DEBUG ---------')
        print(survey_record_id)
        print(consent)
        new_record = DataConsent(
            survey_record_id=survey_record_id,
            consent=consent
        )
        print(new_record.survey_record_id)
        print(new_record.consent)
        survey_record = SurveyRecord.query.get(survey_record_id)
        print(survey_record.id)
        db.session.add(new_record)
        try:
            db.session.commit()
        except Exception as e:
            print('some exception')
            print(e)
            db.session.rollback()
        print('------- END DEBUG ------------')
        return jsonify(new_record.to_dict()), 201


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

@api.route('/survey_record/debriefing/', methods=['POST'])
def debriefing():
    data = request.json
    if request.method == 'POST':
        survey_record_id = data.get('body').get('survey_record_id')
        chart = data.get('body').get('chart')
        video = data.get('body').get('video')
        annotation = data.get('body').get('annotation')
        extended_annotation = data.get('body').get('extended_annotation')
        new_record = Debriefing(
            survey_record_id=survey_record_id,
            chart=chart,
            video=video,
            annotation=annotation,
            extended_annotation=extended_annotation
        )
        print(new_record)
        db.session.add(new_record)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
        return jsonify(new_record.to_dict()), 201

@api.route('/survey_record/scientific_research/', methods=['POST'])
def scientific_research():
    data = request.json
    if request.method == 'POST':
        survey_record_id = data.get('body').get('survey_record_id')
        scientific_research = data.get('body').get('scientific_research')
        new_record = ScientificResearch(
            survey_record_id=survey_record_id,
            scientific_research=scientific_research
        )
        print(new_record)
        db.session.add(new_record)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
        return jsonify(new_record.to_dict()), 201

@api.route('/survey_record/update_tool_rating/', methods=['POST'])
def update_tool_rating():
    data = request.json
    if request.method == 'POST':
        print('------- START DEBUG ---------')
        print(data.get('body'))
        survey_record_id = data.get('body').get('survey_record_id')
        group_id=data.get('body').get('group_id')
        quiz_first=data.get('body').get('quiz_first')
        quiz_second=data.get('body').get('quiz_second')
        biased_article=data.get('body').get('biased_article')
        bias_detection=data.get('body').get('bias_detection')
        bias_facts=data.get('body').get('bias_facts')
        tool_article_ideology=data.get('body').get('tool_article_ideology')
        print(survey_record_id)
        new_record = ToolRating(
            survey_record_id=survey_record_id,
            group_id=group_id,
            quiz_first=quiz_first,
            quiz_second=quiz_second,
            biased_article=biased_article,
            bias_detection=bias_detection,
            bias_facts=bias_facts,
            tool_article_ideology=tool_article_ideology
        )
        print(new_record)
        db.session.add(new_record)
        print('------- END DEBUG ------------')
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
        return jsonify(new_record.to_dict()), 201

@api.route('/survey_record/quality_control/', methods=['POST'])
def quality_control():
    data = request.json
    if request.method == 'POST':
        survey_record_id = data.get('body').get('survey_record_id')
        user_choice = data.get('body').get('quality_check_choice')
        print('------- START DEBUG ---------')
        print(survey_record_id)
        print(user_choice)
        if user_choice == QUALITY_CONTROL_BIAS_SENTIMENT_CORRECT_OPTION_ID:
            # new_record = QualityControl(survey_record_id=id, passed=True)
            passed = True
        else:
            passed = False
        print('------- END DEBUG ------------')
        # db.session.commit()
        return jsonify({'passed': passed}), 200

@api.route('/survey_record/update_ideology_info/', methods=['POST'])
def update_ideology_info():
    data = request.json
    if request.method == 'POST':
        id = data.get('body').get('survey_record_id')
        ideology = data.get('body').get('political_ideology')
        news_check_frequency = data.get('body').get('news_check_frequency')
        followed_news_outlets = data.get('body').get('followed_news_outlets')
        print('------- START DEBUG ---------')
        print(data.get('body'))
        new_record = Ideologies(
            survey_record_id=id,
            political_ideology=ideology,
            followed_news_outlets=followed_news_outlets,
            news_check_frequency=news_check_frequency
        )
        db.session.add(new_record)
        print('------- END DEBUG ------------')
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
        return jsonify(new_record.to_dict()), 201

@api.route('/article/', methods=['POST'])
def article():
    data = request.json
    if request.method == 'POST':
        id = data.get('body').get('survey_record_id')
        print(id)
        query = db.engine.execute('SELECT aGroups.group FROM aGroups WHERE aGroups.survey_record_id=%s', [id])
        prev_group = query.fetchone()
        print("before I was in Group:")
        print(prev_group)
        # Get groups that satisfy the QUOTA and are available for annotation task
        available_groups = _get_available_groups_for_annotation(prev_group)
        # Select a random group from the available groups
        group_id = random.choice(available_groups)
        print("Group number {} randomly picked. Fetching sentences now...".format(group_id))
        if prev_group == (1,):
            new_record = FirstGroup(
                survey_record_id=id,
                group=group_id
            )
        elif prev_group == (2,):
            new_record = SecondGroup(
                survey_record_id=id,
                group=group_id
            )
        elif prev_group == (3,):
            new_record = ThirdGroup(
                survey_record_id=id,
                group=group_id
            )
        elif prev_group == (4,):
            new_record = FourthGroup(
                survey_record_id=id,
                group=group_id
            )
        elif prev_group == (5,):
            new_record = FifthGroup(
                survey_record_id=id,
                group=group_id
            )
        elif prev_group == (6,):
            new_record = SixthGroup(
                survey_record_id=id,
                group=group_id
            )
        elif prev_group == (7,):
            new_record = SeventhGroup(
                survey_record_id=id,
                group=group_id
            )
        elif prev_group == (8,):
            new_record = EighthGroup(
                survey_record_id=id,
                group=group_id
            )
        elif prev_group == (9,):
            new_record = NinthGroup(
                survey_record_id=id,
                group=group_id
            )
        else:
            new_record = TenthGroup(
                survey_record_id=id,
                group=group_id
            )
        db.session.add(new_record)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
        # Get the corresponding sentences
        article = Articles.query.filter_by(group_id=group_id)
        # record = AnnotationSentences.query.order_by(func.random()).limit(5)
        return jsonify({
            'article': [s.to_dict() for s in article]
        })

@api.route('/survey_sentences/', methods=['POST'])
def survey_sentences():
    data = request.json
    if request.method == 'POST':
        id = data.get('body').get('survey_record_id')
        print(id)
        # Get groups that satisfy the QUOTA and are available for annotation task
        available_groups = _get_available_groups_for_tool()
        # Select a random group from the available groups
        group_id = random.choice(available_groups)
        print("Group number {} randomly picked. Fetching sentences now...".format(group_id))
        new_groupRecord = Groups (
            survey_record_id=id,
            group=group_id
        )
        new_record = AGroups (
            survey_record_id=id,
            group=group_id
        )
        db.session.add(new_groupRecord)
        db.session.add(new_record)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
        # Get the corresponding sentences
        sentences = AnnotationSentences.query.filter_by(group_id=group_id)
        # record = AnnotationSentences.query.order_by(func.random()).limit(5)
        return jsonify({
            'survey_sentences': [s.to_dict() for s in sentences]
        })

def _get_available_groups_for_annotation(prev_group):
    # Get all groups
    all_groups = [row.id for row in AnnotationGroups.query.with_entities(AnnotationGroups.id).all()]
    if prev_group == (1,):
        sql_str = """
            SELECT 1Group.group
            FROM 1Group
            """
    elif prev_group == (2,):
        sql_str = """
            SELECT 2Group.group
            FROM 2Group
            """
    elif prev_group == (3,):
        sql_str = """
            SELECT 3Group.group
            FROM 3Group
            """
    elif prev_group == (4,):
        sql_str = """
            SELECT 4Group.group
            FROM 4Group
            """
    elif prev_group == (5,):
        sql_str = """
            SELECT 5Group.group
            FROM 5Group
            """
    elif prev_group == (6,):
        sql_str = """
            SELECT 6Group.group
            FROM 6Group
            """
    elif prev_group == (7,):
        sql_str = """
            SELECT 7Group.group
            FROM 7Group
            """
    elif prev_group == (8,):
        sql_str = """
            SELECT 8Group.group
            FROM 8Group
            """
    elif prev_group == (9,):
        sql_str = """
            SELECT 9Group.group
            FROM 9Group
            """
    else:
        sql_str = """
            SELECT 10Group.group
            FROM 10Group
            """
    sql = text(sql_str)
    all_used_groups = [dict(row) for row in db.session.execute(sql)]
    length = len(all_used_groups)
    modulo = length % 9
    range_amount = length - modulo

    if modulo == 0:
        all_groups_proxy = all_groups
        if prev_group == '(1,)':
            try:
                db.session.query(FirstGroup).delete()
                db.session.commit()
            except:
                db.session.rollback()
        elif prev_group == '(2,)':
            try:
                db.session.query(SecondGroup).delete()
                db.session.commit()
            except:
                db.session.rollback()
        elif prev_group == '(3,)':
            try:
                db.session.query(ThirdGroup).delete()
                db.session.commit()
            except:
                db.session.rollback()
        elif prev_group == '(4,)':
            try:
                db.session.query(FourthGroup).delete()
                db.session.commit()
            except:
                db.session.rollback()
        elif prev_group == '(5,)':
            try:
                db.session.query(FifthGroup).delete()
                db.session.commit()
            except:
                db.session.rollback()
        elif prev_group == '(6,)':
            try:
                db.session.query(SixthGroup).delete()
                db.session.commit()
            except:
                db.session.rollback()
        elif prev_group == '(7,)':
            try:
                db.session.query(SeventhGroup).delete()
                db.session.commit()
            except:
                db.session.rollback()
        elif prev_group == '(8,)':
            try:
                db.session.query(EighthGroup).delete()
                db.session.commit()
            except:
                db.session.rollback()
        elif prev_group == '(9,)':
            try:
                db.session.query(NinthGroup).delete()
                db.session.commit()
            except:
                db.session.rollback()
        else:
            try:
                db.session.query(TenthGroup).delete()
                db.session.commit()
            except:
                db.session.rollback()
    else:
        for x in range(range_amount):
            all_used_groups.pop(0)
        else:
            for x in all_used_groups:
                if x['group'] in all_groups:
                    all_groups.remove(x['group'])
            else:
                all_groups_proxy = all_groups
                print(all_groups)



    #for row in empty_annotations:
     #   if row['sentence_group_id'] not in empty_groups:
     #       key = row['sentence_group_id']
     #       if key is not None:
     #           empty_groups.update({key: 1})
     #   else:
     #       key = row['sentence_group_id']
     #       old_val = empty_groups[key]
     #       if key is not None:
     #           empty_groups.update({key: old_val + 1})

    # print(empty_groups)

    # Get the current annotations
    #sql = text('SELECT survey_record_id, sentence_group_id, COUNT(*) as count FROM survey_annotations GROUP BY survey_record_id')
    #result = [dict(row) for row in db.session.execute(sql)]

    # If nothing is annotated yet
    #if len(result) == 0:
    #    return all_groups

    # Filter the result and calculate annotated sentences' group frequency
    #grp_freq = {}
    #for row in result:
    #    if row['count'] >= GROUP_SENTENCE_COUNT:
    #        if row['sentence_group_id'] not in grp_freq:
    #            key = row['sentence_group_id']
    #            grp_freq.update({key: 1})
    #        else:
    #            key = row['sentence_group_id']
    #            old_val = grp_freq[key]
    #            grp_freq.update({key: old_val + 1})
    #    else:
    #        if row['sentence_group_id'] not in grp_freq:
    #            key = row['sentence_group_id']
    #            grp_freq.update({key: 0})
    #        else:
    #            continue

    # print(grp_freq)

    #for (key, value) in grp_freq.items():
    #    if key in empty_groups:
    #        grp_freq[key] = grp_freq[key] - empty_groups[key]

    # print(grp_freq)
    # dfs = pd.read_excel('./quotas14.08.xlsx', sheet_name=None)
    # dfs = dfs['Sheet1']
    # df_1 = dfs[(dfs['survey_record_id'] < MAX_QUOTA)]
    # df_2 = df_1['survey_record_id'].apply(recalc_quota)
    # updated_quotas_dict = df_2.to_dict()
    # print(updated_quotas_dict)

    #updated_quotas_dict = {1: 11, 2: 12, 3: 11, 10: 11, 11: 11, 13: 11, 18: 11, 21: 11, 28: 11, 29: 11, 31: 12, 35: 11, 37: 11, 39: 11, 44: 11, 50: 11, 51: 11, 53: 11, 64: 11, 67: 11, 69: 11, 70: 11, 76: 11, 77: 11, 78: 11, 79: 11, 84: 12}

    #all_groups_proxy = all_groups
    #for (key, value) in grp_freq.items():
    #    if value >= MAX_QUOTA:
    #        if int(key) in updated_quotas_dict:
    #            if value >= updated_quotas_dict[key]:
    #                all_groups_proxy.remove(int(key))
    #        else:
    #            all_groups_proxy.remove(int(key))

    print('Available groups for annotation => ')
    print(all_groups_proxy)

    #if len(all_groups_proxy) == 0:
    #    print('WARNING: GROUP QUOTAS FULL! RETURNING ALL GROUPS AS A FALLBACK.')
    #    return [1, 5, 10, 15, 20, 35, 50, 65, 85]

    return all_groups_proxy
    # elements_count = collections.Counter(all_annotations)

def _get_available_groups_for_tool():
    # Get all groups
    all_groups = [row.id for row in ToolGroups.query.with_entities(ToolGroups.id).all()]
    sql_str = """
        SELECT groups.group
        FROM groups
        """
    sql = text(sql_str)
    all_used_groups = [dict(row) for row in db.session.execute(sql)]
    length = len(all_used_groups)
    modulo = length % 10
    range_amount = length - modulo

    if modulo == 0:
        all_groups_proxy = all_groups
        try:
            db.session.query(Groups).delete()
            db.session.commit()
        except:
            db.session.rollback()
    else:
        for x in range(range_amount):
            all_used_groups.pop(0)
        else:
            for x in all_used_groups:
                if x['group'] in all_groups:
                    all_groups.remove(x['group'])
            else:
                all_groups_proxy = all_groups
                print(all_groups)



    #for row in empty_annotations:
     #   if row['sentence_group_id'] not in empty_groups:
     #       key = row['sentence_group_id']
     #       if key is not None:
     #           empty_groups.update({key: 1})
     #   else:
     #       key = row['sentence_group_id']
     #       old_val = empty_groups[key]
     #       if key is not None:
     #           empty_groups.update({key: old_val + 1})

    # print(empty_groups)

    # Get the current annotations
    #sql = text('SELECT survey_record_id, sentence_group_id, COUNT(*) as count FROM survey_annotations GROUP BY survey_record_id')
    #result = [dict(row) for row in db.session.execute(sql)]

    # If nothing is annotated yet
    #if len(result) == 0:
    #    return all_groups

    # Filter the result and calculate annotated sentences' group frequency
    #grp_freq = {}
    #for row in result:
    #    if row['count'] >= GROUP_SENTENCE_COUNT:
    #        if row['sentence_group_id'] not in grp_freq:
    #            key = row['sentence_group_id']
    #            grp_freq.update({key: 1})
    #        else:
    #            key = row['sentence_group_id']
    #            old_val = grp_freq[key]
    #            grp_freq.update({key: old_val + 1})
    #    else:
    #        if row['sentence_group_id'] not in grp_freq:
    #            key = row['sentence_group_id']
    #            grp_freq.update({key: 0})
    #        else:
    #            continue

    # print(grp_freq)

    #for (key, value) in grp_freq.items():
    #    if key in empty_groups:
    #        grp_freq[key] = grp_freq[key] - empty_groups[key]

    # print(grp_freq)
    # dfs = pd.read_excel('./quotas14.08.xlsx', sheet_name=None)
    # dfs = dfs['Sheet1']
    # df_1 = dfs[(dfs['survey_record_id'] < MAX_QUOTA)]
    # df_2 = df_1['survey_record_id'].apply(recalc_quota)
    # updated_quotas_dict = df_2.to_dict()
    # print(updated_quotas_dict)

    #updated_quotas_dict = {1: 11, 2: 12, 3: 11, 10: 11, 11: 11, 13: 11, 18: 11, 21: 11, 28: 11, 29: 11, 31: 12, 35: 11, 37: 11, 39: 11, 44: 11, 50: 11, 51: 11, 53: 11, 64: 11, 67: 11, 69: 11, 70: 11, 76: 11, 77: 11, 78: 11, 79: 11, 84: 12}

    #all_groups_proxy = all_groups
    #for (key, value) in grp_freq.items():
    #    if value >= MAX_QUOTA:
    #        if int(key) in updated_quotas_dict:
    #            if value >= updated_quotas_dict[key]:
    #                all_groups_proxy.remove(int(key))
    #        else:
    #            all_groups_proxy.remove(int(key))

    print('Available groups for annotation => ')
    print(all_groups_proxy)

    #if len(all_groups_proxy) == 0:
    #    print('WARNING: GROUP QUOTAS FULL! RETURNING ALL GROUPS AS A FALLBACK.')
    #    return [1, 5, 10, 15, 20, 35, 50, 65, 85]

    return all_groups_proxy
    # elements_count = collections.Counter(all_annotations)


def recalc_quota(curr_quota):
    return MAX_QUOTA + (MAX_QUOTA - curr_quota)



@api.route('/annotate_sentence/', methods=['POST'])
def annotate_sentence():
    data = request.json
    if request.method == 'POST':
        print('------- START DEBUG ---------')
        print(data.get("body"))
        new_annotation = Annotations(
            id=uuid.uuid4().hex,
            survey_record_id = data.get('body').get('survey_record_id'),
            words = data.get('body').get('words'),
            political = data.get('body').get('political'),
            group_id=data.get('body').get('group_id'),
            quiz_left_high=data.get('body').get('quiz_left_high'),
            quiz_left_middle=data.get('body').get('quiz_left_middle'),
            quiz_left_low=data.get('body').get('quiz_left_low'),
            quiz_right_high=data.get('body').get('quiz_right_high'),
            quiz_right_middle=data.get('body').get('quiz_right_middle'),
            quiz_right_low=data.get('body').get('quiz_right_low'),
            quiz_center_high=data.get('body').get('quiz_center_high'),
            quiz_center_middle=data.get('body').get('quiz_center_middle'),
            quiz_center_low=data.get('body').get('quiz_center_low'),
            annotation_biased_article=data.get('body').get('annotation_biased_article'),
            annotation_bias_detection=data.get('body').get('annotation_bias_detection'),
            annotation_bias_facts=data.get('body').get('annotation_bias_facts'),
            annotation_tool_article_ideology=data.get('body').get('annotation_tool_article_ideology')
        )
        print('------- END DEBUG ------------')
        db.session.add(new_annotation)
        try:
            db.session.commit()
            return jsonify({
                'annotated_sentence': new_annotation.to_dict()
            }), 201
        except Exception as e:
            db.session.rollback()
            print('rolling back.. annotate_sentence')
            new_annotation = Annotations(
                id = data.get('body').get('survey_record_id'),
                words = data.get('body').get('words'),
                political = data.get('body').get('political'),
                group_id = data.get('body').get('group_id'),
                quiz_left_high=data.get('body').get('quiz_left_high'),
                quiz_left_middle=data.get('body').get('quiz_left_middle'),
                quiz_left_low=data.get('body').get('quiz_left_low'),
                quiz_right_high=data.get('body').get('quiz_right_high'),
                quiz_right_middle=data.get('body').get('quiz_right_middle'),
                quiz_right_low=data.get('body').get('quiz_right_low'),
                quiz_center_high=data.get('body').get('quiz_center_high'),
                quiz_center_middle=data.get('body').get('quiz_center_middle'),
                quiz_center_low=data.get('body').get('quiz_center_low'),
                annotation_biased_article=data.get('body').get('annotation_biased_article'),
                annotation_bias_detection=data.get('body').get('annotation_bias_detection'),
                annotation_bias_facts=data.get('body').get('annotation_bias_facts'),
                annotation_tool_article_ideology=data.get('body').get('annotation_tool_article_ideology')
            )
            print('------- END DEBUG ------------')
            db.session.add(new_annotation)
            db.session.commit()
            return jsonify({
                'annotated_sentence': new_annotation.to_dict()
            }), 201