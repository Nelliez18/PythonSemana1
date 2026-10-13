preco_original = float(input())
percentual_desconto = float(input())

desconto = preco_original * (percentual_desconto / 100)
preco_final = preco_original - desconto

print(f"Preço final: R$ {preco_final:.2f}")
