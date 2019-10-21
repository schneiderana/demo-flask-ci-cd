build:

# cible "prepare" qui fasse l'installation des dépendences du projet
prepare:
	pipenv install

# cible "test" qui teste la qualité du projet (et plante sinon)

test:
	pipenv run pylint *.py
