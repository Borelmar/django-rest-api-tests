from rest_framework import serializers
from .models import *

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

class TaskOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskOption
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    options = TaskOptionSerializer(many=True)
    class Meta:
        model = Task
        fields = '__all__'

class GetTestDetailSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)
    class Meta:
        model = Test
        fields = ['id', 'subject', 'name', 'description', 'tasks_count', 'owner', 'tasks']

class TaskForUserSerializer(serializers.ModelSerializer):
    options = TaskOptionSerializer(many=True)
    class Meta:
        model = Task
        fields=['test', 'text', 'options_count', 'options']

class GetTestDetailForUserSerializer(serializers.ModelSerializer):
    tasks = TaskForUserSerializer(many=True)
    class Meta:
        model = Test
        fields = ['id', 'subject', 'name', 'description', 'tasks_count', 'owner', 'tasks']
        

class CreateTestSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField( default=serializers.CurrentUserDefault() )
    tasks = TaskSerializer(many=True)

    class Meta:
        model = Test
        fields = ['id', 'subject', 'name', 'description', 'tasks_count', 'owner', 'tasks']
        extra_kwargs = {
            'id': { 'read_only': True, 'required': False},
            'tasks_count': { 'read_only': True, 'required': False },
            'owner': { 'read_only': True, 'required': False},
            'tasks_count': { 'read_only': True, 'required': False}
        }

    def create(self, validated_data):
        tasks_data = validated_data.pop('tasks')
        tasks_count = len(tasks_data)
        test = Test.objects.create(tasks_count=tasks_count, **validated_data)
        for task_data in tasks_data:
            options_data = task_data.pop('options', [])
            opt_count = len(options_data)
            task = Task.objects.create(test=test, options_count=opt_count, **task_data)
            opt_num = 1
            for option_data in options_data:
                TaskOption.objects.create(task=task, ordinal_num=opt_num, **option_data)
                opt_num += 1
        return test

class UserResultSerializer(serializers.Serializer):
    #user = serializers.HiddenField( default=serializers.CurrentUserDefault() )
    #user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    #test = serializers.PrimaryKeyRelatedField(queryset=Test.objects.all())
    test_name = serializers.CharField(max_length=128)
    task_answers = serializers.DictField(child=serializers.CharField(), allow_null=True)#, source='task_answers')

    def create(self, validated_data):
        #user = validated_data['user']
        #test = validated_data['test']
        user = self.context['request'].user
        test = self.context['test']
        test_name = validated_data['test_name']
        task_answers = validated_data['task_answers']

        # Получение заданий для данного теста
        tasks = Task.objects.filter(test=test)

        # Проверка выполненности заданий и подсчет правильных и неправильных ответов
        correct_count = 0
        incorrect_count = 0

        print("*** ans ***")
        print(task_answers)
        print("*** end ans ***")

        for task in tasks:
            task_id = str(task.id)
            if task_id in task_answers:
                user_answer = task_answers[task_id]
                if int(user_answer) == task.correct_ordinal_num:
                    correct_count += 1
                else:
                    incorrect_count += 1

        # Создание записи UserResult
        user_result = UserTest.objects.create(
            user=user,
            test=test,
            test_name=test_name,
            correct_count=correct_count,
            incorrect_count=incorrect_count
        )

        return user_result

class UserResultInfoViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTest
        fields = '__all__'


class GetTestStatisticSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    test = serializers.PrimaryKeyRelatedField(read_only=True)
    test_name = serializers.CharField(read_only=True)
    correct_count = serializers.IntegerField(read_only=True)
    incorrect_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = UserTest
        fields = ['user', 'test', 'test_name', 'correct_count', 'incorrect_count']


"""
class UserTestSubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTest
        #fields = ['id', 'subject', 'name', 'description', 'tasks_count', 'owner', 'tasks']
        fields = ['test_id']

    def create(self, validated_data):
        test_data = validated_data.get('test_id')
        print(test_data)
        #options_data = task_data.pop('options', [])
        raise serializers.ValidationError('All tasks for this test have already been completed.')
"""

"""
class TestResultsSerializer(serializers.Serializer):
    test_name = serializers.CharField(max_length=128)
    answers = serializers.DictField()

    def validate_answers(self, value):
        test_name = self.initial_data.get('test_name')
        correct_count = 0
        incorrect_count = 0

        ddicct = {
        }

        for key, value in value.items():
            if key in ddicct and value == ddicct[key]:
                correct_count += 1
            else:
                incorrect_count += 1

        self.context['correct_count'] = correct_count
        self.context['incorrect_count'] = incorrect_count

        return value

    def create(self, validated_data):
        test_name = validated_data['test_name']
        correct_count = self.context['correct_count']
        incorrect_count = self.context['incorrect_count']

        test_result = TestResult.objects.create(
            test_name=test_name,
            correct_count=correct_count,
            incorrect_count=incorrect_count
        )

        return test_result
"""
