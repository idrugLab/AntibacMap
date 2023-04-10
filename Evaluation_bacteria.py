import argparse
import pandas as pd
from rdkit import Chem
import pickle
import deepchem as dc

def main():
    parser = argparse.ArgumentParser(description='Molecule prediction')
    parser.add_argument('--files', type=str, help='input file path')
    parser.add_argument('--system', type=str, help='system name')
    args = parser.parse_args()
    model_input = './models/target_models/' + args.system + '.pkl'

    # Load model
    with open(model_input, 'rb') as f:
        model = pickle.load(f)

    # Load data
    df = pd.read_csv(args.files)
    smis = df['canonical_smiles'].tolist()
    featurized_smi = []
    for smi in smis:
        mol = Chem.MolFromSmiles(smi)
        featurized_smi.append(dc.feat.CircularFingerprint(size=1024).featurize(mol))

    # Predict
    df_y = pd.DataFrame()
    for fp in featurized_smi:
        y = model.predict_proba(fp)
        df_y = df_y.append({'score': y[0][1]}, ignore_index=True)

    # Save results
    results = pd.DataFrame({'canonical_smiles': df['canonical_smiles'], 'score': df_y['score']})
    results.to_csv(args.system + '_result.csv', index=False)

if __name__ == '__main__':
    main()