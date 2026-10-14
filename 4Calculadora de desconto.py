preco_original = float(input()) # Define o preço original do produto
percentual_desconto = float(input()) # Define o desconto a ser dado no produto

desconto = preco_original * (percentual_desconto / 100) # Multiplica o preço original pela porcentagem em decimal
preco_final = preco_original - desconto # Subtrai pra achar o preço final do produto

print(f"Preço final: R$ {preco_final:.2f}") # Exibe o preço final com duas casas decimais
