from rest_framework import serializers
from .models import *


class TaskOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskOption
        fields = ['text']

class TaskSerializer(serializers.ModelSerializer):
    options = TaskOptionsSerializer(many=True)
    class Meta:
        model = Task
        fields = ['test', 'text', 'options_count', 'correct_answer_num', 'options']
        #fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id',
                'name',
                'description',
                'subject',
                'tasks_count',]
        read_only_fields = ('tasks_count', 'id')

class CreateTestSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField( default=serializers.CurrentUserDefault() )
    class Meta:
        model = Test
        fields = '__all__'
        read_only_fields = ('id', 'tasks_count', 'owner')

class CreateTaskSerializer(serializers.ModelSerializer):
    options = TaskOptionsSerializer(many=True)

    class Meta:
        model = Task
        fields = ['test', 'text', 'options_count', 'options', 'correct_answer_num']

    def create(self, validated_data):

        print('\n*** DATA ***')
        print(validated_data)
        print('*** END DATA ***\n')

        options_data = validated_data.pop('options')

        print('\n*** DATA ***')
        print(validated_data)
        print('*** END DATA ***\n')

        task = Task.objects.create(**validated_data)

        print("\n*** OPT DATA ***")
        print(options_data)
        print("*** END OPT DATA ***\n")

        i = 1
        for option_data in options_data:
            TaskOption.objects.create(task=task, ordinal_num=i, **option_data)
            i+=1

        return task


"""
class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['test', 'text', 'options_count', 'options', 'correct_answer_num']
"""
