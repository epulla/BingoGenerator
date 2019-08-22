.PHONY: run_tabla run_interfaz

run_interfaz:
	python3 main.py

run_tabla:
	python3 tabla.py ${LETTER}
