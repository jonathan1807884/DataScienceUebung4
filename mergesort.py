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



my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
mergeSort(my_list)
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
