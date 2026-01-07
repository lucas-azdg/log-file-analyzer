import csv

def read_log(file_path):
    """Lee el archivo de log y devuelve la lista de líneas"""
    with open(file_path, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file]
    return lines

def analyze_log(lines):
    """Cuenta INFO, WARNING, ERROR y genera ranking de errores"""
    info_count = 0
    warning_count = 0
    error_count = 0
    error_messages = {}

    for line in lines:
        if line.startswith("ERROR"):
            error_count += 1
            if line in error_messages:
                error_messages[line] += 1
            else:
                error_messages[line] = 1
        elif line.startswith("WARNING"):
            warning_count += 1
        elif line.startswith("INFO"):
            info_count += 1

    return info_count, warning_count, error_count, error_messages

def save_error_summary(error_messages, output_file):
    """Guarda ranking de errores en CSV"""
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Error", "Count"])
        for error, count in sorted(error_messages.items(), key=lambda x: x[1], reverse=True):
            writer.writerow([error, count])

# --- MAIN ---
log_file = "system.log"
lines = read_log(log_file)
info_count, warning_count, error_count, error_messages = analyze_log(lines)

print("INFO:", info_count)
print("WARNING:", warning_count)
print("ERROR:", error_count)
print("\nRanking de errores:")
for error, count in sorted(error_messages.items(), key=lambda x: x[1], reverse=True):
    print(f"{error} → {count} veces")

save_error_summary(error_messages, "errors_summary.csv")
print("\nResumen guardado en errors_summary.csv")


