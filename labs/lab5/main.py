def main():
    memory_access_time = int(input("Санах ойд хандах хугацаа (ns)\n"))
    cache_access_time = int(input("Cache -д хандах хугацаа (ns)\n"))
    cache_hit_rate = int(input("Хит хурд (%)\n"))

    return (cache_hit_rate * cache_access_time + (100 - cache_hit_rate) * memory_access_time) / 100


if __name__ == '__main__':
    result = main()
    print(f"Үр ашигтай хандах хугацаа: {result} ns")
