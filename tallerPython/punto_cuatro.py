from decimal import Decimal

def ingresos_mensuales():

    categorias = {
        'alimentación': Decimal('40.0'),
        'vivienda': Decimal('25.0'),
        'transporte': Decimal('15.0'),
        'entrenamiento': Decimal('10.0'),
        'ahorro': Decimal('10.0')  
    }
    
    total_porcentaje = sum(categorias.values())
    if total_porcentaje != 100:
        print(f"Error: Los porcentajes suman {total_porcentaje}% (deben sumar 100%)")
        return
    
    try:
        ingreso = Decimal(input("Ingresa tu ingreso mensual: $"))
        
        if ingreso <= 0:
            print("Error: El ingreso debe ser positivo")
            return

        print("Distribución exacta:")
        for categoria, porcentaje in categorias.items():
            monto = (ingreso * porcentaje) / 100
            print(f"  • {categoria.capitalize():<20} ({porcentaje}%): ${monto:,}")
        
        print(f"\nTotal ingresos: ${ingreso:,}")
        print(f"Total distribuido: ${sum((ingreso * p)/100 for p in categorias.values()):,}")
        print("✓ Porcentajes suman exactamente 100%")
    
    except ValueError:
        print("Error: Ingresa un valor numérico válido")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")

# Ejecutar
ingresos_mensuales()