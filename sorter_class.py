class Sorter:

    def __init__(self, ulist):
        """
        Set ulist to instance variable
        """
        self.ulist = ulist

    def swap(self, x, y):
        """
        Swap the values at index x and y inside self.ulist
        """
        self.ulist[x], self.ulist[y] = self.ulist[y], self.ulist[x]

    def bubble_sort(self):
        """
        Complete this function to return the sorted array
        using the bubble sort algorithm
        """
        n = len(self.ulist)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.ulist[j] > self.ulist[j+1]:
                    self.swap(j, j+1)
        return self.ulist

def main():
    ulist = [64, 34, 25, 12, 22, 11, 90]
    sorter = Sorter(ulist)
    sorted_list = sorter.bubble_sort()
    print("Sorted array is:", sorted_list)
if __name__ == "__main__":
    main()
    