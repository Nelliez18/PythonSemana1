segundos_total = int(input())

horas = segundos_total // 3600
resto = segundos_total % 3600

minutos = resto // 60
segundos = resto % 60

print(f"{horas}h {minutos}m {segundos}s")
