# TesteEverisOK

Em uma máquina com o ansible instalado: 

- Ter um host CentOS acessível na mesma rede
- Para baixar o arquivo: git clone https://github.com/GabrielSBrito/TesteEverisOK

- Acessar o arquivo "hosts" para configurar o host da mesma rede: vim CRUD/ansible/hosts 
- OBS: No Laboratório de teste, executei a playbook em um servidor CentOS7.
- Para configurar as variaveis de login,root,passwords do host onde vai aplicar as configs: vim CRUD/ansible/group_vars/servidores

- Para testar a conexão: ansible <nome_do_host configurado no arquivo hosts> -i hosts -m ping -u <nome_usuario>
- Acessar a papsta: cd CRUD/ansible/
- Executar o comando para iniciar o processo: ansible-playbook plabook.yml

- Diretório com vídeos mostrando o processo que eu executei: