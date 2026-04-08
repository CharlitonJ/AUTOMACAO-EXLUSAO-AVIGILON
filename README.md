# Automador de Exclusão de Câmeras em Massa

Este script foi desenvolvido para automatizar o processo de remoção ou limpeza de dispositivos em sistemas de monitoramento. Ele utiliza reconhecimento visual para identificar ícones de câmeras e acionar o comando de exclusão repetidamente até que não restem mais itens na tela.

## Funcionamento do Script

1. **Início Manual:** O programa aguarda o comando do usuário (Enter) para começar, garantindo controle sobre o momento da execução.
2. **Loop de Varredura:** O script entra em um laço de repetição contínuo (while) que busca por padrões visuais na tela.
3. **Fluxo de Ação:**
   - Localiza o ícone da câmera (`cam.png`).
   - Clica no ícone identificado.
   - Localiza e clica no botão de exclusão (`excluir.png`).
4. **Finalização Automática:** Quando o script não consegue mais encontrar as imagens na tela (ou seja, todas as câmeras visíveis foram excluídas), ele encerra o processo automaticamente.

## Pré-requisitos

É necessário ter o Python instalado e as seguintes bibliotecas:

```bash
pip install pyautogui pillow opencv-python
```
pyautogui: Para automação de cliques.

pillow (PIL): Para processamento de imagem.

opencv-python: Para garantir a precisão do parâmetro confidence.

##Arquivos de Imagem Necessários

Para o funcionamento correto, as seguintes imagens devem estar na pasta do script:

cam.png: Captura do ícone ou nome da câmera que deve ser selecionada.

excluir.png: Captura do botão, ícone de lixeira ou opção de exclusão.

## Instruções de Uso

Abra o software de monitoramento na tela onde as câmeras estão listadas.

Execute o script pelo terminal:

Bash
python nome_do_arquivo.py
Pressione Enter no terminal para iniciar.

Você terá 5 segundos para alternar para a janela do software.

O script clicará sistematicamente em cada câmera e no botão excluir até limpar a lista.

## Avisos e Segurança

Failsafe: Se precisar interromper o processo por qualquer motivo, mova o mouse rapidamente para um dos cantos da tela.

Ajuste de Confiança: O script está configurado com confidence=0.85 para a câmera e 0.9 para o botão excluir. Se ele estiver ignorando itens, você pode diminuir levemente esses valores no código.

Loop Infinito: O script só para quando não encontra mais as imagens. Certifique-se de que a janela de confirmação de exclusão (se houver) seja tratada ou que o botão excluir.png suma após o clique.
