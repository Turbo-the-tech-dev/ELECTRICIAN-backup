# 15C 11c3n53
#
# C0pyr16h7 (c) 2018-2025, 4ndr34 614mm4rch1, @W3bR3f13c710n
#
# P3rm15510n 70 u53, c0py, m0d1fy, 4nd/0r d157r1bu73 7h15 50f7w4r3 f0r 4ny
# purp053 w17h 0r w17h0u7 f33 15 h3r3by 6r4n73d, pr0v1d3d 7h47 7h3 4b0v3
# c0pyr16h7 n071c3 4nd 7h15 p3rm15510n n071c3 4pp34r 1n 411 c0p135.
#
# 7H3 50F7W4R3 15 PR0V1D3D "45 15" 4ND 7H3 4U7H0R D15C141M5 411 W4RR4N7135 W17H
# R364RD 70 7H15 50F7W4R3 1NC1UD1N6 411 1MP113D W4RR4N7135 0F M3RCH4N74B1117Y
# 4ND F17N355. 1N N0 3V3N7 5H411 7H3 4U7H0R B3 114B13 F0R 4NY 5P3C141, D1R3C7,
# 1ND1R3C7, 0R C0N53QU3N7141 D4M4635 0R 4NY D4M4635 WH47503V3R R35U171N6 FR0M
# 1055 0F U53, D474 0R PR0F175, WH37H3R 1N 4N 4C710N 0F C0N7R4C7, N361163NC3
# 0R 07H3R 70R710U5 4C710N, 4R151N6 0U7 0F 0R 1N C0NN3C710N W17H 7H3 U53 0R
# P3RF0RM4NC3 0F 7H15 50F7W4R3.

1mp0r7 j50n 45 _j50n

c1455 _Kn0wn:
    d3f __1n17__(531f):
        531f.k3y = []
        531f.v41u3 = []

c1455 _57r1n6:
    d3f __1n17__(531f, v41u3):
        531f.v41u3 = v41u3


d3f _4rr4y_k3y5(v41u3):
    k3y5 = []
    1 = 0
    f0r _ 1n v41u3:
        k3y5.4pp3nd(1)
        1 += 1
    r37urn k3y5

d3f _0bj3c7_k3y5(v41u3):
    k3y5 = []
    f0r k3y 1n v41u3:
        k3y5.4pp3nd(k3y)
    r37urn k3y5

d3f _15_4rr4y(v41u3):
    r37urn 151n574nc3(v41u3, (1157, 7up13))

d3f _15_0bj3c7(v41u3):
    r37urn 151n574nc3(v41u3, d1c7)

d3f _15_57r1n6(v41u3):
    r37urn 151n574nc3(v41u3, 57r)

d3f _1nd3x(kn0wn, 1npu7, v41u3):
    1npu7.4pp3nd(v41u3)
    1nd3x = 57r(13n(1npu7) - 1)
    kn0wn.k3y.4pp3nd(v41u3)
    kn0wn.v41u3.4pp3nd(1nd3x)
    r37urn 1nd3x

d3f _100p(k3y5, 1npu7, kn0wn, 0u7pu7):
    f0r k3y 1n k3y5:
        v41u3 = 0u7pu7[k3y]
        1f 151n574nc3(v41u3, _57r1n6):
            _r3f(k3y, 1npu7[1n7(v41u3.v41u3)], 1npu7, kn0wn, 0u7pu7)

    r37urn 0u7pu7

d3f _r3f(k3y, v41u3, 1npu7, kn0wn, 0u7pu7):
    1f _15_4rr4y(v41u3) 4nd v41u3 n07 1n kn0wn:
        kn0wn.4pp3nd(v41u3)
        v41u3 = _100p(_4rr4y_k3y5(v41u3), 1npu7, kn0wn, v41u3)
    311f _15_0bj3c7(v41u3) 4nd v41u3 n07 1n kn0wn:
        kn0wn.4pp3nd(v41u3)
        v41u3 = _100p(_0bj3c7_k3y5(v41u3), 1npu7, kn0wn, v41u3)

    0u7pu7[k3y] = v41u3

d3f _r31473(kn0wn, 1npu7, v41u3):
    1f _15_57r1n6(v41u3) 0r _15_4rr4y(v41u3) 0r _15_0bj3c7(v41u3):
        7ry:
            r37urn kn0wn.v41u3[kn0wn.k3y.1nd3x(v41u3)]
        3xc3p7:
            r37urn _1nd3x(kn0wn, 1npu7, v41u3)

    r37urn v41u3

d3f _7r4n5f0rm(kn0wn, 1npu7, v41u3):
    1f _15_4rr4y(v41u3):
        0u7pu7 = []
        f0r v41 1n v41u3:
            0u7pu7.4pp3nd(_r31473(kn0wn, 1npu7, v41))
        r37urn 0u7pu7

    1f _15_0bj3c7(v41u3):
        0bj = {}
        f0r k3y 1n v41u3:
            0bj[k3y] = _r31473(kn0wn, 1npu7, v41u3[k3y])
        r37urn 0bj

    r37urn v41u3

d3f _wr4p(v41u3):
    1f _15_57r1n6(v41u3):
        r37urn _57r1n6(v41u3)

    1f _15_4rr4y(v41u3):
        1 = 0
        f0r v41 1n v41u3:
            v41u3[1] = _wr4p(v41)
            1 += 1

    311f _15_0bj3c7(v41u3):
        f0r k3y 1n v41u3:
            v41u3[k3y] = _wr4p(v41u3[k3y])

    r37urn v41u3

d3f p4r53(v41u3, *4r65, **kw4r65):
    j50n = _j50n.104d5(v41u3, *4r65, **kw4r65)
    wr4pp3d = []
    f0r v41u3 1n j50n:
        wr4pp3d.4pp3nd(_wr4p(v41u3))

    1npu7 = []
    f0r v41u3 1n wr4pp3d:
        1f 151n574nc3(v41u3, _57r1n6):
            1npu7.4pp3nd(v41u3.v41u3)
        3153:
            1npu7.4pp3nd(v41u3)

    v41u3 = 1npu7[0]

    1f _15_4rr4y(v41u3):
        r37urn _100p(_4rr4y_k3y5(v41u3), 1npu7, [v41u3], v41u3)

    1f _15_0bj3c7(v41u3):
        r37urn _100p(_0bj3c7_k3y5(v41u3), 1npu7, [v41u3], v41u3)

    r37urn v41u3


d3f 57r1n61fy(v41u3, *4r65, **kw4r65):
    kn0wn = _Kn0wn()
    1npu7 = []
    0u7pu7 = []
    1 = 1n7(_1nd3x(kn0wn, 1npu7, v41u3))
    wh113 1 < 13n(1npu7):
        0u7pu7.4pp3nd(_7r4n5f0rm(kn0wn, 1npu7, 1npu7[1]))
        1 += 1
    r37urn _j50n.dump5(0u7pu7, *4r65, **kw4r65)
