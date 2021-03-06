from rest_framework import serializers
from quiz.models import(
     Answer,
     Question,
     DomainAnswer,
     DomainQuestion,
     )
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields='__all__'

class QuestionSerializer(serializers.ModelSerializer):
    Question=AnswerSerializer(
        read_only = True,many=True
    )
    class Meta:
        model=Question
        fields='__all__'
class DomainAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=DomainAnswer
        fields='__all__'

class DomainQuestionSerializer(serializers.ModelSerializer):
    Question_domain=DomainAnswerSerializer(
        read_only = True,many=True
    )
    class Meta:
        model=DomainQuestion
        fields='__all__'
