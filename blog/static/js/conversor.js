var objeto = {
    "nome": "Farinha de trigo",
    "xicara" : 120,
    "colher de sopa" : 7,
    "colher de sobremesa": 5,
    "colher de cha": 3,
    "slug" : "farinha-de-trigo"
}

document.addEventListener("DOMContentLoaded", function(){
    let abas_conversor = document.getElementById('abas-conversor')
    let nova_aba = document.createElement('a')
    nova_aba.className = 'nav-link'
    nova_aba.innerHTML = objeto.nome
    nova_aba.href = '#'+objeto.slug
    nova_aba.setAttribute("aria-controls", objeto.slug)
    nova_aba.setAttribute("data-toggle", "pill")
    nova_aba.setAttribute("aria-select", "false")
    nova_aba.setAttribute("role", "tab")

    let conteudo_aba = document.getElementById('conteudo-aba')
    let novo_conteudo = document.createElement('div')
    novo_conteudo.innerHTML = 'aksjdflçasjdf'
    novo_conteudo.className = "tab-pane fade"
    novo_conteudo.id = objeto.slug
    novo_conteudo.role = 'tabpanel'
    novo_conteudo.setAttribute("aria-labelledby", objeto.slug)
    novo_conteudo.setAttribute("role", "tabpanel")

    abas_conversor.appendChild(nova_aba)
    conteudo_aba.appendChild(novo_conteudo)
})

