import Algorithmia


def pesquisar(topic, author):
    language = 'pt'
    # Connecta na API da Algorithimia e "Baixa" texto da Wikipedia
    algorithimiainput = {
        "articleName": topic,
        "lang": language
    }
    apikeyfile = open("algorithmia.txt", "r")
    apikey = apikeyfile.read()
    client = Algorithmia.client(apikey)
    algo = client.algo('web/WikipediaParser/0.1.2')
    text = algo.pipe(algorithimiainput).result
    titulo = text["title"]
    resumo = text["summary"]
    referencias = text["references"]
    imagens = text["images"]
    link = text["url"]
    authortitulo = str(author)+str(titulo)
    filetext = open(authortitulo+"Resuminho.txt", "a+", encoding="utf-8")
    filetext.write("\n===================================")
    filetext.write(f"\n-- Assunto: {titulo}")
    filetext.write(f"\n\n Resumo: {resumo}")
    filetext.write(f"\n\n Referencias: {referencias}")
    filetext.write(f"\n\n Imagens: {imagens}")
    filetext.write(f"\n\n Link da Wikipedia {link}")
    filetext.write("\n===================================")
    filetext.write("\nLucas Agradece por ter usado bot")
    filetext.write("\nPor mais detalhes: http://lucasmellolm.github.io/")
    filetext.write("\n===================================")
    filetext.close()

    return text
