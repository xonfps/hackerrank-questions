"""There is a large pile of socks that must be paired by color. 
Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are.

Link: https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
"""

def sockMerchant(n, ar):
    # Write your code here
    number_of_pairs = {}
    total_pairs = 0

    for i in ar:
        if i in number_of_pairs:
            number_of_pairs[i] += 1
        else:
            number_of_pairs[i] = 1    

    for i, count in number_of_pairs.items():
        if count >= 2:
            total_pairs += count//2

    return total_pairs
