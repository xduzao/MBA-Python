def calcular_media(lista):
  if len(lista) == 0:
    return 0
  else:
    soma = sum(lista)
    media = soma / len(lista)
    return media