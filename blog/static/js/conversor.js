document.addEventListener("DOMContentLoaded", function(){

    //dados que serao exibidos na tabela
    dados = [
        ["Farinha de trigo", 120, 7, 5, 3, "farinha-trigo"],
        ["Açucar cristal", 200, 10, 9, 4, "acucar-cristal"],
        ["Açúcar impalpável", 100, 6, 5, 3, "acucar-impalpavel"],
        ["Amido de milho", 125, 8, 6, 4, "amido-milho"],
        ["Cacau em pó", 85, 5, 4, 3, "cacau-po"],
        ["Chocolate em pó", 150, 10, 8, 7, "chocolate-po"],
        ["Manteiga", 200, 20, 18, 16, "manteiga"],
        ["Queijo ralado", 80, 5, 3, 1.5, "queijo-ralado"],
        ["Polvilho", 150, 9, 5, 3, "polvilho"],
        ["Azeite ou óleo", 180, 15, 12, 9, "azeite"],
        ["Fubá", 126, 7.5, 5, 2.5, "fuba"],
        ["Café", 80, 18, 13, 9, "cafe"],
        ["Coco ralado", 100, 7, 5, 2, "coco"],
        ["Mel", 300, 18, 12, 6, "mel"],
        ["Aveia", 80, 9, 3, 1.5 , "aveia"]
    ]

    //funçao para percorrer o vetor de dados e chamar demais funçoes
    dados.forEach(element => {
        let objeto = criaObjeto(element)
        insereAba(objeto.nome, objeto.slug)
        insereConteudo(objeto.slug, criaTabela(objeto))
    })

    //funçao para converter os dados do vetor em um objeto para facilitar a manipulaçao
    function criaObjeto(dados){
        let objeto = {
            "nome": dados[0],
            "xicara": ["1 xicara", dados[1]],
            "2xicara": ["1/2 xicara", dados[1]/2],
            "3xicara": ["1/3 xicara", dados[1]/3],
            "4xicara": ["1/4 xicara", dados[1]/4],
            "sopa": ["1 colher de sopa", dados[2]],
            "sobremesa": ["1 colher de sobremesa", dados[3]],
            "cha": ["1 colher de cha", dados[4]],
            "slug": dados[5]
        }

        return objeto
    }

    //funcao para criar abas de navegação
    function criaAba(nome, slug){
        let nova_aba = document.createElement('a')
        nova_aba.className = 'nav-link'
        nova_aba.innerHTML = nome
        nova_aba.href = '#'+slug
        nova_aba.setAttribute("aria-controls", slug)
        nova_aba.setAttribute("data-toggle", "pill")
        nova_aba.setAttribute("aria-select", "false")
        nova_aba.setAttribute("role", "tab")
        return nova_aba
    }

    //funcao para criar o elemento de conteudo de uma nova aba e inserir a tabela
    function criaConteudoAba(slug, tabela){
        let novo_conteudo = document.createElement('div')
        novo_conteudo.className = "tab-pane fade"
        novo_conteudo.id = slug
        novo_conteudo.role = 'tabpanel'
        novo_conteudo.setAttribute("aria-labelledby", slug)
        novo_conteudo.setAttribute("role", "tabpanel")
        novo_conteudo.appendChild(tabela)
        return novo_conteudo
    }

    //funçao que faz a criaçao da tabela e inserçao dos dados
    function criaTabela(objeto){
        let responsividade_tabela = document.createElement('div')
        responsividade_tabela.className = 'table-responsive'
        let tabela = document.createElement('table')
        responsividade_tabela.appendChild(tabela)
        tabela.className = 'table'
        let cabecalho = tabela.createTHead()
        let linha_cabecalho = cabecalho.insertRow()
        linha_cabecalho.appendChild(document.createElement('th')).innerText = objeto.nome
        
        let corpo = tabela.createTBody()
        for(var propriedade in objeto){
            if ( !(propriedade == "nome" || propriedade == "slug") ){
                linha_corpo = corpo.insertRow()
                dados_tabela = document.createElement('td')
                linha = linha_corpo.appendChild(dados_tabela)
                linha.innerHTML = objeto[propriedade][0]
                dados_tabela = document.createElement('td')
                linha = linha_corpo.appendChild(dados_tabela)
                linha.innerHTML = objeto[propriedade][1].toFixed(2) + " gramas"
            }  
        }

        return responsividade_tabela
        
    }
    
    //funcao para inserir a aba dentro do documento html 
    function insereAba(nome, slug){
        let abas_conversor = document.getElementById('abas-conversor')
        abas_conversor.appendChild(criaAba(nome, slug))
    }

    function insereConteudo(slug, tabela){
        let conteudo_aba = document.getElementById('conteudo-aba')
        conteudo_aba.appendChild(criaConteudoAba(slug, tabela))
    }
})

