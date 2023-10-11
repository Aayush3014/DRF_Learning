from django.http import HttpResponse, JsonResponse
from DRF_APP.models import Student
from DRF_APP.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.

# Model Object - Single Student Data
# This is for model instance

def student_detail(request, pk):

    # Model instance (stu)
    stu = Student.objects.get(id=pk)
    print(stu)
    
    # Convert Model instance to python native datatype (dict)
    serializer = StudentSerializer(stu)
    # print(serializer)
    # print(serializer.data)

    # Convert python native datatype (dict) to Json
    json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    return HttpResponse(json_data, content_type="application/json")
    

    # This JsonResponse can be used instead of Line 23 and 25.
    # This will run on (safe=True) because it is a single object which is in dict format.

    # return JsonResponse(serializer.data)



# This is for Queryset : All Student Data

def student_list(request):

    # Model instance (stu)
    stu = Student.objects.all()
    print(stu)
    
    # Convert Model instance to python native datatype (dict)
    serializer = StudentSerializer(stu, many=True)
    print(serializer)
    print(serializer.data)

    # Convert python native datatype (dict) to Json
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data, content_type="application/json")



    # This JsonResponse can be used instead of Line 49 and 51.
    # This will not run on safe=True because it is a queryset which is in list format.

    # return JsonResponse(serializer.data)