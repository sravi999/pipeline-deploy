###Information like System Requirements,exposed pods and nodes in BSC.

Types of Nodes in Bsc    

Witness Nodes observe but do not participate in the consensus process. They serve to duplicate data and work as additional messengers in the network to serve up the current chain state.     
Validator Nodes on the other hand, do everything that Witness Nodes do, but they also are responsible for validating the transactions. In addition to the transaction validation, they also work to produce new blocks. You can imagine Validator Nodes as the counterpart to an Ethereum/Bitcoin "miner."     



System Requirements     

BSC Min System requirements(For both full node and validator node) :    
Click for reference:    
VPS running recent versions of Mac OS X or Linux.    

1T GB of free disk space, solid-state drive(SSD).    

8 cores of CPU and 32 gigabytes of memory (RAM).(12 cores and 48 GB in case of validator node)    

A broadband Internet connection with upload/download speeds of at least 5 megabyte per second    


BSC Suggested System requirements(For both full node and validator node) :    
Click for reference    
    
VPS running recent versions of Mac OS X or Linux.    

IMPORTANT 2T GB of free disk space, solid-state drive(SSD), gp3, 8k IOPS, 250MB/S throughput, read latency <1ms. (if start with snap/fast sync, it will need NVMe SSD)    

16 cores of CPU and 64 gigabytes of memory (RAM).    

Suggest m5zn.3xlarge instance type on AWS, c2-standard-16 on Google cloud.    
A broadband Internet connection with upload/download speeds of 5(10 in case of validator) megabyte per second    

Exposed Ports    

HTTP: 8545    
Websockets: 8546    

 
Steps to become a validator    

Who are validators and delegators?    
BSC validators are individuals and groups operating hardware nodes, powering the BSC network by processing transactions and signing blocks. They can be institutional, individual, or community-organized.    
There are two groups of validators: the validator candidates and the elected validators. Validator candidates are all validators that meet the minimum hardware requirements, run a local BSC full node, and self-stake a minimum of 10,000 BNB. Anyone who meets the criteria can become a validator candidate. Elected validators are the top 21 validator candidates with the highest total delegated BNB (self-stake + delegators’ stake) volume. The elected validators change every 24 hours.
Please note, different from other typical PoS/dPoS blockchains, the validators receive the reward in BNB, which is a purely deflationary token; its total supply decreases over time. See the BNB burn schedule for more info.    
The BSC also supports the role of delegators. Delegators are users who stake their BNB via Binance Chain Wallet to support their preferred validator and help the validator achieve the required minimum stake to participate in the validator elections.    
In return for their participation, validators receive rewards in transaction fees from the processed network activity. The delegates receive interest on their BNB (share of validator earnings based on the individual stake) paid in BNB.    
