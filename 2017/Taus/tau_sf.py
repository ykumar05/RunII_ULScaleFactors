from correctionlib import _core

# Load CorrectionSet
fname = '/home/bowerbird/Yash/Work/Jupytr/Scale_Factors/2017/Taus/tau_UL2017.json'
cset = _core.CorrectionSet.from_file(fname)

# Load Correction objects that can be evaluated
corr1 = cset["DeepTau2017v2p1VSjet"]
corr2 = cset["DeepTau2017v2p1VSe"]
corr3 = cset["DeepTau2017v2p1VSmu"]

pt, eta_e,eta_mu, dm, genmatch = 1520.0, 2.10, 2.0, 0, 5

# DeepTau2017v2p1VSjet
sf1 = corr1.evaluate(pt,dm,5,"VTight","nom","pt")
print("DeepTau2017v2p1VSjet sf= %.8f (genmatch=5)"%sf1)

# DeepTau2017v2p1VSe
sf2 = corr2.evaluate(eta_e,1,"Loose","nom")
print("DeepTau2017v2p1VSe sf= %.5f (genmatch=1)"%sf2)

# DeepTau2017v2p1VSmu
sf3 = corr3.evaluate(eta_mu,2,"Loose","nom")
print("DeepTau2017v2p1VSmu sf= %.5f (genmatch=2)"%sf3)
