from rest_framework import serializers
from .models import Student

              # MODEL SERIALIZER

class StudentSerializer(serializers.ModelSerializer):
	         
	           # VALIDATOR

	# def start_with_r(value):
	# 	if value[0].lower() != 'r':
	# 		raise serializers.ValidationError('name start with r')
	# name = serializers.CharField(validators=[start_with_r])
	#name = serializers.CharField(read_only=True)
	class Meta:
		model = Student
		fields = '__all__'
		read_only_fields = ['name', 'roll']


                   # SERIALIZERS

# class StudentSerializer(serializers.Serializer):
# 	name = serializers.CharField(max_length=100, validators=[start_with_r])
# 	roll = serializers.IntegerField()
# 	city = serializers.CharField(max_length=100)


# # class StudentForm(forms.Form):
# # 	name = forms.CharField(max_length=100)
# # 	roll = forms.IntegerField()
# # 	city = forms.CharField(max_length=100)
# 	def create(self, validate_data):
# 		return Student.objects.create(**validate_data)


# 	def update(self, instance, validate_data):
# 		instance.name = validate_data.get('name', instance.name)
# 		instance.roll = validate_data.get('roll', instance.roll)
# 		instance.city = validate_data.get('city', instance.city)
# 		instance.save()
# 		return instance

# 		     # FIELD LEVEL VALIDATION

# 	def validate_roll(self, value):
# 		if value >= 200:
# 			raise serializers.ValidationError('seat full')
# 		return value

# # 		      # OBJECT LEVEL VALIDATION

# 	def validate(self, data):
# 		nm = data.get('name')
# 		ct = data.get('city')
# 		if nm.lower() == 'romin' and ct.lower() != 'ranchi':
# 			raise serializers.ValidationError('city must be ranchi')
# 		return data




