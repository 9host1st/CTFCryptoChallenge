
# This file was *autogenerated* from the file solve.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_6455822262099728871488017333002213763928974244728225916053004114762757288446279146632134559883137763509202760259665317867526185880602417384903035043373123172755205541848380033846647830559956562300790213183285570408285813940654388322823643901338114411098146713766948059574036750169834145669828812062836846441826158939413816441792342997972511615875337134161543579227974534136317577528234543157933263750295100350176275449872173516777290564027194224977405688960141636944708509979113636374750606901261856017099651198201404715950047463077544354559113250673461981023710617386807665904679700243253715051955720384474605996461 = Integer(6455822262099728871488017333002213763928974244728225916053004114762757288446279146632134559883137763509202760259665317867526185880602417384903035043373123172755205541848380033846647830559956562300790213183285570408285813940654388322823643901338114411098146713766948059574036750169834145669828812062836846441826158939413816441792342997972511615875337134161543579227974534136317577528234543157933263750295100350176275449872173516777290564027194224977405688960141636944708509979113636374750606901261856017099651198201404715950047463077544354559113250673461981023710617386807665904679700243253715051955720384474605996461); _sage_const_0p44 = RealNumber('0.44'); _sage_const_1023 = Integer(1023); _sage_const_10 = Integer(10); _sage_const_42209220078437574866361422834065152842384701674177020659394975551630638228773791512185847142423481006715264054186715352545791966183624550240806137742117804368809490341638374030752315967 = Integer(42209220078437574866361422834065152842384701674177020659394975551630638228773791512185847142423481006715264054186715352545791966183624550240806137742117804368809490341638374030752315967); _sage_const_151 = Integer(151); _sage_const_130 = Integer(130); _sage_const_32 = Integer(32); _sage_const_1025 = Integer(1025); _sage_const_5283729370502224111594887226837880395316054773227004499787302073503878519636633822827217253857874355522588395812835740811362707153363560194601186826283559964747701769601487977762111123819420098096415036853595000842267748990264765099199777366178415275775930611456486254983609977806288992648707705283164998069127159450643405479857352132413567941113596062821699046442601516070886895831454313645493977658887986960438243972899363731335524071661232212596476620001731293273701784412244890405468701582192239044191141716454262551899911176914268204608240121498434944371667705131307108367792229003968794133948069333063516311066 = Integer(5283729370502224111594887226837880395316054773227004499787302073503878519636633822827217253857874355522588395812835740811362707153363560194601186826283559964747701769601487977762111123819420098096415036853595000842267748990264765099199777366178415275775930611456486254983609977806288992648707705283164998069127159450643405479857352132413567941113596062821699046442601516070886895831454313645493977658887986960438243972899363731335524071661232212596476620001731293273701784412244890405468701582192239044191141716454262551899911176914268204608240121498434944371667705131307108367792229003968794133948069333063516311066)
from Crypto.Util.number import long_to_bytes as l2b
n = _sage_const_6455822262099728871488017333002213763928974244728225916053004114762757288446279146632134559883137763509202760259665317867526185880602417384903035043373123172755205541848380033846647830559956562300790213183285570408285813940654388322823643901338114411098146713766948059574036750169834145669828812062836846441826158939413816441792342997972511615875337134161543579227974534136317577528234543157933263750295100350176275449872173516777290564027194224977405688960141636944708509979113636374750606901261856017099651198201404715950047463077544354559113250673461981023710617386807665904679700243253715051955720384474605996461 
s = _sage_const_42209220078437574866361422834065152842384701674177020659394975551630638228773791512185847142423481006715264054186715352545791966183624550240806137742117804368809490341638374030752315967 
c = _sage_const_5283729370502224111594887226837880395316054773227004499787302073503878519636633822827217253857874355522588395812835740811362707153363560194601186826283559964747701769601487977762111123819420098096415036853595000842267748990264765099199777366178415275775930611456486254983609977806288992648707705283164998069127159450643405479857352132413567941113596062821699046442601516070886895831454313645493977658887986960438243972899363731335524071661232212596476620001731293273701784412244890405468701582192239044191141716454262551899911176914268204608240121498434944371667705131307108367792229003968794133948069333063516311066 

e = _sage_const_151 

def coopersmith(shiftbits, k):
    F = PolynomialRing(Zmod(n), names=('x',)); (x,) = F._first_ngens(1)
    einv = inverse_mod(e, n)
    f = (s << shiftbits) + x + einv * (k - _sage_const_1 )
    return f.small_roots(X = _sage_const_2  ** shiftbits, beta=_sage_const_0p44 , epsilon=_sage_const_1 /_sage_const_32 )

if __name__ == "__main__":
    for bits in range(_sage_const_1023 , _sage_const_1025 ):
        for k in range(_sage_const_1 , e):
            k = _sage_const_130 
            shiftbits = bits // _sage_const_2  - bits // _sage_const_10 
            x0 = coopersmith(shiftbits, k)
            if(len(x0)) != _sage_const_0 :
                x = Integer(x0[_sage_const_0 ])
                dp = x + (s << shiftbits)
                p = (e * dp - _sage_const_1 ) // k + _sage_const_1 
                q = n // p
                phi = (p - _sage_const_1 ) * (q - _sage_const_1 )
                d = inverse_mod(e, phi)
                print(l2b(pow(c, d, n)))
                break

