import json
import numpy as np
import re
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Transform a mWebNLG json format into ControlPrefixes format')
    parser.add_argument('--input-json', type=str,
                        help='path to the dataset in mWebNLG json format')
    parser.add_argument('--output-path', type=str,
                        help='path to the output folder')
                        
    args = parser.parse_args()
    return args


def serialize_triple(triple):
    s = triple['subject'].replace("_", " ")
    p = re.sub("([a-z])([A-Z])","\g<1> \g<2>", triple['property'])
    o = str(triple['object']).replace("_", " ")
    return f"<H> {s} <R> {p} <T> {o}"


if __name__ == '__main__':
    args = parse_args()

    all_source = []
    all_target = []

    with open(args.input_json, 'r') as f:
        data = json.load(f)
        
        
    for entry in data['entries']:
        source = " ".join(list(map(lambda x: serialize_triple(x), entry['modifiedtripleset'])))
        #print(entry['lexicalisations'].keys())
        target = "default string" #entry['lexicalisations']['en'][0]['lex'].strip().replace('\n', ' ')
        all_source.append(source)
        all_target.append(target)
        
    with open(f"{args.output_path}/test_both.source", 'w') as f:
        for s in all_source:
            print(s, file=f)
        
    with open(f"{args.output_path}/test_both.target", 'w') as f:
        for s in all_target:
            print(s, file=f)
            
            

    blah = np.ones(len(all_source), dtype=int)

    with open(f"{args.output_path}/test_both.source.npy", 'wb') as f:
        np.save(f, blah)
        
    with open(f"{args.output_path}/test_both.source_cat.npy", 'wb') as f:
        np.save(f, blah)
