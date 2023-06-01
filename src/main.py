from polynomials import Polynomial

p = Polynomial({
    0: 1,
    1: -3,
    2: 3
})

p.save_as_json("poly.json")