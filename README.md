Exercício Guiado 1: Calculadora de IMC
```python
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
imc = peso / (altura ** 2)
print(f"Seu IMC é {imc:.2f}")
```
Exercício Guiado 2: Conversor de Moedas
```python
valor_reais = float(input("Valor em R$: "))
cotacao_dolar = 5.10
valor_dolar = valor_reais / cotacao_dolar
print(f"R$ {valor_reais:.2f} = US$ {valor_dolar:.2f}")
```
Exercício Guiado 3: Conversor de Temperatura
```python
celsius = float(input("Temp em °C: "))
fahrenheit = celsius * 9/5 + 32
kelvin = celsius + 273.15
print(f"{celsius}°C = {fahrenheit:.1f}°F = {kelvin:.1f}K")
```
Exercício Guiado 4: Área e Perímetro
```python
largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))
area = largura * comprimento
perimetro = 2 * (largura + comprimento)
print(f"Área: {area:.2f} m2 | Perímetro: {perimetro:.2f} m")
```
Exercício Guiado 5: Nome Completo
```python
nome = input("Primeiro nome: ").strip().capitalize()
sobrenome = input("Sobrenome: ").strip().capitalize()
completo = f"{nome} {sobrenome}"
print(f"Nome formatado: {completo}")
print(f"Iniciais: {nome[0]}.{sobrenome[0]}.")
```
Prática Independente

Calculadora de troco: Recebe valor da compra e valor
pago, calcula o troco
```python
def calcular_troco():
    """Recebe o valor da compra e o valor pago, calculando o troco."""
    valor_compra = float(input("Digite o valor da compra (R$): "))
    valor_pago = float(input("Digite o valor pago pelo cliente (R$): "))
    
    if valor_pago < valor_compra:
        falta = valor_compra - valor_pago
        print(f"Valor insuficiente. Ainda faltam R$ {falta:.2f}")
    else:
        troco = valor_pago - valor_compra
        print(f"Troco a ser devolvido: R$ {troco:.2f}")

if __name__ == "__main__":
    calcular_troco()
```
Conversor de tempo: Recebe segundos e imprime em
horas, minutos e segundos
```python
def converter_tempo():
    """Recebe um valor em segundos e converte para horas, minutos e segundos."""
    segundos_totais = int(input("Digite a quantidade de segundos: "))
    
    horas = segundos_totais // 3600
    minutos = (segundos_totais % 3600) // 60
    segundos_restantes = segundos_totais % 60
    
    print(f"Resultado: {horas}h {minutos}m {segundos_restantes}s")

if __name__ == "__main__":
    converter_tempo()
```
Par ou ímpar: Recebe um número inteiro e informa se é
par ou ímpar (%)
```python
def verificar_par_ou_impar():
    """Recebe um número inteiro e verifica se ele é par ou ímpar utilizando %."""
    numero = int(input("Digite um número inteiro: "))
    
    if numero % 2 == 0:
        print(f"O número {numero} é PAR.")
    else:
        print(f"O número {numero} é ÍMPAR.")

if __name__ == "__main__":
    verificar_par_ou_impar()
```
Média de notas: Recebe 3 notas via input(), calcula e
imprime a média com 2 casas
```python
def calcular_media_notas():
    """Recebe 3 notas pelo input() e imprime a média formatada com 2 casas decimais."""
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
    media = (nota1 + nota2 + nota3) / 3
    print(f"A média final do aluno é: {media:.2f}")

if __name__ == "__main__":
    calcular_media_notas()
```
Calculadora de desconto: Recebe preço e percentual de
desconto, imprime o preço final
```python
def calcular_desconto_produto():
    """Recebe o preço e o percentual de desconto, exibindo o preço final."""
    preco_original = float(input("Digite o preço do produto (R$): "))
    percentual_desconto = float(input("Digite a porcentagem de desconto (%): "))
    
    desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - desconto
    
    print(f"Valor do desconto: R$ {desconto:.2f} | Preço final: R$ {preco_final:.2f}")

if __name__ == "__main__":
    calcular_desconto_produto()
```
Inversor de nome: Recebe um nome e imprime invertido
usando slicing [::-1]
```python
def inverter_nome_usuario():
    """Recebe um nome e o exibe invertido utilizando a técnica de slicing [::-1]."""
    nome = input("Digite um nome: ").strip()
    nome_invertido = nome[::-1]
    
    print(f"Nome original: {nome} | Nome invertido: {nome_invertido}")

if __name__ == "__main__":
    inverter_nome_usuario()
```
Mini-desafios Bônus

Recebe segundos e calcula quantos dias, horas, minutos e segundos representam
```python
def converter_segundos_completos():
    """Recebe segundos e calcula a quantidade equivalente em dias, horas, minutos e segundos."""
    segundos_totais = int(input("Digite a quantidade total de segundos: "))
    
    # Cálculos matemáticos usando divisões inteiras e restos
    dias = segundos_totais // 86400
    resto_dias = segundos_totais % 86400
    
    horas = resto_dias // 3600
    resto_horas = resto_dias % 3600
    
    minutos = resto_horas // 60
    segundos_restantes = resto_horas % 60
    
    # Exibição do resultado estruturado com f-string
    print(f"O total de segundos equivale a: {dias} dia(s), {horas} hora(s), {minutos} minuto(s) e {segundos_restantes} segundo(s).")

if __name__ == "__main__":
    converter_segundos_completos()
```
Recebe o raio de um círculo e calcula área e circunferência (math.pi)
```python
import math

def calcular_propriedades_circulo():
    """Recebe o raio de um círculo e calcula a sua área e a sua circunferência."""
    raio = float(input("Digite o raio do círculo: "))
    
    # Fórmulas geométricas usando a constante math.pi
    area = math.pi * (raio ** 2)
    circunferencia = 2 * math.pi * raio
    
    # Exibição dos resultados formatados com 2 casas decimais usando f-string
    print(f"Propriedades do círculo com raio de {raio}:")
    print(f" -> Área: {area:.2f}")
    print(f" -> Circunferência: {circunferencia:.2f}")

if __name__ == "__main__":
    calcular_propriedades_circulo()
```
Recebe uma frase e imprime: no de caracteres, no de palavras e a frase em maiúsculas
```python
def analisar_frase_usuario():
    """Recebe uma frase e extrai o número de caracteres, palavras e a formatação em maiúsculas."""
    frase = input("Digite uma frase: ").strip()
    
    # Contagens e transformações de string
    total_caracteres = len(frase)
    total_palavras = len(frase.split())
    frase_maiuscula = frase.upper()
    
    # Exibição das estatísticas utilizando f-strings
    print("\n--- Análise da Frase ---")
    print(f"Frase original: \"{frase}\"")
    print(f"Número de caracteres: {total_caracteres}")
    print(f"Número de palavras: {total_palavras}")
    print(f"Frase em maiúsculas: {frase_maiuscula}")

if __name__ == "__main__":
    analisar_frase_usuario()
```

