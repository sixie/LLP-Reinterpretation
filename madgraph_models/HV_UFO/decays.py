# This file was automatically created by FeynRules 2.3.2
# Mathematica version: 12.1.0 for Mac OS X x86 (64-bit) (March 14, 2020)
# Date: Fri 28 May 2021 15:01:09


from object_library import all_decays, Decay
import particles as P


Decay_S0 = Decay(name = 'Decay_S0',
                 particle = P.S0,
                 partial_widths = {(P.g,P.g):'(2*gSg**2*MS0**6)/(cmath.pi*Lambda**2*abs(MS0)**3)',
                                   (P.Vq,P.Vq__tilde__):'((2*gSQv**2*MS0**2 - 8*gSQv**2*MVq**2)*cmath.sqrt(MS0**4 - 4*MS0**2*MVq**2))/(16.*cmath.pi*abs(MS0)**3)'})

Decay_A0 = Decay(name = 'Decay_A0',
                 particle = P.A0,
                 partial_widths = {(P.g,P.g):'(2*gPg**2*MA0**6)/(cmath.pi*Lambda**2*abs(MA0)**3)',
                                   (P.Vq,P.Vq__tilde__):'(gPQv**2*MA0**2*cmath.sqrt(MA0**4 - 4*MA0**2*MVq**2))/(8.*cmath.pi*abs(MA0)**3)'})

Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.b,P.b__tilde__):'((-12*MB**2*yb**2 + 3*MH**2*yb**2)*cmath.sqrt(-4*MB**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.c,P.c__tilde__):'((-12*MC**2*yc**2 + 3*MH**2*yc**2)*cmath.sqrt(-4*MC**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.t,P.t__tilde__):'((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'((-11*ee**2*MC**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MC**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MC**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MC**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.b,P.b__tilde__):'((-7*ee**2*MB**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MB**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MB**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.u,P.d__tilde__):'(CKM1x1*ee**2*MW**4*complexconjugate(CKM1x1))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.u,P.s__tilde__):'(CKM1x2*ee**2*MW**4*complexconjugate(CKM1x2))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.c,P.d__tilde__):'((-MC**2 + MW**2)*((-3*CKM2x1*ee**2*MC**2*complexconjugate(CKM2x1))/(2.*sw**2) - (3*CKM2x1*ee**2*MC**4*complexconjugate(CKM2x1))/(2.*MW**2*sw**2) + (3*CKM2x1*ee**2*MW**2*complexconjugate(CKM2x1))/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.c,P.s__tilde__):'((-MC**2 + MW**2)*((-3*CKM2x2*ee**2*MC**2*complexconjugate(CKM2x2))/(2.*sw**2) - (3*CKM2x2*ee**2*MC**4*complexconjugate(CKM2x2))/(2.*MW**2*sw**2) + (3*CKM2x2*ee**2*MW**2*complexconjugate(CKM2x2))/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'(((-3*CKM3x3*ee**2*MB**2*complexconjugate(CKM3x3))/(2.*sw**2) - (3*CKM3x3*ee**2*MT**2*complexconjugate(CKM3x3))/(2.*sw**2) - (3*CKM3x3*ee**2*MB**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) + (3*CKM3x3*ee**2*MB**2*MT**2*complexconjugate(CKM3x3))/(MW**2*sw**2) - (3*CKM3x3*ee**2*MT**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) + (3*CKM3x3*ee**2*MW**2*complexconjugate(CKM3x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)'})

Decay_b = Decay(name = 'Decay_b',
                particle = P.b,
                partial_widths = {(P.W__minus__,P.t):'(((3*CKM3x3*ee**2*MB**2*complexconjugate(CKM3x3))/(2.*sw**2) + (3*CKM3x3*ee**2*MT**2*complexconjugate(CKM3x3))/(2.*sw**2) + (3*CKM3x3*ee**2*MB**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) - (3*CKM3x3*ee**2*MB**2*MT**2*complexconjugate(CKM3x3))/(MW**2*sw**2) + (3*CKM3x3*ee**2*MT**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) - (3*CKM3x3*ee**2*MW**2*complexconjugate(CKM3x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)'})

Decay_c = Decay(name = 'Decay_c',
                particle = P.c,
                partial_widths = {(P.W__plus__,P.d):'((MC**2 - MW**2)*((3*CKM2x1*ee**2*MC**2*complexconjugate(CKM2x1))/(2.*sw**2) + (3*CKM2x1*ee**2*MC**4*complexconjugate(CKM2x1))/(2.*MW**2*sw**2) - (3*CKM2x1*ee**2*MW**2*complexconjugate(CKM2x1))/sw**2))/(96.*cmath.pi*abs(MC)**3)',
                                  (P.W__plus__,P.s):'((MC**2 - MW**2)*((3*CKM2x2*ee**2*MC**2*complexconjugate(CKM2x2))/(2.*sw**2) + (3*CKM2x2*ee**2*MC**4*complexconjugate(CKM2x2))/(2.*MW**2*sw**2) - (3*CKM2x2*ee**2*MW**2*complexconjugate(CKM2x2))/sw**2))/(96.*cmath.pi*abs(MC)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.W__plus__,P.b):'(((3*CKM3x3*ee**2*MB**2*complexconjugate(CKM3x3))/(2.*sw**2) + (3*CKM3x3*ee**2*MT**2*complexconjugate(CKM3x3))/(2.*sw**2) + (3*CKM3x3*ee**2*MB**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) - (3*CKM3x3*ee**2*MB**2*MT**2*complexconjugate(CKM3x3))/(MW**2*sw**2) + (3*CKM3x3*ee**2*MT**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) - (3*CKM3x3*ee**2*MW**2*complexconjugate(CKM3x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)'})

