import json
from flask import Flask

app = Flask(__name__)


@app.route('/info', methods=['GET'])
def home():
    componente = "resourcemanager"
    desc = "gerencia recursos de / para servidores / clientes"
    ver = "0.1"
    out = {
        "componente": componente,
        "descricao": desc,
        "versao": ver
    }
    return json.dumps(out)


if __name__ == '__main__':
    print()
    app.run()
