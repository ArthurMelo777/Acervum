## Histórico de Revisões

| Data | Versão | Descrição | Autores |
| --- | --- | --- | --- |
| 04/06/2023 | 1.0 | Versão inicial | Arthur Melo |

## 1. Objetivo do projeto

O objetivo do sistema é gerenciar o acervo bibliográfico pessoal de um usuário. Esse sistema permitirá o cadastro dos livros de um dado usuário. O sistema permitirá também o registro de empréstimos para contatos previamente cadastrados no sistema, bem como o registro da devolução dos mesmos.

## 2. Descrição do problema

| Problema | As pessoas precisam de um sistema que facilite a catalogação dos seus livros e o empréstimo de novos. |
| --- | --- |
| Afeta | Pessoas que têm o costume de ler ou que querem iniciar o hábito. |
| Impacta | Por não ter uma aplicação que facilite o gerenciamento de livros, as pessoas se sentem desmotivadas e acabam por não ler. |
| Solução | A proposta de solução é a criação de um sistema que permita o gerenciamento e empréstimo de livros. |

## 3. Descrição dos usuários

| Nome | Descrição | Responsabilidade |
| --- | --- | --- |
| Visitante | O visitante é o usuário que ainda não se cadastrou no site ou que não fez login | O visitante possui como responsabilidade realizar o login ou cadastrar-se. |
| Leitor | O leitor é o usuário que está logado e que poderá realizar todas as funções do site | O leitor possui como responsabilidade manter sua lista de livros atualizada e, caso pegue algum livro emprestado, devolvê-lo na data prevista. |

## 4. Descrição do ambiente dos usuários

Por ser uma aplicação web focada em desktops, o ambiente que os usuários utilizarão o sistema será em local com computador ou notebook. O sistema poderá ser usado a qualquer hora do dia, porém é mais comum que os usuários o utilizem durante o horário comercial para empréstimo e devolução, utilizando o fim de semana e feriados apenas para o cadastro dos próprios livros.

## 5. Principais necessidades dos usuários

Os usuários precisam de um sistema que permita o gerenciamento, empréstimo e devolução de livros. O sistema permitirá todas essas funções.

## 6. Alternativas concorrentes

Por manter um acervo pessoal ao mesmo tempo em que permite o empréstimo de livros, o sistema junta características de vários sistemas já existentes. Apesar disso, após pesquisa não foi possível achar uma aplicação que fizesse o que o Acervum se propõe a fazer.

## 7. Visão geral do produto

O sistema permitirá login e cadastro, além do cadastro de livros pessoais e contatos. O usuário também poderá registrar empréstimos e devoluções dos itens disponíveis e pesquisar os itens através do seu nome.

## 8. Requisitos funcionais

| Código | Nome | Descrição |
| --- | --- | --- |
| F01 | Login e cadastro de usuários. | A aplicação deve permitir o cadastro e login dos usuários interessados, os quais deverão fornecer nome, data de nascimento, email ou telefone, nome de usuário e senha. |
| F02 | Editar perfil do usuário. | A aplicação deve permitir ao usuário editar e desativar seu perfil do sistema. |
| F03 | Cadastro de livros pessoais. | A aplicação deve permitir o cadastro de livros pessoais do usuário.  |
| F04 | Realizar empréstimo de livro. | A aplicação deve permitir que o usuário cadastre o empréstimo de um livro. |
| F05 | Realizar devolução de livro. | A aplicação deve permitir que o usuário cadastre a devolução de um livro. |
| F06 | Pesquisar livros. | A aplicação deve permitir que o usuário pesquise por livros a partir de seu nome.  |

## 9. Requisitos não-funcionais

| Código | Nome | Descrição | Categoria | Classificação |
| --- | --- | --- | --- | --- |
| NF01 | Níveis de permissão | O usuário só poderá acessar certas funcionlidades a partir do seu nível no sistema  | Segurança | Obrigatória |

## 10. Casos de Uso

| Ator | Nome | Código | Prioridade |
| --- | --- | --- | --- |
| Visitante | Realizar cadastro | 001 | Alta |
| Visitante | Realizar login | 002 | Alta |
| Leitor | Editar perfil | 003 | Média |
| Leitor | Excluir perfil | 004 | Média |
| Leitor | Cadastrar livro | 005 | Alta |
| Leitor | Realizar empréstimo | 006 | Alta |
| Leitor | Realizar devolução | 007 | Alta |
| Leitor | Pesquisar livro | 008 | Alta |