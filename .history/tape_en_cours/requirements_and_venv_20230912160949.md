# on créé les requirements 
pip freeze > requirements.txt

# on désactive l'environnement actif
deactivate

# on le supprime 
rm -rf formation_python_avance

# on créé et on active un nouvel env
python -m venv deuxieme_env
source deuxieme_env/bin/activate

# on installe les dépendances dans cet environnement
cd pya_cv_septembre_2023
pip install -r requirements.txt