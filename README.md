# Fotomosaico em python kkkkkkk

## Para gerar o caract.txt:

```
./caract.py base_fotos
```

## Para formatar as imagens (execute no diretorio onde estao os tiles):

```
./format
```

## Para executar o fotomosaico:

```
./photomosaic foto.jpg base_fotos caract.txt <R> <N>
```

Onde:
* **foto.jpg:** Foto base para o fotomosaico;
* **base_fotos:** Diretorio com os tiles;
* **caract.txt:** Arquivo com algumas caracteristicas dos tiles;
* **<R>:** Define se o photomosaic pode ou não ter regiões repetidas, ou seja com a mesma foto reduzida da base de fotos;
* **<N>:** Valor inteiro positivo que define como será feita a divisão da foto em sub-regiões para a criação do photomosaic.

### Nao esqueça de mudar as permissoes dos executaveis
