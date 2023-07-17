# TRABALHO BIG DATA
<img src="images/facens-logo.png" width="100"><br>
Trabalho desenvolvido para o módulo de Big Data do curso de especialização em Ciência de Dados do Centro Universitário Facens

#### Apache Hadoop
**1.1 Instalação**
- Baixar o `hadoop-3.3.6` e salvar o conteúdo em algum diretório local.
- Adicionar o diretório `<diretório local>/hadoop-3.3.6/bin` à variável de ambiente PATH. Para isso edite o arquivo `$HOME/.bash_profile` adicionando na última linha o comando a seguir:
> export PATH=$PATH:<diretório local>/hadoop-3.3.6/bin

**1.2 Configuração do core-site.xml**
- Abrir o arquivo `<diretório do hadoop>/etc/hadoop/core-site.xml`

Incluir a configuração do nome do namenode
```
<property>
  <name>fs.defaultFS</name>
  <value>hdfs://localhost:9000</value>
</property>
```
Configurar o local do diretório temporário
```
<property>
  <name>hadoop.tmp.dir</name>
  <value>/caminho/do/diretório/temporário</value>
</property>
```
Configurar o tamanho do bloco padrão do HDFS (em bytes)
```
<property>
  <name>dfs.blocksize</name>
  <value>134217728</value>
</property>
```
Configurar o diretório de armazenamento de dados em disco
```
<property>
  <name>dfs.datanode.data.dir</name>
  <value>/caminho/para/o/diretório/de/dados</value>
</property>
```

**1.3 Configuração do hdfs-site.xml**
- Abrir o arquivo `<diretório do hadoop>/etc/hadoop/hdfs-site.xml`

Configurar a quantidade de réplicas de dados
```
<property>
  <name>dfs.replication</name>
  <value>3</value>
</property>
```
Configurar o diretório de armazenamento do namenode
```
<property>
  <name>dfs.namenode.name.dir</name>
  <value>/path/to/namenode/directory</value>
</property>
```
Configurar o diretório de armazenamento do datanode
```
<property>
  <name>dfs.datanode.data.dir</name>
  <value>/path/to/datanode/directory</value>
</property>
```
Configurar o modo seguro do HDFS
```
<property>
  <name>dfs.permissions.enabled</name>
  <value>true</value>
</property>
```