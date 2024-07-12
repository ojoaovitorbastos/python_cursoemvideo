# Preço de algum produto com 5% de desconto
produto_original = float(input('Qual o preço do produto? '))

desconto = produto_original * 0.05

produto_com_desconto = produto_original - desconto

print('Se um produto vale {}R$ e está com 5% de desconto, ele vale {:.2f}R$'.format(produto_original, produto_com_desconto))
