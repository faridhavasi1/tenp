def getPrefixSuffix(a, b, l):
	prefix = a[: l]
	lb = len(b)
	suffix = b[lb - l:]

	return (prefix + suffix)

a = 'ali'
b = 'lia'
l = 5
print(getPrefixSuffix(a, b, l))




