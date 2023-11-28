#!/usr/bin/python3

#!/usr/bin/env python3

for c in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format(c) if (ord('z') - c) % 2 == 0 else "{:c}".format(c - 32),
        end="")
