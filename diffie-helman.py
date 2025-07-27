import random

# Public parameters (agreed upon openly)
# WARNING: Use a 2048+ bit prime in practice.
p = 23    # Prime modulus
g = 5     # Primitive root modulo p

def generate_private_key(p):
    """Generate a random private key in the range [2, p-2]."""
    return random.randint(2, p - 2)

def generate_public_key(private_key, g, p):
    """Compute public key: public = g^private_key mod p."""
    return pow(g, private_key, p)

def generate_shared_secret(public_key, private_key, p):
    """Compute shared secret: shared_secret = public_key^private_key mod p."""
    return pow(public_key, private_key, p)

# Alice's side
a_private = generate_private_key(p)  # Alice's private key
A_public = generate_public_key(a_private, g, p)  # Alice's public key

# Bob's side
b_private = generate_private_key(p)  # Bob's private key
B_public = generate_public_key(b_private, g, p)  # Bob's public key

# Exchange public keys (A_public and B_public) over the insecure channel

# Alice computes shared secret
alice_shared_secret = generate_shared_secret(B_public, a_private, p)

# Bob computes shared secret
bob_shared_secret = generate_shared_secret(A_public, b_private, p)

# Both should now have the same shared secret
print(f"Alice's shared secret: {alice_shared_secret}")
print(f"Bob's shared secret:   {bob_shared_secret}")
print(f"Secrets match: {alice_shared_secret == bob_shared_secret}")
