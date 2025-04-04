
lista = []


def aggiungi():

    valore = input("Inserisci l'elemento da aggiungere alla lista: ")

    lista.append(valore)
    print(f"{valore} è stato aggiunto alla lista.")


def visualizza():
        for i in range(len(lista)):
            print(f"{i + 1}. {lista[i]}")

def rimuovi():

    visualizza()

    try:
        indice = int(input("Inserisci il numero dell'elemento da rimuovere: ")) - 1
     
        if 0 <= indice < len(lista):
       
            elemento_rimosso = lista.pop(indice)
            print(f"{elemento_rimosso} è stato rimosso dalla lista.")
        else:
            print("Indice non valido!")
    except ValueError:
        print("Per favore, inserisci un numero valido.")


def conta_elementi():

    print(f"Ci sono {len(lista)} elementi nella lista.")

def svuota_lista():

    lista.clear()
    print("La lista è stata svuotata.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Aggiungi un elemento alla lista")
        print("2. Visualizza la lista")
        print("3. Rimuovi un elemento dalla lista")
        print("4. Conta gli elementi della lista")
        print("5. Svuota la lista")
        print("6. Esci")
        
        scelta = input("Scegli un'opzione (1-6): ")
  
        if scelta == '1':
            aggiungi()
        elif scelta == '2':
            visualizza()
        elif scelta == '3':
            rimuovi()
        elif scelta == '4':
            conta_elementi()
        elif scelta == '5':
            svuota_lista()
        elif scelta == '6':
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida, riprova.")

menu()
