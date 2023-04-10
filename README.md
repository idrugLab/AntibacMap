Usage of AntibacMap



## A. Configuration preparation:

​			1. rdkit

​			2. deepchem

​			3. sklearn

​			4. tensorflow



## B. Instructions:
​			1.The selection parameter of the file of molecules to be predicted, the file reference format is described in D part.
```
--files xx.csv
```
​			2.The selection parameter of the model to be predicted, select the model provided by this local application for prediction (target level such as Bacillus_anthracis_CHEMBL209, Escherichia_coli_CHEMBL1809; bacterial level such as Aeromonas_hydrophila, Bacillus_anthracis)
```
--files xx.csv
```

​			3. When using Evaluation_bacteria.py or Evaluation_target.py, you need to decompress models.7z

​			4. After the application is started, the corresponding scoring file will be automatically generated under the current path, in the format of csv.



## C. Examples:

​			1.Select a model at the target level:

```
	python Evaluation_target.py --files test.csv – system Bacillus_anthracis_CHEMBL209
```

​			2.Select a model at the bacterial level:

```
	python Evaluation_bacteria.py --files test.csv --system Bacillus_anthracis
```



## D. The format of the input file:

​			 1. The format of the input file should be csv.

​			 2. In the input file, the contents are as follows:

|canonical_smiles                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------|
| O=C1CC[C@]2([C@@H](CC[C@@]3([C@@H]2CC[C@@H]2[C@@H]4[C@@](CC[C@]23C)(CC[C@H]4C(C)=C)C(=O)[O-])C)C1(C)C)C                   |
| O=C1CC[C@]2([C@@H](CC[C@@]3([C@@H]2CC[C@@H]2[C@@H]4[C@@](CC[C@]23C)(CC[C@H]4C(C)=C)C(OCCCC[NH+](CC)CC)=O)C)C1(C)C)C       |
| O=C1CC[C@]2([C@@H](CC[C@@]3([C@@H]2CC[C@@H]2[C@@H]4[C@@](CC[C@]23C)(CC[C@H]4C(C)=C)C(OCCCC[NH+]2CCCC2)=O)C)C1(C)C)C       |
| O=C1CC[C@]2([C@@H](CC[C@@]3([C@@H]2CC[C@@H]2[C@@H]4[C@@](CC[C@]23C)(CC[C@H]4C(C)=C)C(OCCCC[NH+]2CCCCC2)=O)C)C1(C)C)C      |
| O1CC[NH+](CC1)CCCCOC(=O)[C@]12[C@@H]([C@H]3CC[C@H]4[C@](CC[C@@H]5[C@@]4(CCC(=O)C5(C)C)C)(C)[C@@]3(CC1)C)[C@@H](CC2)C(C)=C |
| O=C1CC[C@]2([C@@H](CC[C@@]3([C@@H]2CC[C@@H]2[C@@H]4[C@@](CC[C@]23C)(CC[C@H]4C(C)=C)C(OCCC[NH+](CC)CC)=O)C)C1(C)C)C        |
| O=C1CC[C@]2([C@@H](CC[C@@]3([C@@H]2CC[C@@H]2[C@@H]4[C@@](CC[C@]23C)(CC[C@H]4C(C)=C)C(OCCC[NH+]2CCCC2)=O)C)C1(C)C)C        |
| ……                                                                                                                        |

