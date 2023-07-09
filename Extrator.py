class ExtratorURL:
    def __init__(self, url):
        """Salva a url em um atributo do objeto (self.url = url) e verifica se a url é válida"""
        ...

    def sanitiza_url(self, url):
        """Retorna a url removendo espaços em branco."""
        ...

    def valida_url(self):
        """Valida se a url está vazia"""
        ...

    def get_url_base(self):
        """Retorna a base da url."""
        ...

    def get_url_parametros(self):
        """Retorna os parâmetros da url."""
        ...

    def get_valor_parametro(self, parametro_busca):
        """Retorna o valor do parametro `parametro_busca`."""

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)
