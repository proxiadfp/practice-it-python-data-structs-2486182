from collections import deque

# Initialisation de la to-do list
todo_list = deque()

# Fonction pour ajouter une tâche classique
def ajouter_tache(tache):
    todo_list.append(tache)
    print(f"Tâche ajoutée : {tache}")

# Fonction pour ajouter une tâche avec prio
def ajouter_tacheprio(tache):
    todo_list.appendleft(tache)
    print(f"Tâche prio ajoutée : {tache}")    

# Fonction pour retirer la première tâche (prio)
def retirer_tacheprio():
    if todo_list:
        tache = todo_list.popleft()
        print(f"Tâche prio terminée : {tache}")
    else:
        print("La to-do list est vide !")

# Fonction pour retirer la derniere tâche (classique)
def retirer_tache():
    if todo_list:
        tache = todo_list.pop()
        print(f"Tâche classique terminée : {tache}")
    else:
        print("La to-do list est vide !")        

# Fonction pour afficher les tâches
def afficher_taches():
    if todo_list:
        print("\nTo-Do List :")
        for i, tache in enumerate(todo_list, 1):
            print(f"{i}. {tache}")
    else:
        print("\nLa to-do list est vide !")



def main():
#add code here
# Exemple d'utilisation
    ajouter_tache("Faire les courses")
    ajouter_tacheprio("Envoyer un e-mail important")
    ajouter_tache("Appeler le médecin")

    afficher_taches()

    retirer_tache()
    retirer_tacheprio()
    afficher_taches()
    return    


if __name__ == "__main__":
    main()