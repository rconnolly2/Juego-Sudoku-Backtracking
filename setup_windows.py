import subprocess

# Este script va a crear un entorno virtual, utilizarlo y instalar requirements.txt

# Creo entorno virtual de software
subprocess.run(["python", "-m", "venv", "venvSudokuSolver"])

# Activo el entorno virtual
subprocess.run(["venvSudokuSolver\Scripts\activate.bat"], shell=True)

# Instalo librerías de requirements.txt
subprocess.run(["pip", "install", "-r", "requirements.txt"])

# Desactivo el entorno virtual
subprocess.run(["venvSudokuSolver\Scripts\deactivate.bat"], shell=True)