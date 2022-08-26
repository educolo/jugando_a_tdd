class Operacion:
	def __init__(self, primer_numero, segundo_numero):
		self.__primer_numero = primer_numero
		self.__segundo_numero = segundo_numero

	@property
	def primer_numero(self):
		return self.__primer_numero
	
	@property
	def segundo_numero(self):
		return self.__segundo_numero

	def ejecutar(self):
		raise Exception('implementalo wey, bien de pinga')
