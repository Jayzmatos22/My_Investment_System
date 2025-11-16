# MY INVESTMENT SYSTEM V. 1.00

# TECNOLOGIAS: 100% PYTHON, BIBLIOTECAS NATIVAS, PROCEDURAL (POREM UM POUCO MODULAR COM FUNÇÕES).
# DEV: JAILTON SANTOS DE MATOS

# FUNCIONALIDADES:
                # VALIDAÇÕES DE DADOS (PESSOAIS E DE LOGIN),
                # SISTEMA DE CORES ANSI PARA UX,
                # SIMULADOR DE CÂMBIO (MINI CONTABILIDADE),
                # CRUD SIMPLES (ATUALIZAÇÃO, DELETE, LEITURA DE DADOS...),
                # CONTABILIDADE: LUCRO, RENDIMENTO, MARGEM, ROI, IMPOSTOS...


import statistics
import time
import datetime
import math
from time import sleep
import calendar

# SISTEMA DE USO DE CORES ANSI. EU USO A CHAVE PARA INFORMAR A COR (NO CASO DE CORES APLICADOS SOBRE O TEXTO) E AS CHAMO PELO SEU VALOR, DENTRO DO DICIONÁRIO.
# O CÓDIGO DA COR É APLICADO NA STRING QUE ESTOU FORMATANDO, SEJA PARA O TETXO OU PARA O FUNDO.
cores_texto = {'branco': '\033[30m', 'vermelho': '\033[31m',
               'verde': '\033[32m', 'amarelo': '\033[33m',
               'azul': '\033[34m', 'roxo': '\033[35m',
               'azulfraco': '\033[36m', 'cinza': '\033[37m'}

texto_formato = {'none': '\033[m', 'grifado': '\033[1m', 'sublinhado': '\033[4m', 'invertido': '\033[7m'}

cores_fundo = {'branco': '\033[40m', 'vermelho': '\033[41m',
               'verde': '\033[42m', 'amarelo': '\033[43m',
               'azul': '\033[44m', 'roxo': '\033[45m',
               'azulfraco': '\033[46m', 'cinza': '\033[47m'}

hoje = datetime.date.today()
dia_atual = hoje.day
mes_atual = hoje.month
ano_atual = hoje.year
print(f'\n{cores_texto['verde']}ACESSANDO DIA: {dia_atual} - MÊS: {mes_atual}\033[m\n')

# 2. Gerar e imprimir o calendário do mês
print(
    f'{cores_texto['azulfraco']}{texto_formato['sublinhado']}{texto_formato['grifado']}{calendar.month(ano_atual, mes_atual)}\033[m--- BEM VINDO ---')


def validar_nome(m: str, nome_minimo: int = 7, nome_maximo: int = 30):
    while True:
        # SIMBOLOS PROIBIDOS DE USAR NO NOME.
        simbolos = ('\033[35m!@#$%^&*"()-_=+[]{};:,.<>?/|`~¬§±¢£¥€©®™¶•†‡∞≠≈≤≥÷×√∑∏µΩ∆π∂∞→←↑↓↔↕↩↪↠↯∀∃⊂⊃⊆⊇⊕⊗⊥∴∵∽≡∈∉∧∨¬-Q'
                    '\∩∪◊□■▪▫▲△▼▽◆◇○●◉◎◌◍☀☁☂☃☄★☆✡✦✧✩✪✫✬✭✮✯✰✱✲✳✴✵✶✷✸✹✺✻✼✽✾✿❀❁❂❃❄❅❆❇❈❉❊❋☼☽☾☯☮☢☣⚐⚑⚒⚓⚔⚕⚖'
                    '⚗⚙⚛⚜♠♣♥♦♤♧♡♢♩♪♫♬♭♮♯⌘⌂⌛⌚⌫⏎⏏⎈⎋\033[m')
        erros_nome_usuario = []  # VETOR QUE ARMAZENA OS ERROS DO USUÁRIO NO NOME.
        contar_erros_nome = 0  # CONTABILIZA OS ERROS
        name = input(m).strip().upper()

        # LIMPEZA DE ERROS. ARMAZENA NO VETOR E MOSTRA NO FINAL.
        try:
            if name.isdigit() or name.isnumeric():
                erros_nome_usuario.append(f'{cores_texto['vermelho']}Erro, digite apenas palavras!\033[m')
                contar_erros_nome += 1
            if '.' in name:
                erros_nome_usuario.append(
                    f'{cores_texto['vermelho']}Erro, não pode conter pontos/pontos duplos (".")\033[m')
                contar_erros_nome += 1
            if len(name.replace(" ", "")) < nome_minimo:
                erros_nome_usuario.append(f'{cores_texto['vermelho']}Erro, tamanho mínimo exigído: {nome_minimo}\033[m')
                contar_erros_nome += 1
            if len(name.replace(' ', '')) > nome_maximo:
                erros_nome_usuario.append(
                    f'{cores_texto['vermelho']}Erro, tamanho máximo permitido: {nome_maximo}\033[m')
                contar_erros_nome += 1
            if any(s in simbolos for s in name):
                erros_nome_usuario.append(
                    f'{cores_texto['vermelho']}Erro, nome não pode conter símbolos/caracteres não puramente alfabéticos!\033[m')
                contar_erros_nome += 1
            if not ' ' in name:
                erros_nome_usuario.append(
                    f'{cores_texto['vermelho']}Erro, formato inválido, use "nome - sobrenome ..."!\033[m')
                contar_erros_nome += 1
            if erros_nome_usuario:
                sleep(0.3)
                print(f'{cores_texto['cinza']}-->VALIDANDO\033[m\n')
                sleep(0.3)
                print(f'{texto_formato['grifado']}{contar_erros_nome} ERRO(S) ENCONTRADO(S):')
                sleep(0.3)
                for e_u in erros_nome_usuario:
                    sleep(0.3)
                    print(f'{e_u}')
                sleep(0.3)
                print(f'{cores_texto['verde']}{texto_formato['grifado']}### TENTE NOVAMENTE ###\033[m\n')

            # COMO CADA IF FOI FEITO SEPARADAMENTE, SE NÃO HÁ ERRO PEGO PELO IF ANTERIOR, ENTÃO RETORNA "name".
            else:
                return name
        except TypeError:
            continue


def validar_flutuante(msg: str):
    while True:
        entrada = input(msg).strip()
        try:
            return float(entrada)
        except ValueError:
            print(f'{cores_texto['vermelho']}Inserção incorreta, digite apenas números/decimais!\033[m\n')
            continue


def validar_codigo_numerico(msg: str, codigo_minimo: int = 6, codigo_maximo: int = 15):
    while True:
        erros_codigo = []  # VETOR ONDE É ARMAZENADO OS ERROS
        contar_erros_resgate = 0
        numero = input(msg).strip()

        # TARTATIVA DE ERROS.
        try:
            if not numero or numero == '' or ' ' in numero:
                erros_codigo.append(f'{cores_texto['vermelho']}-Erro, caixa vazia ou com espaços!\033[m')
                contar_erros_resgate += 1
            if len(numero) > codigo_maximo:
                erros_codigo.append(
                    f'{cores_texto['vermelho']}-Erro, o código deve ter no máximo\033[m \033[34m{codigo_maximo}\033[m \033[31mdígitos!\033[m')
                contar_erros_resgate += 1
            if len(numero) < codigo_minimo:
                erros_codigo.append(
                    f'{cores_texto['vermelho']}-Erro, o código deve ter ao menos\033[m \033[34m{codigo_minimo}\033[m \033[31mdígitos!\033[m')
                contar_erros_resgate += 1
            if not numero.isdigit():
                erros_codigo.append(f'{cores_texto['vermelho']}-Erro, digite apenas números!\033[m')
                contar_erros_resgate += 1
            if ' ' in numero or '.' in numero:
                erros_codigo.append(
                    f'{cores_texto['vermelho']}-Erro, não pode conter pontos, nem espaços vazios.\033[m')
                contar_erros_resgate += 1
            if erros_codigo:
                print(f'{cores_texto['vermelho']}{contar_erros_resgate} Erro(s) encontrado(s) no código:\033[m\n')
                for e in erros_codigo:
                    sleep(0.3)
                    print(f'{e}\n')
                    continue
            else:
                return int(numero)
        except ValueError:
            continue


def validar_numero_inteiro(msg: str):
    while True:
        valorIT = input(msg)  # CONVERTE EM INTEIRO
        try:
            valorIT = int(valorIT)
            return int(valorIT)
        except ValueError:
            sleep(0.5)
            print(f'{cores_texto['vermelho']}ERRO, USE APENAS NÚMEROS!\033[m\n')
            continue


def validar_senha(msg: str, tamanho_senha: int = 6):
    while True:  # Uso de while True para que o usuário sempre tenha a chance de acessar a conta.
        password = input(msg).strip()  # Variavel que recebe o input da senha.
        erros_senha = []  # VETOR QUE ARMAZENA OS ERROS PEGO PELOS IF.                                                                                             # Vetor que recebe os erros acumulados em cada if, alocados atraves do método 'append'
        simbolos = '\033[35m@#$%^&*~!"¨><´`()-_=+[]{};:,.?/\\|\033[m'  # Símbolos aceitos na validação de senha.
        contar_erros_senha = 0  # Soma a quantidade de erros que o usuário cometeu, vindo após isso os erros em si (erros_senha).
        # SÉRIE DE CRITÉRIOS PARA UMA SENHA FORTE. USO DO ANY PARA VALIDAR PELO MENOS UM 1 CRITÉRIO DA CONDIÇÃO DENTRO DA SENHA
        if not any(c.isupper() for c in password):
            erros_senha.append(
                f'{cores_texto['vermelho']}A SENHA DEVE CONTER AO MENOS\033[m \033[34m1\033[m \033[31mCARACTERE MAIÚSCULO!\033[m')
            contar_erros_senha += 1
        if not any(c.islower() for c in password):
            erros_senha.append(
                f'{cores_texto['vermelho']}A SENHA DEVE CONTER AO MENOS\033[m \033[34m1\033[m \033[31mCARACTERE MINÚSCULO!\033[m')
            contar_erros_senha += 1
        if not any(c.isdigit() for c in password):
            erros_senha.append(
                f'{cores_texto['vermelho']}A SENHA DEVE CONTER AO MENOS\033[m \033[34m1\033[m \033[31mDÍGITO!\033[m')
            contar_erros_senha += 1
        if len(password) < tamanho_senha:
            erros_senha.append(
                f'{cores_texto['vermelho']}A SENHA DEVE CONTER AO MENOS\033[m \033[34m{tamanho_senha}\033[m \033[31mCARACTERES!\033[m')
            contar_erros_senha += 1
        if not any(c in simbolos for c in password):
            erros_senha.append(
                f'{cores_texto['vermelho']}A SENHA DEVE CONTER ALGUM SÍMBOLO ESPECIAL! \033[m' + simbolos)
            contar_erros_senha += 1

        # MOSTRA O VETOR DE ERROS SOMENTE SE ELE CONTÉM ALGUM ELEMENTO:
        if erros_senha:  # Condição para ser possível exibir os erros e a sua soma. o else abaixo verifica a inexistência dos erros, retornando, assim, "password'.
            if contar_erros_senha == 1:
                sleep(0.5)
                print(f'{cores_texto['cinza']}---->VALIDANDO...\033[m')
                sleep(0.5)
                print(
                    f'{cores_texto['vermelho']}{contar_erros_senha}\033[m \033[37mERRO ENCONTRADO NA SUA SENHA:\033[m\n')
                sleep(0.5)
                for erro in erros_senha:
                    sleep(0.5)
                    print(erro)
                print(f'{cores_texto['verde']}### TENTE NOVAMENTE! ###\033[m\n')
            else:
                sleep(0.5)
                print(f'{cores_texto['cinza']}---->VALIDANDO...\033[m')
                sleep(0.5)
                print(
                    f'{cores_texto['vermelho']}{contar_erros_senha}\033[m \033[37mERROS ENCONTRADOS NA SUA SENHA:\033[m\n')
                for erroS in erros_senha:
                    sleep(0.5)
                    print(erroS)
                print(f'{cores_texto['verde']}### TENTE NOVAMENTE! ###\033[m\n')
                sleep(0.5)
        else:
            return password


def validar_email(mg: str, tamanho_email: int = 10):
    while True:  # while True para o restante da função, pois os critérios devem ser atentidos, podendo ser possível refazer o processo caso o usuário erre em algum critério.
        contar_erros_email = 0  # Variável para soma dos erros dos usuário na criação do email.
        erros_email = []  # Vetor onde é armazenado os erros cometidos pelo usuário na criação do email.
        emai = input(
            mg).strip().lower()  # A funão lower é usada para ignorar maiusculas, de forma que se o usuário cria um email "XXX', ele pode acessar como 'XxX'.
        # SÉRIE DE CRITÉRIOS ('@', SEM DOIS PONTOS SEGUIDOS '..' ETC) QUE OS EMAILS NORMALMENTE POSSUEM.
        if not emai:
            erros_email.append(f'{cores_texto['vermelho']}ERRO, ESPAÇO VAZIO!\033[m')
            contar_erros_email += 1
        if ' ' in emai:
            erros_email.append(f'{cores_texto['vermelho']}NÃO PODE CONTER ESPAÇOS!\033[m')
            contar_erros_email += 1
        if len(emai) < tamanho_email:
            erros_email.append(
                f'{cores_texto['vermelho']}O EMAIL DEVE CONTER AO MENOS\033[m \033[34m{tamanho_email}\033[m \033[31mCARACTERES!\033[m')
            contar_erros_email += 1
        if not '@' in emai:
            erros_email.append(f'{cores_texto['vermelho']}O EMAIL DEVE CONTER\033[m \033[32m"@"\033[m')
            contar_erros_email += 1
        if emai.count('@') > 1:
            erros_email.append(f'{cores_texto['vermelho']}ERRO, DEVE CONTER APENAS UM\033[m \033[32m"@"\033[m')
            contar_erros_email += 1
        if '..' in emai:
            erros_email.append(f'{cores_texto['vermelho']}ERRO, NÃO É PERMITIDO PONTOS CONSECUTIVOS!\033[m')
            contar_erros_email += 1
        if not '.' in emai:
            erros_email.append(f'{cores_texto['vermelho']}O EMAIL DEVE CONTER PONTO "."\033[m')
            contar_erros_email += 1
        if '@' in emai:
            local, dominio_parte = emai.split('@', 1)
            if local.startswith('.') or local.endswith('.'):
                erros_email.append(
                    f'{cores_texto['vermelho']}ERRO, PARTE\033[m \033[32m"@"\033[m \033[31mNÃO PODE COMEÇAR NEM TERMINAR COM PONTO: "."\033[m')
                contar_erros_email += 1
            if dominio_parte.startswith('.') or dominio_parte.endswith('.'):
                erros_email.append(
                    f'{cores_texto['vermelho']}DOMÍNIO DEPOIS\033[m \033[32m"@"\033[m \033[31mNÃO PODE COMEÇAR/TERMINAR COM PONTO: "."\033[m')
                contar_erros_email += 1
            if '..' in emai:
                erros_email.append(f'{cores_texto['vermelho']}NÃO PODE CONTER PONTOS CONSECUTIVOS: ".."\033[m')
        if erros_email:  # Condição para exibição dos erros.
            if contar_erros_email == 1:
                print(f'{cores_texto['cinza']}---->VALIDANDO...\033[m')
                print(f'{cores_texto['vermelho']}{contar_erros_email}\033[m \033[37mERRO ENCONTRADO!\033[m\n')
                for erro in erros_email:
                    sleep(0.5)
                    print(erro)
                print(f'{cores_texto['verde']}### TENTE NOVAMENTE ###\033[m\n')
            else:
                sleep(0.5)
                print(f'{cores_texto['cinza']}---->VALIDANDO...\033[m')
                sleep(0.5)
                print(f'{cores_texto['vermelho']}{contar_erros_email}\033[m \033[37mERROS ENCONTRADOS!\033[m\n')
                for erro in erros_email:
                    sleep(0.5)
                    print(erro)
                print(f'{cores_texto['verde']}{texto_formato['grifado']}### TENTE NOVAMENTE ###\033[m\n')
        else:
            return emai


# SIMULAÇÃO APROXIMADA DO CÂMBIO ENTRE AS MOEDAS.
taxas = {
    # 1 BRL compra esta quantidade da moeda estrangeira.
    "USD": 0.1989,  # Dólar Americano (ex: 1 BRL = 0.1989 USD)
    "EUR": 0.1843,  # Euro
    "GBP": 0.1558,  # Libra Esterlina
    "JPY": 29.6200,  # Iene Japonês (Mantenha mais casas decimais para precisão)
    "AUD": 0.3060,  # Dólar Australiano
    "CAD": 0.2596,  # Dólar Canadense
    "CNY": 1.4550,  # Yuan Chinês
    "MXN": 3.7900,  # Peso Mexicano
    "ARS": 180.0000,  # Peso Argentino (Valor muito variável, este é um valor recente)
    "BRL": 1.0000  # Real Brasileiro (Moeda Base)
}


def conversor_de_moedas(valor, moeda_origem, moeda_destino):
    """Realiza a conversão de moedas com base nas taxas."""
    try:
        # 1. Correção: Se moedas iguais, retorna o valor
        if moeda_origem == moeda_destino:
            return valor

        # O cálculo é: (Valor / Taxa Base Origem) * Taxa Base Destino
        # Como todas as taxas estão em relação ao BRL (1.0000), a fórmula fica:
        # Conversão = valor * (Taxa Origem / Taxa Destino)
        taxa = taxas[moeda_destino] / taxas[moeda_origem]  # Corrigi a lógica para usar a taxa BRL como base

        conversao = valor * taxa
        return conversao
    except KeyError:
        # Não imprime o erro aqui. Deixa a função retornar None para ser tratado.
        return None


def validar_altura(msg: str):
    while True:
        # MÉTRICAS REAIS DE ALTURA MÁXIMA E MÍNIMA.
        altura_maxima = 2.72
        altura_minima = 0.54
        altura = input(msg).strip()
        try:
            altura = float(altura)
            if altura > altura_maxima:
                print(f'{cores_texto['vermelho']}Erro, altura máxima permitida: {altura_maxima}m\033[m\n')
                continue
            elif altura < altura_minima:
                print(f'{cores_texto['vermelho']}Erro, altura mínima permitida: {altura_minima}m\033[m\n')
                continue
            return altura
        except ValueError:
            print(f'{cores_texto['vermelho']}Erro, digite apenas números e/ou números decimais.\033[m\n')


def validar_idade(msg: str):
    while True:

        # INICIAMOS VÁRIAS VARIÁVEIS ANTES DE PROSSEGUIR.
        # CADA UMA DELAS É UM MÍNIMO OU LIMITE REAL DOS DADOS
        idade_maxima = 122
        idade_minima = 10
        idade = input(msg).strip()
        try:
            idade = int(idade)
            if idade > idade_maxima:
                print(f'{cores_texto['vermelho']}Erro, idade máxima permitida: {idade_maxima}\033[m\n')
                continue
            elif idade < idade_minima:
                print(f'{cores_texto['vermelho']}Erro, idade mínima permitida: {idade_minima}\033[m\n')
                continue
            return idade
        except ValueError:
            print(f'{cores_texto['vermelho']}Erro, digite apenas números inteiros sem pontos.\033[m\n')


def validar_ramo_investimento(msg: str):
    while True:
        erros_ramo = []
        contar_erros_ramo = 0
        tamanho_maximo_ramo = 25
        tamanho_minimo_ramo = 2
        ramo = input(msg).strip().upper()
        try:
            ramo = str(ramo)
            if len(ramo) > tamanho_maximo_ramo:
                erros_ramo.append(f'{cores_texto['vermelho']}-Erro, tamanho máximo: {tamanho_maximo_ramo}\033[m\n')
                contar_erros_ramo += 1
            if len(ramo) < tamanho_minimo_ramo:
                erros_ramo.append(f'{cores_texto['vermelho']}-Erro, tamanho mínimo: {tamanho_minimo_ramo}\033[m\n')
                contar_erros_ramo += 1
            if not ramo.replace(' ', '').isalpha():
                erros_ramo.append(f'{cores_texto['vermelho']}-Erro, digite apenas palavras\033[m\n')
                contar_erros_ramo += 1
            if not ramo or ramo is None:
                erros_ramo.append(f'{cores_texto['vermelho']}-Erro, caixa vázia\033[m\n')
                contar_erros_ramo += 1
            if erros_ramo:
                sleep(0.3)
                print(f'{cores_texto['vermelho']}{contar_erros_ramo} ERROS ENCONTRADOS:\033[m\n')
                for erro_r in erros_ramo:
                    sleep(0.3)
                    print(erro_r)
            else:
                return ramo
        except ValueError:
            print(f'Erro, insira um nome válido\033[m\n')


# FUNÇÃO PARA RETORNAR SEXUALIDADE DO USUÁRIO.
def validar_sexo(sx: str):
    while True:
        s = input(sx).strip().upper()
        if s != 'MASCULINO' and s != 'FEMININO':
            print(f'{cores_texto['vermelho']} Sexo inválido, tente novamente.\033[m\n')
            continue
        else:
            return s


def validar_peso(pu: str):
    while True:

        # PESO MÁXIMO E MÍNIMOS REGISTRADOS NA HISTÓRIA
        peso_maximo = 635
        peso_minimo = 2.1
        ps = validar_flutuante(pu)
        if ps > peso_maximo:
            sleep(0.3)
            print(f'{cores_texto['vermelho']} Peso inválido, máximo: {peso_maximo}Kg.\033[m\n')
            continue
        if ps < peso_minimo:
            sleep(0.3)
            print(f'{cores_texto['vermelho']} Peso inválido, mínimo: {peso_minimo}Kg.\033[m\n')
            continue
        else:
            sleep(0.3)

            return ps


# FUNÇÃO PRARA PARA VALIDAR CPF.
def validar_cpf(c: str):
    while True:

        # COLETA DE ERROS PARA AJUDAR USUÁRIO.
        tamanho_cp = 11
        erros_cpf = []
        contar_erros_cpf = 0
        try:
            sleep(0.3)
            cp = input(c)
            if not cp:
                erros_cpf.append(f'{cores_texto['vermelho']}Caixa vazia\033[m\n')
                contar_erros_cpf += 1
            if not cp.isdigit():
                erros_cpf.append(f'{cores_texto['vermelho']}Digite apenas números\033[m\n')
                contar_erros_cpf += 1
            if len(cp) > tamanho_cp or len(cp) < tamanho_cp:
                erros_cpf.append(f'{cores_texto['vermelho']}Tamanho inválido, necessário {tamanho_cp} dígitos\033[m\n')
                contar_erros_cpf += 1
            if erros_cpf:
                sleep(0.3)
                print(f'{cores_texto['vermelho']}{contar_erros_cpf} Erro(s) encontrados: \033[m\n')
                sleep(0.3)
                for cc in erros_cpf:
                    print(cc)
            else:
                sleep(0.3)

                return cp
        except ValueError:
            continue


# FUNÇÃO PARA VALIDAR RG. USA PARÂMETROS PARECIDOS COM O CPF.
def validar_rg(r: str):
    while True:
        tamanho_rg_ma = 12
        tamanho_rg_mi = 7
        erros_rg = []
        contar_erros_rg = 0
        try:
            sleep(0.3)
            rg = input(r)
            if not rg:
                erros_rg.append(f'{cores_texto['vermelho']}Caixa vazia\033[m\n')
                contar_erros_rg += 1
            if not rg.isdigit():
                erros_rg.append(f'{cores_texto['vermelho']}Digite apenas números\033[m\n')
                contar_erros_rg += 1
            if len(rg) > tamanho_rg_ma or len(rg) < tamanho_rg_mi:
                erros_rg.append(
                    f'{cores_texto['vermelho']}Tamanho inválido, {tamanho_rg_mi} a {tamanho_rg_ma} dígitos.\033[m\n')
                contar_erros_rg += 1
            if erros_rg:
                sleep(0.3)
                print(f'{cores_texto['vermelho']}{contar_erros_rg} Erro(s) encontrados: \033[m\n')
                sleep(0.3)
                for er in erros_rg:
                    print(er)
            else:
                sleep(0.3)

                return rg
        except ValueError:
            continue


print('')
print(f'{cores_texto['verde']}====**====\033[m' * 4)
print(
    f'\033[45m---*{texto_formato['invertido']}{cores_texto["verde"]}{cores_fundo["branco"]}  * PASSO 1 - CRIAR CONTA\033[m\033[45m*---\033[m')
print(f'{cores_texto['verde']}====**====\033[m' * 4)
print('')

# ÁREA ONDE FAREMOS APLICAÇÕES DAS FUNÇÕES E AS VALIDAÇÕES.
while True:

    # DICIONÁRIOS ONDE SERÃO ARMAZENADOS AS INFORMAÇÕES COLETADAS.
    email_resgate = {}
    senha_resgatar = {}
    dados_usuario = {}
    print()
    criar_meu_email = validar_email(f'{texto_formato['invertido']} CRIE UM EMAIL:\033[m ')
    email_resgate['EMAIL RESGATADO'] = criar_meu_email
    print()
    criar_minha_senha = validar_senha(f'{texto_formato['invertido']} CRIE UMA SENHA:\033[m ')
    senha_resgatar['SENHA RESGATADA'] = criar_minha_senha
    print()
    codigo_de_resgate = validar_codigo_numerico(f'{texto_formato['invertido']} CRIE UM CÓDIGO DE RESGATE:\033[m ')
    print()
    nome_usuario = validar_nome(f'{texto_formato['invertido']} INFORME SEU NOME COMPLETO:\033[m ').upper()
    dados_usuario['NOME'] = nome_usuario
    print()
    print(f'\033[1m{cores_texto['amarelo']}1: CONFIRMAR - QUALQUER OUTRO BOTÃO: REDIGITAR\033[m\n')
    confirmar_login = str(input(f'{texto_formato['invertido']}  CONFIRMAR LOGIN:\033[m ')).strip()

    if confirmar_login == '1':

        print(f'{cores_texto['amarelo']}Login confirmado!\033[m]\n')

    elif confirmar_login != '1':
        sleep(0.3)
        print(f'{cores_texto['amarelo']}Voltando...\033[m')
        continue

    while True:

        print(
            f'\033[1m{texto_formato['invertido']}{cores_fundo['branco']}{cores_texto['verde']}--- PREENCHA SEUS DADOS PESSOAIS ---\033[m\n')

        # APLICAMOS A FUNÇÃO NA VARIÁVEL.
        idade_usuario = validar_idade(f'{texto_formato['invertido']} INFORME SUA IDADE:\033[m ')
        dados_usuario['IDADE'] = idade_usuario
        print()
        # WHILE PARA CONTROLAR FLUXO E TRATAR ERROS USANDO VARIÁVEIS DO WHILE.
        # USO DE 2 WHILE PARA O USUÁRIO NÃO PRECISAR DIGITAR IDADE NOVAMENTE QUANDO ERRAR ALTURA NO WHILE ANTERIOR.

        while True:

            altura_usuario = validar_altura(f'{texto_formato['invertido']} INFORME SUA ALTURA:\033[m ')

            # ALOCAMOS A ALTURA NO DICIONÁRIO DOS DADOS DO USUÁRIO.

            dados_usuario['ALTURA'] = altura_usuario
            print()

            while True:

                ramo_investimento = validar_ramo_investimento(
                    f'{texto_formato['invertido']} INFORME O RAMO DA SUA EMPRESA/INVESTIMENTO:\033[m ')

                dados_usuario['RAMO'] = ramo_investimento
                print()
                while True:

                    sexo_usuario = validar_sexo(
                        f'{texto_formato['invertido']} INFORME SEU SEXO (MASCULINO/FEMININO):\033[m ')

                    dados_usuario['SEXO'] = sexo_usuario
                    print()
                    while True:

                        peso_usuario = validar_peso(f'{texto_formato['invertido']} INFORME SEU PESO (Kg):\033[m ')

                        dados_usuario['PESO'] = peso_usuario
                        print()
                        while True:

                            cpf_usuario = validar_cpf(
                                f'{texto_formato['invertido']} INFORME SEU CPF (APENAS NÚMEROS):\033[m ')

                            dados_usuario['CPF'] = cpf_usuario
                            print()
                            while True:
                                rg_usuario = validar_rg(
                                    f'{texto_formato['invertido']} INFORME SEU RG (APENAS NÚMEROS):\033[m ')

                                dados_usuario['RG'] = rg_usuario
                                print()
                                break
                            break
                        break
                    break

                # WHILR PARA RECONFIRMAR OS DADOS PESSOAIS. ESSE WHILE SO VAI SER QUEBRADO QUANDO:
                # USUARIO QUISER RECONFIRMAR DADOS OU CONFIRMAR OS DADOS.
                while True:
                    # RECONFIRMAÇÃO DE DADOS.
                    print(
                        f'\033[1m{cores_texto['amarelo']}CONFIRMAR DADOS? (APERTE QUALQUER BOTÃO: VOLTAR PARA DADOS PESSOAIS, 1: CONFIRMAR)\033[m\n')
                    sleep(0.3)
                    confirmacao_dados = str(input(f'{texto_formato['invertido']} ESCOLHA:\033[m ')).strip()

                    # OUTRO BOTÃO = VOLTAR PARA DADOS PESSOAIS
                    if confirmacao_dados != '1':

                        sleep(0.3)
                        print()
                        print(f'\033[32m\033[1mINFORME SEUS DADOS NOVAMENTE!\033[m\n')
                        break
                    # OUTRO BOTÃO = VOLTAR PARA DADOS PESSOAIS
                    else:

                        # SEQUÊNCIA DE BREAK PARA QUEBRAR TODOS OS WHILE ATÉ CHEGAR NO PRIMEIRO.
                        print(f'{cores_texto['verde']}DADOS SALVOS COM SUCESSO!\033[m\n')
                        break
                break
            break
        break
    break

print()

# USO DE DICIONARIO PARA ATUALIZAÇÃO DEDADOS, CONFORME NECESSIDADE ESPECÍFICA DE FUNÇÃO.
mapeamento_de_funcoes_dados = {'NOME': validar_nome,
                               'IDADE': validar_idade,
                               'SEXO': validar_sexo,
                               'ALTURA': validar_altura,
                               'RAMO': validar_ramo_investimento,
                               'CPF': validar_cpf,
                               'RG': validar_rg,
                               'PESO': validar_peso,
                               }

# ESSE É UM DICIONÁRIO USADO NA FUNÇÃO ATUALIZAR_DADOS PARA ENCONTRAR A CHAVE PELO NÚMERO.
numero_dicionario_dados = {
    '1': 'NOME', '2': 'IDADE', '3': 'ALTURA', '4': 'RAMO',
    '5': 'CPF', '6': 'RG', '7': 'PESO', '8': 'SEXO',
}


def atualizar_dados():
    while True:
        print()
        # Exibe o menu usando o dicionário de mapeamento
        print(f'\033[1m{cores_texto['verde']}--- ATUALIZAR DADOS PESSOAIS ---\033[m\n')
        sleep(0.3)
        print(f'\033[1m{cores_texto['verde']}DADOS QUE PODEM SER ATUALIZADOS:\033[m\n')
        sleep(0.3)
        for num_opcao, chave_dado in numero_dicionario_dados.items():
            print(
                f'\033[1m{cores_texto['verde']}[{num_opcao}] {chave_dado.upper()} (ATUAL: {dados_usuario[chave_dado]})\033[m')
            sleep(0.2)
        print(f"{cores_texto['amarelo']}[9] ATUALIZAR TODOS.\033[m")
        print(f"{cores_texto['vermelho']}[10] SAIR DA ATUALIZAÇÃO.\033[m\n")

        atualizar = input(f'{texto_formato['invertido']} DESEJA ATUALIZAR QUAL DADO?\033[m ').strip()

        if atualizar == '10':
            sleep(0.3)
            print('\033[31mRetornando...\033[m')
            return dados_usuario

        # ATUALIZAMOS TODOS OS DADOS MANUALMENTE, POIS PRECISAMOS APLICAR AS FUNÇÕES DEVIDAS.
        if atualizar == '9':
            print()
            dados_usuario['NOME'] = validar_nome(f'{texto_formato['invertido']}INFORME NOVO NOME:\033[m ')
            print()
            dados_usuario['IDADE'] = validar_idade(f'{texto_formato['invertido']}INFORME NOVA IDADE:\033[m ')
            print()
            dados_usuario['ALTURA'] = validar_altura(f'{texto_formato['invertido']}INFORME NOVA ALTURA:\033[m ')
            print()
            dados_usuario['RAMO'] = validar_ramo_investimento(f'{texto_formato['invertido']}INFORME NOVO RAMO:\033[m ')
            print()
            dados_usuario['CPF'] = validar_cpf(f'{texto_formato['invertido']}INFORME NOVO CPF:\033[m ')
            print()
            dados_usuario['RG'] = validar_rg(f'{texto_formato['invertido']}INFORME NOVO RG:\033[m ')
            print()
            dados_usuario['PESO'] = validar_peso(f'{texto_formato['invertido']}INFORME NOVO PESO:\033[m ')
            print()
            dados_usuario['SEXO'] = validar_sexo(f'{texto_formato['invertido']}INFORME NOVO SEXO:\033[m ')
            print()
            print(f'{cores_texto['verde']}TODOS OS DADOS FORAM ATUALIZADOS COM SUCESSO!\033[m')

        if atualizar in numero_dicionario_dados:
            sleep(0.3)
            chave_do_dado = numero_dicionario_dados[atualizar]  # Ex: '2' -> 'IDADE'

            # 🎯 PASSO CHAVE: Busca a função correta
            funcao_de_entrada = mapeamento_de_funcoes_dados.get(chave_do_dado)

            if funcao_de_entrada:
                print()
                sleep(0.3)
                prompt = f'{cores_texto['azul']}DIGITE NOVO VALOR PARA {chave_do_dado.upper()}:\033[m '

                # 🎯 EXECUÇÃO: Executa a função específica e armazena o valor validado
                novo_valor = funcao_de_entrada(prompt)

                # Atualização CORRETA
                dados_usuario[chave_do_dado] = novo_valor
                sleep(0.3)
                print(f"✅ CAMPO '{chave_do_dado.upper()}' ATUZALIZADO!.")
            else:
                print("⚠️ Campo sem função de validação definida.")
                # Lógica de fallback, se necessário

        if atualizar != '9' and atualizar != '10' and atualizar not in numero_dicionario_dados:
            sleep(0.3)
            print(f'{cores_texto['vermelho']}Opção inválida. Tente novamente.\033[m\n')


# ÁREA ONDE SERÁ FEITA A VALIDÇÃO DOS DADOS CADASTRAIS.
# NÃO SERÁ NECESSARIO TRATAR ERROS DE CRITÉRIOS, APENAS DE VALIDAÇÃO ENTRE O QUE FOI CRIADO E ACESSADO, POIS ELES FORAM TRATADOS DURANTE O USO DA FUNÇÃO.


while True:  # Todas as condições estarão dentro do while True, ou seja, elas serão testadas até o usuário acertar.
    print(f'{cores_texto['vermelho']}====**===\033[m' * 4)
    print(f'{texto_formato['invertido']}{cores_texto['azul']} ** PASSO 2 - ACESSAR CONTA **\033[m')
    print(f'{cores_texto['vermelho']}====**===\033[m' * 4)
    print(' ')
    acessar_meu_email = input(
        f'{texto_formato['invertido']} INFORME SEU ENDEREÇO DE EMAIL:\033[m ').strip().lower()  # variável de acesso ao email já criado.
    print()
    acessar_minha_senha = input(
        f'{texto_formato['invertido']} INFORME SUA SENHA:\033[m ').strip()  # variável de acesso à senha já criado.
    if acessar_minha_senha == criar_minha_senha and acessar_meu_email == criar_meu_email:  # Condição para validar email e senha, a fim de liberar acesso e quebrar o resto do código (break).
        sleep(0.5)
        print(f'{cores_texto['cinza']}---->VALIDANDO DADOS...\033[m')
        print()
        sleep(0.5)
        print(f'{cores_texto['cinza']}ACESSANDO CONTA EM:\033[m\n')
        for i in range(3, 0, -1):
            print(f'{i}°')
            sleep(0.5)
        print(f'{cores_texto['verde']}{texto_formato['grifado']}--- LOGIN ACESSADO COM SUCESSO! ---\033[m')
        break
    if acessar_minha_senha != criar_minha_senha and acessar_meu_email != criar_meu_email:  # Condição para ignorar o bloco abaixo e voltar ao início, pois não é possível usar o código de resgate aqui.
        sleep(0.3)
        print(f'{cores_texto['cinza']}---->VALIDANDO DADOS...\033[m')
        sleep(0.3)
        print()
        print(
            f'{texto_formato['invertido']}{cores_texto['branco']}{cores_fundo['vermelho']} O EMAIL E SENHA INSERIDOS NÃO EXISTEM, POR FAVOR INSIRA OS DADOS CORRETAMENTE! \033[m\n')
        continue
    if acessar_minha_senha == criar_minha_senha and acessar_meu_email != criar_meu_email:  # Condição para uso do código de resgate para resgatar email criado.
        sleep(0.5)
        print(f'{cores_texto['vermelho']}ACESSO NEGADO, EMAIL INCORRETO.\033[m\n')
        contar_erro_codigo1 = 3
        for i in range(1, contar_erro_codigo1 + 1):
            sleep(0.3)
            print(f'{cores_texto['azul']}Resgate seu email com o código de resgate, para acessar conta:\033[m\n')
            sleep(0.3)
            resgatar_email = validar_codigo_numerico(
                f'{texto_formato['invertido']} DIGITE SEU CÓDIGO DE RESGATE:\033[m ')  # Variável para digitar o código de resgate e validar.
            if resgatar_email == codigo_de_resgate:  # Tratando código inválido com for.
                sleep(0.3)
                print(f'\033[1m{cores_texto["roxo"]}SEU EMAIL: {email_resgate.get('EMAIL RESGATADO')}\033[m')
                print()
                break
            else:
                if i < 3:
                    sleep(0.3)
                    print(f'{cores_texto['vermelho']}CÓDIGO INVÁLIDO, TENTE NOVAMENTE! TENTATIVA N°{i}\033[m')
                    print()
                elif i == 3:
                    print(f'{cores_texto['vermelho']}TENTATIVAS ESGOTADAS, REFAÇA O PROCESSO DE LOGIN!\033[m')
    elif acessar_minha_senha != criar_minha_senha and acessar_meu_email == criar_meu_email:  # Condição para tratar senha errada, através do código também.
        sleep(0.3)
        contar_erro_codigo2 = 3
        print(f'{cores_texto['vermelho']}ACESSO NEGADO, SENHA INCORRETA.\033[m\n')
        for i in range(1, contar_erro_codigo2 + 1):
            sleep(0.3)
            print(f'{cores_texto['azul']}Resgate sua senha com o código de resgate, para acessar conta:\033[m\n')
            sleep(0.3)
            resgatar_senha = validar_codigo_numerico(
                f'{texto_formato['invertido']} DIGITE SEU CÓDIGO DE RESGATE:\033[m ')  # Variável para digitar o código de resgate e validar.
            print()
            if resgatar_senha == codigo_de_resgate:  # Tratndo erro no código de resgate para senha.
                sleep(0.3)
                print(f'\033[1m{cores_texto["roxo"]}SUA SENHA: {senha_resgatar.get('SENHA RESGATADA')}\033[m')
                print()
                break
            else:
                if i < 3:
                    sleep(0.3)
                    print(f'{cores_texto['vermelho']}CÓDIGO INVÁLIDO, TENTE NOVAMENTE! TENTATIVA N°{i}\033[m')
                elif i == 3:
                    print(f'{cores_texto['vermelho']}TENTATIVAS ESGOTADAS, REFAÇA O PROCESSO DE LOGIN!\033[m')

print('')
print(f'{cores_texto['roxo']}===**===\033[m' * 6)
print(f'{cores_fundo['roxo']}*** PASSO 3: PLANEJAMENTO E INVESTIMENTO ***\033[m')
print(f'{cores_texto['roxo']}===**===\033[m' * 6)
print('')

print(f'{cores_texto['amarelo']}====**====\033[m' * 7)
print(
    f'{cores_texto['verde']}$$\033[m {cores_texto['vermelho']}INFORMAÇÕES OBRIGATÓRIAS - FATURAMENTO, DEPESAS E TRIBUTOS\033[m {cores_texto['verde']}$$\033[m')
print(f'{cores_texto['amarelo']}====**====\033[m' * 7)

# ÁREA DE INFORME DE DESPESAS E FATURA
while True:
    print()

    # WHILE PARA PERMITIR NOVAS INSERÇÕES EM CASO DE ERRO.
    fatura_bruta = validar_flutuante(f'{cores_texto['cinza']}VALOR - FATURAMENTO:\033[m ')
    print()
    despesas_infraestrutura = validar_flutuante(f'{cores_texto['cinza']}VALOR DESPESAS - INFRAESTRUTURA:\033[m ')
    print('')
    despesas_funcionarios = validar_flutuante(f'{cores_texto['cinza']}GASTO MENSAL - FUNCIONÁRIOS:\033[m ')
    print()
    impostos_federais = validar_flutuante(f'{cores_texto['cinza']}PORCENTAGEM - IMPOSTOS FEDERAIS:\033[m ')
    print()
    impostos_estaduais = validar_flutuante(f'{cores_texto['cinza']}PORCENTAGEM - IMPOSTOS ESTADUAIS:\033[m ')
    print()
    investimento = validar_flutuante(f'{cores_texto['cinza']}VALOR INVESTIDO:\033[m ')
    print()
    meta_lucro_liquido = validar_flutuante(f'{cores_texto['cinza']}LUCRO LIQUIDO ESPERADO:\033[m ')
    print()
    marketing_mensal = validar_flutuante(f'{cores_texto['cinza']}VALOR - MARKETING MENSAL:\033[m ')
    print()
    impostos_totais = ((impostos_federais * fatura_bruta) / 100) + ((impostos_estaduais * fatura_bruta) / 100)
    meta_roi = validar_flutuante(f'{cores_texto['cinza']}META - ROI:\033[m ')
    print()
    meta_margem_lucro = validar_flutuante(f'{cores_texto['cinza']}META - MARGEM LUCRO:\033[m ')
    print()

    print((f'\033[1m{cores_texto['amarelo']} DIGITE: 1: CONFIRMAR - QUALQUER OUTRO BOTÃO: REDIGITAR\033[m\n'))
    confirmar_insercao_faturas = str(input(f'{texto_formato['invertido']} CONFIRMAR: '))
    if confirmar_insercao_faturas == '1':
        sleep(0.3)
        print('\033[32mDADOS SALVOS.\033[m')
        break
    else:
        sleep(0.3)
        print('\033[33mReinsira dados...\033[m')
        continue

print()
print(f'{cores_texto['cinza']}CARREGANDO INFORMAÇÕES...')
time.sleep(1.0)

# BARRA DE CARREGAMENTO PARA PROGRESSO DAS INFORMAÇÕES. USABILIDADE UX.

print(f'{cores_texto['vermelho']}0%\033[m', end='')
for i in range(50):
    while i >= 0 and i < 10:
        print(f'{cores_fundo['vermelho']}-\033[m', end='')
        break
    sleep(0.040)
    while i > 10 and i <= 20:
        print(f'{cores_fundo['amarelo']}-\033[m', end='')
        break
    while i > 20 and i <= 30:
        print(f'{cores_fundo['azul']}-\033[m', end='')
        break
    while i > 30 and i <= 40:
        print(f'{cores_fundo['azulfraco']}-\033[m', end='')
        break
    while i > 40 and i <= 50:
        print(f'{cores_fundo['verde']}-\033[m', end='')
        break
print(f'{texto_formato['grifado']}{cores_texto['verde']}100%\033[m')
print()

# SAÍDA DE DADOS REFERENTE AO QUE O USUÁRIO INFORMOU. NESTA PARTE, NENHUM CÁLCULO É APLICADO.
print(f'{cores_texto['cinza']}====* VOCÊ FORNECEU AS SEGUINTES INFORMAÇÕES ====*\033[m\n')
print(f'{texto_formato['invertido']} NOME: {dados_usuario['NOME']}', end=' - ')
print(f'{texto_formato['invertido']} CPF: {dados_usuario['CPF']} \033[m\n')
print(
    f'{cores_texto['amarelo']}-->FATURAMENTO:\033[m {cores_texto['verde']}${fatura_bruta}\033[m\n{cores_texto['amarelo']}-->DESPESAS - INFRAESTRUTURA:\033[m {cores_texto['vermelho']}${despesas_infraestrutura}\033[m\n'
    f'{cores_texto['amarelo']}-->DESPESAS - FUNCIONÁRIOS:\033[m {cores_texto['vermelho']}${despesas_funcionarios}\033[m\n{cores_texto['amarelo']}-->IMPOSTOS FEDERAIS:\033[m {cores_texto['vermelho']}%{impostos_federais}\n'
    f'{cores_texto['amarelo']}-->IMPOSTOS ESTADUAIS:\033[m {cores_texto['vermelho']}%{impostos_estaduais}\033[m\n{cores_texto['amarelo']}-->INVESTIMENTO: {cores_texto['vermelho']}${investimento}\033[m\n'
    f'{cores_texto['amarelo']}-->LUCRO LÍQUIDO ESPERADO:\033[m {cores_texto['verde']}${meta_lucro_liquido}\033[m\n'
    f'{cores_texto['amarelo']}-->VALOR - MARKETING MENSAL:\033[m {cores_texto['vermelho']}${marketing_mensal}\033[m\n{cores_texto['amarelo']}-->META - ROI:\033[m {cores_texto['verde']}%{meta_roi}\033[m\n'
    f'{cores_texto['amarelo']}-->META - MARGEM LUCRO:\033[m {cores_texto['verde']}${meta_margem_lucro}\033[m')
print('')
print(f'{cores_texto['cinza']}{texto_formato['invertido']}====\033[m' * 10)

for contagem in range(3, 0 - 1, -1):
    if contagem == 3:
        print(f'---- \033[37mGERANDO SEGUNDO RELATÓRIO EM:  -->¨°{contagem}\033[m')
    elif contagem == 2:
        print(f'---- \033[37mGERANDO SEGUNDO RELATÓRIO EM:  -->¨°{contagem}\033[m')
    elif contagem == 1:
        print(f'---- \033[37mGERANDO SEGUNDO RELATÓRIO EM:  -->¨°{contagem}\033[m')
    elif contagem == 0:
        print(f'---- \033[37mGERANDO SEGUNDO RELATÓRIO EM:  -->¨°{contagem}\033[m\n')
    time.sleep(0.4)

# CÁLCULOS GERAIS SOBRE AS INFORMAÇÕES OBTIDAS

print(f'\033[36m\033[7m"¨¨¨¨¨"\033[m\033[36m\033[4m VISÃO GERAL SOBRE INVESTIMENTO\033[m \033[36m\033[7m"¨¨¨¨¨"\033[m')
print('')
despesas_operacionais_totais = math.fsum([despesas_funcionarios, despesas_infraestrutura, marketing_mensal])
lucro_liquido = fatura_bruta - (despesas_operacionais_totais + impostos_totais)
roi = (lucro_liquido / investimento) * 100
margem_lucro = (lucro_liquido / fatura_bruta) * 100
maior_gasto = max(despesas_funcionarios, despesas_infraestrutura, marketing_mensal)
menor_gasto = min(despesas_funcionarios, despesas_infraestrutura, marketing_mensal)
percentual_imposto_sobre_faturamento = (impostos_totais / fatura_bruta) * 100
gasto_medio = statistics.fmean([despesas_funcionarios, despesas_infraestrutura, marketing_mensal])
percentual_gastos_operacionais_sobre_faturamento = (despesas_operacionais_totais / fatura_bruta) * 100
print(
    f'{cores_texto['azul']}-->GASTOS OPERACIONAIS TOTAIS: {cores_texto['vermelho']}${despesas_operacionais_totais:.2f}\033[m\n'
    f'{cores_texto['azul']}-->GASTOS TRIBUTÁRIOS TOTAIS:\033[m {cores_texto['vermelho']}${impostos_totais:.2f}\033[m\n'
    f'{cores_texto['azul']}-->PERCENTUAL DE IMPOSTO SOBRE FATURAMENTO:\033[m {cores_texto['vermelho']}%{percentual_imposto_sobre_faturamento:.2f}\033[m\n'
    f'{cores_texto['azul']}-->PERCENTUAL DE GASTOS OPERACIONAIS SOBRE FATURAMENTO:\033[m {cores_texto['vermelho']}%{percentual_gastos_operacionais_sobre_faturamento:.2f}\033[m\n'
    f'{cores_texto['azul']}-->ROI - RETORNO SOBRE INVESTIMENTO:\033[m {cores_texto['verde']}%{roi:.2f}\033[m\n{cores_texto['azul']}-->MARGEM DE LUCRO:\033[m {cores_texto['verde']}%{margem_lucro:.2f}\033[m\n'
    f'{cores_texto['azul']}-->MAIOR GASTO UNITÁRIO:\033[m {cores_texto['vermelho']}${maior_gasto:.2f}\033[m\n{cores_texto['azul']}-->GASTO MÉDIO:\033[m {cores_texto['vermelho']}${gasto_medio:.2f}\033[m\n'
    f'{cores_texto['azul']}-->MENOR GASTO UNITÁRIO:\033[m {cores_texto['vermelho']}${menor_gasto:.2f}\033[m\n{cores_texto['azul']}-->LUCRO LÍQUIDO:\033[m {cores_texto['verde']}${lucro_liquido:.2f}\033[m\n')

# ARMAZENAMOS OS DADOS INFORMADOS EM UM DICIONÁRIO, DENTRO DE UM VETOR, SERVIRÁ PARA CONSULTA UNITÁRIA NA OPÇÃO 3 DO MENU.
dados_operacoes_iniciais = {
    'FATURAMENTO': fatura_bruta, 'DESPESAS INFRAESTRUTURA': despesas_infraestrutura,
    'DESPESAS FUNCIONÁRIOS': despesas_funcionarios, 'IMPOSTOS FEDERIAS': impostos_federais,
    'IMPOSTOS ESTADUAIS': impostos_estaduais, 'INVESTIMENTO': investimento,
    'LUCRO LIQUIDO ESPERADO': meta_lucro_liquido,
    'MARKETING MENSAL': marketing_mensal, 'META ROI': meta_roi, 'META MARGEM LUCRO': meta_margem_lucro
}

# ARMAZENAMOS OS DADOS JÁ CALCULADOS EM UM DICIONÁRIO, DENTRO DE UM VETOR, SERVIRÁ PARA CONSULTA UNITÁRIA NA OPÇÃO 3 DO MENU, DA MESMA FORMA QUE O VETOR ANTERIOR.

dados_operacoes_calculadas = {
    'GASTOS OPERACIONAIS TOTAIS': despesas_operacionais_totais, 'GASTOS TRIBUTÁRIOS TOTAIS': impostos_totais,
    'PERCENTUAL DE IMPOSTO SOBRE FATURAMENTO': percentual_imposto_sobre_faturamento,
    'PERCENTUAL DE GASTOS OPERACIONAIS SOBRE FATURAMENTO': percentual_gastos_operacionais_sobre_faturamento,
    'ROI - RETORNO SOBRE INVESTIMENTO': roi, 'MARGEM DE LUCRO': margem_lucro, 'MAIOR GASTO UNITÁRIO': maior_gasto,
    'GASTO MÉDIO': gasto_medio, 'MENOR GASTO UNITÁRIO': menor_gasto, 'LUCRO LIQUIDO': lucro_liquido
}

while True:
    # LISTA DE OPÇÕES DE FUNCIONALIDADES QUE  O USUÁRIO PODE USAR.
    print(f'\033[1m{texto_formato['invertido']}==== MENU GERAL - CONSULTAS E PESQUISA ==== \033[m\n')
    print(f'\033[1m{cores_texto['roxo']}--> 0. SAIR DO MENU\033[m\n'
          f'\033[1m{cores_texto['roxo']}--> 1. AVALIAÇÃO: EXPECTATIVA X DADOS DOS INVESTIMENTOS\033[m\n'
          f'\033[1m{cores_texto['roxo']}--> 2. CONVERSÃO PARA OUTRAS MOEDAS\033[m\n'
          f'\033[1m{cores_texto['roxo']}--> 3. CONSULTAS SOBRE NEGÓCIO\033[m\n'
          f'\033[1m{cores_texto['roxo']}--> 4. MEUS DADOS PESSOAIS\033[m\n'
          f'\033[1m{cores_texto['roxo']}--> 5. ATUALIZAR DADOS DE LOGIN\033[m\n')
    opcao_menu_geral = str(input(f'{texto_formato['invertido']} ESCOLHA:\033[m ')).strip()
    print()

    # OPÇÕES QUE REINCINDEM AO MENU GERAL NOVAMENTE.
    if (
            opcao_menu_geral != '0' and opcao_menu_geral != '1'
            and opcao_menu_geral != '2' and opcao_menu_geral != '3'
            and opcao_menu_geral != '4' and opcao_menu_geral != '5'
    ):

        sleep(0.3)
        print()
        print(f'{cores_texto['vermelho']}OPÇÃO INVÁLIDA, TENTE NOVAMENTE!\033[m\n')
        continue

    elif opcao_menu_geral == '0':
        sleep(0.3)

        # Loop para a CLASSIFICAÇÃO (permite reclassificar)
        while True:
            print(f'{cores_texto['amarelo']}-- AVALIE SUA NEVAGAÇÃO NESSE SISTEMA --\033[m\n')
            print(
                f'{cores_texto['cinza']}NOTAS:\033[m {cores_texto['vermelho']}0: SAIR DO SISTEMA;\033[m {cores_texto['vermelho']}1 - 3: RUIM;\033[m {cores_texto['amarelo']}4 - 6: REGULAR;\033[m {cores_texto['azul']}7 - 9: BOM;\033[m {cores_texto['verde']}10: ÓTIMO.\033[m\n')

            feedback_usuario = validar_numero_inteiro(
                f'{texto_formato['invertido']} FAÇA SUA AVALIAÇÃO (0 a 10):\033[m ')
            print()

            # Garante que a nota está no range 0-10
            if feedback_usuario < 0 or feedback_usuario > 10:
                print('\033[31mEscolha uma nota entre 0 e 10.\033[m\n')
                continue  # Volta ao topo do loop de CLASSIFICAÇÃO

            # Se a nota for 0, encerra a avaliação
            if feedback_usuario == 0:
                sleep(0.3)
                print(f'{cores_texto['vermelho']}AVALIAÇÃO IGNORADA.\033[m\n')
                break  # Sai do loop de CLASSIFICAÇÃO e passa para a CONFIRMAÇÃO FINAL

            # Loop para a CONFIRMAÇÃO
            while True:
                # 1. Determinar o texto de feedback para exibir na confirmação
                if feedback_usuario >= 1 and feedback_usuario <= 3:
                    resultado_avaliacao = f'{cores_texto["vermelho"]}RUIM!\033[m'
                elif feedback_usuario >= 4 and feedback_usuario <= 6:
                    resultado_avaliacao = f'{cores_texto["amarelo"]}REGULAR!\033[m'
                elif feedback_usuario >= 7 and feedback_usuario <= 9:
                    resultado_avaliacao = f'{cores_texto["azul"]}BOM!\033[m'
                elif feedback_usuario == 10:
                    resultado_avaliacao = f'{cores_texto["verde"]}ÓTIMO!\033[m'

                # 2. Pedir confirmação
                print(f'Sua avaliação é: {resultado_avaliacao}')
                print()
                confirmar_feedback = validar_numero_inteiro(
                    f'{texto_formato['invertido']} CONFIRMAR SAÍDA E NOTA (0: RECLASSIFICAR - 1: SAIR):\033[m ')

                if confirmar_feedback == 0:
                    print(f'{cores_texto['amarelo']}\nRECLASSIFICANDO NOTA...\033[m\n')
                    # Usa 'break' para sair do loop de CONFIRMAÇÃO e 'continue' para o loop de CLASSIFICAÇÃO
                    break

                elif confirmar_feedback == 1:
                    print(f'\n{cores_texto['azul']}REGISTRANDO AVALIAÇÃO: {resultado_avaliacao}\033[m')

                    # Usa 'break' para sair do loop de CONFIRMAÇÃO
                    break

                else:
                    print(f'{cores_texto['vermelho']}\nOpção inválida. Tente novamente.\033[m\n')
                    continue  # Volta ao topo do loop de CONFIRMAÇÃO

            # Se a confirmação foi 1 (SAIR), o break acima foi executado.
            if confirmar_feedback == 1:
                break  # Sai do loop de CLASSIFICAÇÃO para a SAÍDA FINAL

            # Se a confirmação foi 0 (RECLASSIFICAR), o continue acima foi executado.
            if confirmar_feedback == 0:
                continue
        print()
        # SAÍDA FINAL (Fora dos loops de Classificação e Confirmação)
        print(f'{cores_texto['vermelho']}-- PROGRAMA ENCERRADO, VOLTE SEMPRE! -- \033[m')
        break  # Sai do loop WHILE TRUE PRINCIPAL

    # AQUI USAREMOS O CONVERSOR DE MOEDAS, QUE O USUÁRIO PODE USAR COM BASE NOS CÁLCULOS FEITOS
    elif opcao_menu_geral == "2":
        while True:
            sleep(0.3)
            print(f'{cores_texto['azul']}MOEDAS DISPONÍVEIS:\033[m {cores_texto['verde']}',
                  " - ".join(taxas.keys()))  # Lista
            print('\033[m')
            moeda_origem = str(
                input(f'{texto_formato['invertido']} MOEDA DE ORIGEM (ou "SAIR"):\033[m ')).strip().upper()
            if not moeda_origem.isalpha():
                sleep(0.3)
                print(f'{cores_texto['vermelho']}ERRO, APENAS LETRAS!\033[m')
                sleep(0.3)
                continue
            if moeda_origem == 'SAIR':
                sleep(0.3)
                print(f'{cores_texto['vermelho']}CONVERSÃO ENCERRADA!\033[m')
                print()
                break  # SAI DO LOOP (menu)
            if moeda_origem not in taxas:
                sleep(0.3)
                print(f'{cores_texto['vermelho']}MOEDA DE ORIGEM INVÁLIDA!\033[m\n')
                sleep(0.3)
                continue
            sleep(0.3)
            print()
            while True:
                moeda_destino = str(input(f'{texto_formato['invertido']} MOEDA DE DESTINO:\033[m ')).strip().upper()
                print()
                if not moeda_destino.isalpha():
                    sleep(0.3)
                    print(f'{cores_texto['vermelho']}ERRO, APENAS LETRAS!\033[m')
                    continue
                if moeda_destino not in taxas:
                    sleep(0.3)
                    print(f'{cores_texto['vermelho']}MOEDA DE DESTINO INVÁLIDA!\033[m\n')
                    sleep(0.3)
                    continue
                break
            while True:
                try:
                    valor = validar_flutuante(f'{texto_formato['invertido']} INFORME O VALOR A SER CONVERTIDO:\033[m ')
                    break
                except ValueError:
                    print(f'{cores_texto['vermelho']}VALOR INVÁLIDO; SOMENTE NÚMEROS!\033[m')
                    continue
            # Chamada e tratamento do resultado
            conversao_realizada = conversor_de_moedas(valor, moeda_origem, moeda_destino)
            if conversao_realizada is not None:
                # 2. Melhoria: Formatação de saída para moedas
                print()
                print(
                    f'{cores_texto['verde']}{texto_formato['grifado']}CONVERSÃO: {valor:.2f} {moeda_origem} convertido fica: {conversao_realizada:.2f} {moeda_destino}\033[m')
            else:
                # Mensagem de erro.
                print(F'{cores_texto['vermelho']}EERO DE CONVERSÃO. Verifique as moedas informadas.\033[m')
                continue

    # SISTEMA QUE INFORMA QUANTAS E QUAIS METAS O USUÁRIO BATEU
    # DADOS: O LUCRO ESPERADO, ROI E A MARGEM.
    elif opcao_menu_geral == '1':
        metas = 0  # CONTABILIZA METAS
        sleep(0.3)
        print(f'{cores_texto['verde']}==== AVALIAÇÃO DE METAS ====\033[m')
        print()
        sleep(0.3)

        # NESSA PARTE VERIFICAMOS SE AS METAS FORAM INFERIORES AOS RESULTADOS.
        # USANDO AS VARIÁVEIS PARA ANALISAR O DADO REAL VS A META ESTABELECIDA.
        if lucro_liquido < meta_lucro_liquido:
            sleep(0.3)
            print(
                f'{cores_texto['vermelho']}--> Você não atingiu o lucro líquido esperado, faltou:\033[m \033[32mR${meta_lucro_liquido - lucro_liquido:.2f}\033[m')
        else:
            if meta_lucro_liquido == lucro_liquido:
                metas += 1
                sleep(0.3)
                print(f'{cores_texto['verde']}--> Parabéns, você atingiu o lucro líquido esperado!\033[m')
            elif lucro_liquido > meta_lucro_liquido:
                metas += 1
                sleep(0.3)
                print(f'{cores_texto['verde']}--> Parabéns, você superou o lucro líquido esperado!\033[m'
                      f'{cores_texto['azulfraco']} --> META: {meta_lucro_liquido} - ALCANÇOU: {lucro_liquido:.2f}\033[m')
        if roi < meta_roi:
            sleep(0.3)
            print(f'{cores_texto['vermelho']}--> Você não atingiu o ROI esperado, faltou {meta_roi - roi:.2f}\033[m')
        else:
            if meta_roi == roi:
                metas += 1
                sleep(0.3)
                print(f'{cores_texto['verde']}--> Parabéns, você atingiu o ROI esperado!\033[m')
            elif roi > meta_roi:
                metas += 1
                sleep(0.3)
                print(f'{cores_texto['verde']}--> Parabéns, você superou o ROI esperado!\033[m'
                      f'{cores_texto['azulfraco']} --> META: {meta_roi}, ALCANÇOU: {roi:.2f}\033[m')
        if margem_lucro < meta_margem_lucro:
            sleep(0.3)
            print(
                f'{cores_texto['vermelho']}--> Você não atingiu a margem de lucro esperada, faltou {meta_margem_lucro - margem_lucro:.2f}\033[m')
        else:
            if meta_margem_lucro == margem_lucro:
                sleep(0.3)
                metas += 1
                print(f'{cores_texto['verde']}--> Parabéns, você atingiu a margem de lucro esperada!\033[m')
            else:
                if margem_lucro > meta_margem_lucro:
                    metas += 1
                    sleep(0.3)
                    print(f'{cores_texto['verde']}--> Parabéns, você superou a margem de lucro esperada!\033[m'
                          f'{cores_texto['azulfraco']}META: {meta_margem_lucro}, ALCANÇOU: {margem_lucro:.2f}.\033[m')
        # VERIFICANDO SE ELE BATEU ALGUMA META.
        if metas == 0:
            sleep(0.3)
            print(f'{cores_texto['vermelho']}--> Infelizmente você ainda não bateu nenhuma meta!\033[m')
            continue
        else:
            sleep(0.3)
            print(f'{cores_texto['cinza']}Contabilizando metas...\033[m')
            sleep(0.7)
            print(f'\033[32m--> Parabéns, você bateu {metas} meta(s)!\033[m')
            print()
            continue

    # AQUI SERÁ RESERVADO PARA O USUÁRIO CONSULTAR SEUS PRÓPRIOS DADOS FINANCEIROS.
    elif opcao_menu_geral == '3':  # USAREMOS OS VETORES 'DADOS_OPERACOES_INICIAIS' E 'DADOS_OPERACOES_CALCULADAS' PARA RETORNAR DADOS UNITÁRIOS PARA CONSULTA
        while True:
            print()
            print(f'{cores_texto['azulfraco']} -- REALIZAR CONSULTAS DE OPERAÇÃO -- \033[m\n')
            print(f'{cores_texto['verde']}0: SAIR - 1: CONSULTAS INICIAIS - 2: CONSULTAS PÓS-CÁLCULOS.\033[m\n')
            menu_consultas_iniciais = str(input(f'{texto_formato['invertido']} INFORME SUA ESCOLHA:\033[m '))
            print()
            if menu_consultas_iniciais == '0':
                print()
                print(f'{cores_texto['vermelho']}Consulta encerrada\033[m\n')
                break
            elif menu_consultas_iniciais != '0' and menu_consultas_iniciais != '1' and menu_consultas_iniciais != '2':
                print()
                print(f'{cores_texto['vermelho']}Opção inválida, tente novamente.\033[m]')
                continue

            # USAMOS UM WHILE TRUE PARA ISOLAR ESSA PARTE
            if menu_consultas_iniciais == '1':
                while True:
                    # ARMAZENAMOS CADA VARIÁVEL INFORMADA (SEM CÁLCULOS) EM UM DICIONÁRIO. ELE SERÁ USADO PARA RETORNAR CADA VALOR, DE ACORDO COM O QUE O USUÁRIO DIGITAR NOS MENUS DE CONSULTAS, CONTROLADO POR "controlar_consulta_unitaria"
                    acessar_consulta_inicial_por_numero_string = {
                        '0': fatura_bruta, '1': despesas_infraestrutura,
                        '2': despesas_funcionarios, '3': impostos_estaduais,
                        '4': impostos_federais, '5': investimento,
                        '6': meta_lucro_liquido, '7': marketing_mensal,
                        '8': meta_roi, '9': meta_margem_lucro
                    }

                    # MENU COM AS OPÇÕES DO USUÁRIO, SE FOR '1' em menu_consultas_iniciais'
                    # O MENU ESTÁ SINCRONIZADO COM O DICIONÁRIO ACIMA, PARA CONSULTAS DO USUÁRIO.

                    print('\033[4m\033[7m \033[42m \033[1mCONSULTAS INICIAIS DISPONÍVEIS:\033[m\n'
                          '\033[7m\033[36m 11: SAIR - 0: FATURAMENTO - 1: DESPESAS INFRA\033[m'
                          '\033[7m\033[36m 2: DESPESAS FUNCIONÁRIOS - 3: IMPOSTOS ESTADUAIS\033[m\n'
                          '\033[7m\033[36m 4: IMPOSTOS FEDERAIS - 5: INVESTIMENTO'
                          '\033[7m\033[36m 6:LUCRO LÍQUIDO ESPERADO - 7: GASTO MARKETING MENSAL\033[m\n'
                          '\033[7m\033[36m 8: META ROI - 9: META MARGEM LUCRO \033[m\n')

                    # USAMOS MAIS UM WHILE PARA CONTROLAR A VOLTA PARA O MENU ANTERIOR.
                    while True:
                        escolher_consulta_inicial = str(
                            input(f'{texto_formato['invertido']} ESCOLHA SUA CONSULTA UNITÁRIA:\033[m ')).strip()
                        escolha_consulta_do_usuario = acessar_consulta_inicial_por_numero_string.get(
                            escolher_consulta_inicial)
                        if escolher_consulta_inicial == '11':  # SAIR = 11, POIS 0(ZERO) NÃO CONSTA NO DICIONÁRIO. SÃO APENAS 10 ITENS.
                            sleep(0.3)
                            print('\033[31mEncerrando consultas iniciais, voltando ao menu...\033[m\n')
                            break
                        elif escolha_consulta_do_usuario is None:
                            sleep(0.3)
                            print(f'{cores_texto['vermelho']}Consulta inválida, tente novamente.\033[m\n')
                            continue
                        sleep(0.3)

                        # BUSCAMOS O VALOR DAS CHAVES EM DICIONÁRIO "dados_operacoes_iniciais", COMPARAMOS SEU VALOR COM O VALOR RETORNADO PELO DICIONÁRIO "acessar_consulta_inicial_por_numero_string".
                        # COMPARAMOS COM O QUE É RETORNADO PELAS CONSULTAS POR NUMERO_STRING. SE FOR IGUAL, O "nome_da_metrica" GUARDA ESSE NOME RESPECTIVO DO VALOR CONSULTADO.
                        nome_da_metrica_inicial = None
                        for nome, valor in dados_operacoes_iniciais.items():
                            if valor == escolha_consulta_do_usuario:
                                nome_da_metrica_inicial = nome

                        if nome_da_metrica_inicial:
                            print(
                                f'{cores_texto['verde']}->{nome_da_metrica_inicial}: {escolha_consulta_do_usuario:.2f}\033[m\n')
                        else:
                            print(f'{cores_texto['vermelho']}Erro, informe corretamente\033[m\n')
                            continue

                        # VARIÁVEL QUE DETERMINARÁ SE O USUÁRIO FARÁ UMA NOCA CONSULTA SEM PRECISAR SAIR PARA O MENU ANTERIOR.
                        decisao_apos_consulta_inicial = str(input(
                            f'{texto_formato['invertido']}DESEJA CONTINUAR CONSULTA? (0: Sair - 1: Continuar:\033[m '))
                        if decisao_apos_consulta_inicial == '1':
                            sleep(0.3)
                            print(f'{cores_texto['verde']}Próxima consulta --> \033[m\n')
                            continue
                        elif decisao_apos_consulta_inicial == '0':
                            sleep(0.3)
                            print()
                            print(f'{cores_texto['vermelho']}Encerrando consultas iniciais...\033[m\n')
                            break
                        else:
                            sleep(0.3)
                            print(f'{cores_texto['vermelho']}Opção inválida, tente novamente.\033[m\n')
                            continue
                    break
            elif menu_consultas_iniciais == '2':
                while True:
                    # FAREMOS A MESMA LÓGICA ANTERIOR PARA ACESSAR O VALOR E O NOME DA CHAVE.
                    # NESSE CASO, USAREMOS O DICIONÁRIO "dados_operacoes_calculadas" PARA FAZER A BUSCA, POIS SÃO OUTROS DADOS.
                    acessar_consulta_calculada_por_numero_string = {
                        '0': despesas_operacionais_totais, '1': impostos_totais,
                        '2': percentual_imposto_sobre_faturamento,
                        '3': percentual_gastos_operacionais_sobre_faturamento,
                        '4': roi, '5': margem_lucro,
                        '6': maior_gasto, '7': gasto_medio,
                        '8': menor_gasto, '9': lucro_liquido
                    }

                    print(f'{cores_texto['azulfraco']}--- CONSULTAS PÓS-CÁLCULOS --- \033[m\n')

                    # MENU COM AS OPÇÕES QUE O USUÁRIO VAI TER.
                    print('\033[4m\033[7m \033[42m \033[1mCONSULTAS PÓS-CÁLCULOS DISPONÍVEIS:\033[m\n'
                          '\033[7m\033[36m 11: SAIR - 0: GASTOS OPERACIONAIS TOTAIS - 1: GASTOS TRIBUTÁRIOS TOTAIS\033[m'
                          '\033[7m\033[36m 2: PERCENTUAL DE IMPOSTO SOBRE FATURAMENTO\033[m'
                          '\033[7m\033[36m 3: PERCENTUAL DE GASTOS OPERACIONAIS SOBRE FATURAMENTO\033[m\n'
                          '\033[7m\033[36m 4: ROI - RETORNO SOBRE INVESTIMENTO - 5: MARGEM DE LUCRO\033[m\n'
                          '\033[7m\033[36m 6: MAIOR GASTO UNITÁRIO - 7: GASTO MÉDIO\033[m\n'
                          '\033[7m\033[36m 8: MENOR GASTO UNITÁRIO - 9: LUCRO LIQUIDO \033[m\n')

                    # WHILE PARA CONTROLE DE FLUXO DE DECISÃO
                    while True:
                        escolher_consulta_calculada = str(
                            input(f'{texto_formato['invertido']} ESCOLHA SUA CONSULTA SOBRE OPERAÇÕES:\033[m ')).strip()
                        escolha_consulta_do_usuario_c = acessar_consulta_calculada_por_numero_string.get(
                            escolher_consulta_calculada)
                        if escolher_consulta_calculada == '11':  # SAIR = 11, POIS 0(ZERO) NÃO CONSTA NO DICIONÁRIO. SÃO APENAS 10 ITENS (DENOVO).
                            sleep(0.3)
                            print('\033[31mEncerrando consultas calculadas, voltando ao menu...\033[m\n')
                            break
                        elif escolha_consulta_do_usuario_c is None:
                            sleep(0.3)
                            print(f'{cores_texto['vermelho']}Consulta inválida, tente novamente.\033[m\n')
                            continue
                        sleep(0.3)

                        # FAZEMOS O MESMO ESQUEMA DE BUSCA, COMO NA ANTERIOR.
                        # COMPARAMOS, DESSA VEZ, COM 'dados_operacoes_calculadas'.
                        nome_da_metrica_calculada = None
                        for nome_c, valor_c in dados_operacoes_calculadas.items():
                            if valor_c == escolha_consulta_do_usuario_c:
                                nome_da_metrica_calculada = nome_c
                        if nome_da_metrica_calculada:
                            print(
                                f'{cores_texto['verde']}->{nome_da_metrica_calculada}: {escolha_consulta_do_usuario_c:.2f}\033[m\n')
                        else:
                            print(f'{cores_texto['vermelho']}Erro, informe corretamente!\033[m\n')
                            continue

                        # DECISÃO QUE DETERMINARÁ SE ELE VOLTA AO MENU OU FAZ MAIS CONSULTAS.
                        decisao_apos_consulta_calculada = str(input(
                            f'{texto_formato['invertido']} DESEJA CONTINUAR CONSULTA? (0: Sair - 1: Continuar:\033[m '))
                        if decisao_apos_consulta_calculada == '1':
                            sleep(0.3)
                            print(f'{cores_texto['verde']}Próxima consulta --> \033[m\n')
                            continue
                        elif decisao_apos_consulta_calculada == '0':
                            sleep(0.3)
                            print()
                            print(f'{cores_texto['vermelho']}Encerrando consultas calculadas...\033[m\n')
                            break
                        elif decisao_apos_consulta_calculada != '0' and decisao_apos_consulta_calculada != '1':
                            sleep(0.3)
                            print(f'{cores_texto['vermelho']}Opção inválida, tente novamente.\033[m\n')
                            continue
                    # ONDE ACABA O LOOP ANTES DO MENU FINAL
                    break
    elif opcao_menu_geral == '4':

        # WHILE PARA CONTROLAR FLUXO DE DECISÕES COM ''if'.
        while True:
            sleep(0.3)
            print()
            print(f'\033[7m\033[1m{cores_fundo['amarelo']}--- CONSULTAR - ALTERAR DADOS ---\033[m\n')
            sleep(0.3)
            print(f'\033[1m{cores_texto['verde']}OPÇOES: 0: SAIR - 1: CONSULTAR - 2: ATUALIZAR\033[m\n')
            consultar_dados = str(input(f'{texto_formato['invertido']} CONSULTAR DADOS:\033[m ')).strip()

            # CONDIÇÃO PARA RETORNAR ERRO DE ENTRADA.
            if consultar_dados != '0' and consultar_dados != '1' and consultar_dados != '2':
                print(f'{cores_texto['vermelho']}Erro, opção inválida!\033[m')
                continue
            elif consultar_dados == '0':
                for i in range(3, 0 - 1, -1):
                    sleep(0.3)
                    print(f'\033[1m{cores_texto['amarelo']}\rEncerrando consultas de dados: {i}°', end='')
                    print()
                    print(f'\033[1m{cores_texto['vermelho']}Retornou ao menu.\033[m\n')
                    # ONDE ACABA O LOOP PRINCIPAL
                    break
                break
            elif consultar_dados == '1':
                sleep(0.3)
                print()
                print(f'\033[1m{cores_texto['verde']}--- SEUS DADOS PESSOAIS ---\033[m\n')
                for chave, valor in dados_usuario.items():
                    print(f'{cores_texto['amarelo']}\033[m] \033[1m\033[32m{chave.upper()}: {valor}\033[m')
                print()
            elif consultar_dados == '2':
                while True:
                    print()

                    # ÁREA ONDE SERÁ VALIDADA A SENHA PARA PERMITIR ATUALIZAÇÃO DOS DADOS.

                    sleep(0.3)
                    print(
                        f'\033[1m{cores_texto['amarelo']}-- ATENÇÃO: PARA ATUALIZAR SEUS DADOS, É NECESSÁRIO INFORMAR SENHA --\033[m\n')

                    # PARA ATUALIZAR DADOS USAMOS A SENHA COMO CONTROLADOR, POIS SÃO DADOS SENSÍVEIS.

                    print(f'\033[1m{cores_texto['amarelo']}DIGITE --> 0: SAIR  -  SUA SENHA (ATUALIZAR).\033[m\n')
                    chave_acesso_dados = str(input(
                        f'{texto_formato['invertido']} INFORME SUA CHAVE/SENHA DE ACESSO PARA ATUALIZAÇÃO:\033[m ')).strip()
                    print()
                    if chave_acesso_dados != criar_minha_senha and chave_acesso_dados != '0':
                        sleep(0.3)
                        print(f'{cores_texto['vermelho']}Senha inválida! Tente novamente.\033[m\n')
                        continue
                    elif chave_acesso_dados != criar_minha_senha and chave_acesso_dados == '0':
                        sleep(0.3)
                        print(f'{cores_texto['vermelho']}Atualização de dados cancelada, retornando ao menu...\033[m\n')
                        break

                    elif chave_acesso_dados == criar_minha_senha:

                        # EXIBIMOS TODOS OS ITENS (DADOS) QUE PODEM SER MUDADOS.
                        sleep(0.3)
                        print(f'\033[1m{cores_texto['verde']}Senha válida! Você pode atualizar seus dados.\033[m\n')

                        # USAMOS A FUNÇÃO PARA TRABALHAR PARA NÓS.
                        atualizar_dados()
                        print()
                        break
            break
    elif opcao_menu_geral == '5':
        # AQUI O USUÁRIO PODERÁ ATUALIZAR SUA SENHA DE ACESSO AO SISTEMA E O CÓDIGO DE RESGATE.
        while True:
            sleep(0.3)
            print()
            print(f'\033[1m{cores_texto['amarelo']}-- ATUALIZAÇÃO DE DADOS DE LOGIN --\033[m\n')
            sleep(0.3)
            print(
                f'\033[1m{cores_texto['amarelo']}DIGITE --> 0: SAIR  -  SUA SENHA ATUAL (ATUALIZAR).\033[m\n')

            chave_acesso_login = str(input(
                f'{texto_formato['invertido']} INFORME SUA CHAVE/SENHA DE ACESSO PARA ATUALIZAÇÃO:\033[m ')).strip()
            print()
            if chave_acesso_login != criar_minha_senha and chave_acesso_login != '0':
                sleep(0.3)
                print(f'{cores_texto['vermelho']}Senha inválida! Tente novamente.\033[m\n')
                continue
            elif chave_acesso_login != criar_minha_senha and chave_acesso_login == '0':
                sleep(0.3)
                print()
                print(f'\033[1m{cores_texto['amarelo']}Retornando ao menu...\033[m\n')

                break


            # A SENHA LIBERA ATUALIZAÇÃO DA PRÓPRIA SENHA E CÓDIGO DE RESGATE.
            elif chave_acesso_login == criar_minha_senha:
                sleep(0.3)
                print(f'\033[1m{cores_texto['verde']}Senha válida! Você pode atualizar sua senha.\033[m\n')

                # WHILE PARA CONTROLAR ERROS NAS ESCOLHAS DE ATUALIZAÇÃO DE SENHA E CÓDIGO.
                while True:

                    print()
                    print(
                        f'\033[1m{cores_texto["verde"]}-- 0: SAIR - 1. ATUALIZAR SENHA - 2 ATUALIZAR CÓDIGO-RESGATE --\033[m\n')
                    atualizar_login_opcao = str(
                        input(f'{texto_formato["invertido"]} ESCOLHA SUA OPÇÃO:\033[m ')).strip()
                    print()
                    if atualizar_login_opcao == '0':
                        sleep(0.3)
                        print(f'{cores_texto["vermelho"]}Atualização de login cancelada...\033[m\n')
                        break
                    elif atualizar_login_opcao == '1':
                        print()

                        # USO DE WHILE PARA EVITAR SENHA IGUAL A ANTERIOR.
                        while True:
                            nova_senha_atualizar = validar_senha(
                                f'{texto_formato["invertido"]} DIGITE NOVA SENHA:\033[m ')
                            if nova_senha_atualizar == criar_minha_senha:
                                sleep(0.3)
                                print()
                                print(f'{cores_texto['vermelho']}Erro, senha não pode ser igual a anterior.\033[m\n')
                                continue
                            criar_minha_senha = nova_senha_atualizar
                            print(f'{cores_texto['verde']}Senha atualizada!\033[m')
                            break

                    elif atualizar_login_opcao == '2':
                        while True:
                            novo_codigo__atualizar = validar_codigo_numerico(
                                f'{texto_formato["invertido"]} DIGITE NOVO CÓDIGO:\033[m ')
                            if novo_codigo__atualizar == codigo_de_resgate:
                                sleep(0.3)
                                print()
                                print(f'{cores_texto['vermelho']}Erro, código não pode ser igual ao anterior.\033[m\n')
                                continue
                            codigo_de_resgate = novo_codigo__atualizar
                            print(f'{cores_texto['verde']}Código atualizado!\033[m')
                            break

            break