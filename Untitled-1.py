vars 
versao1= {"login", "registro", "perfil", "mensagens", "notificações",
"relatórios"}
versao2= {"login", "registro", "perfil", "pagamentos", "notificações", "ajuda",
"relatórios", "backup"}

apenas_lista1= len(versao1-versao2)
apenas_lista2= len(versao2-versao1)
interseção= len(versao1 & versao2)

print("Apenas versao 1:", apenas_lista1, "elementos")
print("Apenas versao 2:", apenas_lista2, "elementos")
print("intersecção",interseção, "elementos")