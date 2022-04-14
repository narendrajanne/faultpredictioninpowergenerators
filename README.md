# faultpredictioninpowergenerators
Electric Fault Prediction of Power Generators in Cloud Computing

Electrical powers system is growing in size and complexity in all sectors such as generation, transmission, distribution and load systems. Types of faults like short circuit condition in power system network results in severe economic losses and reduces the reliability of the electrical system.
Electrical fault is an abnormal condition, caused by equipment failures such as transformers and rotating machines, human errors and environmental conditions. Theses faults cause interruption to electric flows, equipment damages.

File Description 
classData.csv:
This dataset contains to classify the types of fault.
Ia, Ib, Ic are current and Va, Vb, Vc are voltages in line A, line B, line C respectively.

G, C, B, A are Ground and fault at line C, B, and A respectively.

detect_dataset.csv

This dataset to detect faults in a power system.
Inputs - [Ia,Ib,Ic,Va,Vb,Vc] - Line Current and Voltage as inputs to Data Mining Algorithm  
Outputs - 0 (No-fault) or 1(Fault is present)


0 0 0 0 - No Fault

1 0 0 1 - LG fault (Between Phase A and Ground)

0 1 1 0 - LL fault (Between Phase B and Phase C)

1 0 1 1 - LLG Fault (Between Phases A, B, and ground)

0 1 1 1 - LLL Fault(Between all three phases)

1 1 1 1 - LLLG fault( Three phase symmetrical fault)
