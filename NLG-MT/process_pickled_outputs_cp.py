import pickle
import io
import torch

class CPU_Unpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == 'torch.storage' and name == '_load_from_bytes':
            return lambda b: torch.load(io.BytesIO(b), map_location='cpu')
        else:
            return super().find_class(module, name)
            
            
with open("outputs_all_testsets.pkl", 'rb') as f:
    outputs = CPU_Unpickler(f).load()
    

with open("predictions.txt", 'w') as fp, open("gold.txt", 'w') as fg:    
    for batch in outputs:
        print(*batch['preds'], sep='\n', file=fp)
        print(*batch['target'], sep='\n', file=fg)
