# Validação — integração 0.1.0

- Runtime oficial SpeedBreaker: Carbon v0.1.3 Linux x86-64 conferido contra o SHA-256 da release.
- 78 arquivos do jogo comparados com o manifesto oficial; o verificador nativo confirmou todos os arquivos da edição USA.
- Inicialização pelo atalho Steam no ROG Ally com Bazzite. Os atalhos anteriores foram preservados.
- GPU AMD Ryzen Z1 Extreme / RADV PHOENIX selecionada; Vulkan e áudio inicializados.
- Janela e swapchain 1920×1080 fullscreen; renderização interna alterada para 1.5x (1920×1080) a pedido do usuário; limite configurado em 60 FPS.
- V-Sync interno desativado: a apresentação passou de 30 para 60 FPS, observados no contador do Steam durante a corrida. Limite do compositor Steam conferido em 60 FPS, tela em 120 Hz.
- Amostra de 30 segundos após o ajuste: 15 registros do port, média 59,55 FPS, mínimo 56,7 e máximo 60,0 por intervalo. Houve quadros isolados de até 116,7 ms; não é garantia de 60 FPS constantes em toda a campanha.
- Abertura, título e transição para o jogo observados por capturas reais.
- Usuário confirmou Menu/Start, A, analógico e gatilhos no controle físico.
- Pausa do jogo observada em corrida; menu de configurações do port usado para ajustar resolução e sincronização durante a sessão.
- Perfil nativo criado pelo usuário observado em `data/save/`; campanha completa e recuperação de saves avançados não verificadas.

Limites: a campanha completa, todas as pistas, split screen e a retomada de uma carreira avançada não foram testados. A versão upstream é 0.1.3; a versão 0.1.0 refere-se apenas a esta integração.
