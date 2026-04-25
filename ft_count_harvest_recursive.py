def ft_count_harvest_recursive(n):
    if n <= 0:
        return
    ft_count_harvest_recursive(n - 1)
    print("Day: ", n)
days = int(input("Days until harvest: "))
ft_count_harvest_recursive(days )
print ("Harvest time!")