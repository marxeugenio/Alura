Utilizamos o comando with para gerenciar o contexto de utilização do arquivo. Além de arquivos, podemos utilizar o with para gerenciar processos que precisam de uma pré e pós condição de execução; por exemplo: abrir e fechar o arquivo, realizar conexão com o banco de dados, sockets, entre outros.

O objeto que está sendo manipulado pelo with precisa implementar dois métodos mágicos: __enter__() e __exit__().

O método __enter__() é executado logo no início da chamada da função e retorna uma representação do objeto que está sendo executada no contexto (ou context guard). Ao final, o método __exit__() é invocado, e o contexto da execução, finalizado.

Para saber um pouco mais sobre o statement, leia este post do blog preshing.com (em inglês).
