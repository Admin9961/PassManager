Questo è un cross-platform password manager scritto interamente in Python.

*Come usarlo*

Ovviamente inizierete con l'installazione delle dipendenze, attraverso "pip install -r requirements.txt", che sono "zipfile" e "cryptography".

1. *main.py* è il cuore del programma. Digitate nei campi "username", "password" e "descrizione" i rispettivi valori. Descrizione server per ricordarvi a che servizio era associato il login (es. Google, login di Linux). Questo file accetta un solo paio di credenziali alla volta, e può sia cifrarle che decifrarle, sfruttando la chiave in "secret.key" per decifrare il contenuto dell'output "passwords.txt";
2. *encryptor.py* serve per criptare ulteriormente "passwords.txt" con una seconda password, e questo è un componente molto importante del tool, perché questa seconda password dovrete ricordarla a memoria, e riscriverla nel momento in cui si vorrà decriptarla.
3. *zipper.py* serve per zippare i file criptati in un archivio e ripulire i file temporanei. I file zippati dovranno essere poi riestratti manualmente, e per risalire alla passowrd originale, prima vanno decriptati attraverso "encryptor.py" e infine con "main.py".

4. Leggi bene le istruzioni sopra. Non mi riterrò responsabile qualora smarrirai una password in seguito ad un uso errato del PW manager. G00d luck
