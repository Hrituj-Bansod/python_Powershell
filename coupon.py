import random

#taking input to get that many numbers of coupouns.
n = int(input("Enter the Number : "))

class CouponCollector:
    @staticmethod
    def generate_random_number(n):
        return random.randint(1, n)

    @staticmethod
    def collect_coupons(n):
        distinct_coupons = set()
        random_numbers_generated = 0

        while len(distinct_coupons) < n:
            random_numbers_generated += 1
            coupon = CouponCollector.generate_random_number(n)
            distinct_coupons.add(coupon)

        return random_numbers_generated

random_numbers_generated = CouponCollector.collect_coupons(n)
print(f"Total random numbers generated to collect all distinct coupons: {random_numbers_generated}")