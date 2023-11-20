# EmbedChain-simple-chatbot
A simple chatbot implemented with embedchain and openAI APIs 

Documentazione Chatbot con EmbedChain + ChatGPT

## Introduzione
Questo documento illustra quali sono i prerequisiti per poter installare ed utilizzare il chatbot, delle informazioni sul funzionamento del chatbot e alcuni esempi con domande e risposte. 
Prerequisiti

Assicurarsi di avere le seguenti risorse:
1.	Account OpenAI API: Ottenere un API Key da OpenAI per accedere ai servizi GPT. Tale chiave deve essere inserita tra doppi apici all’interno del file variables.env
2.	Ambiente di Sviluppo: Installare un ambiente di sviluppo Python, e in corrispondenza della cartella contenente i sorgenti del codice, creare e attivare il virtual enviroment tramite i seguenti comandi su una terminale (Windows):
    -	$python3 –m venv chat_bot_env 
  	- $.\chat_bot_env\Script\Activate.ps1
    - c.	$pip install –r req.txt


## Funzionamento del Chatbot
L'obiettivo principale è configurare il comportamento di ChatGPT3.5 come assistente garantendo un supporto rapido ed efficace per rispondere alle domande frequenti dei clienti relative a prodotti, ordini, spedizioni e politiche di reso, in un contesto di e-commerce.
Per implementare questa funzionalità, è stato adottato un approccio basato su un sistema RAG (Retrieval Augmented Generation) fornito tramite il framework EmbedChain. Questo sistema, basandosi sulla domanda dell'utente, effettua una ricerca nel database vettoriale precedentemente caricato. Durante questa ricerca, vengono estratti "chunks" di dati correlati alla query dell'utente. Queste informazioni fungono da contesto nelle interazioni con ChatGPT, consentendo al modello di generare risposte accurate, precise e contestualmente rilevanti.
Per funzionare il chatbot ha usa i seguenti files che rappresentano la knowledge-base:
-	products.csv: tabella in formato csv, che simula una tabella database, che contiene i prodotti elettronici disponibili sul sito web. Le colonne sono id_prodotto, nome_prodotto, produttore, quantita, descrizione, prezzo, tipo_prodotto.
-	orders.csv: tabella in formato csv, che simula una tabella database, che contiene gli ordini dei clienti. Le colonne sono numero_ordine, nome_utente, email, dettagli_ordine, stato_ordine, codice_tracciabilita, corriere, prezzo_totale.
-	FAQ.docx: un documento contenente un insieme di domande e risposte principalmente sulle politiche di reso dei prodotti.

Per avviare il chatbot è necessario aprire una finestra di terminale, recarsi sulla folder del chatbot, attivare il virtual enviroment come spiegato precedente ed infine eseguire il comando:
- $python3 chatbot.py

Aspettare qualche secondo e il chatbot sarà pronto a rispondere alle domande inserite.
