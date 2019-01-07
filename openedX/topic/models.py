# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from mongoengine import *

# Create your models here.

# class TopicNode(Document):
#     name = StringField(required=True)
#     meta = {'collection': 'topics', 'strict': False}

# class CoverEdges(Document):
#     topic = ReferenceField('TopicNode')
#     covers = ReferenceField('TopicNode')
#     meta = {'collection': 'topic_edges', 'strict': False}


# class PrerequisiteEdges(Document):
#     topic = ReferenceField('TopicNode')
#     prerequisite = ReferenceField('TopicNode')
#     meta = {'collection': 'topic_edges', 'strict': False}



class Topic(Document):
    name = StringField(required=True)
    covered_by = ListField(ReferenceField('self'))
    prerequisites = ListField(ReferenceField('self'))
    meta = {'collection': 'topics', 'strict': False}



# db.topics.aggregate( [ { $graphLookup: { from: "topics", startWith: "$covered_by", connectFromField: "covered_by", connectToField: "_id", as: "topicHier" } } ] ).pretty()

 # db.topics.aggregate( [ { $graphLookup: { from: "topics", startWith:"$_id" , connectFromField: "_id", connectToField: "covered_by", depthField: "numConnections" ,   as: "topicHier" } } ] ).pretty()