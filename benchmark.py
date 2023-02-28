import subprocess
from settings import Manager
from elements import TextElements as text

class Benchmarker:

    def get_benchmarks(self, model, engine, batch, time, scenario):

        model = Manager.models[model]
        engine = Manager.engines[engine]
        
        cmd = [
            f"deepsparse.benchmark {model} \
            --engine {engine} \
            --batch_size {batch} \
            --time {time} \
            --scenario {scenario}"
        ]
        return subprocess.check_output(cmd, shell=True).decode("utf-8")
