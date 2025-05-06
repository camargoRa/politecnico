from decimal  import Decimal

def calcular_viaje():    
    val_cabaña_dia = Decimal('250000')
    val_transporte = Decimal('150000')
    
    cant_personas = int(input("Ingrese la cantidad de personas que asistiran: "))
    dias_asistidos = input("Ingrese los dias de asistencia a la cabaña: 1, 2 o 3:  ").strip()
    val_viveres = Decimal(input("Ingrese el total de la compra de los viveres: "))
    
    if dias_asistidos == "1":
        costo_cabaña = val_cabaña_dia

    elif dias_asistidos == "2":
        costo_cabaña = val_cabaña_dia * 2
        
    elif dias_asistidos == "3":
        costo_cabaña = val_cabaña_dia * 3
    
    else: 
        print("Erro: Dias de asistencias no validos")
        return

    total_transporte = val_transporte * 2
    total_pag = (cant_personas * costo_cabaña) + val_viveres + (cant_personas * total_transporte)
    total_por_persona = total_pag / cant_personas


    print("   Detalles de Cobro   ")
    print(f"Costo de la cabaña $({dias_asistidos} dias): ${costo_cabaña}".replace(',','.') )    
    print(f"Valor de víveres: ${val_viveres}")
    print(f"Transporte por persona (ida y vuelta): ${total_transporte}")
    print(f"Total personas: {cant_personas}")
    print(f"Total a pagar: ${total_pag}")
    print(f"Total por persona: ${total_por_persona}")
  
calcular_viaje()
