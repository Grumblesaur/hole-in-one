"""Accept a string of 1s and 0s and invert them."""

b=lambda s:''.join(['10'[c>'0']for c in s])
print b(raw_input())
