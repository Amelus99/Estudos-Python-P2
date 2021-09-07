from abc import ABC, abstractmethod

class Vacina(ABC):
    def __init__(self, numDoses, tecnologia):
        self.__nDoses = nDoses
        self.__aprovada = False
        self.__preco = 0.0
        self.__tecnologia = tecnologia

        @property
        def numDoses(self):
          return self.__nDoses

        @numDoses.setter
        def nDoses(self, nDoses):
          self.__nDoses = nDoses

        @property
        def aprovada(self):
          return self.__aprovada

        @aprovada.setter
        def aprovada(self, status):
          self.__aprovada = status

        @property
        def preco(self):
          return self.__preco

        @preco.setter
        def preco(self, novoPreco):
          assert novoPreco >= 0
          self.__preco = novoPreco

        @abstractmethod
        def country(self):
          pass

#------------------------------------------------------------------------

class Oxford(Vacina):
    __LABORATORIO = 'AstraZeneca'

    def __init__(self, numDoses, intervalo, tecnologia, eficacia):
        super().__init__(numDoses, tecnologia)
        self.__intervalo = intervalo  # intervalo mínimo para aplicar a próxima dose
        self.__eficaciaGlobal = eficacia  # após as n doses


    @property
    def intervalo(self):
        return self.__intervalo

    @intervalo.setter
    def intervalo(self, novoIntervalo):
        self.__intervalo = novoIntervalo

    @property
    def eficacia(self):
      return self.__eficaciaGlobal

    @eficacia.setter
    def eficacia(self, novaeficacia):
      self.__eficaciaGlobal = novaeficacia

    def country(self):
        return 'England'

    @classmethod
    def laboratorio(cls):
        return cls.__LABORATORIO

    def __str__(self):
        return f'''
    Vacina {Oxford.__name__}, 
    Laboratório: {self.laboratorio()}, 
    Numero de Doses = {self.numDoses},
    Tecnologia: {self.tecnologia},
    Intervalo mínimo para aplicação da próxima dose: {self.intervalo}, 
    Eficacia: {self.eficacia}%'''

# -------------------------------------------------------

class Sinovac(Vacina):
    __LABORATORIO = 'Sinovac BioTech'

    def __init__(self, nDoses, intervalo, tecnologia, voluntários):
        super().__init__(nDoses, tecnologia)
        self.__intervalo = intervalo  # intervalo mínimo para a próxima dose
        self.__voluntários = voluntários  # voluntários em ensaios clínicos no Brasil

    @property
    def voluntários(self):
        return self.__voluntários

    @voluntários.setter
    def volutários(self, novoNumero):
        self.__voluntários = novoNumero

    @property
    def intervalo(self):
        return self.__intervalo

    @intervalo.setter
    def intervalo(self, novoIntervalo):
        self.__intervalo = novoIntervalo

    def country(self):
        return 'China'

    @classmethod
    def laboratorio(cls):
        return cls.__LABORATORIO

    def __str__(self):
        return f'''
    Vacina {Sinovac.__name__}, 
    Laboratório: {self.laboratorio()}, 
    Numero de Doses = {self.nDoses},
    Tecnologia: {self.tecnologia},
    Intervalo mínimo para aplicação da próxima dose: {self.intervalo}, 
    Voluntários nos ensaios clínicos (BR): {self.voluntários}'''

# --------------------------------------------------------------------

class Janssen(Vacina):
    __LABORATORIO = 'Johnson & Johnson'

    def __init__(self, nDoses, tecnologia, armazenamento):
        super().__init__(nDoses, tecnologia)
        self.__armazenamento = armazenamento


    @property
    def armazenamento(self):
        return self.__armazenamento

    @armazenamento.setter
    def armazenamento(self, novoArmazenamento):
        self.__armazenamento = novoArmazenamento

    def country(self):
        return 'USA'

    @classmethod
    def laboratorio(cls):
        return cls.__LABORATORIO

    def __str__(self):
        return f'''
    Vacina {Janssen.__name__}, 
    Laboratório: {self.laboratorio()}, 
    Numero de Doses = {self.nDoses},
    Tecnologia: {self.tecnologia},
    Armazenamento: {self.armazenamento}'''

#---------------------------------------------------------------------------------------------------

class OMS:
  def __init__(self):
    self.__vdacinas = []

  def cadastrarVacina(self, vacina):
    self.__vacinas.append (vacina)

  @property
  def vacinas(self):
      return self.__vacinas

  def listarVacinasAprovadas(self):
    print('----------------------------------------------------------------------------------------------------')
    print('{:<10}{:<10}{:<10}{:<10}'.format('Vacina', 'Laboratorio', 'País', 'Tecnologia'))
    print('----------------------------------------------------------------------------------------------------')

    for vacin in self.vacinas:
        if vacin.aprovada == True:
            print('{:<10}{:<10}{:<10}{:<10}'.format(type(vacin).__name__, vacin.laboratorio(), vacin.country(), vacin.tecnologia()))

o = Oxford(2, 14, 'Vetor Viral (adenovirus)', 77)
o.aprovada = True
print(o)
print()

s = Sinovac(2,20, 'Virus inativado (morto)', 12000)
s.aprovada = True
print(s)
print()

j = Janssen(1,'Vetor Viral (adenovirus)','De 2 a 8 graus Celcius')
j.aprovada = True
print(j)

oms = OMS()
oms.cadastrarVacina(o)
oms.cadastrarVacina(s)
oms.cadastrarVacina(j)

print('\n\nListagem por polimorfismo')
print('--------------------------')
oms.listarVacinasAprovadas()