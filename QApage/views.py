from django.shortcuts import render, HttpResponse

import os

from django.shortcuts import render
from django.conf import settings

def QA(request):
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'example.txt')
    query = request.GET.get('query')
    if query:
        try:
            with open(file_path, 'r') as file:
                matching_lines = []
                for line in file:
                    if query.upper() in line.strip().upper():
                        matching_lines.append(line.strip())
                if matching_lines:
                    context = {
                        'result': matching_lines,
                        'query': query,
                    }
                    # Remove brackets and quotes from each line in the result list
                    context['result'] = [line.strip().strip("[]'") for line in context['result']]
                    return render(request, 'base.html', context)
                else:
                    return render(request, 'base.html', {'error': f'No results found for "{query}".'})
        except FileNotFoundError:
            return render(request, 'base.html', {'error': 'File not found.'})
    return render(request, 'base.html')