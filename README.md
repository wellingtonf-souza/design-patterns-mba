## Sinergia entre Padrões
---

Analise abaixo dois trechos do documento de requisitos de um novo sistema inteligente de monitoramento de edifícios:

## Requisito Funcional:
Um novo empreendimento imobiliário está com intenção de desenvolver um sistema inteligente de monitoramento de elevadores. Você foi incumbido de projetar uma solução computacional que gerencia o controle de movimentação dos vários elevadores do edifício. Os elevadores são convencionais, podendo subir, descer e parar nos andares solicitados.

A inteligência do sistema está no fato de que o edifício deve monitorar o funcionamento dos elevadores para proporcionar mais segurança e também uma experiência de uso mais agradável para os moradores. As ações que o sistema pode tomar variam desde ações de segurança até mesmo a ações de entretenimento, como reprodução de músicas dentro do elevador.

Exemplos:
* Se um determinado elevador emperrar durante seu funcionamento, o sistema deve perceber e automaticamente invocar a equipe de manutenção e segurança. Enquanto isso uma música agradável pode começar a ser reproduzida naquele elevador específico para acalmar o usuário.
* Se um determinado elevador estiver em manutenção, o sistema pode, entre outras ações, interferir na velocidade de deslocamento dos outros elevadores.

## Requisitos Não-Funcionais:
* O código cliente que manipula os elevadores deve ser o mais inconsciente possível dos objetos concretos existentes
* Nesta primeira versão do sistema, um elevador nunca estará em dois estados ao mesmo tempo.
* Embora não haja limitação de memória na infraestrutura computacional usada, deve-se prezar para que não haja criação desnecessária de objetos em memória.

Entrega:

* Ao término da atividade deve ser submetido no ambiente de ensino um arquivo compactado, nomeado como esbd3-at2-<sobrenome>.zip, com o seguinte conteúdo:
* Trechos de código Java ou Python descrevendo as principais partes da solução. As principais partes são aquelas em que é possível observar como se dá a interação entre os padrões 
* Diagrama UML com as classes envolvidas na sinergia entre os padrões.