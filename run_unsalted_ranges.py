from unsalted_hash_crack import *

def main():
    
    total = 100000
    start = 0
    
    while start + 10 <= total:
        combinitions_in_range.delay(start, start+10)
        start = start + 10

if __name__ == "__main__":
    main()

