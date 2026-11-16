# Need for Speed Carbon CE — ROG Ally / Bazzite

Integração 0.1.0 para executar **SpeedBreaker: Carbon v0.1.3**, uma recompilação nativa Linux da edição Xbox 360 USA Collector's Edition. Sem Proton ou emulador. Traga sua própria cópia do jogo.

Este repositório contém somente o launcher, o instalador e documentação próprios. Não inclui jogo, código recompilado do jogo, bibliotecas, saves ou artes. Projeto independente, sem afiliação com Electronic Arts, Microsoft ou os autores do SpeedBreaker.

## Instalação

Requer Linux x86-64 com AVX2, Vulkan e Python 3.11.8 ou superior. O Bazzite do Ally já oferece os componentes necessários; não são instalados pacotes no sistema.

Baixe `SpeedBreaker-Carbon-steamos-x86_64.tar.xz` da [release oficial v0.1.3](https://github.com/SpeedBreakerProject/speedbreaker-carbon/releases/tag/v0.1.3). O instalador confere seu SHA-256 e usa o instalador oficial para verificar todos os 78 arquivos da sua cópia USA Collector's Edition.

```bash
python3 tools/instalar.py --game "/caminho/ao/disco.iso" --runtime-archive "/caminho/SpeedBreaker-Carbon-steamos-x86_64.tar.xz"
```

`--game` também aceita uma pasta extraída com `default.xex`. O destino padrão é `~/Games/NFSCarbonCE`; use `--destination` para outro local. Um destino existente é recusado para preservar dados.

Adicione `jogar.sh` à biblioteca Steam como jogo externo. Deixe a compatibilidade forçada desativada. O script inicia o launcher oficial, que escolhe suas bibliotecas empacotadas sem alterar as do sistema. Não execute `lib/SpeedBreaker` diretamente.

## Controles

| Controle do Ally | Função |
|---|---|
| Analógico esquerdo | Direção |
| RT / LT | Acelerar / frear e ré |
| A | Confirmar nos menus; freio de mão na corrida |
| B | Voltar nos menus; nitro na corrida |
| X | Speedbreaker |
| Y | Acionar companheiro |
| LB / RB | Olhar para trás / câmera |
| Menu / Start | Pausa do jogo |
| View + Menu | Configurações do port, pausando a partida |

## Imagem e desempenho

Configuração inicial: tela cheia e renderização interna **1920×1080** (1.5x), limite de **60 FPS**, V-Sync interno desativado. No Ally testado, com limite de 60 FPS do Steam, o V-Sync interno fazia a apresentação cair para 30 apesar de o port registrar 60; desativá-lo recuperou os 60 FPS observados na corrida. A imagem mantém a proporção 16:9. Vídeos podem rodar a 30 FPS. A primeira passagem por uma cena pode preparar shaders; a campanha inteira não foi medida. A resolução pode ser alterada nas configurações do port.

## Saves

Modo portátil: configurações e saves ficam em `SpeedBreaker-Carbon/data/`; cache em `SpeedBreaker-Carbon/cache/`. O jogo mantém seu salvamento nativo. O launcher faz uma cópia dos arquivos de `data/save/` antes de abrir e após uma saída normal, em `backups/`. Encerramento forçado pode impedir o backup de saída; o save nativo permanece na pasta do port. As cópias não são apagadas automaticamente.

O backup não salva o carro no meio de uma corrida. Para transportar o progresso, feche o jogo e copie `SpeedBreaker-Carbon/data/save/` e `data/settings.toml`. Não importe saves de terceiros junto com um pacote do jogo.

## Fontes e validação

- [SpeedBreaker: Carbon](https://github.com/SpeedBreakerProject/speedbreaker-carbon), projeto de origem; suas licenças permanecem no pacote oficial.
- Runtime v0.1.3 SHA-256: `0ad165dafc0af5f8891ebd89e70c17a1b56ed70f412e6ac978af49e764bcc600`.
- [Validação no Ally](docs/VALIDACAO.md).

Somente os arquivos de `PUBLIC_FILES.txt` entram na release desta integração. Execute `python3 tools/publicar_pacote.py --check` antes de publicar. As artes da instalação particular permanecem privadas.
