import caixa_acoplada
import alavanca_acionamento
import valvula_alimentacao
import comporta_vedacao

comporta = comporta_vedacao.ComportaVedacao()
alavanca = alavanca_acionamento.AlavancaAcionamento()
valvula = valvula_alimentacao.ValvulaAlimentacao()
caixa = caixa_acoplada.CaixaAcoplada()

print('\n')
# Testando modulo de comporta
print('\n_____ Modulo de Comporta _____\n')
print(comporta.get_status())
comporta.abrir()
print(comporta.get_status())
comporta.fechar()
print(comporta.get_status())

print('\n')
# Testando modulo de alavanca de acionamento
print('\n_____ Modulo de Alavanca _____\n')
alavanca.acionar()
alavanca.relatorio()

print('\n')
# Testando modulo de valvula de alimentacao
print('\n_____ Modulo de Valvula _____\n')
valvula.encher_agua()
print(valvula.get_vazao())

print('\n')
# Testando Modulo da Caixa Acoplada
print('\n_____  Modulo de Caixa  _____\n')
caixa.encher_caixa()


print('\n_____     _____\n')
caixa.acionar(1)
print('\n')
caixa.acionar(2)

print('\n_____   _____\n')
caixa.relatorio()

print('\n')
caixa.statusDescarga()
