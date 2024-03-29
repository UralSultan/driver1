from rest_framework import serializers
from .models import Test, Question, Answer


class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = [
            'title',
        ]


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:

        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]


class RandomQuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:

        model = Question
        fields = [
            'title', 'answer',
        ]


class QuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    test = TestSerializer(read_only=True)

    class Meta:

        model = Question
        fields = [
            'test', 'title', 'answer',
        ]
