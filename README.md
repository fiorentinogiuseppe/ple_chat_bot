# ple_chat_bot

* SQuAD2.0 tests the ability of a system to not only answer reading comprehension questions, but also abstain when presented with a question that cannot be answered based on the provided paragraph.

* https://github.com/ThilinaRajapakse/simpletransformers#question-answering
* https://simpletransformers.ai/docs/qa-data-formats/#train-data-format

## Exemplo de post https
* curl  --header "Content-Type: application/json"   --request POST   --data @./examples/example.json  https://127.0.0.1:5000/responde --insecure
## Exemplo de post http
* curl  --header "Content-Type: application/json"   --request POST   --data @./examples/example.json  http://127.0.0.1:5000/responde