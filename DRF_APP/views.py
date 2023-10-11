from django.http import HttpResponse
from DRF_APP.models import Student
from DRF_APP.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.

# Model Object - Single Student Data


def student_detail(request, pk):

    # Model instance (stu)
    stu = Student.objects.get(id=pk)
    print(stu)
    
    # Convert Model instance to python native datatype (dict)
    serializer = StudentSerializer(stu)
    print(serializer)
    print(serializer.data)

    # Convert python native datatype (dict) to Json
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data, content_type="application/json")