# views.py
from django.shortcuts import render
from .forms import RiskDataForm
from .models import RiskData
from .Rating import calculate_risk_score
import datetime

def home(request):
    data = None
    rate = None

    if request.method == "POST":
        form = RiskDataForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['name']
            try:
                rate = calculate_risk_score(data)
                RiskData.objects.create(name=data, rate=rate)
            except Exception as e:
                print(f"Error calculating rate: {str(e)}")

    else:
        form = RiskDataForm()

    return render(request, 'home.html', {'form': form, 'data': data, 'rate': rate})



from .serializers import RiskDataSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_rate(request, company_name):
    try:
        # Call the calculate_risk function to get the rate
        rate = calculate_risk_score(company_name)
        
        # Save the company name, rate, and current date to the database
        risk_data = RiskData(name=company_name, rate=rate, date=datetime.now())
        risk_data.save()
        
        # Serialize the data and return it in the response
        serializer = RiskDataSerializer(risk_data)
        return Response(serializer.data)
    except RiskData.DoesNotExist:
        return Response({'error': 'Company not found'}, status=404)
    except Exception as e:
        return Response({'error': f'Error: {str(e)}'}, status=500)
