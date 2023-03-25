import sys
import os
import time

# Benutzerdefinierte Variablen
CUSTOM_VARIABLES = {}

# Benutzerdefinierte Befehle
CUSTOM_COMMANDS = {
    'waitMS': lambda args: time.sleep(int(args[0])/1000) if len(args) == 1 and args[0].isdigit() else None,
    'waitS': lambda args: time.sleep(int(args[0])) if len(args) == 1 and args[0].isdigit() else None,
    'var': lambda args: CUSTOM_VARIABLES.update({args[0]: args[1]}) if len(args) == 2 else None,
    'epy': lambda args: exec(args[0]) if len(args) == 1 else None,
}

# Hauptfunktion des Interpreters
def run_interpreter(filename):
    # Überprüfen, ob die Datei existiert
    if not os.path.isfile(filename):
        print(f"Datei {filename} existiert nicht.")
        return
    # Datei öffnen
    with open(filename, 'r') as f:
        # Befehle trennen, Kommentare entfernen und Semicolons hinzufügen
        commands = []
        for line in f:
            line = line.strip()
            if not line.startswith('^') and line:
                if ';' not in line:
                    print(f"Ungültiger Befehl '{line}' in Datei '{filename}'. Ein Semikolon ';' ist erforderlich.")
                    return
                commands.extend(line.split(';'))
    # Jeden Befehl ausführen
    for i, command in enumerate(commands):
        try:
            # OS-Befehl ausführen oder benutzerdefinierten Befehl ausführen
            if command.startswith("waitMS"):
                args = command.split()[1:]
                CUSTOM_COMMANDS['waitMS'](args)
            elif command.startswith("waitS"):
                args = command.split()[1:]
                CUSTOM_COMMANDS['waitS'](args)
            elif command.startswith("var"):
                args = command.split()[1:]
                CUSTOM_COMMANDS['var'](args)
            elif command.startswith("epy"):
                args = [command.split("epy ",1)[1]]
                CUSTOM_COMMANDS['epy'](args)
            else:
                # Variablen ersetzen, falls vorhanden
                for key, value in CUSTOM_VARIABLES.items():
                    command = command.replace(f"${key}", str(value))
                os.system(command.strip())
        except Exception as e:
            print(f"Fehler beim Ausführen des Befehls in Zeile {i+1} '{command}': {e}")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Bitte geben Sie den Namen der .bbatch-Datei als Argument an.")
        sys.exit()

    filename = sys.argv[1]

    # Hier rufst du die Funktion run_interpreter aus deinem vorherigen Skript auf:
    run_interpreter(filename)
