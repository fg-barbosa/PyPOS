E-Commerce & PDV Console Application

Uma aplicação modular em Python que simula o ecossistema completo de uma loja virtual (E-Commerce) e Frente de Caixa (PDV). O projeto adota boas práticas de arquitetura de software, separando completamente as interfaces do Cliente e do Gerente, utilizando o SQLite para persistência real de dados.

---

Estrutura do Projeto

O projeto foi desenhado seguindo o princípio de desacoplamento, garantindo que a lógica de banco de dados não fique misturada com a interface visual do usuário.

```
├── models/
│   └── produto.py             # Modelo/Classe que define a estrutura de um produto
├── services/
│   └── produtos_service.py    # O coração do sistema (Comandos SQL e conexão SQLite)
├── app_gerente.py             # Painel Administrativo (Cadastro de estoque e relatórios)
├── app_cliente.py             # Vitrine da Loja Virtual (Filtros, carrinho e checkout)
└── README.md                  # Documentação do projeto
