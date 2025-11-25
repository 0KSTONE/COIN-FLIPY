import random

def flip_coins(num_flips: int = 50):
    # Use getrandbits(1) for a fast, uniform random 0/1
    heads = 0
    tails = 0
    flips = []

    for _ in range(num_flips):
        bit = random.getrandbits(1)  # 0 or 1 with equal probability
        if bit == 1:
            heads += 1
            flips.append("H")
        else:
            tails += 1
            flips.append("T")

    # Totals
    total = heads + tails
    heads_pct = (heads / total) * 100
    tails_pct = (tails / total) * 100

    # Determine winner
    if heads > tails:
        winner = "Heads"
    elif tails > heads:
        winner = "Tails"
    else:
        winner = "Tie"

    # Print results
    print("Flips:", "".join(flips))
    print(f"Total flips: {total}")
    print(f"Heads: {heads} ({heads_pct:.2f}%)")
    print(f"Tails: {tails} ({tails_pct:.2f}%)")
    print("Winner:", winner)

if __name__ == "__main__":
    flip_coins(50)  # change this number if you want more/less flips
