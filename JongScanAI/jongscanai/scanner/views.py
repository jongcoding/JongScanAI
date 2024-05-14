from django.shortcuts import render,redirect
from .forms import ScanForm
from .models import ScanResult
def scan_website(url):
    # 실제로는 OWASP ZAP 등의 도구를 사용하여 스캔을 수행하고 결과를 반환해야 합니다.
    return {
        'url': url,
        'risk': 'High',
        'description': 'Example vulnerability description',
        'solution': 'Example solution'
    }
def home(request):
    if request.method == 'POST':
        form = ScanForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            scan_result = scan_website(url)
            # ScanResult 모델에 스캔 결과 저장
            result = ScanResult.objects.create(
                url=scan_result['url'],
                risk=scan_result['risk'],
                description=scan_result['description'],
                solution=scan_result['solution']
            )
            return redirect('scan_results', result_id=result.id)
    else:
        form = ScanForm()
    return render(request, 'scanner/home.html', {'form': form})
def scan_results(request):
    results = ScanResult.objects.all()
    return render(request, 'scanner/results.html', {'results': results})
# Create your views here.
