from django.shortcuts import render

# Données factices : une liste de dictionnaires Python (pas de base de données).
TASKS = [
    {
        "id": 1,
        "title": "Installer Django",
        "description": "Créer l'environnement virtuel et installer Django 5.2.",
        "completed": True,
    },
    {
        "id": 2,
        "title": "Créer l'application tasks",
        "description": "Utiliser startapp puis déclarer l'application dans INSTALLED_APPS.",
        "completed": True,
    },
    {
        "id": 3,
        "title": "Afficher la liste des tâches",
        "description": "Écrire la vue task_list et le template task_list.html.",
        "completed": False,
    },
]


def task_list(request):
    context = {"tasks": TASKS}
    return render(request, "tasks/task_list.html", context)
