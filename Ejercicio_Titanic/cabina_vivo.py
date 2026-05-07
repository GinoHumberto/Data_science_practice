def cantidad_sobrevivientes(dataset):
    filtrado = dataset['deck'].notnull() == True
    con_cabina = dataset[filtrado]
    sobrevivio = (con_cabina['survived'] == 1).sum()
    no_sobrevivio = (con_cabina['survived'] == 0).sum()
    return sobrevivio, no_sobrevivio

