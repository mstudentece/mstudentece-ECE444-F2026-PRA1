from utils import utils

u = utils()

# Test reversed function
assert u.reversed(1234) == 4321
assert u.reversed(-567) == -765

try:
    u.reversed("1234")
    assert False, "Should fail on string"
except TypeError:
    pass

try:
    u.reversed(12.34)
    assert False, "Should fail on float"
except TypeError:
    pass

assert u.formatter(10) == ('0b1010', '0o12')

try:
    u.formatter("10")
    assert False, "Should fail on string"
except TypeError:
    pass

try:
    u.formatter(10.5)
    assert False, "Should fail on float"
except TypeError:
    pass

print("All tests passed!")