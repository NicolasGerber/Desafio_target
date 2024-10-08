sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

soma_total=(sp+rj+mg+es+outros)
percentual_sp = (sp * 100)/soma_total
percentual_rj = (rj * 100)/soma_total
percentual_mg = (mg * 100)/soma_total
percentual_es = (es * 100)/soma_total
percentual_outros = (outros * 100)/soma_total

print(f"O percentua de representação de SP é {percentual_sp:.2f}%")
print(f"O percentua de representação de RJ é {percentual_rj:.2f}%")
print(f"O percentua de representação de MG é {percentual_mg:.2f}%")
print(f"O percentua de representação de ES é {percentual_es:.2f}%")
print(f"O percentua de representação dos Outros é {percentual_outros:.2f}%")