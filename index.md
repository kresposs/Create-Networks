## Cisco Meraki - Network creation in bulk mode - ITA 🍕

### Scopo
Creazione rapida delle Network all'interno di una Organization. <br>
Il file CSV preso in pasto dovrà contenere i seguenti campi: ```ORG_ID;NETWORK_NAME;NETWORK_DEVICEs_TYPE```

### Piccoli inconvenienti
Fra una richiesta API per la creazione di una Network e la successiva, sono necessari *almeno* 60 secondi di attesa. Da qui:<br>
```python 
time.sleep(60)
```
### Script per la modifica in maniera massiva delle VLAN
Ad oggi, per poter mandare in produzione delle Network in maniera rapida, ho *hardcodato* il VLAN tag e altro. Ovviamente aggiorno il tutto con molta calma e molta progettazione...

### Roadmap
- Creazione delle Network e possibile binding ad un template;
- Semplificazione del file CSV, escludendo l'hardcoding dell'Organization ID e di altri campi;
- Pulizia, pulizia, pulizia...
___

Il codice è banale, puoi leggerlo [qui](https://kresposs.github.io/Create-Networks/ "Meraki Automation").

