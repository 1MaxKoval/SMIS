from .models import Staff, Student
from django.core.exceptions import ObjectDoesNotExist

def user_model_check(userName):
    #This function returns false if the username does not exist in the database and true if it does.
    try:
        Staff.objects.get(username=userName)
        return(True)
    except ObjectDoesNotExist:
        return(False)
    
def check_if_active(userName):
    userModel = Staff.objects.get(username=userName)
    if userModel.active == False:
        return False
    if userModel.active == True:
        return True
