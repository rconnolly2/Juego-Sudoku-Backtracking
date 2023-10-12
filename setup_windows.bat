@echo off

:: Variable nombre entorno de software
set NOMBRE_VENV=venvSudokuSolver

:: Variable python puede ser tambien python3 por ejemplo
set VARIABLE_PYTHON=python

:: Create the virtual environment
%VARIABLE_PYTHON% -m venv %NOMBRE_VENV%

:: Activar entorno virtual
call %NOMBRE_VENV%\Scripts\activate.bat

:: Instalar requisitos => requirements.txt
pip install -r requirements.txt

:: Desactivar entorno virtual
call %NOMBRE_VENV%\Scripts\deactivate.bat