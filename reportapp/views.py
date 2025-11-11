from django.shortcuts import render
from .forms import ReportForm


def analyze_reports(request):
    """Vue pour analyser les rapports soumis via un formulaire.
    Paramètres:
        request: Objet HttpRequest.
        Retourne: Objet HttpResponse avec le rendu du template et les résultats de l'analyse.
    """
    result = None
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            data = []
            # Priorité au fichier si uploadé
            if form.cleaned_data['file_input']:
                file = form.cleaned_data['file_input']
                if file.name.endswith('.txt'):  # Validation simple du format
                    data = file.read().decode('utf-8').strip().splitlines()
                else:
                    form.add_error('file_input', "Le fichier doit être un .txt")
            else:
                
                data = form.cleaned_data['text_input'].strip().splitlines()

            # Analyse des rapports 
            count = 0
            for line in data:
                if not line.strip():
                    continue
                try:
                    levels = list(map(int, line.split()))
                except ValueError:
                    continue  # Skip lignes invalides
                if len(levels) < 2:
                    continue
                diffs = [levels[i] - levels[i-1] for i in range(1, len(levels))]
                if all(1 <= abs(d) <= 3 for d in diffs):
                    if all(d > 0 for d in diffs) or all(d < 0 for d in diffs):
                        count += 1
            result = count
    else:
        form = ReportForm()

    return render(request, 'home.html', {'form': form, 'result': result})