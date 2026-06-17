#Imports am Anfang des Dokuments
import matplotlib.pyplot as plt

# def ASSIGNEMENT entfernt (Zuweisung jetzt in Hauptfunktion)


#Umbenennung von "list_to_sort_by_merge" zu "arr"
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        mergeSort(left)
        mergeSort(right)

        #Variblen i,j und k
        i = 0
        j = 0
        k = 0
        
        #Anpassen der Variablen und Namen des arrays, das sortiert werden soll
        while j < len(left) and k < len(right):
            if left[j] <= right[k]:
                #Zuweisung direkt im Code
                arr[i] = left[k]
                j += 1
            else:
                #Zuweisung direkt im Code
                arr[i] = right[k]
                k += 1
            i += 1

        while l < len(left):
            arr[i] = left[j]
            j += 1
            i += 1

        while k < len(right):
            arr[i] = right[k]
            k += 1
            i += 1



#Umbennenung von my_list zu data
data  = [54, 26, 93, 17, 77, 31, 44, 55, 20]

#Umbenennung in x_values für bessere Übersichtlichkeit
x_values = range(len(data))

#Plot erstellen in Größe für gute Lesbarkeit
plt.figure(figsize=(10,5))

#Plot 1 mit unsortierten Daten
plt.subplot(1,2,1)
plt.bar(x_values, data, color='blue', edgecolor = 'black')
plt.title("Unsortierte Daten", fontsize=14)
plt.xlabel("Index", fontsize=12)
plt.ylabel("Wert", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(x_values)

#Sortierung durchführen
merge_sort(data)

#Plot 2 mit sortierten Daten
plt.subplot(1, 2, 2)
plt.bar(x_values, data, color='red', edgecolor='black')
plt.title("Sortierte Daten mit Merge Sort", fontsize=14)
plt.xlabel("Index", fontsize=12)
plt.ylabel("Wert", fontsize=12)
plt.grid(axis = 'y', linestyle='--', alpha=0.7)
plt.xticks(x_values)

#Layout optimierter anzeigen lassen
plt.tight_layout()
plt.show()
