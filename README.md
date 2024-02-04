# Pokemon Card Base Set Finder UK

This script simply finds available in Pokemon card collectible base set stock purchase in the UK

## Requirements

- Python 3.12
- Pipenv

## Installation Dependencies

```shell
python -m pipenv install
```

## Run

```shell
python ./main
```

To show out of stock items use flag `--show-out-of-stock`

## Example output

```shell
Starting to check BigOrbitCards...


Checking url https://www.bigorbitcards.co.uk/pokemon/base-set/page-1/?resultsPerPage=24/...

Alakazam (Holo) (Unlimited Edition): ['Light Play ~ 2 in Stock ~ £27.95']
Blastoise (Holo) (Unlimited Edition): ['Light Play ~ 1 in Stock ~ £99.95', 'Moderate Play ~ 2 in Stock ~ £71.95', 'Heavy Play ~ 2 in Stock ~ £41.95']
Chansey (Holo) (Unlimited Edition): ['Moderate Play ~ 1 in Stock ~ £11.95', 'Heavy Play ~ 1 in Stock ~ £6.95']
Charizard (Holo) (Unlimited Edition): ['Light Play ~ 2 in Stock ~ £249.95', 'Moderate Play ~ 5 in Stock ~ £179.95', 'Heavy Play ~ 1 in Stock ~ £104.95']
Gyarados (Holo) (Unlimited Edition): ['Light Play ~ 1 in Stock ~ £16.95', 'Moderate Play ~ 1 in Stock ~ £11.95', 'Heavy Play ~ 1 in Stock ~ £6.95']

Checking url https://www.bigorbitcards.co.uk/pokemon/base-set/page-2/?resultsPerPage=24/...

Machamp (Holo) (1st Edition): ['Moderate Play ~ 1 in Stock ~ £7.75']
Magneton (Holo) (Base Set 2000): ['Light Play ~ 1 in Stock ~ £13.45']
Magneton (Holo) (Unlimited Edition): ['Moderate Play ~ 1 in Stock ~ £11.95']
Mewtwo (Holo) (Unlimited Edition): ['Light Play ~ 1 in Stock ~ £12.75', 'Heavy Play ~ 1 in Stock ~ £5.25']
Nidoking (Holo) (Unlimited Edition): ['Moderate Play ~ 2 in Stock ~ £13.75']
Ninetales (Holo) (Unlimited Edition): ['Light Play ~ 2 in Stock ~ £16.95', 'Moderate Play ~ 1 in Stock ~ £11.95']
```
