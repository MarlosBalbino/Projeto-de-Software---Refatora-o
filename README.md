# Projeto-de-Software_Refatorado

## Projeto de Software - 2021.1

O objetivo do projeto é construir um sistema de folha de pagamento. O sistema consiste do
gerenciamento de pagamentos dos empregados de uma empresa. Além disso, o sistema deve
gerenciar os dados destes empregados, a exemplo os cartões de pontos. Empregados devem receber
o salário no momento correto, usando o método que eles preferem, obedecendo várias taxas e
impostos deduzidos do salário.

## Funcionalidades Principais

1. Adição de um empregado.
2. Remoção de um empregado.
3. Lançar um carte de ponto.
4. Lançar Resultado de venda.   
5. Lançar uma taxa de serviço.
6. Alterar detalhes de um empregado.
7. Rodar a folha de pagamento para hoje.
8. Undo/Redo.
9. Agenda de pagamento.
10. Criação de novas agendas de pagamento.

## Padrões 

1. Command
    >- Padrão implementado para substituir
   > switch case das funcionalidades no menu principal.
   > Dentro do diretório 'commands' se encontram as
   > classes command que implementam a interface 
   > 'CommandInterface'. Um objeto invoker é instanciado
   > no módulo 'main.py' onde a opção desejada é passado como 
   > argumento no método 'run()' da classe 'Invoker', e 
   > associada à classe command correta.
   
2. Strategy
   >- Foi implementado a interface 'SalaryInterface' que contém o método
   > abstrato 'calculateSalary()' que será implementado nas classes 'Hourly',
   > 'Salaried' e 'Commissioned'.
   > Ao rodar a folha de pagamento, o método 'calculateSalary()' é 
   > invocado sobre o objeto employee (não importando qual tipo seja)
   > para calcular o salário bruto daquele empregado. Esse padrão foi
   > implementado em função de substituir os condicionais que verificam
   > o tipo daquele empregado.
   > Os módulos que contém a implementação citada são 'hourly.py',
   > 'salaried.py', 'commissioned.py' e 'SalaryInterface.py' no diretório
   > 'employee'. O padrão Strategy é implementado no módulo 'payRoll.py' no
   > diretório 'management'.

3. Template Method
   >- Este padrão é implementado em algumas partes do projeto,
   > mas aqui será citada a parte mais relevante:
   > Os métodos 'getData()' e '_repr()' foram retirados das subclasses 
   > 'Hourly', 'Salaried' e 'Commissioned', pois estavam duplicados, e
   > subidos para a superclasse Employee.
   
4. Expert
   >- Na classe 'Invoker' inicialmente foram criados dois métodos, um para
   > receber o comando e outro para executar. Mas tendo em vista que ambas
   > as tarefas poderiam ser executadas em um único método, o padrão Expert
   > foi implementado.

5. Introduce Null Object
   >- O módulo NoneObject, encontrado no diretório 'commands', implementa
   > a classe 'CommandInterface', para que caso um comando seja inválido 
   > o programa retorne ao menu principal sem fazer nem uma alteração ou
   > levantar exceção. Normalmente, nesse caso, seria retornado Null
   > (ou, no caso de python, None).
