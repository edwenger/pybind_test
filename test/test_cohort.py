import emod

c = emod.Cohort(10)
assert c.count == 10

c.count += 10
assert c.count == 20

fraction = 0.5
n_draws = 100
results = [0] * (c.count + 1)

for _ in range(n_draws):
    number = c.drawFraction(fraction)
    results[number] += 1

print('binomial_distribution(%d, %0.2f):' % (c.count, fraction))
for number in range(c.count + 1):
    print('%d: %s' % (number, '*' * results[number]))

# TODO: add binomial comparison check
