import Pregunta1 as p
# Códigos ANSI
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"  # Restablece el color original

raiz_3 = p.root_t(p.cos_t(3/7)+ p.ln_t(2), 3)
sinh = p.sinh_t(p.sqrt_t(2))
arctan = p.atan_t(p.exp_t(-1))

print(f"{RED}Resultados del testFuntras{RESET}")
print ((raiz_3*p.div_t(sinh))+arctan)



