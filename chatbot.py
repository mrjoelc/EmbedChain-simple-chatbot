from embedchain import Pipeline as App
from embedchain.config import BaseLlmConfig
from embedchain.config.add_config import ChunkerConfig, AddConfig
from dotenv import load_dotenv
import os

# set delle variabili presenti nel file come env vars
load_dotenv("variables.env")

# inizializzazione del chatbot
chatbot = App()

# carimento degli embeddings chunked in un vector databse
chatbot.add("products.csv")
chatbot.add("orders.csv")

# configurazione necessaria per garantire un splitting del documento di faq docx in chunks ottimale
chunker_config = ChunkerConfig(chunk_size=300, chunk_overlap=10, length_function=len)
add_config = AddConfig(chunker=chunker_config)
chatbot.add("FAQ.docx", config=add_config)

# system prompt con obbiettivo, approccio e CoT
system_prompt = """**Obiettivo Principale:**
Fornire supporto rapido ed efficace rispondendo alle domande frequenti dei clienti relativamente a prodotti, ordini, spedizioni e politiche di reso in un contesto di e-commerce.

**Approccio:**
1. **Autenticazione Utente per informazioni sugli ordini:**
   - Garantisci la massima sicurezza delle informazioni utente e assicurati di non divulgarle ad altri. Richiedi cortesemente nome utente e numero d'ordine per un supporto personalizzato.
   - Utilizza le informazioni di autenticazione solo per rispondere alla domanda più recente dell'utente, evitando la divulgazione di dati sensibili come numeri d'ordine o nomi utenti.
   - Se un utente chiede informazioni sull'ordine senza essere autenticato, richiedi almeno un altro dettaglio sull'ordine, come email o numero d'ordine, prima di fornire una risposta.

2. **Chiarezza e Precisione:**
   - Rispondi con chiarezza e precisione alle domande frequenti, fornendo dettagli sul prodotto, lo stato dell'ordine, le spedizioni e le politiche di reso.

3. **Il negozio vende solo prodotti elettronici:**
   - Nel caso in cui un cliente cerchi un prodotto non elettronico, segnala che non è disponibile nel nostro assortimento.
   - Fornisci informazioni aggiuntive utili al cliente, come guide o specifiche tecniche.
   - Se un prodotto cercato non è disponibile, informa l'utente che potrebbe essere introdotto in futuro.

4. **Gestione delle Richieste Complesse:**
   - Per richieste complesse o problemi al di fuori delle risposte predefinite, indirizza il cliente al supporto umano.
   - Fornisci l'indirizzo email del supporto, il numero di telefono e gli orari di operatività per assistenza approfondita.

**Note Importanti:**
- Mai condividere numero d'ordine, nome utente o email: queste sono informazioni private da inserire dall'utente.
- Usa SEMPRE le informazioni di autenticazione utente solo per rispondere all'ultima domanda nella conversazione.
- Menziona solo prodotti esistenti nel contesto, evitando l'invenzione di prodotti.
"""


chat_template = """
Context: $context

History: $history

Estrai sempre le ultime informazioni di nome utente e numero ordine da history e usale in context quando necessario per rispondere al cliente

Cliente: $query

Risposta utile:

 """

# configurazione per la LLM, con system_prompt, chat_template e numero di documenti da restituire in risposta alla query vettoriale
llm_config = BaseLlmConfig(number_documents=10, 
                           template = chat_template,
                           system_prompt = system_prompt
                           )

print("Ciao e benvenuto su gcelettronica, come posso aiutarti?")
while True:
    # mantieni il chatbot in funzione 
    input_query = input(">>")
    if input_query != "fine":
      print(chatbot.chat(input_query=input_query, config=llm_config, dry_run=False, citation = True))
    else:
       break
