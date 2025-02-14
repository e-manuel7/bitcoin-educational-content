---
name: Privacy on Bitcoin
goal: Understand and master the principles of privacy protection when using Bitcoin
objectives: 

  - Define the theoretical concepts needed to understand the stakes of privacy protection
  - Know how to identify and mitigate risks associated with loss of user privacy on Bitcoin
  - Using methods and tools to protect your privacy on Bitcoin
  - Understand chain analysis methods and develop defense strategies

---
# Protect your privacy on bitcoin

In a world where privacy of financial transactions is gradually becoming a luxury, understanding and mastering the principles of privacy protection in your use of Bitcoin is essential. This training provides you with all the keys, both theoretical and practical, to achieve this goal on your own.

Today, on Bitcoin, there are companies that specialize in chain analysis. Their core business is precisely to intrude into your privacy in order to compromise the confidentiality of your transactions. In fact, the "right to privacy" on Bitcoin does not exist. It is therefore up to you, the user, to assert your natural rights and protect the confidentiality of your transactions, because no one else will do it for you.

This training is presented as a comprehensive, generalist course. Every technical notion is detailed and supported by explanatory diagrams. The goal is to make knowledge accessible to everyone. BTC204 is therefore accessible for beginner and intermediate users. This training also offers added value to more experienced bitcoiners, as we delve into some often unfamiliar technical concepts.

Join us to transform your use of Bitcoin and become an informed user, able to understand the issues surrounding confidentiality and protect your privacy.

+++
# Introduction

<partId>e17474a8-8899-4bdb-a7f8-bc52ddb01440</partId>

## Introduction to Training

<chapterId>08ba1933-f393-4fb5-8279-777d874caedb</chapterId>

In a world where privacy of financial transactions is gradually becoming a luxury, understanding and mastering the principles of privacy protection in your use of Bitcoin is essential. This training provides you with all the keys, both theoretical and practical, to achieve this goal on your own.

Today, in the Bitcoin ecosystem, there are companies that specialize in blockchain analysis. Their core business is precisely to intrude into your privacy, compromising the confidentiality of your transactions. In fact, the "right to privacy" on Bitcoin does not exist. It is therefore up to you, the user, to assert your natural rights and protect the confidentiality of your transactions, because no one else will do it for you.

Bitcoin is not only there for "Number Go Up" and the preservation of the value of savings. Due to its unique features and history, it is primarily the tool of the alternative economy. Thanks to this remarkable invention, you can freely manage your money, spend it and accumulate it, without anyone being able to stop you.

Bitcoin offers a peaceful escape from the yoke of states, allowing you to fully enjoy your natural rights, which cannot be challenged by established laws. Thanks to Satoshi Nakamoto's invention, you have the power to enforce your right to private property and regain your freedom to contract.

However, Bitcoin is not anonymous by default, which may pose a risk to individuals engaged in the alternative economy, especially in regions under despotic regimes. But this is not the only danger. Because bitcoin is a valuable and uncensored asset, it could attract the attention of thieves. Therefore, protecting your privacy also becomes a security issue: it can help you prevent cyber attacks and physical assaults.

As we will see, although the protocol offers certain inherent privacy protections, it is crucial to use additional tools to optimize and defend this privacy. This course is designed as a comprehensive, generalist path to understanding privacy issues on Bitcoin. Each technical notion is discussed in detail and supported by explanatory diagrams. The goal is to make the knowledge accessible to everyone, including beginner and intermediate users. For more experienced bitcoiners, we also cover very technical and sometimes lesser-known concepts during this course to deepen understanding of each topic.

The goal of this course is not to make you completely anonymous in your use of Bitcoin, but rather to provide you with the essential tools to know how to protect your privacy according to your personal goals. You will have the freedom to choose from the concepts and tools presented to develop your own strategies, tailored to your specific goals and needs.

### Section 1: Definitions and Key Concepts

To begin, we will look together at the fundamentals that govern how Bitcoin works, and then calmly approach privacy-related notions. It is essential to master some basic concepts, such as UTXOs, receiving addresses or scripts, before we can fully grasp the concepts we will address in the following sections. We will also introduce the general privacy model of Bitcoin, as envisioned by Satoshi Nakamoto, which will allow us to grasp the issues and associated risks.

![BTC204](assets/it/11/1.webp)

### Section 2: Understanding Chain Analysis and How to Protect Yourself

In the second section, we study the techniques used by blockchain analytics companies to track your activity on Bitcoin. Understanding these methods is critical to improving the protection of your privacy. This part aims to examine attackers' strategies to better understand the risks and lay the groundwork for the techniques we will study in subsequent sections. We will analyze transaction patterns, internal and external heuristics, as well as plausible interpretations of these patterns. In addition to a theoretical component, we will learn how to use a block explorer to perform chain analysis through practical examples and exercises.

![BTC204](assets/fr/002.webp)

### Section 3: Mastery of Best Practices to Protect Your Privacy

In the third section of our course, we get to the heart of the matter: practice! The goal is to master all the essential best practices that should become natural reflexes for any Bitcoin user. We will cover the use of fresh addresses, labeling, consolidation, the use of full nodes, as well as KYC and acquisition methods. The goal is to provide you with a comprehensive overview of the pitfalls to avoid in order to establish a solid foundation in our quest for privacy protection. For some of these practices, you will be guided to a specific tutorial to implement them.

![BTC204](assets/it/11/3.webp)

### Section 4: Understanding Coinjoin Transactions

How can we talk about bitcoin privacy without discussing coinjoin? In section 4, you will find out everything you need to know about this method of mixing. You will learn what a coinjoin is, its history and goals, as well as the different types of coinjoins that exist. Finally, for more experienced users, we will find out what anonsets and entropy are, and how to calculate these indicators.

![BTC204](assets/it/11/4.webp)

### Section 5: Understanding the Issues of Other Advanced Privacy Techniques

In the fifth section, we will provide an overview of all the other existing techniques for protecting your privacy on Bitcoin besides coinjoin. Over the years, developers have shown considerable creativity in designing tools dedicated to privacy. We will examine all of these methods, such as payjoin, collaborative transactions, Coin Swap and Atomic Swap, detailing how they work, their goals and potential weaknesses.

We will also address privacy at the node network level and transaction diffusion. We will also discuss the various protocols that have been proposed over the years to improve user privacy on Bitcoin, including static address protocols.

![BTC204](assets/fr/005.webp)

# Definitions and Key Concepts

<partId>b9bbbde3-34c0-4851-83e8-e2ffb029cf31</partId>

## The UTXO Model of Bitcoin

<chapterId>8d6b50c5-bf74-44f4-922b-25204991cb75</chapterId>

Bitcoin is primarily a currency, but do you know concretely how BTC is represented in the protocol?

### UTXOs of Bitcoin: What Are They?

In the Bitcoin protocol, the management of monetary units is based on the UTXO model, which stands for "_Unspent Transaction Output_."

This model is profoundly different from traditional banking systems, which rely on an account and balance mechanism to track financial flows. In fact, in the banking system, individual balances are maintained in accounts linked to an identity. For example, when you buy a baguette from a baker, your bank simply debits the amount of the purchase from your account, thus reducing your balance, while the baker's account is credited with the same amount, increasing its balance. In this system, there is no notion of a link between the money coming into your account and the money going out of it, other than transaction records.

On Bitcoin, things work differently. The concept of an account does not exist, and monetary units are managed not through balances but through UTXOs. A UTXO represents a specific amount of bitcoin that has not yet been spent, thus forming a `piece of bitcoin,' which can be large or small. For example, a UTXO could be worth `500 BTC` or only `700 SATS`.

**> Reminder:** The satoshi, often shortened to sat, is the smallest unit of Bitcoin, comparable to a penny in fiat currencies.

```plaintext
1 BTC = 100,000,000 SATS
```

Theoretically, a UTXO can represent any value in bitcoin, ranging from a sat up to the theoretical maximum of about 21 million BTC. However, it is logically impossible to own all 21 million bitcoins, and there is a lower economic threshold called "dust," below which a UTXO is considered economically uneconomic to spend.

**>Did you know?** The largest UTXO ever created on Bitcoin had a value of `500,000 BTC`. It was created by the MtGox platform during a consolidation operation in November 2011: [29a3efd3ef04f9153d47a990bd7b048a4b2d213daaa5fb8ed670fb85f13bdbcf](https://mempool.space/fr/tx/29a3efd3ef04f9153d47a990bd7b048a4b2d213daaa5fb8ed670fb85f13bdbcf)

### UTXO and Spending Conditions

UTXOs are the tools of exchange on Bitcoin. Each transaction involves the consumption of UTXOs as inputs and the creation of new UTXOs as outputs. When a transaction is made, the UTXOs used as inputs are considered "spent," and new UTXOs are generated and assigned to the recipients indicated in the transaction's outputs. Thus, a UTXO simply represents an unspent transaction output, and thus an amount of bitcoin belonging to a user at a given time.

![BTC204](assets/it/21/2.webp)

All UTXOs are protected by scripts that define the conditions under which they can be spent. To consume a UTXO, a user must demonstrate to the network that he or she meets the conditions set by the script protecting that UTXO. Generally, UTXOs are protected by a public key (or a receiving address representing this public key). To expend a UTXO associated with this public key, the user must prove that he or she holds the corresponding private key by providing a digital signature made with this key. This is why it is said that your bitcoin wallet does not actually contain bitcoins, but rather holds your private keys, which in turn give you access to your UTXOs and, by extension, the bitcoins they represent.

![BTC204](assets/it/21/3.webp)

Since the concept of an account is absent in Bitcoin, the balance of a wallet is simply the sum of the values of all the UTXOs it can spend. For example, if your Bitcoin wallet can spend the following 4 UTXOs:

```plaintext
- 2 BTC
- 8 BTC
- 5 BTC
- 2 BTC
```

The total balance of your wallet would be `17 BTC`.

![BTC204](assets/it/21/4.webp)

## The structure of Bitcoin transactions

<chapterId>29d3aaab-de2e-4746-ab40-c9748898850c</chapterId>

### The inputs and outputs of a transaction

A bitcoin transaction is a transaction recorded on the blockchain that enables the transfer of ownership of bitcoins from one person to another. More specifically, because we are in a UTXO model and there are no accounts, the transaction satisfies the spending conditions that protected one or more UTXOs, consumes them and, equivalently, creates new UTXOs equipped with new spending conditions. In short, a transaction moves bitcoins from a script that is satisfied to a new script intended to protect them.

![BTC204](assets/it/22/1.webp)

Each Bitcoin transaction is thus composed of one or more inputs and one or more outputs. The inputs are UTXOs consumed by the transaction to generate the outputs. The outputs are new UTXOs that will be usable as inputs for future transactions.

![BTC204](assets/it/22/2.webp)

**> Did you know?** Theoretically, a bitcoin transaction could have an infinite number of inputs and outputs. Only the maximum block size limits this number. Each input in a bitcoin transaction refers to a previous unspent UTXO (Unspent Transaction Output). To use a UTXO as an input, its holder must prove that it is the rightful owner by validating the script associated with it, i.e., satisfying the imposed spending condition. Generally, this involves providing a digital signature produced with the private key corresponding to the public key that initially secured that UTXO. The script then verifies that the signature matches the public key used when receiving the funds.

Each output, on the other hand, specifies the amount of bitcoin to be transferred, as well as the recipient. The latter is defined by a new script that generally locks the newly created UTXO with a receiving address or a new public key.

For a transaction to be considered valid according to the consensus rules, the total outputs must be less than or equal to the total inputs. In other words, the sum of new UTXOs generated by the transaction must not exceed the sum of UTXOs consumed as inputs. This principle is logical: if you only have an amount of `500,000 SATS`, you cannot make a purchase of `700,000 SATS`.

### Exchange and Consolidation in a Bitcoin Transaction

The action of a Bitcoin transaction on UTXOs can thus be compared to the melting of a gold coin. In fact, a UTXO is not divisible, but only unified. This means that a user cannot simply divide a UTXO representing a certain amount of bitcoin into several smaller UTXOs. He must consume it entirely in a transaction to create one or more new UTXOs of arbitrary values in the outputs, which must be less than or equal to the initial value.

This mechanism is similar to that of a gold coin. Imagine you own a 2-ounce coin and want to make a payment of 1 ounce, assuming the seller cannot give you change. You would have to melt your coin and mint 2 new coins of 1 ounce each.

On bitcoin, the operation is similar. Suppose Alice has a UTXO of `10,000 SATS` and wants to buy a baguette that costs `4,000 SATS`. Alice will perform a transaction with an input of 1 UTXO of `10,000 SATS` which she will consume entirely, and in the outputs, she will create 2 UTXOs valued `4,000 SATS` and `6,000 SATS`. The UTXO of `4,000 SATS` will be sent to the baker as payment for the baguette, while the UTXO of `6,000 SATS` will return to Alice as change. This UTXO that returns to the initial sender of the transaction is what is called "change" in Bitcoin jargon.

Now imagine that Alice does not have a single UTXO of `10,000 SATS`, but rather two UTXOs of `3,000 SATS` each. In this situation, none of the individual UTXOs is sufficient to cover the `4,000 SATS` for the baguette. Therefore, Alice must use both UTXOs of `3,000 SATS` as inputs for her transaction simultaneously. In this way, the total input will reach `6,000 SATS`, allowing her to cover the payment of `4,000 SATS` to the baker. This method, which involves grouping several UTXOs into the inputs of a transaction, is often referred to as `consolidation.

### Transaction Fees

Intuitively, one might think that transaction fees also represent an output of a transaction. But in reality, this is not the case. Transaction fees represent the difference between total inputs and total outputs. This means that after using part of the value of the inputs to cover the desired outputs in a transaction, a certain sum of the inputs remains unused. This remaining sum constitutes transaction fees.

```plaintext
Commissioni = input totali - output totali
```

Let us return to the example of Alice who has a UTXO of `10,000 SATS` and wants to buy a baguette for `4,000 SATS`. Alice creates a transaction with her UTXO of `10,000 SATS` as input. She then generates an output of `4,000 SATS` intended for the baker to pay for the baguette. To encourage the miners to include her transaction in a block, Alice assigns `200 SATS` as commission. In doing so, she creates a second output, the remainder, which will be returned to her, amounting to `5,800 SATS`.

Applying the commission formula, we actually see that there are `200 SATS` left for the miners:

```plaintext
Commissioni = input totali - output totali
Spese = 10.000 - (4.000 + 5.800)
Spese = 10.000 - 9.800
Spese = 200
```

When a miner successfully validates a block, they are entitled to collect these fees for all transactions included in their block, through what is known as a "coinbase" transaction.

### The Creation of UTXO on Bitcoin

If you have followed the previous paragraphs carefully, you now know that UTXOs can only be created by consuming other existing UTXOs. Thus, coins on Bitcoin form a continuous chain. However, you might wonder how the first UTXOs appeared in this chain. This raises a problem similar to that of the chicken and the egg: where did these original UTXOs come from?

The answer lies in the **coinbase transaction**.

Coinbase is a specific type of Bitcoin transaction, unique to each block and always the first in them. It allows the miner who has found a valid proof of work to receive their block reward. This reward consists of two elements: **the block grant** and **transaction fees** discussed in the previous part.

The unique feature of the coinbase transaction is that it is the only one that can create bitcoins from nothing, without the need to consume inputs to generate its outputs. These newly created bitcoins constitute what might be called the "original UTXOs."

Bitcoins from the block grant are new BTC created out of thin air, following a predefined issuance schedule in consensus rules. The block grant is halved every 210,000 blocks, about every four years, in a process called "halving." Initially, 50 bitcoins were created per subsidy, but this amount has gradually decreased; currently, it is 3,125 bitcoins per block.

As for the transaction fees part, although it represents newly created BTC, they must not exceed the difference between the total inputs and outputs of all transactions in a block. We saw earlier that these fees represent the part of the inputs that is not used in the outputs of the transactions. This part is technically "lost" during the transaction, and the miner has the right to recreate this value in the form of one or more new UTXOs. It is, therefore, a transfer of value from the sender of the transaction to the miner who adds it to the blockchain.

**> Did you know?** Bitcoins generated from a coinbase transaction are subject to a 100-block maturation period during which they cannot be spent by the miner. This rule is intended to avoid complications associated with the use of newly created bitcoins on a chain that may later be rendered obsolete.

### The implications of the UTXO model

First, the UTXO model directly affects transaction fees in Bitcoin. Because the capacity of each block is limited, miners favor transactions that offer the best fees relative to the space they will occupy in the block. In fact, the more UTXO a transaction includes as input and output, the heavier it is and, therefore, requires higher fees. This is one of the reasons why there is often an effort to reduce the number of UTXOs in our portfolio, which can also affect privacy, a topic we will explore in detail in the third part of this training.

Next, as mentioned in the previous parts, coins on Bitcoin are essentially a chain of UTXOs. Each transaction thus creates a link between a past UTXO and a future UTXO. UTXOs thus allow explicit tracking of the path of bitcoins from their creation to their current spending. This transparency can be viewed positively, as it allows each user to ensure the authenticity of bitcoins received. However, it is also on this principle of traceability and auditability that chain analysis is based, a practice designed to compromise your privacy. We will study this practice in depth in the second part of the training.

## Bitcoin's privacy model

<chapterId>769d8963-3ed5-4094-b21d-9203c7d9e465</chapterId>

### Currency: Authenticity, Integrity and Double Spending

One of the functions of currency is to solve the problem of double coincidence of wants. In a barter-based system, making an exchange requires not only finding an individual who offers a good that satisfies my need, but also providing them with a good of equivalent value that satisfies their need. Finding this balance proves complex.

This is why currency is used, which enables the transfer of value in both space and time.

For currency to solve this problem, it is essential that the party providing a good or service be convinced of its ability to spend that amount later. Therefore, any rational individual who wishes to accept a form of currency, whether digital or physical, will ensure that it meets two basic criteria:


- The coin must be intact and authentic;**- **and must not be spent twice.**

When using physical currency, the first characteristic is the most complex to assert. Throughout different historical periods, the integrity of metal coins has often been compromised by practices such as cutting or punching. For example, during ancient Rome, it was common for citizens to scrape the edges of gold coins to collect some of the precious metal, while preserving them for future transactions. The intrinsic value of the coin was thus reduced, but its face value remained the same. This is remarkably the reason why later stripes were coined on the edge of coins.

Authenticity is also a difficult characteristic to verify by physical monetary means. Today, techniques to combat counterfeiting are increasingly complex, forcing merchants to invest in expensive verification systems.

On the other hand, because of their nature, double payment is not a problem for physical currencies. If I give you a €10 note, it irrevocably leaves my possession to enter yours, of course excluding any possibility of spending the same monetary units multiple times. In short, I will not be able to spend that €10 note again.

For digital currency, the difficulty is different. Ensuring the authenticity and integrity of a coin is often easier. As we saw in the previous section, Bitcoin's UTXO model allows a coin to be traced back to its origin, thus verifying that it was indeed created in accordance with consensus rules by a miner.

However, ensuring the absence of double payment is more complex, as any digital good is essentially information. Unlike physical goods, information does not divide during exchanges but propagates by multiplying. For example, if I email you a document, it is duplicated. For your part, you cannot verify with certainty that I have deleted the original document.

### Preventing Double Payment on Bitcoin

The only way to avoid duplication of a digital asset is to be aware of all exchanges within the system. That way, you can know who owns what and update everyone's ownership based on the transactions made. This is what is done, for example, with scriptural money in the banking system. When you pay €10 to a merchant with a credit card, the bank records this exchange and updates the ledger.

On Bitcoin, double payment prevention is accomplished in the same way. The goal is to confirm the absence of a transaction that has already spent the coins in question. If these coins have never been used, then we can be sure that no double payment will occur. This principle was described by Satoshi Nakamoto in the White Paper with this famous sentence:

**"_The only way to confirm the absence of a transaction is to be aware of all transactions._"**

However, unlike the banking model, there is no desire to have to trust a central entity on Bitcoin. It is necessary for all users to be able to confirm this absence of double payment, without relying on a third party. Therefore, everyone needs to be aware of all Bitcoin transactions. This is why Bitcoin transactions are publicly broadcast on all nodes of the network and recorded in plain text on the blockchain.

It is precisely this public dissemination of information that complicates privacy protection on Bitcoin. In the traditional banking system, in theory, only the financial institution is aware of the transactions made. On the other hand, on Bitcoin, all users are informed of all transactions, via their respective nodes.

### The privacy model: banking system vs. Bitcoin

In the traditional system, your bank account is linked to your identity. The banker is able to know which customer belongs to which bank account and what transactions are associated with it. However, this flow of information is interrupted between the bank and the public domain. In other words, it is impossible to know the balance and transactions of a bank account that belongs to another person. Only the bank has access to this information.

For example, your banker knows that you buy your baguette every morning at the neighborhood bakery, but your neighbor is unaware of this transaction. Thus, the flow of information is accessible to interested parties, particularly the bank, but remains inaccessible to outsiders.

Because of the constraint of public dissemination of transactions that we saw in the previous part, Bitcoin's privacy model cannot follow the model of the banking system. In the case of Bitcoin, because the flow of information cannot be interrupted between the transactions and the public domain, **the privacy model is based on the separation between the identity of the user and the transactions** themselves.

For example, if you buy a baguette from the baker paying in BTC, your neighbor, who owns his own full node, can see your transaction take place, just as he can see all other transactions in the system. However, if privacy principles are respected, they should not be able to link this specific transaction to your identity.

But because Bitcoin transactions are made public, it still becomes possible to establish links between them to infer information about the parties involved. This activity even constitutes a specialty in itself called "chain analysis." In the next part of the course, I invite you to explore the fundamentals of chain analysis to understand how your bitcoins are being tracked and know how to better defend yourself.

# Understanding Chain Analysis and How to Protect Yourself

<partId>4739371e-9fef-45b0-bcaa-b7a4df6b4470</partId>

## What is Chain Analysis on Bitcoin?

<chapterId>7d198ba6-4af2-4f24-86cb-3c79cb25627e</chapterId>

### Definition and Operation

Chain analysis is a practice that encompasses all methods used to track the flow of bitcoin on the blockchain. Generally, chain analysis is based on observing features in samples of previous transactions. It then involves identifying these same features in a transaction one wishes to analyze and inferring plausible interpretations. This method of problem solving from a practical approach to finding a good enough solution is what is called "heuristics."

To simplify, the chain analysis is carried out in three main steps:

1. **Observing the blockchain;**

2. **Identify known characteristics;**

3. **Deducing assumptions.**

Blockchain analysis can be performed by anyone. It is sufficient to have access to the public information of the blockchain through a full node to observe transaction movements and make assumptions. There are also free tools that facilitate this analysis, such as the website [OXT.me](https://oxt.me/), which we will explore in detail in the last two chapters of this part. However, the main privacy risk comes from companies that specialize in chain analysis. These companies have taken chain analysis to an industrial scale and sell their services to financial institutions or governments. Among these companies, Chainalysis is probably the best known.

### The Goals of Chain Analysis

One of the goals of chain analysis is to group together various activities on Bitcoin in order to determine the uniqueness of the user who performed them. Next, it will be possible to attempt to link this set of activities to an actual identity.

Recall the previous chapter. I explained why Bitcoin's privacy model was originally based on separating user identities from their transactions. Therefore, it would be tempting to think that on-chain analysis is useless, since even if you can group onchain activities, they cannot be associated with an actual identity.

Theoretically, this statement is accurate. In the first part of this training, we saw that cryptographic key pairs are used to establish conditions on the UTXO. By essence, these key pairs do not reveal any information about the identity of their holders. Thus, even if we are able to group activities associated with different key pairs, this tells us nothing about the entity behind these activities.

However, the practical reality is much more complex. There is a multitude of behaviors that risk linking a real identity to an onchain activity. In analysis, this is called an entry point, and there are many.

The most common, of course, is KYC (_Know Your Customer_). If you withdraw your bitcoins from a regulated platform to one of your personal receiving addresses, then some people are able to link your identity to this address. More generally, an entry point can be any form of interaction between your real life and a bitcoin transaction. For example, if you post a receiving address on your social networks, this can be an entry point for analysis. If you make a bitcoin payment to your baker, they can associate your face (which is part of your identity) with a Bitcoin address.

These entry points are almost inevitable in the use of Bitcoin. Although you can try to limit their scope, they will remain present. That is why it is crucial to combine methods aimed at preserving your privacy. Although maintaining a separation between your real identity and your transactions is an attractive approach, it remains insufficient today. Indeed, if all your onchain activities can be grouped together, then the slightest point of entry is likely to compromise the one layer of privacy you had established.

### Defending Against Chain Analysis

Therefore, it is also necessary to be able to address blockchain analysis in our use of Bitcoin. By proceeding in this way, we can minimize the aggregation of our activities and limit the impact of an entry point on our privacy.

In fact, to better counter blockchain analysis, what better approach than to familiarize yourself with the methods used in blockchain analysis? If you want to know how to improve your privacy on Bitcoin, you need to understand these methods. This will enable you to better understand techniques such as coinjoin or payjoin (techniques that we will study in the latter parts of the training), and reduce the mistakes you might make.

In this context, we can make an analogy with cryptography and cryptanalysis. A good cryptographer is first and foremost a good cryptanalyst. To devise a new cryptographic algorithm, you need to know what attacks it will face and also study why previous algorithms have been hacked. The same principle applies to privacy on Bitcoin. Understanding the methods of analyzing the blockchain is the key to protecting against it. That is why I propose an entire section on blockchain analysis in this training.

https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef
https://planb.network/fr/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f
### The methods of blockchain analysis

It is important to understand that blockchain analysis is not an exact science. It relies on heuristics derived from previous observations or logical interpretations. These rules allow for fairly reliable results, but never with absolute precision. In other words, **blockchain analysis always involves a probability dimension in the conclusions issued**. For example, one can estimate with greater or lesser certainty that two addresses belong to the same entity, but total certainty will always be out of reach.

The main goal of blockchain analysis lies precisely in the aggregation of various heuristics in order to minimize the risk of error. It is, in a sense, an accumulation of evidence that allows us to get closer to reality.

These famous heuristics can be grouped into several categories that we will detail together:


- Transaction models (or transaction models);**
- Internal heuristics of the transaction;**
- Heuristics external to the transaction.**

### Satoshi Nakamoto and blockchain analysis

It should be noted that the first two heuristics for chain analysis were discovered by Satoshi Nakamoto himself. He discusses them in Part 10 of the Bitcoin White Paper. These are:


- the Common Input Property Heuristics (CIOH);
- and the reuse of addresses.

![BTC204](assets/fr/031.webp)

Source: S. Nakamoto, "Bitcoin: A Peer-to-Peer Electronic Cash System," https://bitcoin.org/bitcoin.pdf, 2009.

In the following chapters, we will explore what this is all about, but it is already interesting to note that these two heuristics still maintain prominence in chain analysis today.

## Transaction Templates

<chapterId>d365a101-2d37-46a5-bfb9-3c51e37bf96b</chapterId>

A transaction model is simply a general pattern or structure of a typical transaction that can be found on the blockchain, the interpretation of which is presumably known. When we study patterns, we will focus on a single transaction that we will analyze at a high level.

In other words, we will only look at the number of UTXOs in the inputs and the number of UTXOs in the outputs, without dwelling on the more specific details or environment of the transaction. From the observed pattern, we will be able to interpret the nature of the transaction. We will then look for features in its structure and infer an interpretation.

![BTC204](assets/it/32/01.webp)

In this part, we will discover together the main transaction patterns that can be encountered in chain analysis, and for each pattern, I will give you the likely interpretation of this structure, along with a concrete example.

### Simple Sending (or Simple Payment)

Let us start with a very popular model, since it is the one that appears in most bitcoin payments. The simple payment model is characterized by consuming one or more UTXOs in the inputs and producing 2 UTXOs in the outputs. This model will therefore appear like this:

![BTC204](assets/it/32/02.webp)

When we identify this transaction structure on the blockchain, we can already draw an interpretation. As the name suggests, this pattern indicates that we are dealing with a send or pay transaction. The user has consumed their UTXOs in input to satisfy in output a payment UTXO and a change UTXO (money returned to the same user).

Thus, we know that the observed user is probably no longer in possession of one of the two output UTXOs (the payment one), but is still in possession of the other UTXO (the change one).

At present, it is impossible for us to specify which output represents which UTXO, since this is not the goal of the study of models. We will achieve this goal by relying on the heuristics that we will study in the following parts. At this stage, our goal is limited to identifying the nature of the transaction in question, which in this case is a simple sending.

For example, here is a Bitcoin transaction that adopts the simple sending model:

```plaintext
b6cc79f45fd2d7669ff94db5cb14c45f1f879ea0ba4c6e3d16ad53a18c34b769
```

![BTC204](assets/it/32/03.webp)

Fonte: [Mempool.space](https://mempool.space/fr/tx/b6cc79f45fd2d7669ff94db5cb14c45f1f879ea0ba4c6e3d16ad53a18c34b769)

After this first example, you should have a better understanding of what it means to study a "transaction model." We examine a transaction by focusing only on its structure, without taking into account its environment or transaction-specific details. We only look at it globally in this first step.

Now that you understand what a model is, let's move on to the other existing models.

### Sweeping

This second model is characterized by consuming a single UTXO as input and producing a single UTXO as output.

![BTC204](assets/it/32/04.webp)

The interpretation of this model is that we are dealing with an auto-transfer. The user has transferred his bitcoins to himself, to another address owned by him. Since there is no remainder in the transaction, it is very unlikely that we are dealing with a payment. In fact, when a payment is made, it is almost impossible for the payer to have a UTXO that exactly matches the amount requested by the seller, plus transaction fees. Generally, the payer is therefore forced to produce a remainder output.

Therefore, we know that the observed user is probably still in possession of this UTXO. In the context of a chain analysis, if we know that the UTXO used as input in the transaction belongs to Alice, we can assume that the UTXO in output also belongs to her. What will become interesting later is to find heuristics internal to the transaction that might strengthen this assumption (we will study these heuristics in Section 3.3).

For example, here is a Bitcoin transaction that adopts the sweeping model:

```plaintext
35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d
```

![BTC204](assets/it/32/05.webp)

Source:[Mempool.space](https://mempool.space/fr/tx/35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d) However, this type of pattern may also reveal a self-transfer to a cryptocurrency exchange platform account. It will be the study of the known addresses and the context of the transaction that will allow us to know whether it is a consolidation to a self-storage wallet or a withdrawal to a platform. Indeed, the addresses of exchange platforms are often easily identifiable.

Let us return to the Alice example: if the consolidation leads to a known address of a platform (such as Binance, for example), this may mean that the bitcoins were transferred out of Alice's direct possession, probably with the intention of selling them or storing them on this platform. On the other hand, if the destination address is unknown, it is reasonable to assume that it is simply another wallet still belonging to Alice. But this type of study falls more into the category of heuristics and not the study of patterns.

### Consolidation

This model is characterized by consuming several UTXOs as input and producing a single UTXO as output.

![BTC204](assets/it/32/06.webp)

The interpretation of this pattern is that we are in the presence of consolidation. This is a common practice among Bitcoin users to merge several UTXOs in anticipation of a possible increase in transaction fees. By performing this operation during a period when fees are low, it is possible to save on future fees. We will discuss more about this practice in Chapter 4.3.

We can infer that the user behind this transaction model was probably in possession of all the input UTXOs and is still in possession of the output UTXO. This is definitely an autotransfer.

Just like consolidation, this type of pattern may also reveal a self-transfer to an exchange platform account. It will be the study of the known addresses and the context of the transaction that will allow us to know whether it is a consolidation to a self-custody wallet or a withdrawal to a platform.

For example, here is a Bitcoin transaction that adopts the consolidation scheme:

```plaintext
77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94
```

![BTC204](assets/it/32/07.webp)

Fonte: [Mempool.space](https://mempool.space/fr/tx/77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94)

In the context of a chain analysis, this model can reveal a lot of information. For example, if we know that one of the inputs belongs to Alice, we can assume that all other inputs and output of this transaction belong to her. This assumption would then allow us to trace back through previous transaction chains to discover and analyze other transactions likely associated with Alice.

![BTC204](assets/it/32/08.webp)

### Grouped Spending

This model is characterized by the consumption of a few UTXOs as input (often only one) and the production of numerous UTXOs as output.

![BTC204](assets/it/32/09.webp)

The interpretation of this pattern is that we are dealing with bundled spending. This is a practice that is likely to reveal significant economic activity, such as an exchange platform. Grouped spending allows these entities to save on fees by consolidating their expenses into a single transaction.

We can infer from this model that the UTXO input comes from a company with significant economic activity and that the UTXO outputs will disperse. Many will belong to the company's customers who withdrew bitcoin from the platform. Others may go to partner companies. Finally, there will certainly be one or more exchanges that return to the issuing company.

For example, here is a Bitcoin transaction that adopts the grouped spending model (probably, it is a transaction issued by the Bybit platform):

```plaintext
8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43
```

![BTC204](assets/it/32/10.webp)

Fonte: [Mempool.space](https://mempool.space/fr/tx/8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43)

### Protocol Specific Transactions

Among transaction patterns, we can also identify patterns that reveal the use of a specific protocol. For example, Whirlpool coinjoins (which we will discuss in Part 5) will have an easily identifiable structure that allows them to be differentiated from other more traditional transactions.

![BTC204](assets/it/32/11.webp)

Analysis of this pattern suggests that we are probably dealing with a collaborative transaction. It is also possible to observe a coinjoin. If the latter hypothesis proves accurate, then the number of outputs could give us a rough estimate of the number of coinjoin participants.

For example, here is a Bitcoin transaction that adopts the coinjoin collaborative transaction type model:

```plaintext
00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea
```

![BTC204](assets/it/32/12.webp)

Fonte: [Mempool.space](https://mempool.space/fr/tx/00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea)

There are many other protocols that have their own specific structures. Thus, we could distinguish transactions of the type Wabisabi, Stamps transactions, or even Runes, for example.

Thanks to these transaction models, we can already interpret a certain amount of information about a given transaction. But the structure of the transaction is not the only source of information for analysis. We can also study its details. These details, internal to a transaction, are what I like to call "internal heuristics," and we will study them in the following chapter.

## Internal Heuristics

<chapterId>c54b5abe-872f-40f4-a0d0-c59faff228ba</chapterId>

An internal heuristic is a specific feature identified within a transaction itself, without the need to examine its environment, which allows us to make inferences. Unlike models that focus on the overall structure of the transaction at a high level, internal heuristics are based on the set of extractable data. This includes:


- The quantities of different UTXOs in and out;
- Everything about scripts: receiving addresses, versioning, locktimes, etc.

Generally, this type of heuristic will allow us to identify the remainder in a specific transaction. By doing so, we can then continue to track an entity across multiple transactions. In fact, if we identify a UTXO belonging to a user we wish to track, it is crucial to determine, when they make a transaction, which output has been transferred to another user and which output represents the remainder, thus remaining in their possession.

![BTC204](assets/it/33/01.webp)

I remind again that these heuristics are by no means accurate. Taken individually, they only allow us to identify plausible scenarios. It is the accumulation of different heuristics that helps to reduce uncertainty, without ever eliminating it completely.

### Internal Similarities

This heuristic involves studying the similarities between the inputs and outputs of the same transaction. If we observe the same feature on the inputs and on only one of the outputs of the transaction, then it is likely that this output constitutes the rest.

The most obvious feature is the reuse of a receiving address in the same transaction.

![BTC204](assets/it/33/02.webp)

This heuristic leaves little room for doubt. Unless one's private key has been hacked, the same receiving address inevitably reveals the activity of a single user. The interpretation that follows is that the rest of the transaction is the output with the same address as the input. This allows continuous tracking of the individual based on this remainder.

For example, here is a transaction on which this heuristic can be reasonably applied:

```plaintext
54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0
```

![BTC204](assets/fr/046.webp)

Fonte: [Mempool.space](https://mempool.space/tx/54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0)

These similarities between input and output do not stop at address reuse. Any similarity in the use of scripts can allow the application of heuristics. For example, sometimes the same versioning can be observed between an input and one of the transaction outputs.

![BTC204](assets/it/33/04.webp)

In this diagram, we can see that input No. 0 unlocks a P2WPKH script (SegWit V0 starting with `bc1q`). Output No. 0 uses the same type of script. However, output #1 uses a P2TR script (SegWit V1 beginning with `bc1p`). The interpretation of this feature is that it is likely that the address with the same versioning as the input is the address of the rest. It would therefore still belong to the same user.

Here is one transaction on which this heuristic can be reasonably applied:

```plaintext
db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578
```

![BTC204](assets/fr/048.webp)

Fonte: [Mempool.space](https://mempool.space/tx/db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578)

In this case, we can see that input No. 0 and output No. 1 use P2WPKH scripts (SegWit V0), while output No. 0 uses a different type of script, P2PKH (Legacy). In the early 2010s, this heuristic based on script version was relatively unhelpful due to the limitation of available script types. However, over time and with subsequent updates to Bitcoin, an increasing diversity of script types has been introduced. This heuristic is becoming increasingly relevant because, with a wider range of script types, users are divided into smaller groups, thus increasing the chances of applying this internal version reuse heuristic. For this reason, from a privacy perspective alone, it is advisable to opt for the most common script type. For example, as I write these lines, Taproot scripts (`bc1p`) are less commonly used than SegWit V0 scripts (`bc1q`). Although the former offer economic and privacy advantages in certain specific contexts, for more traditional single-signature uses, it may be wise to stick with an older standard for privacy reasons until the new standard is more widely adopted.

### Payments with Rounded Numbers

Another internal heuristic that can help us identify the remainder is that of the rounded number. Generally, when faced with a simple payment scheme (1 input and 2 outputs), if one of the outputs spends a rounded amount, then it represents the payment.

![BTC204](assets/it/33/06.webp)

By elimination, if one output represents payment, the other represents change. It can therefore be inferred that it is likely that the user who entered the transaction still possesses the output identified as change.

It should be noted that this heuristic is not always applicable, as most payments are still made in fiat currency units. In fact, when a merchant in France accepts bitcoin, he generally does not display stable prices in sats. He would rather opt for a conversion between the price in euros and the amount in bitcoin to be paid. Therefore, there should not be a rounded number in the transaction output.

However, an analyst might attempt to make this conversion by taking into account the exchange rate in effect at the time the transaction was transmitted over the network. Take the example of a transaction with an input of `97,552 sats` and two outputs, one of `31,085 sats` and the other of `64,152 sats`. At first glance, this transaction does not appear to involve rounded amounts. However, applying the exchange rate of `64.339 at the time of the transaction, we obtain a conversion to euros that appears as follows:


- An input of €62.76;
- An output of €20;
- An output of €41.27.

Once converted to fiat currency, this transaction allows the application of the heuristics of payments with rounded amounts. The output of €20 was probably intended for a merchant, or otherwise changed owners. By inference, the output of €41.27 probably remained in the possession of the original user.

![BTC204](assets/it/33/07.webp)

If one day, Bitcoin becomes the preferred unit of account in our transactions, this heuristic could become even more useful for analysis.

For example, here is a transaction where this heuristic can probably be applied:

```plaintext
2bcb42fab7fba17ac1b176060e7d7d7730a7b807d470815f5034d52e96d2828a
```

![BTC204](assets/fr/051.webp)

Fonte: [Mempool.space](https://mempool.space/tx/2bcb42fab7fba17ac1b176060e7d7d7730a7b807d470815f5034d52e96d2828a)

### The Greatest Output

When there is a significantly large difference between two outputs of a transaction in a simple payment model, it can be estimated that the larger output is likely to be the remainder.

![BTC204](assets/it/33/09.webp)

This largest output heuristic is probably the most inaccurate of all. When identified alone, it is rather weak. However, this feature can be combined with other heuristics to reduce the uncertainty of our interpretation.

For example, if we examine a transaction that has one output with a round amount and another output with a larger amount, the joint application of the heuristics of round payments and the heuristics related to the larger output allows us to reduce our level of uncertainty.

For example, here is a transaction where this heuristic can probably be applied:

```plaintext
b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf
```

![BTC204](assets/fr/053.webp)

Fonte: [Mempool.space](https://mempool.space/tx/b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf)

## External Heuristics

<chapterId>4a170e3b-200d-431a-8285-18a23ff617ba</chapterId>

The study of external heuristics involves analyzing the similarities, patterns and characteristics of certain elements that are not intrinsic to the transaction itself. In other words, if we were previously limited to exploiting elements intrinsic to the transaction with internal heuristics, we are now expanding our field of analysis to the environment of the transaction through external heuristics.

### Reuse of Addresses

This is one of the most well-known heuristics among Bitcoin enthusiasts. Address reuse allows a connection to be established between different transactions and different UTXOs. It is observed when a Bitcoin receiving address is used multiple times.

Thus, it is possible to exploit address reuse within the same transaction as an internal heuristic to identify the remainder (as we saw in the previous chapter). However, address reuse can also serve as an external heuristic to recognize the uniqueness of an entity behind several transactions.

The interpretation of address reuse is that all UTXOs locked on this address belong (or have belonged) to the same entity. This heuristic leaves little room for uncertainty. When it can be identified, the interpretation that follows is most likely to correspond to reality. It thus allows the clustering of different onchain activities.

![BTC204](assets/it/34/01.webp)

As explained in the introduction to this Part 3, this heuristic was discovered by Satoshi Nakamoto himself. In the White Paper, he specifically mentions a solution for users to avoid it, which is simply to use a new address for each new transaction:

"_As an additional protection, a new key pair could be used for each transaction to prevent them from being linked to a common owner._"

![BTC204](assets/fr/055.webp)

Source: S. Nakamoto, "Bitcoin: A Peer-to-Peer Electronic Cash System," https://bitcoin.org/bitcoin.pdf, 2009.

For example, here is an address reused in multiple transactions:

```plaintext
bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0
```

Source:[Mempool.space](https://mempool.space/address/bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0)

### Similarity of Scripts and Fingerprints of Wallets

In addition to address reuse, there are a number of other heuristics for linking shares to the same portfolio or to a cluster of addresses.

First of all, an analyst can take advantage of similarities in script usage. For example, certain minority scripts such as multisig can be identified more easily than SegWit V0 scripts. The larger the group we hide in, the more difficult it is to identify us. This is why, in good Coinjoin protocols, all participants use exactly the same type of scripts.

More generally, an analyst can also focus on the fingerprint characteristics of a portfolio. These are specific processes related to usage that one might try to identify with the goal of exploiting them as tracking heuristics. In other words, if one observes an accumulation of the same internal characteristics on transactions attributed to the tracked entity, one can attempt to identify these same characteristics on other transactions.

For example, it can be identified that the traced user systematically sends their remainder to P2TR addresses (`bc1p...`). If this process is repeated, it can be used as a heuristic for the continuation of our analysis. Other fingerprints can be used, such as the order of the UTXOs, the placement of the remainder in the outputs, the RBF (Replace-by-Fee) signaling, or even, the version number, the `nSequence` field, and the `nLockTime` field.

As [@LaurentMT](https://twitter.com/LaurentMT) specifies in [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji) (a Francophone podcast), the utility of wallet fingerprints in chain analysis increases significantly over time. Indeed, the increasing number of script types and the increasingly gradual deployment of these new capabilities by wallet software accentuate the differences. It may even be the case that one can accurately identify the software used by the entity being tracked. It is therefore important to understand that the study of a wallet's digital footprint proves particularly relevant for recent transactions, more so than for those initiated in the early 2010s.

To summarize, a fingerprint can be any specific practice, performed automatically by the wallet or manually by the user, that can be found on other transactions to assist in our analysis.

### The Heuristics of the Common Ownership of Inputs (CIOH)

CIOH, for "Common Input Ownership Heuristic" in English, is a heuristic that states that when a transaction includes multiple inputs, they are likely to come from a single entity. As a result, their ownership is common.

To apply Common Ownership Heuristics of Inputs (CIOH), we first observe a transaction that has multiple inputs. This could be from a minimum of 2 inputs up to a maximum of 30 inputs. Once this characteristic is identified, we check whether the transaction does not fit a known transaction model. For example, if it has 5 inputs with roughly equal amounts and 5 outputs with exactly the same amount, we know it is the structure of a coinjoin. Therefore, we cannot apply IOCH.

However, if the transaction does not fit any known model of collaborative transaction, then we can infer that all inputs are probably from the same entity. This can be very useful to expand a known cluster or to continue tracking.

CIOH was discovered by Satoshi Nakamoto. He discusses this in part 10 of the White Paper:

"_[...] linkage is inevitable with multi-input transactions, which necessarily reveal that their inputs were owned by the same owner. The risk is that if the owner of a key is revealed, linkages may reveal other transactions that belonged to the same owner._"

It is particularly fascinating to note that Satoshi Nakamoto, even before the official launch of Bitcoin, had already identified the two main privacy vulnerabilities for users, namely IOCH and address reuse. Such a prediction is quite remarkable, as these two heuristics remain, to this day, the most useful in blockchain analysis.

To give you an example, here is a transaction on which we can probably apply IOCH:

```plaintext
20618e63b6eed056263fa52a2282c8897ab2ee71604c7faccfe748e1a202d712
```

Fonte: [Mempool.space](https://mempool.space/tx/20618e63b6eed056263fa52a2282c8897ab2ee71604c7faccfe748e1a202d712)

### Offchain data

Of course, on-chain analysis is not limited exclusively to onchain data. Data from previous analyses or available on the Internet can also be used to refine an analysis.

For example, if it is observed that tracked transactions are systematically transmitted from the same Bitcoin node and its IP address can be identified, it might be possible to identify other transactions from the same entity, as well as to determine part of the identity of the sender. Although this practice is not easily accomplished, as it requires many nodes to operate, it is possible that some companies specializing in chain analysis will employ it.

The analyst also has the option of relying on analyses previously made open-source, or on his own previous analyses. Perhaps an output could be found that points to an address cluster that had already been identified. Sometimes, it is also possible to rely on output that points to an exchange platform, the addresses of these companies being generally known.

Similarly, one can perform analysis by elimination. For example, if during the analysis of a transaction with two outputs, one of them is connected to an address cluster already known but distinct from the entity being tracked, then it can be interpreted that the other output probably represents the rest.

Chain analysis also includes a part of OSINT (_Open Source Intelligence_) that is a bit more generalist with internet searches. This is why it is not recommended to post receiving addresses directly on social media or on a website, whether under a pseudonym or not.

![BTC204](assets/fr/063.webp)

### Temporal Patterns

It is less commonly considered, but certain human behaviors are recognizable on-chain. The most useful in analysis might be your sleeping pattern! Yes, when you sleep, you are presumably not transmitting Bitcoin transactions. Because you generally sleep at the same times, it is common to use temporal analysis in on-chain analysis. This simply involves cataloging the times when a given entity's transactions are transmitted to the Bitcoin network. Analyzing these temporal patterns allows us to infer a lot of information.

First of all, a temporal analysis will sometimes identify the nature of the entity being tracked. If it is observed that transactions are transmitted consistently over 24 hours, then this will reveal strong economic activity. The entity behind these transactions is likely a company, potentially international, and perhaps with internally automated procedures.

For example, [I had recognized this pattern a few months ago](https://twitter.com/Loic_Pandul/status/1701127409712452072) by analyzing [the transaction that had mistakenly allocated 19 bitcoins in fees](https://mempool.space/tx/d5392d474b4c436e1c9d1f4ff4be5f5f9bb0eb2e26b61d2781751474b7e870fd). A simple temporal analysis had allowed me to assume that we were dealing with an automated service, and therefore probably a large entity such as an exchange platform.

In fact, a few days later, it was discovered that the funds belonged to PayPal, via the Paxos exchange platform.

Conversely, if we see that the time pattern is rather spread out over 16 very specific hours, then we can estimate that we are dealing with an individual user, or perhaps a local business depending on the volumes traded.

In addition to the nature of the observed entity, the temporal model can also give us an approximate location of the user through time zones. We can then link other transactions, and use the timestamps of these as additional heuristics that can be added to our analysis.

For example, on the reused address I mentioned earlier, we can observe that transactions, both incoming and outgoing, are concentrated on a 13-hour interval.

```plaintext
bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0
```

![BTC204](assets/fr/064.webp)

Source: OXT.me

This range probably corresponds to Europe, Africa or the Middle East. We can therefore infer that the user behind these transactions lives there.

In a different register, it is also such a time analysis that allowed for the hypothesis that Satoshi Nakamoto was not operating from Japan, but actually from the United States: [_The Time Zones of Satoshi Nakamoto_](https://medium.com/@insearchofsatoshi/the-time-zones-of-satoshi-nakamoto-aa40f035178f)

## Practical Application with a Block Explorer

<chapterId>6493cf2f-225c-405f-9375-c4304f1087ed</chapterId>

In this final chapter, we will concretely apply the concepts we have studied so far. I will present examples of real Bitcoin transactions, and you will have to extract the information I ask for.

Ideally, for these exercises, the use of a professional chain analysis tool would be preferable. However, following the shutdown of the creators of Samourai Wallet, the only free analysis tool OXT.me is no longer available. Therefore, we will opt for a classic block explorer for these exercises. I recommend using [Mempool.space](https://mempool.space/) for its many features and range of chain analysis tools, but you can also choose another explorer such as [Bitcoin Explorer](https://bitcoinexplorer.org/). To begin, I will introduce the exercises. Use your block explorer to complete them and write your answers on a piece of paper. Then, at the end of this chapter, I will provide the answers so you can check and correct your results.

_The transactions selected for these exercises were chosen solely for their characteristics somewhat randomly. This chapter is intended for educational and informational purposes only. I want to make it clear that I do not advocate or encourage the use of these tools for malicious purposes. The goal is to teach you how to protect yourself from chain analysis, not to conduct analysis to expose private information of others._

### Exercise 1

ID of the transaction to be analyzed:

```plaintext
3769d3b124e47ef4ffb5b52d11df64b0a3f0b82bb10fd6b98c0fd5111789bef7
```

What is the model name of this transaction and what plausible interpretations can be drawn by examining only its model, i.e., the structure of the transaction?

### Exercise 2

ID of the transaction to be analyzed:

```plaintext
baa228f6859ca63e6b8eea24ffad7e871713749d693ebd85343859173b8d5c20
```

What is the model name of this transaction and what plausible interpretations can be drawn by examining only its model, i.e., the structure of the transaction?

### Exercise 3

ID of the transaction to be analyzed:

```plaintext
3a9eb9ccc3517cc25d1860924c66109262a4b68f4ed2d847f079b084da0cd32b
```

What is the pattern of this transaction?

After identifying its model, using the internal heuristics of the transaction, what output is likely to represent the rest?

### Exercise 4

ID of the transaction to be analyzed:

```plaintext
35f0b31c05503ebfdf7311df47f68a048e992e5cf4c97ec34aa2833cc0122a12
```

What is the pattern of this transaction?

After identifying its model, using the internal heuristics of the transaction, what output is likely to represent the rest?

### Exercise 5

Imagine that Loïc posted one of his Bitcoin addresses to receive payments on the social network Twitter:

![BTC204](assets/fr/065.webp)

```plaintext
bc1qja0hycrv7g9ww00jcqanhfpqmzx7luqalum3vu
```

Using **only address reuse heuristics**, what Bitcoin transactions can we link to Loïc's identity?

_Obviously, I am not the real owner of this receiving address and I did not post it on social media. It is an address that I randomly chose from the blockchain._

### Exercise 6

Following Exercise 5, using address reuse heuristics, you were able to identify several Bitcoin transactions in which Loïc appears to be involved. Normally, among the identified transactions, you should have identified this one:

This transaction represents the very first one that sends funds to Loïc's address. Where do you think the bitcoins received by Loïc through this transaction came from?

### Exercise 7

Following Exercise 5, using address reuse heuristics, you were able to identify several Bitcoin transactions in which Loïc appears to be involved. You now wish to find out where Loïc came from. Based on the transactions found, conduct a time analysis to find the likely time zone used by Loïc. From this time zone, determine a location where Loïc appears to live (country, state/region, city...).

### Exercise 8

Here is the Bitcoin transaction to study:

```plaintext
bb346dae645d09d32ed6eca1391d2ee97c57e11b4c31ae4325bcffdec40afd4f
```

Looking only at this transaction, what information can we interpret?

### Solutions to the exercises

**_Exercise 1:_**

The model of this transaction is that of a simple payment. If we study only its structure, we can interpret that one output represents change and the other output represents an actual payment. We then know that the observed user is probably no longer in possession of one of the two UTXOs in the outputs (the one for payment), but is still in possession of the other UTXO (the one for change).

**_Exercise 2:_**

The pattern of this transaction is that of batch spending. This pattern probably indicates a significant economic activity, such as an exchange platform. We can infer that the input UTXO comes from a company with significant economic activity and that the output UTXOs will disperse. Some will belong to the company's customers who have withdrawn their bitcoins to self-storage wallets. Others may go to partner companies. Finally, there will certainly be a remainder that returns to the issuing company.

**_Exercise 3:_**

The model of this transaction is that of a simple payment. Therefore, we can apply internal heuristics to the transaction to try to identify the remainder.

Personally, I have identified at least two internal heuristics that support the same hypothesis:


- The reuse of the same type of script;
- Largest output.

The most obvious heuristic is the reuse of the same type of script. In fact, the output `0` is a `P2SH`, recognizable by its receiving address beginning with `3`:

```plaintext
3Lcdauq6eqCWwQ3UzgNb4cu9bs88sz3mKD
```

While the output `1` is a `P2WPKH`, identifiable by its address beginning with `bc1q`:

```plaintext
bc1qya6sw6sta0mfr698n9jpd3j3nrkltdtwvelywa
```

The UTXO used as input for this transaction also uses a `P2WPKH` script:

```plaintext
bc1qyfuytw8pcvg5vx37kkgwjspg73rpt56l5mx89k
```

Thus, we can assume that output `0` corresponds to a payment and output `1` is the rest of the transaction, which would mean that the input user still owns output `1`.

To support or refute this hypothesis, we can look for other heuristics that confirm our thinking or decrease the probability that our hypothesis is correct.

I have identified at least one other heuristic. It is the largest output. The `0` output measures `123,689 sats`, while the `1` output measures `505,839 sats`. There is, therefore, a significant difference between these two outputs. The heuristic of the larger output suggests that the more voluminous output is probably the remainder. This heuristic therefore further strengthens our initial hypothesis.

It seems likely that the user who provided the input UTXO still holds the output `1`, which seems to represent the rest of the transaction.

**_Exercise 4:_**

The model of this transaction is that of a simple payment. Therefore, we can apply internal heuristics to the transaction to try to identify the remainder.

I have personally identified at least two internal heuristics that support the same hypothesis:


- The reuse of the same type of script;
- The output of a round amount.

The most obvious heuristic is the reuse of the same type of script. In fact, the output `0` is a `P2SH`, recognizable by its receiving address beginning with `3`:

```plaintext
3FSH5Mnq6S5FyQoKR9Yjakk3X4KCGxeaD4
```

While the output `1` is a `P2WPKH`, identifiable by its address beginning with `bc1q`:

```plaintext
bc1qvdywdcfsyavt4v8uxmmrdt6meu4vgeg439n7sg
```

The UTXO used as input for this transaction also uses a `P2WPKH` script:

```plaintext
bc1qku3f2y294h3ks5eusv63dslcua2xnlzxx0k6kp
```

Thus, we can assume that output `0` corresponds to a payment and output `1` is the rest of the transaction, which would mean that the input user still holds output `1`.

To support or refute this hypothesis, we can look for other heuristics that confirm our thinking or decrease the probability that our hypothesis is correct.

I have identified at least one other heuristic. It is the output of a round amount. The output `0` measures `70,000 sats`, while the output `1` measures `22,962 sats`. Therefore, we are dealing with a perfectly round output in BTC units of account. The heuristic of round output suggests that the UTXO with one round amount is probably the payment, and by elimination, the other represents the remainder. This heuristic therefore further strengthens our initial hypothesis.

However, in this example, another heuristic might challenge our initial assumption. In fact, the output `0` is larger than the output `1`. If we base our reasoning on the heuristic that the largest output is generally the remainder, we might infer that output `0` is the remainder. However, this counter-hypothesis seems implausible, since the other two heuristics appear substantially more convincing than the largest output heuristic. Consequently, it seems reasonable to maintain our initial hypothesis despite this apparent contradiction.

Therefore, it seems likely that the user who provided the UTXO as input still holds the `1` output, which seems to represent the rest of the transaction.

**_Exercise 5:_**

We can see that 8 transactions can be associated with Loïc's identity. Of these, 4 involve the receipt of bitcoin:

```plaintext
2d9575553c99578268ffba49a1b2adc3b85a29926728bd0280703a04d051eace
8b70bd322e6118b8a002dbdb731d16b59c4a729c2379af376ae230cf8cdde0dd
d5864ea93e7a8db9d3fb113651d2131567e284e868021e114a67c3f5fb616ac4
bc4dcf2200c88ac1f976b8c9018ce70f9007e949435841fc5681fd33308dd762
```

The other 4 is about sending bitcoin:

```plaintext
8b52fe3c2cf8bef60828399d1c776c0e9e99e7aaeeff721fff70f4b68145d540
c12499e9a865b9e920012e39b4b9867ea821e44c047d022ebb5c9113f2910ed6
a6dbebebca119af3d05c0196b76f80fdbf78f20368ebef1b7fd3476d0814517d
3aeb7ce02c35eaecccc0a97a771d92c3e65e86bedff42a8185edd12ce89d89cc
```

**_Exercise 6:_**

If we examine the pattern of this transaction, it is evident that it is a grouped expenditure. In fact, the transaction has a single input and 51 outputs, indicating significant economic activity. We can therefore assume that Loïc made a bitcoin withdrawal from an exchange platform.

Several elements reinforce this hypothesis. First, the type of script used to protect the input UTXO is a P2SH multisig 2/3 script, indicating an advanced level of security typical of exchange platforms:

```plaintext
OP_PUSHNUM_2
OP_PUSHBYTES_33 03eae02975918af86577e1d8a257773118fd6ceaf43f1a543a4a04a410e9af4a59
OP_PUSHBYTES_33 03ba37b6c04aaf7099edc389e22eeb5eae643ce0ab89ac5afa4fb934f575f24b4e
OP_PUSHBYTES_33 03d95ef2dc0749859929f3ed4aa5668c7a95baa47133d3abec25896411321d2d2d
OP_PUSHNUM_3
OP_CHECKMULTISIG
```

In addition, the analyzed address `3PUv9tQMSDCEPSMsYSopA5wDW86pwRFbNF` was reused in more than 220,000 different transactions, which is often characteristic of exchange platforms that are generally not concerned about their privacy. Temporal heuristics applied to this address also show a regular spread of transactions almost daily over a 3-month period, with extended hours over 24 hours, suggesting the continuous activity of an exchange platform.

Finally, the volumes processed by this entity are huge. In fact, the address received and sent 44 BTC during 222,262 transactions between December 2022 and March 2023. These significant volumes further confirm the likely nature of the activity of an exchange platform.

**_Exercise 7:_**

Analyzing transaction confirmation times, the following UTC times can be seen:

```plaintext
05:43
20:51
18:12
17:16
04:28
23:38
07:45
21:55
```

By analyzing these times, it is apparent that UTC-7 and UTC-8 time zones are consistent with a range of common human activities (between 8 a.m. and 11 p.m.) for most times:

```plaintext
05:43 UTC > 22:43 UTC-7
20:51 UTC > 13:51 UTC-7
18:12 UTC > 11:12 UTC-7
17:16 UTC > 10:16 UTC-7
04:28 UTC > 21:28 UTC-7
23:38 UTC > 16:38 UTC-7
07:45 UTC > 00:45 UTC-7
21:55 UTC > 14:55 UTC-7
05:43 UTC > 21:43 UTC-8
20:51 UTC > 12:51 UTC-8
18:12 UTC > 10:12 UTC-8
17:16 UTC > 09:16 UTC-8
04:28 UTC > 20:28 UTC-8
23:38 UTC > 15:38 UTC-8
07:45 UTC > 23:45 UTC-8
21:55 UTC > 13:55 UTC-8
```

The UTC-7 time zone is particularly relevant in summer, as it includes states and regions such as:


- California (with cities such as Los Angeles, San Francisco, and San Diego);
- Nevada (with Las Vegas);
- Oregon (with Portland);
- Washington (with Seattle);
- The Canadian region of British Columbia (with cities such as Vancouver and Victoria).

This information suggests that Loïc could conceivably reside on the West Coast of the United States or Canada.

**_Exercise 8:_**

Analysis of this transaction reveals 5 inputs and a single output, which seems to indicate consolidation. Application of the CIOH heuristic suggests that all UTXOs in the inputs are held by a single entity, and that the UTXO in the output also belongs to this entity. It appears that the user chose to consolidate several UTXOs owned by him into a single UTXO in the output, with the goal of consolidating his own coins. This approach was probably motivated by a desire to take advantage of the low transaction fees of the moment to reduce future fees.

---
_For the writing of this Part 3 on chain analysis, I relied on the following resources:_


- _The four-article series entitled: [Understanding Bitcoin Privacy with OXT](https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923), produced by Samourai Wallet in 2021;_
- _The various reports of [OXT Research](https://medium.com/oxt-research), as well as their free chain analysis tool (which is currently no longer available following the arrest of the founders of Samourai Wallet);_
- _More generally, my knowledge comes from the various tweets and content of [@LaurentMT](https://twitter.com/LaurentMT) and [@ErgoBTC](https://twitter.com/ErgoBTC);_
- \_The [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji) in which I participated along with [@louneskmt](https://twitter.com/louneskmt), [@TheoPantamis](https://twitter.com/TheoPantamis), [@Sosthene\_\_](https://twitter.com/Sosthene___), and [@LaurentMT](https://twitter.com/LaurentMT).\_

_I would like to thank their authors, developers, and producers. Thanks also to the reviewers who meticulously corrected the article that served as the basis for this part 3 and honored me with their expert advice:_


- _[Gilles Cadignan](https://twitter.com/gillesCadignan);_
- _[Ludovic Lars](https://viresinnumeris.fr/)._

# Mastering Best Practices to Protect Your Privacy

<partId>9bd04b63-f1af-4e50-9061-6bc90009df68</partId>

## Reuse of Addresses

<chapterId>f3e97645-3df3-41bc-a4ed-d2c740113d96</chapterId>

Having studied the techniques that can compromise your privacy on Bitcoin, in this third part, we will now examine the best practices you can adopt to protect yourself. This part does not aim to explore methods to improve privacy, a topic that will be addressed later, but rather to understand how to properly interact with Bitcoin to maintain the privacy it naturally offers, without resorting to additional techniques.

Of course, to begin this third part, we will talk about address reuse. This phenomenon is the main threat to users' privacy. Therefore, this chapter is probably the most important in the entire course.

### What is a receiving address?

A bitcoin receiving address is a character string or identifier used to receive bitcoin into a wallet.

Technically, a bitcoin receiving address does not "receive" bitcoin in the literal sense, but rather defines the conditions under which bitcoins can be spent. Specifically, when a payment is sent to you, the sender's transaction creates a new UTXO destined for you in the output from the UTXOs it consumed in the inputs. On this output, a script is applied that defines how this UTXO can be spent later. This script is known as "_ScriptPubKey_" or "_Locking Script_." Your receiving address, more precisely its payload, is embedded in this script. To simplify, this script essentially states:

> "_To expend this new UTXO, a digital signature must be provided using the private key associated with this receiving address._"
![BTC204](assets/fr/067.webp)

Bitcoin addresses come in different types depending on the script model used. The first models, known as "_Legacy_," include `P2PKH` (_Pay-to-PubKey-Hash_) and `P2SH` (_Pay-to-Script-Hash_) addresses. P2PKH addresses always begin with `1` and P2SH with `3`. Although still secure, these formats are now obsolete, as they carry higher transaction fees and offer less privacy than the new standards.

SegWit V0 (`P2WPKH` and `P2WSH`) and Taproot / SegWit V1 (`P2TR`) addresses represent modern formats. SegWit addresses begin with `bc1q` and Taproot addresses, introduced in 2021, begin with `bc1p`.

For example, here is a Taproot receiving address:

```text
bc1ps5gd2ys8kllz9alpmcwxqegn7kl3elrpnnlegwkm3xpq2h8da07spxwtf5
```

The way the ScriptPubKey is constructed will depend on the standard you are using:

| Script Template | ScriptPubKey || ---------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |

| P2PKH | OP_DUP OP_HASH160 `<pubKeyHash>` OP_EQUALVERIFY OP_CHECKSIG |

| P2SH | OP_HASH160 `<scriptHash>` OP_EQUAL |

| P2WPKH | 0 `<pubKeyHash>` |

| P2WSH | 0 `<witnessScriptHash>` |

| P2SH - P2WPKH | OP_HASH160 `<redeemScriptHash>` OP_EQUAL |

| P2SH - P2WSH | OP_HASH160 `<redeemScriptHash>` OP_EQUAL |

| P2TR | 1 `<pubKey>` |

As for the construction of the receiving addresses, it also depends on the script template chosen:


- For `P2PKH` and `P2WPKH` addresses, the payload, or the core of the address, represents the hash of the public key;
- For `P2SH` and `P2WSH` addresses, the payload represents the hash of a script;
- As for `P2TR` addresses, the payload is a modified public key. The `P2TR` outputs combine aspects of _Pay-to-PubKey_ and _Pay-to-Script_. The modified public key is the result of adding a classical spending public key with a "modification," derived from the Merkle root of a set of scripts that can also be used to spend bitcoin.

![BTC204](assets/it/67/01.webp)

The addresses displayed on your wallet software also include a HRP (_Human-Readable Part_), typically `bc` for post-SegWit addresses, a separator `1`, and a version number `q` for SegWit V0 and `p` for Taproot/SegWit V1. A checksum is also added to ensure the integrity and validity of the address during its transmission.

Finally, addresses are put into a standard format:


- Base58check for old Legacy addresses;
- Bech32 for SegWit addresses;
- Bech32m for Taproot addresses.

Here is the addition matrix for bech32 and bech32m formats (SegWit and Taproot) from base 10:

| + | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |

| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| 0 | q | p | z | r | y | 9 | x | 8 | 8

| 8 | g | f | 2 | t | v | d | w | 0 |

| 16 | s | 3 | j | n | 5 | 4 | k | h | | 24 | c | e | 6 | m | u | a | 7 | l | l

### What is Address Reuse?

Address reuse refers to the practice of using the same receiving address to block several different UTXOs.

As we saw in the previous section, each UTXO has its own ScriptPubKey that locks it and must be satisfied in order for the UTXO to be consumed as input in a new transaction. It is within this ScriptPubKey that the receive addresses (payloads) are embedded.

When several ScriptPubKeys contain the same receiving address, this is known as address reuse. In practice, this means that a user has provided the same address multiple times to senders to receive bitcoin through multiple payments. And indeed, this practice is catastrophic for your privacy.

### Why is Address Reuse a Problem?

Because the blockchain is public, it is easy to see which addresses block which UTXOs and how many bitcoins. If the same address is used for multiple transactions, it becomes possible to infer that all bitcoins associated with that address belong to the same person. This practice compromises user privacy by allowing deterministic links to be established between different transactions and tracking bitcoins on the blockchain. Satoshi Nakamoto himself highlighted this problem in the Bitcoin White Paper:

> _As an additional firewall, a new key pair could be used for each transaction to prevent them from being linked to a common owner._
![BTC204](assets/fr/055.webp)

Source: S. Nakamoto, "Bitcoin: A Peer-to-Peer Electronic Cash System," https://bitcoin.org/bitcoin.pdf, 2009.

The goal sought by Satoshi with this statement was to create an additional firewall in case of association between the user's identity and a key pair on Bitcoin, to avoid having all their activity publicly linked to their identity. Today, with the proliferation of blockchain analytics companies and KYC regulations, the use of unique addresses is no longer an "additional firewall," but a necessary practice for anyone wishing to preserve their privacy at a minimum.

When you reuse an address, you create an almost indisputable link between all transactions associated with that address. Although this does not directly endanger your funds, because encryption on elliptic curves ensures the security of your private keys, it makes it easier to monitor your activities. In fact, anyone with a node can observe your transactions and address balances, completely compromising your anonymity.

![BTC204](assets/it/34/01.webp)

To illustrate this point, let us take the example of Bob, a user who regularly buys bitcoins in small amounts via Dollar Cost Averaging (DCA) and always sends them to the same address. After two years, this address contains a substantial amount of bitcoin. If Bob uses this address to make a payment to a local merchant, the merchant could see all the associated funds and deduct Bob's wealth. This could lead to personal security risks, including attempts at theft or extortion. If Bob had used a fresh address to receive each periodic purchase, he would have revealed infinitely less information to his merchant.

In the chain analysis, we differentiate between 2 types of address reuse:


- External reuse;
- Internal reuse within a transaction.

The first is observed when an address is reused in several different Bitcoin transactions. This is what we discussed earlier: this heuristic allows us to infer that all UTXOs that are passed through this address belong to a single entity.

Reuse of internal addresses is observed not when reuse occurs across multiple transactions, but when it occurs within the same transaction. Indeed, if the same address that was used to lock an input is used as an output in a transaction, then we can infer that this output still belongs to the same user (remainder), and that the second output represents the actual payment. This other heuristic allows funds to be tracked across multiple transactions.

![BTC204](assets/it/33/02.webp)

Address reuse is a real scourge on Bitcoin. According to the website OXT.me (currently inaccessible), the overall rate of address reuse on Bitcoin was about 52 percent in 2022:

![BTC204](assets/fr/069.webp)

This rate is huge, but it comes overwhelmingly from exchange platforms rather than individual users.

### How to avoid address reuse?

Avoiding address reuse is quite simple: **just use a fresh address for each new incoming payment in your wallet**.

Thanks to BIP32, modern portfolios are now deterministic and hierarchical. This means that a user can generate a large number of addresses from a single piece of initial information: the seed. By saving this single piece of information, all the private keys in the wallet can be restored, thus accessing the funds secured by the corresponding addresses.

![BTC204](assets/fr/070.webp)

That is why, when you press the "_receive_" button in your wallet software, you are offered an unused receiving address each time. After receiving bitcoin on this address, the software automatically suggests a new address.

> _PS: Recently, some wallet software has announced its intention to stop generating blank addresses, fearing that this may be perceived as a form of money laundering by the authorities. If your software is among them, I strongly advise you to replace it immediately, as this is not acceptable to the user._
If you need a static identifier to receive payments, such as to receive donations, for example, using a classic Bitcoin address is not recommended because of the risk of reuse. You prefer to use a Lightning address, or for a static onchain payment identifier, you can opt for BIP47 or Silent Payments. How these protocols work is detailed in Part 6 of this training.

## Coin Labeling and Control

<chapterId>fbdb07cd-c025-48f2-97b0-bd1bc21c68a8</chapterId>

As we discovered in the section on chain analysis, there are a multitude of heuristics and patterns that can be used to infer information about a transaction. As a user, it is important to be aware of these techniques to better protect yourself.

This greatly involves strict management of one's wallet in personal custody, which includes knowing the origin of one's UTXOs, as well as thoughtful selection of UTXOs to be consumed during payments. This effective wallet management relies on two important features of good Bitcoin wallets: labeling and coin control.

In this chapter, we will study these features and see how you could use them intelligently, without adding too much workload, to greatly optimize your privacy on Bitcoin.

### What is Labeling?

Tagging is a practice that involves assigning an annotation or label to a specific UTXO in a Bitcoin wallet. These annotations are stored locally by the wallet software and are never transmitted over the Bitcoin network. Tagging is thus a tool for personal management.

For example, if I own a UTXO from a P2P purchase on Bisq with Charles, I might assign it the label "`Non-KYC Bisq Charles`".

Tagging is a good practice that helps to remember the origin or intended destination of a UTXO, thereby facilitating the management of funds and optimizing privacy. In fact, your Bitcoin wallet is likely to contain several UTXOs. If the sources of these UTXOs are different, you may not want to merge these UTXOs in the future, otherwise you may reveal their common ownership. By properly labeling all your coins, you ensure that you will remember their origin when you need them, even if that is not until several years from now.

### What is coin control?

The active use of tagging becomes even more attractive when combined with the coin control option on your wallet software.

Coin control is a feature found in good Bitcoin wallet software that gives you the ability to manually select specific UTXOs to use as input to perform a transaction. In fact, to satisfy an outgoing payment, you must consume an incoming UTXO in return. For several reasons that we will see later, you may want to choose precisely which coins to consume as input to satisfy a given payment. This is exactly what coin control allows. To give you an analogy, this functionality is similar to the action of choosing a specific coin in your wallet when you pay for your baguette.

The use of coin-controlled wallet software, combined with the labeling of UTXOs, enables users to accurately distinguish and select UTXOs for their transactions.

### How to label your UTXOs correctly?

There is no universal method for labeling UTXOs that fits everyone. It is up to you to define a labeling system so that you can easily navigate your portfolio. In any case, keep in mind that good labeling is what you will be able to understand when you need it. If your Bitcoin wallet is primarily for savings, it may be that the labels will not be useful to you until several decades from now. Therefore, make sure they are clear, accurate, and inclusive.

It is important that your loved ones can easily identify the source of the funds if, one day, they need access to your portfolio. This could help them for privacy reasons as well as for legal needs, should they need to justify the origin of the funds before an authority.

The most important aspect of labeling is to note the source of the UTXO. You should simply indicate how this coin arrived in your wallet. Did it come from a purchase on an exchange platform? A payment from a customer? A peer-to-peer exchange? Or is it the remainder of a purchase? So, you could specify:


- `Pickup Exchange.com`;
- `Payment Client David`;
- `Buy P2P Charles`;
- `Retaining from sofa purchase`

To refine your management of UTXOs and adhere to your strategies of segregating funds within your portfolio, you could enrich your labels with an additional marker to reflect these separations. If your portfolio contains two categories of UTXOs that you do not wish to mix, you could integrate a marker into your labels to clearly distinguish these groups. These separation markers will depend on your criteria, such as distinguishing between UTXOs from an acquisition process involving KYC, or between professional and personal funds. Taking the previously mentioned examples of labels, this could translate into:


- `KYC - Exchange.com Withdrawal`;
- `KYC - Customer Payment David`;
- `NO KYC - Purchase P2P Charles`;
- `NO KYC - Remainder from sofa purchase`

It is also advisable to perpetuate the labeling of a coin during transactions. For example, when consolidating UTXOs without KYC, be sure to mark the resulting UTXO not only as `consolidation`, but specifically as `no-KYC consolidation` to maintain a clear trace of the coin's origin.

Finally, it is not mandatory to put a date on a label. Most wallet software already shows the date of the transaction, and it is always possible to retrieve this information on a block explorer using its TXID.

### How to Choose Your Coins Correctly?

When you make a transaction, coin control allows you to specifically choose which UTXOs to consume as input to satisfy the payment output. Two aspects should be considered in this choice:


- The ability for the payment recipient to link a part of your identity to the UTXOs used as input;
- The ability of an outside observer to make connections among all UTXOs consumed as input.

To illustrate the first point, let's take a concrete example. Suppose you buy a baguette with bitcoins from your local baker. You use one or more UTXOs of your own as input to cover at least the price of the baguette in output, plus transaction fees. Your baker could then potentially associate your face, or any other part of your identity that he knows, with the coins used as input. Knowing the existence of this link, you might prefer to choose one specific UTXO over another when making payment.

For example, if one of your UTXOs comes from an exchange platform and you prefer that the baker not be aware of your account on this platform, you would avoid using this UTXO for payment. If you have a high-value UTXO that reveals a significant amount of bitcoin, you might also choose not to use it to prevent the baker from knowing your BTC fortune.

The choice of UTXOs to use for this first point is therefore based on a personal decision, influenced by what you are willing to disclose or not. The labels you have assigned to your UTXOs upon receipt will help you select those that, when spent, display only the information you are comfortable with revealing to the recipient.

In addition to the information potentially revealed to the recipient, your choice of inputs also affects what you disclose to all blockchain observers. In fact, by using multiple UTXOs as inputs to your transaction, you reveal that they are owned by the same entity, according to the Common Ownership Heuristics of Inputs (CIOH).

When you select your coins, you should therefore be aware that the transaction you are about to transmit will create a link between all the UTXOs used. This link can be problematic for your personal privacy, especially if the UTXOs come from different sources.

Back to the example of my UTXO without KYC from Bisq; I want to avoid combining it with a UTXO from, say, a regulated exchange platform that knows my identity. In fact, if I ever used these 2 UTXOs as inputs in the same transaction, the regulated platform would be able to link my identity with the UTXO I purchased on Bisq, whereas before it was not linked to my identity.

Finally, to properly choose which UTXOs to consume as input for a transaction, the most important thing is to avoid using multiple UTXOs. Whenever possible, select a single coin that is large enough to cover your payment. By doing so, you completely avoid the risks associated with COINJOIN. However, if no individual UTXO is sufficient for your payment and you need to consume several, make sure they come from similar sources to minimize the risks of unwanted connections. Also, keep in mind that the recipient may associate the information they have about you with the history of the coins used as input.

### Understanding Automatic Coin Selection

In previous sections, we discussed the manual selection of UTXOs for a transaction. But what happens when the wallet software makes this selection automatically? There are several methods for determining which coins to consume, and the selection of UTXOs is a real field of research in Bitcoin. The main goal of this automatic process is often to minimize transaction fees for the user.

UTXO selection methods such as FIFO (_First In First Out_) and LIFO (_Last In First Out_) are among the simplest but also the least efficient. With FIFO, the oldest coins in the portfolio are used first. This approach is generally inefficient both to minimize transaction fees and to preserve privacy, except in cases where relative timelocks are used and must be renewed regularly. In contrast, LIFO prioritizes the use of the most recent UTXOs. Although simple, these two methods often prove inefficient.

A more advanced method is the _Knapsack Solver_. This was the method used in the Bitcoin Core wallet up to version 0.17. It involves iteratively and randomly selecting UTXOs from the wallet, summing them into subgroups, and keeping the solution that reduces the transaction weight as much as possible in order to reduce user fees.

The _Branch-and-Bound_ (BNB), often nicknamed "Murch's algorithm" in reference to its inventor, replaced the _Knapsack Solver_ in Bitcoin Core starting with version 0.17. This more advanced method aims to find a set of UTXOs that exactly matches the amount needed to satisfy the outputs of a transaction. The goal of BNB is to minimize the amount of remainder as well as fees by reducing what is called the waste criterion that takes into account both immediate costs and expected future costs for the remainder. This method is derived from the original _Branch-and-Bound_ concept, designed in 1960 by Ailsa Land and Alison Harcourt, and offers more precise commission optimization than the _Knapsack Solver_.

All these automatic UTXO selection methods can be effective in reducing transaction fees, but they are often inefficient in preserving user privacy. In fact, these algorithms may merge several UTXOs into input, thus revealing a common ownership of these UTXOs due to COH. Obviously, these methods cannot take into account the labels attached to the UTXOs, which are crucial for consciously choosing which coins to reveal to the transaction recipient. Currently, the only solution to optimize privacy in coin selection is to do it manually.

### UTXO Labeling Tutorial

If you would like to find out how to tag your UTXOs, we have put together a comprehensive tutorial on the main existing Bitcoin wallet software:

https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52
## KYC and Key Identification

<chapterId>cec6b9d9-0eed-4f85-bc4e-1e9aa59ca605</chapterId>

KYC stands for "Know Your Customer," which is a regulatory procedure implemented by some companies operating in the Bitcoin industry. This procedure aims to verify and record the identity of their customers with the stated goal of combating money laundering and terrorist financing.

Concretely, KYC involves the collection of various personal information from the client, which may vary by jurisdiction, but generally includes an ID, photograph, and proof of residence. This information is then verified and stored for future use.

This procedure has become mandatory for all regulated exchange platforms in most Western countries. This means that anyone wishing to exchange fiat currencies for bitcoin through these platforms must comply with KYC requirements.

This procedure is not without risks to user privacy and security. In this chapter, we will examine these risks in detail and analyze the specific impacts of KYC and identification processes on Bitcoin users' privacy.

### Facilitating Onchain Tracking

The first risk associated with KYC is that it provides a preferred entry point for blockchain analysis. As we saw in the previous section, analysts can group and track activity on the blockchain using transaction patterns and heuristics. Once they have managed to cluster a user's onchain activity, finding only one entry point among all their transactions and keys is enough to completely compromise their privacy.

![BTC204](assets/fr/078.webp)

When you submit to KYC, you provide a very high quality entry point for chain analysis, as you link the receiving addresses used when you withdraw your bitcoins from an exchange platform to your full, verified identity. In theory, this information is known only to the company to which you provided it, but, as we will see later, the risk of data loss is real. Moreover, the mere fact that a company holds this information can be problematic, even if it does not share it.

Thus, unless other measures are taken to limit the pooling of one's activities on the blockchain, anyone who is aware of the entry point that is KYC can potentially link all of their activity on Bitcoin to their identity. From this company's perspective, the use of Bitcoin therefore loses all confidentiality.

![BTC204](assets/fr/079.webp)

To illustrate this with a comparison, it is as if one's banker at _Bank X_ had access not only to all transactions made with _Bank X_, but could also observe transactions with _Bank Y_ and all one's own cash transactions.

Recall from the first part of this training: the privacy model of Bitcoin, as designed by Satoshi Nakamoto, is based on the separation between the user's identity and his key pairs. Although this layer of privacy is no longer sufficient today, it is still wise to limit its degradation as much as possible.

### Exposure to State Surveillance

The second major problem with KYC is that it reveals to the state that one has possessed bitcoin at some time. When you purchase bitcoins through a regulated actor, it becomes possible for the state to know this possession. Currently, this may seem trivial, but it is important to remember that the political and economic future of one's country is not in one's own hands.

First of all, the state can quickly adopt an authoritarian stance. History is full of examples where policies have changed abruptly. Today, in Europe, Bitcoin enthusiasts can write articles about Bitcoin, attend conferences, and manage their own self-storage wallets. But who can say what tomorrow will hold? If Bitcoin suddenly becomes public enemy number one, being associated with it in state registries could prove problematic.

Later, in the face of severe economic crises, the state might consider seizing bitcoins held by citizens. Perhaps tomorrow, bitcoiners will be seen as taking advantage of the crisis and will be overtaxed because of their capital gains in the face of fiat currency devaluation.

You might think this is not a problem because your bitcoins are shuffled and therefore untraceable. However, traceability is not the problem here. The real problem is that the state knows that you have possessed bitcoins. This simple piece of information could be enough to incriminate you or demand an account. You could try to claim that you spent your bitcoins, but that would have to be reflected in your tax return, and you would be found out. You could also say you lost your keys in a boating accident, but beyond the Twitter joke, do you really think that would be enough to exonerate you?

Therefore, it is important to consider the risk associated with the simple fact that the state might know that you owned BTC, even though this risk may seem far away today.

Another issue posed by KYC in terms of state oversight is mandatory reporting by regulated platforms. Although I am unfamiliar with regulations in other jurisdictions, in France, _Digital Asset Service Providers_ (PSANs) are required to report to financial supervisors any movement of funds they consider suspicious.

Thus, in France in 2023, 1,449 suspicious acts were reported by PSANs. For now, most of these acts are crime-related. However, authorities are also asking regulated platforms to report any suspicious Bitcoin transactions based solely on its structure. If you conduct a collaborative transaction, or even just a transaction that has a somewhat atypical pattern, and this transaction occurs near the withdrawal of your bitcoins from these platforms, you may find yourself reported to the authorities. Even in the absence of wrongdoing and in the legitimate exercise of your rights, this reporting could lead to increased scrutiny and surveillance, inconveniences you would have avoided without KYC.

### The risk of loss of personal data

Another problem with KYC lies in the fact that it requires storing all your personal data on a private company's servers. Recent events have reminded us that no one is immune to failure, whether financial or IT-related. In 2022, Celsius customers suffered the consequences. As a result of the company's bankruptcy, the names of creditors and the amount of their assets were made public by the U.S. justice system during administrative proceedings.

Just over two years ago, a leading cybersecurity entity in the cryptocurrency domain suffered the theft of its customers' personal data. Although this incident was not directly related to the purchase of bitcoin, this risk also remains for exchange platforms. Therefore, there is a definite risk associated with this personal data.

It is true that we already entrust much of our personal data to private companies. However, the risk here is twofold since this data not only allows you to be identified but is also linked to activity on bitcoin. Indeed, when a hacker is able to access the data of customers of an exchange platform, they can reasonably assume that these customers own bitcoin. This risk is thus exacerbated by the fact that bitcoin, like any other valuable asset, attracts the interest of thieves.

In the event of a data breach, at best, you could be the target of targeted phishing attempts. At worst, you could find yourself at the center of physical threats to your home.

In addition to the specific risks associated with Bitcoin, it is also necessary to consider the dangers associated with the transmission of identity documents. Indeed, in the event of a data leak, it is possible to become a victim of identity theft. Therefore, the issues at stake are not only limited to protecting the confidentiality of transactions, but also affect the personal security of each individual.

### Common misunderstandings regarding KYC

It is important to dispel some common misconceptions about KYC that are frequently found on Twitter or in our discussions among bitcoiners.

First of all, it is wrong to think that protecting one's privacy for bitcoins acquired through KYC (Know Your Customer) is useless. The tools and methods for privacy on bitcoin are varied and serve different purposes. Using coinjoin transactions on bitcoin from KYC, for example, is not a bad idea. Of course, you need to be cautious with regulated exchange platforms to avoid having your account frozen or banned, but from a strictly technical standpoint, these practices are not incompatible. Coinjoin has the effect of disrupting a coin's history, which helps counter some of the chain analysis risks associated with KYC. Although it does not eliminate all risks, it is already a significant benefit.

Privacy on bitcoin should not be viewed in a binary way, as a distinction between "anonymous" bitcoins and others that are not. Owning bitcoins acquired through KYC does not mean that all is lost; on the contrary, the use of privacy tools may prove even more beneficial.

Conversely, acquiring bitcoin through a non-KYC method does not guarantee perfect privacy and does not exempt you from the need to take other protective measures. If you hold non-KYC bitcoin but reuse receiving addresses multiple times, your transactions can be tracked and grouped. The slightest connection to the world outside of bitcoin could compromise the one layer of privacy you had. Therefore, it is important to consider all tools and methods that improve privacy on Bitcoin as complementary. Each technique addresses a specific risk and can add an additional layer of protection. Thus, owning non-KYC bitcoin absolutely does not exempt you from taking other precautions.

### Can the KYC be cancelled?

I am sometimes asked if it is possible to "go back" after completing KYC and, as you can imagine from the preceding paragraphs, the answer is nuanced. To avoid the risks associated with KYC, the simplest method is not to use it when acquiring bitcoins. We will elaborate on this topic in the next chapter. However, if KYC has already been performed and bitcoins have been purchased, are there ways to mitigate the risks incurred?

As for the risk of tracking your transactions, the use of coinjoin is one solution. We will discuss this method in detail later in the training, but know that coinjoin can disrupt a coin's history and prevent its past-present and present-past traceability. Even for BTC obtained through a regulated platform, this technique can prevent its traceability.

However, coinjoin does not eliminate the second risk associated with KYC: the fact that the state is informed of your bitcoin holdings. In fact, even if your coins are no longer traceable, the state, depending on the jurisdiction, may have access to your crypto-active alienation statements. Since this risk is not technical but administrative, there are no bitcoin-specific solutions to eliminate it, other than initially avoiding exposure to KYC. The only legal approach to mitigate this risk is to sell your bitcoins acquired through regulated platforms on regulated platforms, and then buy them back through means without KYC. By selling and declaring the disposal, the administration should note that you no longer own them.

As for the risk of your personal data and identity documents being disclosed, this is a danger external to Bitcoin, and there is no technical solution to avoid it. Once your data has been disclosed, it is difficult to reverse this. You can try to close your account on the platform, but this does not guarantee the elimination of your KYC data, especially when identity verification is outsourced. Verifying the complete elimination of your information is impossible. Therefore, there is no solution to completely prevent this risk and ensure that it no longer exists.

### The difference between KYC and key identification

Sometimes, some bitcoiners tend to extend the term "KYC" to any BTC exchange involving a transfer or credit card payment, since these means can also reveal the origin of the payment, just as KYC would. However, it is important not to confuse KYC with key identification. Personally, I must admit that my perception of this topic has evolved over time.

KYC refers specifically to a regulatory procedure implemented by some companies to verify and record the identity of their customers. It is a binary issue: when you acquire your bitcoins, you either submit to KYC, or you do not. However, key identification, which is about linking an aspect of a user's identity to onchain activity, is not so binary but rather represents a continuum. Indeed, in the context of buying or selling bitcoin, this identification is always possible to varying degrees.

For example, if you buy bitcoin on a regulated platform in Switzerland, KYC (Know Your Customer) is not required. However, there may be an identification of your keys since the purchase was made through your bank account. This is where the first two risks associated with KYC arise - facilitating onchain tracking and exposure to government surveillance - which can also manifest in a non-KYC exchange. If the Swiss entity reports suspicious transactions to authorities in your country, they can simply check the bank account used for the purchase to discover your identity. Thus, buying without KYC on regulated platforms is quite high on the risk scale for key identification.

However, avoiding regulated platforms and opting for P2P (Peer-to-Peer) acquisition methods does not completely eliminate the risk of key identification but simply reduces it. Consider the example of a purchase on Bisq or another P2P platform. To settle with your counterpart, you will probably use your bank account. If the authorities question the person you traded with and ask for your name, we encounter risks 1 and 2 mentioned above. These risks are certainly much lower than a non-KYC purchase on a platform, and even lower than a purchase with KYC, but they are still present to a lesser extent.

Finally, even if you purchase your bitcoins through a physical cash exchange, you are not completely anonymous. The person you did business with saw your face, which is part of your identity. Although minimal in this example, the possibility of an identification key still exists.

In conclusion, during an exchange of bitcoin for other assets, whether it is a fiat currency purchase or a sale for a real asset, there is always a form of key identification. Depending on the exchange method chosen, this identification can vary in intensity. It is important not to confuse this identification with KYC, which is a well-defined regulatory process. However, there is a link between KYC and the identification spectrum, since KYC is at the upper end of this spectrum, as it systematically facilitates the identification of user keys by authorities.

## Sales and Acquisition Methods

<chapterId>756598af-95aa-4c77-ac48-243c7ad89530</chapterId>

After reading the previous chapter, you may be wondering how to buy or sell bitcoin without having to undergo an identity verification process in order to avoid the risks associated with KYC. There are several methods for making exchanges.

### P2P Exchanges in Cash

As we have seen, the best method in terms of privacy remains P2P (peer-to-peer) exchange with cash settlement. This method allows you to minimize the traces left behind and significantly reduces the possibility of key identification, whether you are a buyer or a seller.

However, this practice carries personal security risks. The main danger lies in the fact that, during the exchange, the counterparty will know that you hold a significant amount, either in cash or bitcoin. This information can attract the attention of malicious individuals. In fact, it is generally advised to remain discreet about the possession of bitcoin. This advice could also be applied to cash. However, during an in-person exchange, it is inevitable to disclose that you possess bitcoin, which can arouse greed.

To limit this risk, I recommend that you prioritize cash transactions with trusted people, such as family members or close friends. Alternatively, you might also consider doing exchanges at [local Bitcoin meetings](https://btcmap.org/communities/map), after attending several times. This will allow you to get to know the other participants better and not be alone during the physical exchange. However, it is important to recognize that P2P cash exchange inherently carries risks to your personal security that do not exist when making purchases through a regulated platform and your bank account.

Also, depending on where you live, transporting and storing large sums of money can pose risks, whether bitcoin or cash.

Exchanging cash can also pose legal risks during police or other checks. Although in most countries there is no restriction on the amount of cash you can carry, excessively large sums can arouse suspicion. Therefore, be cautious, especially if you have to travel long distances, and avoid transactions that are too large at once so that you do not have to justify the possession of significant sums.

Finally, another disadvantage of P2P purchases is that the price is often higher than that observed on regulated platforms. Sellers often impose a surcharge ranging from 1% to sometimes more than 10%. Several reasons explain this price difference. First, it is a common practice among P2P sellers that has been established over time. In addition, sellers have transaction fees associated with sending funds to the buyer. There is also a higher risk of theft in P2P sales than in platform transactions, which justifies a fee for the risk taken. Finally, the premium may be relative to demand and the quality of the exchange in terms of privacy. As a buyer, the privacy gain is priced into the surcharge charged by the seller. Some bitcoiners also believe that the increased price of BTC purchased in P2P reflects their true value and argue that the lower prices on regulated platforms are the result of a trade-off on the privacy of your personal information.

### P2P Exchanges via a Matching Platform

A less risky alternative in terms of personal security is to conduct P2P exchanges exclusively online, via electronic payment methods such as PayPal, bank transfers or Revolut.

This approach helps avoid many risks associated with cash transactions. However, the risk of the counterparty not honoring its commitments during an online exchange is greater. In fact, during a physical exchange, if you hand over money to the seller who does not send you bitcoins in return, you can immediately call him out on it since he is standing in front of you. Online, on the other hand, it is often impossible to find a person who has stolen from you.

To mitigate this risk, specialized matching platforms can be used for P2P exchanges. These platforms use conflict resolution mechanisms to protect aggrieved users. Generally, they offer an escrow system, where bitcoins are held until payment in fiat currency is confirmed by the seller.

In terms of personal security, this purchase method is significantly safer than physical cash exchanges. However, as mentioned earlier, online P2P exchanges leave more traces than a physical exchange, which can be detrimental to privacy on Bitcoin. By using an online fiat payment method such as a bank, you expose more information that could facilitate key identification.

Once again, I recommend against large trades in a single transaction on these platforms. By splitting your transactions, you spread the risks associated with potential theft by the counterparty.

Another disadvantage of P2P purchases is that the price is often higher than that observed on regulated platforms. Sellers often impose a surcharge ranging from 1% to sometimes more than 10%. Several reasons explain this price difference. First, it is a common practice among P2P sellers that has been established over time. In addition, sellers have transaction fees associated with sending funds to the buyer. There is also a higher risk of theft in P2P sales than in platform transactions, which justifies a fee for the risk taken. Finally, the premium may be relative to demand and the quality of the exchange in terms of privacy. As a buyer, the privacy gain is priced into the surcharge charged by the seller. Some bitcoiners also believe that the higher price of P2P-purchased BTC reflects its true value and argue that the lower prices on regulated platforms are the result of a trade-off on the privacy of your personal information.

As for solutions, I have personally always used [Bisq](https://bisq.network/) and am very satisfied with them. Their system is well established and seems reliable. However, Bisq is only available on PC and its interface may be too complex for beginners. Another disadvantage is that Bisq operates exclusively with onchain transactions, which can become expensive during periods of high transaction fees on Bitcoin.

-> Learn about our tutorial on Bisq.

https://planb.network/tutorials/exchange/peer-to-peer/bisq-fe244bfa-dcc4-4522-8ec7-92223373ed04
For an easier option, you can try [Peach](https://peachbitcoin.com/), a mobile app that facilitates the connection between buyers and sellers with an integrated dispute resolution system. The process is more intuitive than Bisq's.

-> Learn about our tutorial on Peach.

Another online option is [HodlHodl](https://hodlhodl.com/), a well-established platform that offers good liquidity, although I personally have not tested it.

-> Learn about our tutorial on HodlHodl.

https://planb.network/tutorials/exchange/peer-to-peer/peach-wallet-db64fe42-17ca-4b24-abb8-e7d4c03b2028
https://planb.network/tutorials/exchange/peer-to-peer/hodlhodl-d7344cd5-6b18-40f5-8e78-2574a93a3879
For Lightning Network-based solutions, you can try [RoboSats](https://learn.robosats.com/) and [LNP2PBot](https://lnp2pbot.com/). RoboSats is accessible via a website and is relatively simple to use. LNP2PBot is more atypical in that it operates through an exchange system on the messaging app Telegram.

-> Check out our tutorial on RoboSats.

-> Check out our tutorial on LNP2PBot.

https://planb.network/tutorials/exchange/peer-to-peer/robosats-b60e4f7c-533a-4295-9f6d-5368152e8c06
https://planb.network/tutorials/exchange/peer-to-peer/lnp2pbot-v2-e6bcb210-610b-487d-970c-7cce85273e3c
### Regulated platforms without KYC

Depending on the country you live in, you may have access to regulated platforms that do not require a KYC procedure to buy or sell bitcoin. In Switzerland, for example, you can use platforms such as [Relai](https://relai.app/) and [MtPelerin](https://www.mtpelerin.com/).

-> Learn about our tutorial on Relai.

As we saw in the previous chapter, this type of platform spares you the risks associated with KYC procedures, but they present a higher level of risk for key identification. In terms of privacy on Bitcoin, these platforms therefore offer better protection than KYC purchase methods, but are less attractive than P2P exchanges.

However, in terms of personal security, using these platforms is significantly less risky than P2P exchanges. They are also often easier to use than platforms that facilitate P2P exchanges.

https://planb.network/tutorials/exchange/centralized/relai-v2-30a9671d-e407-459d-9203-4c3eae15b30e
### ATM

Another option to buy or sell bitcoin without KYC are cryptocurrency ATMs (ATMs). Personally, I have never had the opportunity to test this solution, as there are none in my country. But this method can be very interesting depending on where you live.

The issue with ATMs is that they are prohibited in some countries or heavily regulated in others. If an ATM requires an identity verification process, then it faces the same risks as those inherent in regulated KYC platforms. However, if the ATM allows transactions without identity verification for small amounts, then its use can offer a level of privacy comparable to that of a cash-based P2P exchange, avoiding most of the risks associated with this type of exchange.

The main disadvantage of ATMs lies in their often high foreign exchange fees, ranging from a few percent sometimes up to 15 percent of the amount exchanged.

### Gift Cards

Finally, I also wanted to present a solution that works well for those who wish to use their bitcoins daily for purchases rather than selling them for fiat currencies.

The best way to spend BTC is obviously to use bitcoin directly or the Lightning Network to purchase goods or services. However, in many countries, the number of merchants accepting bitcoin remains limited. A practical alternative is therefore the use of gift cards.

Several platforms that do not require a KYC procedure offer the ability to exchange bitcoin for gift cards that can be used in major stores. These platforms include [CoinsBee](https://www.coinsbee.com/), [The Bitcoin Company](https://thebitcoincompany.com/), and [Bitrefill](https://www.bitrefill.com/). These platforms greatly facilitate the daily use of your bitcoins by allowing you to access a wide range of products and services without having to go through a fiat currency conversion.

https://planb.network/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1
### Other Methods of Acquisition

Among other methods of acquiring bitcoin while protecting your privacy is, of course, mining. To start mining sats, you do not need to reveal your identity; simply find a valid proof of employment and submit it to the network. If you opt for pooled mining, some pools require a form of identification, such as KYC, while others do not.

Another method is to work in exchange for bitcoin. This method of acquisition can be attractive, but the degree of identification required varies greatly depending on the circumstances.

\To write this chapter, I used the BTC205 course created by [@pivi\_\_](https://x.com/pivi___) on the Plan ₿ Network (available only in French for the time being).\_

## Consolidation, UTXO and CIOH Management

<chapterId>d0486c8f-332d-402b-ae2e-949416752b9c</chapterId>

One of the most complicated aspects to manage when you have your own self-storage portfolio is undoubtedly consolidation. Should you consolidate? What is the purpose? What size of UTXO should you seek to achieve? What are the privacy tradeoffs? That is what we will try to explore in this section.

### What is consolidation?

The operation of Bitcoin is similar to an auction market where transactions offering the best fees are favored by miners. However, each block has a maximum weight, limiting the number of transactions that can be included. Since a block is produced on average every 10 minutes, the space available in each block is a rare resource.

Miners, whose business involves significant costs in terms of electricity, capital and maintenance, naturally seek to maximize their profitability. They tend to favor transactions that offer them the highest fees relative to their weight.

In fact, not all Bitcoin transactions weigh the same. Those with more input and output will weigh more. For example, consider 2 transactions:


- Transaction A includes 1 input and 1 output. It assigns 1,994 sats of fees and its weight is 141 vB;
- The more complex transaction B, with 2 inputs and 2 outputs, allocates 2,640 sats of commissions for a weight of 220 vB.

In the example, although transaction B proposes a higher commission total, miners will favor transaction A because it offers a better commission-to-weight ratio. Here is the calculation for each transaction, expressed in sats per virtual byte (sat/vB):

```text
TXA: 1994 / 141 = 14 sat/vB
TXB: 2640 / 220 = 12 sat / vB
```

This means that for each unit of weight, transaction A offers more fees than transaction B, even though the latter offers more fees in absolute value.

Therefore, it is increasingly attractive for the user to consume the minimum possible amount of input in their transactions. However, it is necessary to consume sufficient quantities in order to satisfy the output payment. In managing one's portfolio, it is therefore necessary to have sufficiently large UTXOs.

The principle of consolidation is precisely to take advantage of periods when fees on Bitcoin are low to merge one's small UTXOs into one larger UTXO. Thus, when fees on Bitcoin rise, one can transact with minimal input, and thus spend less in absolute fees. The goal is to plan for mandatory transactions to be made during periods of high commissions.

In addition to saving on transaction fees, consolidating UTXOs helps avoid the creation of "dust." Dust refers to UTXOs whose value in sats is so low that it is not sufficient to cover the transaction fees required to spend them. This makes these UTXOs economically irrational to use as long as transaction fees remain high. By proactively grouping your UTXOs, you prevent them from turning to dust, ensuring that all your funds remain usable.

### What is the minimum size for your UTXOs?

Sometimes, I am asked what is the minimum recommended value for a UTXO. Unfortunately, there is no universal answer, as it depends on your preferences and market conditions for commissions. However, here is a formula that can help you determine a threshold that suits your needs:

$$
\frac {P \times F}T = M
$$

Where:


- $P$ is the weight of the transaction;
- $F$ represents the maximum rate in satoshi per vbyte (sats/vB) that you are willing to cover;
- $T$ is the percentage of the transaction fee you are willing to pay relative to the total value of the UTXO;
- $M$ is the minimum amount in satoshi for each UTXO.

Assuming you want to cover the commissions for a standard SegWit transaction with 1 input and 2 outputs, weighing 141 vB. If you cover up to 800 sats/vB, and you are willing to spend up to 12 percent of the UTXO value in commissions at most, then the calculation would be:

$$
\frac{141 \times 800}{0.12} = 940\ 000
$$

In this example, it would be wise to maintain a minimum value of 940,000 sat for UTXOs in your portfolio.

### Consolidation and the COIH

One of the most widely used heuristics in blockchain analysis is the COIH (_Common Input Ownership Heuristic_), which allows us to assume that all inputs to a Bitcoin transaction belong to the same entity. Precisely, the principle of consolidation is to consume several UTXOs as input and create a single UTXO as output. Therefore, consolidation allows the application of COIH.

![BTC204](assets/fr/097.webp)

In practice, this means that an outside observer can infer that all the consolidated UTXOs probably belong to the same person and that the only output generated belongs to them as well. This situation can compromise your privacy by linking different transaction histories. For example, say I consolidate 3 UTXOs acquired in P2P with one UTXO obtained through a platform that requires KYC:

![BTC204](assets/fr/098.webp)

By doing so, any entity with access to exchange platform data, potentially including government agencies, can identify that I hold other amounts in BTC. Previously, these UTXOs were not directly linked to my identity; now they are. Furthermore, this reveals to all sources that I am in possession of a certain amount of bitcoin.

In managing UTXOs, economic considerations, which push for consolidation to reduce fees, thus conflict with good privacy practices, which would recommend never merging your UTXOs. The choice between economics and privacy thus depends on each user's priorities.

If you can avoid consolidation while maintaining substantial sizes of UTXOs, that is ideal. To do this, optimize your acquisition methods. If you buy your bitcoins in DCA, try to space your one-time purchases as widely as possible to group value into fewer UTXOs. It will be easier to manage a one-time purchase of €1,000 every 2 months than a €120 purchase every week. This minimizes the number of UTXOs generated and simplifies the management of your portfolio while preserving your privacy.

If you find yourself in need of consolidating your bitcoins, prioritize the consolidation of UTXOs from the same source. For example, merging 10 UTXOs from a single platform will have less impact on your privacy than mixing 5 UTXOs from platform A with 5 UTXOs from platform B. If consolidation from various sources is unavoidable, try to separate them according to their characteristics. For example, group UTXOs acquired through KYC into one transaction, and those obtained in P2P into another.

In any case, remember that any consolidation inevitably leads to a loss of privacy. Therefore, carefully assess the need for this and the potential impacts on your privacy, taking into account the risk.

## Other Good Practices

<chapterId>b5216965-7d13-4ea1-9b7c-e292966a487b</chapterId>

Let's explore together some other best practices that can help you optimize your privacy on Bitcoin.

### The Complete Knot

Having your bitcoins in personal custody is good, but using your own full node is better! This is why having your own node is crucial for fully sovereign use of bitcoin:


- Resistance to Censorship**: Your transactions cannot be blocked by anyone;
- Independence from Third Parties**: You no longer depend on any external service to verify blockchain data;
- Active Participation**: You have the ability to set your own validation rules and participate directly in consensus;
- Contribution to the Network**: By running a node, you help strengthen and distribute the Bitcoin network;
- Technical Education**: Running a full node is a great way to deepen your technical knowledge about Bitcoin.

In addition to these benefits, using a full node also improves your privacy when you transmit your transactions. When you issue a transaction, it is first created and signed through your wallet. To transmit it on the Bitcoin network, it must be known to at least one node. By using your own node, you directly control this transmission, thus improving your privacy and limiting the risk of data loss.

![BTC204](assets/fr/099.webp)

If you do not have your own Bitcoin node, you will be forced to use that of a third party, such as one offered by your wallet software provider. In addition to transaction transmission, your wallet requires access to various information such as pending transactions, balances associated with your addresses, or the number of confirmations for your transactions. To access all this data, you need to query a node.

![BTC204](assets/fr/100.webp)

The main risk when you do not use your Bitcoin node is that the third-party node operator may observe your activities on the blockchain, or even share this information with other entities. To limit this risk, an intermediate solution is to use wallet software that allows you to mask your connections via Tor. This can reduce the exposure of your data. However, the optimal solution remains to have your own Bitcoin node and use it to transmit your transactions. Of course, you will also have to make sure that no information leaks out of your node, but that is another topic we will explore in the following sections.

In addition to the obvious benefit to your privacy, having your own full node also ensures the veracity of data on the blockchain, protects against censorship, and allows you to actively participate in Bitcoin governance. By using your own node, you contribute your economic weight to the blockchain of your choice, which is important during conflicts within the community, such as during the Block Size War from 2015 to 2017, for example. In the event of a fork, using a third party's node could lead you to support a chain you do not wish to favor, as the node operator makes the choice for you. As you can understand, from a privacy and more general individual sovereignty perspective, it is essential to run and use your own full node!

### Deceiving Analysis Heuristics

More generally, it is important to understand the heuristics we discussed in the previous section in order to better avoid or deceive them. Adopting a number of best practices can prove beneficial, even if they are not essential. They offer an additional layer of protection that can be important for maintaining good privacy when using Bitcoin.

The first piece of advice I might give is to blend into the densest crowd. On Bitcoin, this means using the most widely adopted script templates. For example, P2WSH scripts, often used for multisig SegWit V0 configurations, are very rare. They do not allow you to hide in a large set of anonymity. The same is true for older models such as P2PKH or P2SH. Although they are widely present in the UTXO set, they are used less and less for new transactions.

In general, it is safer to move toward the latest script standard, as long as it is sufficiently adopted. Thus, while in 2022 I would have advised against the use of P2TR (Taproot) because of its low adoption, by 2024 I would recommend opting for this type of script, or failing that, for the SegWit V0 script, since the number of transactions using P2TR is beginning to represent a very significant portion.

Source:[txstats.com](https://txstats.com/d/000000054/utxo-set-repartition-by-output-type)

Another tip for preserving your privacy is to try to circumvent internal transaction heuristics. For example, when you make a payment, you might try to avoid creating an output with a round amount, as this might signal that the other output represents change. If you have to send 100k satoshi to a friend, consider transferring a slightly higher amount to escape this heuristic. Similarly, try not to create remainder outputs that are disproportionately high compared to the payment made, as this could also reveal which of the outputs represents remainder.

Finally, if you conduct Bitcoin transactions regularly, make sure that you do not always transmit them at the same times. By distributing the transmission of your transactions throughout the day and week, you avoid giving outside observers the ability to detect a time pattern based on time zones that could improve their analysis.

In addition to all of these best practices to adopt on a daily basis, there are even more effective methods to completely break the traceability of your bitcoins. These include, of course, coinjoin transactions, which we will study in depth in the following section.

# Understanding Coinjoin Transactions

<partId>6d0bbf16-3714-4db1-9897-2d45019f6bdc</partId>

## What is a Coinjoin Transaction?

<chapterId>0862bc6b-1c48-4aa4-b76d-4f547b469008</chapterId>

Having studied the basics of privacy protection, we will now discuss more sophisticated techniques aimed at actively defending your privacy, particularly by disassociating your bitcoin history. In the next part, we will explore many small techniques, but first I want to tell you about coinjoin.

Coinjoin is often considered the most effective way to protect the privacy of Bitcoin users. But what exactly is a coinjoin transaction? Let's find out together.

### The Basic Principles of Coinjoin

Coinjoin is a technique that disrupts the tracking of bitcoins on the blockchain. It is based on a collaborative transaction with a specific structure of the same name: the coinjoin transaction.

As we saw in the first parts of this training, transactions on Bitcoin are known to all users via their node. It is therefore easy to verify the electronic signature chain of each coin and observe its history. This means that all users can attempt to analyze other users' transactions. As a result, anonymity at the transaction level is impossible. However, anonymity is preserved at the level of individual identification. Unlike traditional banking where each account is linked to a personal identity, on Bitcoin, funds are associated with cryptographic key pairs (or scripts), thus offering users a form of pseudonymity behind cryptographic identifiers.

![BTC204](assets/it/51/01.webp)

Thus, confidentiality on bitcoin is compromised when outside observers are able to associate specific UTXOs with identified users. Once this association is established, it becomes possible to track their transactions and analyze their bitcoin history. Coinjoin is precisely a technique developed to disrupt the tracking of UTXOs in order to provide some level of confidentiality to Bitcoin users at the transaction level.

Coinjoins improve the confidentiality of Bitcoin users by complicating chain analysis for outside observers. Their structure allows several coins from different users to be merged into a single transaction, thus obfuscating traces and making it difficult to determine links between input and output addresses.

It is important to understand that the goal of a coinjoin transaction is to disrupt a coin's history. This technique does not confer permanent anonymity or permanently stop the traceability of bitcoins, contrary to what one might think. Coinjoin only aims to interrupt history at the point where the coinjoin transaction is performed. However, before and after this transaction, the coin remains subject to the same privacy risks.

![BTC204](assets/fr/104.webp)

### How do coinjoins work?

The principle of coinjoin is based on a collaborative approach: several users who wish to mix their bitcoins deposit identical amounts into the inputs of the same transaction. These amounts are then redistributed in outputs of equal values to each user.

![BTC204](assets/fr/105.webp)

At the end of the transaction, it becomes impossible to associate a specific output with a known user input. There is no direct link between inputs and outputs, which breaks the association between users and their UTXOs, as well as the history of each coin.

![BTC204](assets/fr/106.webp)

Let's take the example of Alice. She wants to send about 100,000 satoshi (sats) to her sister Eve for her birthday. However, Alice does not want Eve to be able to track her transaction history because she does not want to reveal how many bitcoins she owns or how she obtained them. To do this, Alice decides to disrupt her UTXO history with a coinjoin transaction. She arranges with Bob, Charles, David, and Frank to conduct a collaborative transaction: Alice, Bob, Charles, David, and Frank each pledge a UTXO of 105,000 sats (with 5,000 sats for mining fees) as input for the transaction:

![BTC204](assets/fr/107.webp)


- In return for using these inputs, each generates a new address to create five identical outputs of 100,000 sats each. Each participant retrieves one output:

![BTC204](assets/fr/108.webp)


- Alice ends up with a UTXO of 100,000 sats whose history is mixed. She uses this UTXO in a new transaction to send the amount to Eve for her birthday:

![BTC204](assets/fr/109.webp)


- If Eve tries to analyze this transaction to extract information, she will come across the coinjoin transaction involving Alice, Bob, Charles, David, and Frank. Since Eve cannot distinguish to whom each input belongs because of the uniformity of the amounts, she cannot trace the history of Alice's UTXO or determine how many bitcoins her sister owns or how she acquired them:

![BTC204](assets/fr/110.webp)

In this scenario, Alice used the coinjoin technique to increase her privacy against backward analysis. In fact, Alice protects herself against a possible analysis by Eve that would start from a specific transaction to trace the history of the UTXO backwards. This protection against analysis from the present to the past is what we call retrospective anonset. We will explore this concept in more detail in the last chapters of this part.

However, coinjoin also offers the possibility of improving privacy against past-to-present analysis, what is called prospective anonset. Let us return to our example where Alice sent 98,000 sats to Eve on her birthday, but reversing the roles. Let us now imagine that it is Eve who is concerned about her privacy. In fact, Alice might be tempted to follow the coin she sent to Eve to gather information. Eve could consolidate this newly received UTXO with all her other UTXOs, which could reveal to Alice the amount of bitcoin she holds in her wallet. To avoid this, Eve can also disrupt the history of the newly received coin.


- Eve, Grace, Mallory, Oscar and Victor each put a UTXO of 98,000 sats as input into a Bitcoin transaction:

![BTC204](assets/fr/111.webp)


- In exchange for using these inputs, each provides a new address to create 5 outputs of 97,500 sats each, perfectly equal. Each user retrieves one output:

![BTC204](assets/fr/112.webp)


- Eve now holds a UTXO of 97,500 sats with a broken history. She can use it without fear for future transactions. In fact, if Alice tries to follow the bitcoins she sent to Eve, she will come across a coinjoin transaction. She will not be able to determine to which UTXO output Eve belongs. Analysis then becomes impossible:

![BTC204](assets/fr/113.webp)

In the first example, we saw how coinjoin can protect the privacy of a coin in relation to its past, and in the second example, how it can also secure the history of a coin in relation to its future. That is why I mentioned that coinjoin should be seen as a one-time event that segments a coin's history in both directions:

![BTC204](assets/fr/104.webp)

### Mixing, coinjoins, mixers... What is the difference?

The term "mixing" is sometimes used to describe coinjoins, a term that some bitcoiners reject because they fear confusion with custodial mixers. However, I think this apprehension is unfounded because, in a mathematical context, coinjoin precisely embodies the concept of mixing.

In the general field of mathematics, mixing refers to the property of a dynamical system where, after a certain time, all portions of the initial space can theoretically be mixed with any other portion. Mixing implies that the position of a particle or the state of a system evolves in such a way that its future distribution is independent of its initial distribution, thus reaching a state where the characteristics of the initial state are uniformly distributed in the space of the system. This is exactly what happens in a coinjoin with bitcoins. So, in my opinion, coinjoin is really a coin mixing method.

![BTC204](assets/fr/114.webp)

However, it is important to distinguish coinjoins from mixers. A mixer is a service where users send their bitcoins to be mixed. These services were popular during the 2010s, but their use has declined due to two major disadvantages compared to coinjoin:


- They require users to relinquish custody of their funds during the mixing process, exposing them to risk of theft;
- There is no guarantee that the mixer will not record transaction details, or even sell this information to blockchain analytics companies.

![BTC204](assets/fr/115.webp)

Today, users therefore prefer coinjoin, as it allows them to maintain full control over their funds throughout the process. Participants in a coinjoin do not risk having their bitcoins stolen by other parties involved. Let us explore together how this is possible in the next chapter.

## Zerolink and Chaumian Coinjoins

<chapterId>326c9654-b359-4906-b23d-d6518dd5dc3e</chapterId>

The privacy provided by a coinjoin is based on the size of the group in which our piece is hidden. Therefore, it is necessary to find as many participants as possible. It is entirely possible to run a coinjoin manually, with independently found users, but this method is complex and does not allow for large anonsets.

This is why coinjoin coordinators have developed on Bitcoin. Their role is to connect different users and transmit the information necessary for the successful completion of the collaborative transaction.

![BTC204](assets/fr/116.webp)

But how can we ensure that the coordinator never has control over users' bitcoins, and although he or she is the person who constructs the coinjoin transaction, how can we ensure that he or she cannot link users' inputs and outputs, which could be a loss of privacy?

### Chaum's Blind Signatures

Modern coinjoin implementations use David Chaum's blind signatures to prevent information leakage. Let's quickly study together how these blind signatures work.

Chaum blind signatures are a form of digital signature in which the issuer of a signature does not know the content of the message it is signing. However, the signature can be verified later with the original message. This technique was developed by cryptographer David Chaum in 1983.

Take the example of a company that wishes to authenticate a confidential document, such as a contract, without revealing its contents. The company applies a masking process that cryptographically transforms the original document in a reversible way. This modified document is sent to a certification authority that applies a blind signature without knowing the underlying content. After receiving the signed document, the company removes the masking from the signature. The result is an original document authenticated by the authority's signature, without the authority ever having seen the original content.

Chaum's blind signatures thus enable certification of the authenticity of a document without knowing its contents, ensuring both the confidentiality of the user's data and the integrity of the signed document.

### Chaumian Coinjoins

In "Chaumian CoinJoins," the use of Tor and David Chaum's blind signatures are combined to ensure that the coordinator cannot know which user each output belongs to. The process of coinjoin transaction construction consists of 3 main steps: input registration, output registration, and transaction signing. Let us examine this process through the example of Alice, one of the coinjoin participants. All other participants follow the same steps as Alice, each on their own.

**Step 1: Registration of inputs.**


- Alice sends the coordinator the UTXO she wants to use as input for the transaction, as well as the masked receiving address she wants to use as output to receive her bitcoins. Therefore, the coordinator cannot know Alice's address. It only sees her masked version.
- The coordinator verifies the validity of the inputs, then signs Alice's masked address with her private key. He then sends Alice the blind signature.

**Step 2: Recording outputs.**


- Alice can now remove the masquerade from her address signed by the coordinator's private key. She establishes a new connection under a different Tor identity. The coordinator cannot identify that it is Alice connecting under this new identity.
- Alice sends the undisguised address and signature to the coordinator (who still does not know it is Alice).

**Step 3: Sign the transaction.**


- The coordinator similarly retrieves unmasked outputs from all participants. With the associated signatures, he can verify that each output sent anonymously was actually signed by his private key previously, ensuring its legitimacy. It is then ready to construct the coinjoin transaction and sends it to the participants for them to sign.
- Alice, like the other participants, verifies that her input and output are correctly included in the transaction constructed by the coordinator. If everything is satisfactory, she sends the signature that unlocks the script of her input to the coordinator.
- After collecting signatures from all coinjoin participants, the coordinator can transmit the transaction over the Bitcoin network so that it can be added to a block.

In this system, the coordinator is unable to link an input to a specific output. In addition, he cannot take possession of participants' funds, since he never has access to the private keys needed to unlock their UTXOs. Throughout the process, and until the end of step 3, he does not even have access to the signatures. When Alice and the other participants sign the global transaction, after verifying that everything is correct, the coordinator can no longer modify this transaction, including the outputs, without invalidating it. This thus prevents bitcoin theft by the coordinator.

Ultimately, when they register their output in the transaction, the coinjoin user desires guarantees similar to those of a citizen voting in an election. There is a duality between the public and private aspects of these actions. On the one hand, there is what you want to keep private: for the voter, they do not want their ballot to be linked to their identity; for the coinjoin user, they do not want their output to be associated with their input. In fact, if the coordinator, or any other party, manages to establish a link between an input and an output, coinjoin loses its entire purpose. As explained earlier, the coinjoin must function as a break in the history of a coin. This pause occurs precisely because of the inability to associate a specific input with a specific output in the coinjoin transaction (prospective anonset) and vice versa (retrospective anonset).

On the other hand, there is the public aspect: the voter wants to make sure that their ballot is included in the ballot box; similarly, the coinjoin user wants to make sure that their output is included in the coinjoin transaction. In fact, it is absolutely necessary for coinjoin participants to be able to verify the presence of their output before signing the transaction, otherwise the coordinator could steal the funds.

It is precisely these 2 public and private aspects, made possible by the use of David Chaum's blind signatures, that assure Chaumians coinjoin participants that their bitcoins will not be stolen, and that their funds cannot be traced.

### Who invented the concept of coinjoin?

It is difficult to determine with certainty who first introduced the idea of coinjoin on Bitcoin, and who came up with the idea of using David Chaum's blind signatures in this context. It is often thought that it was Gregory Maxwell who first mentioned it in [a post on BitcoinTalk in 2013](https://bitcointalk.org/index.php?topic=279249.0):

Using Chaum's Blind Signatures: Users connect and provide input (and addresses for the rest) as well as a cryptographically obscured version of the address to which they wish to send their private coins; the server signs the tokens and returns them to the users. Users reconnect anonymously, reveal their output addresses, and send them back to the server. The server can see that all outputs have been signed by it and that, as a result, all outputs are from valid participants. Later, people reconnect and sign.

Maxwell, G. (2013, August 22). _CoinJoin: Bitcoin's privacy for the real world_. BitcoinTalk Forum. https://bitcointalk.org/index.php?topic=279249.0

However, there have been previous mentions of both Chaum signatures in the context of mixing and coinjoins. [In June 2011, Duncan Townsend presented on BitcoinTalk](https://bitcointalk.org/index.php?topic=12751.0) a mixer that uses Chaum signatures in a manner quite similar to modern Chaumians coinjoins.

In the same thread, there is [a hashcoin message in response to Duncan Townsend](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793) to improve his mixer. The process described in this message represents precisely what is closest to coinjoins. A similar system is also mentioned in [a message from Alex Mizrahi in 2012](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry), as he was advising the creators of Tenebrix, one of the first altcoins that served as the basis for the creation of Litecoin later on. Even the term "coinjoin" itself was not invented by Greg Maxwell, but came from an idea of Peter Todd.

![BTC204](assets/fr/125.webp)

### Zerolink

Zerolink is a comprehensive mixing protocol that integrates Chaumiani coinjoins and various strategies to protect user anonymity against various forms of chain analysis, greatly reducing errors related to wallet management. This protocol [was introduced by nopara73 and TDevD in 2017](https://github.com/nopara73/ZeroLink/blob/master/README.md).

![BTC204](assets/fr/126.webp)

As the name suggests, the principle of Zerolink is to perform coinjoin transactions that ensure that links between inputs and outputs cannot be traced. This feature is achieved by ensuring that all outputs have perfectly identical amounts.

![BTC204](assets/fr/127.webp)

An important preventive measure by Zerolink involves the complete separation of unmixed UTXOs from mixed UTXOs using separate sets of cryptographic keys, or even separate wallets. In this way, the "pre-mix" wallet, intended for coins before mixing, is differentiated from the "post-mix" wallet, reserved for coins that have been mixed.

![BTC204](assets/fr/128.webp)

This strict separation of UTXOs serves primarily to prevent accidental associations between a mixed and an unmixed UTXO. In fact, if such links occur, the effectiveness of coinjoin on the blended UTXO is nullified without the user's knowledge, thus compromising the confidentiality of a UTXO whose history was believed to have been broken. These links can arise either through address reuse to secure a mixed UTXO with an unmixed one, or by applying Common Input Ownership Heuristics (CIOH) if the user consumes mixed and unmixed UTXOs as inputs to the same transaction. By separating pre-mixing and post-mixing portfolios, these accidental associations are avoided and the user is protected against unintentional errors.

![BTC204](assets/fr/129.webp)

This separation also offers the possibility of applying distinct rules between pre-mixing and post-mixing portfolios at the level of the portfolio software. For example, in the post-mixing portfolio, the software can prohibit the merging of input UTXOs to prevent the application of CIOH that would compromise user anonset. It is also possible to standardize the use of scripts and transaction options (such as RBF signaling, for example) to prevent identification by wallet fingerprinting.

Currently, Whirlpool is the only coinjoin implementation that strictly enforces the Zerolink protocol. In the following chapter, we will explore the different existing coinjoin implementations and the advantages and disadvantages of each.

## Coinjoin implementations

<chapterId>e37ed073-9498-4e4f-820b-30951e829596</chapterId>

_In 2024, we are seeing significant changes in the tools available to users who wish to run coinjoins on Bitcoin. We are currently in a crucial period, and the coinjoin market is undergoing a major restructuring. Therefore, this chapter will likely be updated over time._

For the time being, there are mainly 3 different implementations of coinjoin on Bitcoin:


- Whirlpool;
- Wabisabi;
- JoinMarket.

Each of these implementations aims to break the history of UTXOs through coinjoin transactions. However, their mechanisms vary significantly. Therefore, it is essential to understand how each works in order to choose the option that best suits your needs.

### JoinMarket

JoinMarket, created in 2015 by Adam Gibson and Chris Belcher, differs from other coinjoin implementations because of its unique user-matching model. This system is based on a P2P exchange marketplace where some users, the "makers," make their bitcoins available for mixing, while others, the "takers," use these funds to execute coinjoins in exchange for a fee.

![BTC204](assets/fr/130.webp)

In this model, "makers" leave their bitcoins available to "takers" and receive fees in exchange for their service. The "takers," on the other hand, pay to use the "makers'" bitcoins to conduct their own coinjoin transactions. Service fees vary according to role: "makers" accumulate fees for their liquidity offerings, while "takers" pay commissions. This marketplace operates freely without conditions of use.

A major disadvantage of JoinMarket is its complexity of use, which requires some familiarity with terminals to exploit it effectively. Although this complexity is not a barrier to an experienced user, it can limit access to the general public. However, the recent introduction of a web interface called JAM has somewhat facilitated its use.

![BTC204](assets/fr/131.webp)

Source: [JAM](https://github.com/joinmarket-webui/jam/blob/devel/docs/assets/screenshot-dark.webp)

However, the technical barrier remains a major obstacle. In the coinjoin ecosystem, where confidentiality is enhanced by the number of participants, any limitation that reduces accessibility directly affects available liquidity, which is a crucial factor in mixing efficiency. Bitcoin, already a niche in financial transactions, sees the use of coinjoins as a sub-niche, and JoinMarket represents an even more specialized fraction, thus limiting its potential to increase the anonsets of its users.

Despite its innovative P2P matching model for coinjoins, JoinMarket has some significant drawbacks, especially in terms of transactional structure. Unlike other implementations such as Whirlpool, JoinMarket does not guarantee perfect equality between outputs, and deterministic links can be drawn between inputs and outputs. It also lacks tools to prevent already mixed coins from being mixed again, which could compromise the confidentiality sought by users. Finally, although the concept of JoinMarket is attractive, especially to those interested in a dynamic liquidity market, its structural weaknesses and technical complexity make it, in my opinion, less attractive, both to novices and experts seeking coinjoin implementation.

### Wabisabi

Wabisabi is another implementation of coinjoin, with an approach that centralizes the coordination of transactions. This model was designed by Ádám Ficsór (nopara73), Yuval Kogman, Lucas Ontivero, and István András Seres in 2021, and was integrated into Wasabi 2.0 software the following year. Wabisabi precisely represents an evolution of the coinjoin model of the Wasabi software launched in 2018.

In the late 2010s, Wasabi adopted a transactional structure for its coinjoins that was radically different from Whirlpool's. To increase the anonsets of its participants, Wasabi used very large coinjoin transactions that grouped dozens of participants. In contrast, Whirlpool opted for multiple small transactions, allowing an exponential increase in anonsets with each cycle.

The methods for handling the remainder also distinguished the two implementations. With Whirlpool, the remainder was excluded and isolated from UTXOs before coinjoin cycles by TX0, a concept I will explain further in the next chapter. By Wasabi, on the other hand, the remainder formed one of the outputs of the coinjoin transaction, maintaining deterministic links between some inputs and outputs.

With Wabisabi, version 2.0 of Wasabi has adapted its approach to coinjoins to approximate that of Whirlpool. Although coinjoin transactions remain very large, it is now possible to chain several successive rounds, thus following Whirlpool's model. A special effort has also been made on the management of the change: unlike Wasabi 1.0, where the change was directly linked to user input, Wabisabi tries to divide the change into several small amounts, distributed in equal denominations for all participants.

We will illustrate this with a simplified example involving only 2 users: Alice wants to mix 115,000 sats and Bob, 210,000 sats. Ignoring commissions, with Wasabi 1.0, a coinjoin transaction would have generated 3 outputs of 100,000 sats, plus 1 remainder of 15,000 sats for Alice and 1 remainder of 10,000 sats for Bob. The remainder outputs would always be linked to the inputs:

Under Wabisabi, the same transaction would produce 3 outputs of 100,000 sats and 5 outputs of 5,000 sats, thus dispersing the remainder so that it is not directly traceable to a specific input:

Personally, I believe that change management in Wabisabi presents several risks that could compromise its effectiveness in terms of privacy:


- When a user contributes a UTXO significantly larger than those of other participants, he inevitably ends up with an amount of change that will be linked to his input. This goes against the initial goal of the protocol, which aims to eliminate any identifiable change;
- Multiplication of designations in order to fragment the rest can paradoxically harm mixing efficiency. This process can lead to a decrease in anonsets for certain outputs as they become more easily identifiable;
- This method also generates low-value UTXOs that pose a management problem for the user. These small UTXOs, if they become too expensive to spend relative to their value, can become "dust." This phenomenon prompts the user to merge several input UTXOs in their future transactions or to consolidate them. In either case, due to COH, this can decrease the anonsets obtained or completely cancel out the privacy benefits gained from the initial coinjoin.

Unlike Whirlpool, which implements the ZeroLink protocol by ensuring strict segregation between UTXO pre-mix and post-mix, Wabisabi does not maintain this strict segregation. There have also been problems with address reuse by some of Wasabi's customers, which is obviously very harmful to the user.

In version 2.0 of Wasabi, a new coinjoin pricing policy was implemented. Now, coordinator fees are set at 0.3 percent for UTXOs larger than 0.01 bitcoin, while for smaller UTXOs, these fees are completely zeroed out. In addition, remixes for these smaller UTXOs are free, although mining fees remain for all transactions, including remixes.

This policy contrasts with that of Whirlpool, where commissions remain fixed, regardless of the size of anonsets obtained. With Wasabi 2.0, although coordinator commissions are reset to zero for small UTXOs, the user still has to pay mining commissions on all transactions, including remixes.

At the time of writing, the use of Wabisabi has become considerably more complex as a result of recent events. Indeed, after the arrest of the founders of Samourai Wallet, zkSNACKs, the company that finances and manages the development of Wasabi, announced the termination of its coinjoin coordination service on June 1, 2024. This coordinator, which was set to default to Wasabi, had the vast majority of the liquidity.

With the closure of this main coordinator, users must now connect to new independent coordinators. This change raises concerns: on the one hand, the new coordinators may not have sufficient liquidity, thus reducing the effectiveness of coinjoins in terms of privacy. On the other, there is a risk of encountering a malicious coordinator. This situation adds significant new risks for those seeking to use Wabisabi.

In addition to technical issues, the decision by zkSNACKs, the company behind Wasabi, to use the services of a blockchain analytics company to filter participants into coinjoins raises serious ethical and strategic questions. The initial idea was to prevent the use of coinjoins on Wasabi by criminals, a move that may seem legitimate. However, it raises a paradox: paying fees to a coordinator, whose main mission is to increase user privacy, only to then fund a company whose goal is to compromise that same privacy.

Even more troubling is the principle of filtering, which contrasts sharply with Bitcoin's philosophy of providing an open and uncensored financial system. Although it may seem justified to want to exclude criminal activity, this filtering could also target individuals whose actions, although classified as illegal in some contexts, might be morally justifiable or socially beneficial. The example of Edward Snowden illustrates this dichotomy perfectly: considered a criminal by some governments for his revelations, he is seen by others as a whistleblower who acted in the public interest. This complexity underscores the potential danger of filtering, which, although it starts with a good intention, could ultimately harm the rights and security of legitimate users. I could also have mentioned persecuted activists and journalists under certain authoritarian regimes. As you may have guessed, my preference is undoubtedly for the Whirlpool model for conducting coinjoins on Bitcoin. This system stands out for its rigor and offers superior guarantees in terms of privacy. It is also the only one to propose a mixing that is considered perfect in a mathematical context. In my opinion, this model represents the future of coinjoins on Bitcoin. I therefore invite you to explore this model in more depth in the next chapter.

## The Operation of Whirlpool

<chapterId>bdbd7109-e36d-4b4f-a3c6-928df4e9bfda</chapterId>

Whirlpool differs from other coinjoin methods by using "_ZeroLink_" transactions, which ensure that there is technically no possible connection between all inputs and all outputs. This perfect mixing is achieved through a structure in which each participant contributes an identical amount in input (with the exception of mining fees), thus generating outputs of perfectly equal amounts.

This restrictive approach on inputs gives Whirlpool's coinjoin transactions a unique characteristic: the total absence of deterministic links between inputs and outputs. In other words, each output has an equal probability of being attributed to any participant, relative to all other outputs in the transaction.

![BTC204](assets/fr/136.webp)

### The General Operation of Whirlpool

Initially, the number of participants in each Whirlpool coinjoin was limited to 5, with 2 new entrants and 3 remixers (we will explain these concepts later). However, the increase in fees for on-chain transactions observed in 2023 prompted Samourai's teams to rethink their model to improve privacy while reducing costs. Thus, taking into account the commission market situation and the number of participants, the coordinator can now organize coinjoins that include 6, 7, or 8 participants. These enhanced sessions are designated under the name "_Surge Cycles_." It is important to note that regardless of the configuration, there are always only 2 new entrants in Whirlpool coinjoins.

Thus, Whirlpool transactions are characterized by an identical number of inputs and outputs, which can be:


- 5 inputs and 5 outputs;

![BTC204](assets/fr/137.webp)


- 6 inputs and 6 outputs;

![BTC204](assets/fr/138.webp)


- 7 inputs and 7 outputs;

![BTC204](assets/fr/139.webp)


- 8 inputs and 8 outputs.

![BTC204](assets/fr/140.webp)

Whirlpool's proposed model is thus based on small coinjoin transactions. Unlike Wabisabi and JoinMarket, where the robustness of anonsets is based on the volume of participants in a single cycle (or a few cycles), Whirlpool relies on the concatenation of multiple small cycles. In this model, users incur costs only at their initial entry into a pool, allowing them to participate in a multitude of remixes at no additional cost. It is the new entrants who cover the mining costs for the remixers.

With each additional coinjoin in which a coin participates, along with its peers encountered in the past, the anonsets will grow exponentially. The goal, then, is to take advantage of these free remixes, which, with each occurrence, help to strengthen the density of anonsets associated with each coin mix.

Whirlpool was designed with two important requirements in mind:


- The accessibility of implementation on mobile devices, since Samourai Wallet is primarily a smartphone application;
- The speed of remixing cycles to encourage a significant increase in anonsets.

These imperatives guided the Samourai Wallet developers' choices in designing Whirlpool, leading them to limit the number of participants per cycle. Too few participants would have compromised the effectiveness of coinjoin, drastically reducing the anonsets generated in each cycle, while too many participants would have posed management problems on the mobile applications and hampered the flow of cycles.

Ultimately, it is not necessary to have a high number of participants to coinjoin on Whirlpool since anonsets are realized on the accumulation of several coinjoin cycles. The most important principle here is the homogeneity of the UTXOs of all participants, as this allows a perfect mix, and thus to fully benefit from the mixing and remixing cycles.

### Coinjoin pools and rates

For these multiple cycles to effectively increase the anonsets of the mixed coins, some framework must be established to limit the amounts of UTXO used. Whirlpool therefore defines several pools.

A pool represents a group of users who wish to mix together, who agree on the amount of UTXO to be used to optimize the coinjoin process while maintaining perfect coin homogeneity. Each pool specifies a fixed amount for UTXO, which the user must meet in order to participate. Thus, to perform coinjoins with Whirlpool, a pool must be selected. The pools currently available are as follows:


- 0.5 bitcoin;
- 0.05 bitcoin;
- 0.01 bitcoin;
- 0.001 bitcoin (= 100,000 sats).

By joining a pool with your bitcoins, these will be divided to generate UTXOs perfectly homogeneous with those of the other participants in the pool. Each pool has a maximum limit; therefore, for amounts that exceed this limit, you will be forced to either make two separate entries into the same pool or turn to another pool with a larger amount:

| Pool (bitcoin) | Maximum amount per entry (bitcoin) |

|----------------|----------------------------------------|

| 0,5 | 35 |

| 0,05 | 3,5 |

| 0,01 | 0,7 |

| 0,001 | 0,025 |

A UTXO is considered to belong to a pool when it is ready to be integrated into a coinjoin. However, this does not mean that the user loses possession of it. As we saw in the first chapters of this part, through the different mixing cycles, you retain full control of your keys and, consequently, of your bitcoins. This is what differentiates the coinjoin technique from other centralized mixing techniques.

To join a coinjoin pool, service fees as well as mining fees must be paid. Service fees are fixed for each pool and are intended to compensate the teams responsible for Whirlpool development and maintenance.

Service fees for using Whirlpool must be paid a single time upon entering the pool. Once this step is completed, you have the ability to participate in an unlimited number of remixes without additional fees. Here are the current fixed fees for each pool:

| Pool (bitcoin) | Input fee (bitcoin) |

| -------------- | --------------------------------- |

| 0.5 | 0.0175 |

| 0.05 | 0.00175 |

| 0.01 | 0.0005 (50,000 sats) |

| 0.001 | 0.00005 (5,000 sats) |

These fees essentially function as an entry ticket to the pool you choose, regardless of the amount you enter into coinjoin. So whether you enter the 0.01 BTC pool with exactly 0.01 BTC or enter with 0.5 BTC, the fees will remain the same in absolute value.

Before proceeding with Whirlpool coinjoins, the user then has a choice between 2 strategies:


- Opt for a smaller pool to minimize service fees, knowing that they will receive several smaller UTXOs in return;
- Or prefer a larger pool, agreeing to pay higher fees to end up with a small number of higher value UTXOs.

Generally, it is not recommended to merge several mixed UTXOs after coinjoin cycles, as this could compromise the privacy gained, especially because of the common input ownership heuristic (CIOH: _Common-Input-Ownership-Heuristic_). Therefore, it might be wise to choose a larger pool, even if it means paying more, to avoid having too many small-valued UTXOs as output. The user must evaluate these trade-offs to choose the pool he or she prefers.

In addition to service fees, the mining fees inherent in any Bitcoin transaction must also be considered. As a Whirlpool user, you will need to pay mining fees for the preparation transaction (`Tx0`) as well as those for the first coinjoin. All subsequent remixes will be free, due to Whirlpool's model of paying new entrants.

In fact, in each Whirlpool coinjoin, 2 users among the inputs are new participants. The other inputs come from remixers. As a result, the mining fees for all participants in the transaction are covered by these 2 new participants, who will then also benefit from free remixes:

![BTC204](assets/it/54/07.webp)

Because of this fee system, Whirlpool truly differs from other coinjoin implementations because the anonsets of UTXOs are not proportional to the price paid by the user. Thus, considerably high levels of anonymity can be achieved by paying only the pool entry fee and mining fees for 2 transactions (the `Tx0` and the initial mix).

It is important to note that the user will also have to cover the mining fees for withdrawing their UTXOs from the pool after running their multiple coinjoins, unless they have selected the `mix to` option, which allows them to provide an external address that will directly receive the funds as the output of a coinjoin, without any additional transaction.

### HD Wallet Accounts

To perform a coinjoin through Whirlpool, the wallet must generate several separate accounts. This is the principle of the ZeroLink protocol. An account, in the context of an HD (_Hierarchical Deterministic_) wallet, constitutes a section completely isolated from the others, this separation occurs at the third level of depth of the wallet hierarchy, i.e., at the `xpub` level.

![BTC204](assets/it/54/08.webp)

An HD wallet can theoretically derive up to `2^(32/2)` different accounts. The initial account, used by default on all Bitcoin wallets, corresponds to the `0'` index.

For portfolios adapted to Whirlpool, 4 accounts are used to meet the requirements of the ZeroLink process:


- The **deposit account**, identified by the index `0'`;
- The **bad bank account** (or "toxic exchange"), identified by the index `2 147 483 644'`;
- The **premix account**, identified by the index `2 147 483 645'`;
- The **postmix account**, identified by the index `2 147 483 646'`.

Each of these accounts performs a specific function in the coinjoin process, which we will explore in the following sections.

All these accounts are linked to a single seed, allowing the user to recover access to all their bitcoins using their recovery phrase and, if necessary, their passphrase. However, it is necessary to specify to the software, during this recovery operation, the different indices of the accounts that have been used.

Let us now examine the different stages of a Whirlpool coinjoin within these accounts.

### The TX0

The starting point of any Whirlpool coinjoin is the **deposit account**. This account is what you automatically use when you create a new bitcoin wallet. This account must be credited with the bitcoins you wish to mix.

The `Tx0` represents the first step in the Whirlpool mixing process. It aims to prepare and equalize the UTXOs for coinjoin, dividing them into units corresponding to the amount of the selected pool, to ensure homogeneity of mixing. The equalized UTXOs are then sent to the **premix account**. As for the difference that cannot enter the pool, it is separated into a specific account: the **bad bank** (or "toxic exchange").

This initial `Tx0` transaction also serves to settle the service fees due to the coinjoin coordinator. Unlike the subsequent steps, this transaction is not collaborative; therefore, the user must bear the full cost of the mining fees:

![BTC204](assets/it/54/09.webp)

In this `Tx0` transaction example, an input of `372 000 sats` from our **deposit account** is divided into several UTXOs of output, which are distributed as follows:


- An amount of `5,000 sats` allocated to the coordinator for service fees, corresponding to the entry into the pool of `100,000 sats`;
- 3 UTXOs prepared for mixing, redirected to our **premix account** and registered with the coordinator. These UTXOs are equalized at `108 000 sats` each, to cover the mining fees for their future initial mix;
- The surplus that cannot enter the pool, being too small, is considered as toxic exchange. It is sent to its specific account. Here, this exchange amounts to `40 000 sats`;
- Finally, there are `3,000 sats` that do not constitute output, but are the mining fees required to confirm `Tx0`.

For example, here is a real Tx0 Whirlpool (not mine):[edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://mempool.space/fr/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)

![BTC204](assets/fr/145.webp)

### The Toxic Change

The excess that could not be integrated into the pool, here equivalent to `40,000 sats`, is redirected to the **bad bank** account, also referred to as "toxic exchange," to ensure strict separation from other UTXOs in the portfolio.

This UTXO is dangerous to user privacy because not only is it still linked to the user's past, and thus possibly to the identity of its owner, but it is also marked as belonging to a user who has participated in a coinjoin.

![BTC204](assets/fr/146.webp)

If this UTXO is merged with shuffled outputs, they will lose all privacy gained during coinjoin cycles, greatly due to CIOH (_Common-Input-Ownership-Heuristic_). If it is merged with other toxic changes, the user risks losing privacy since this will link the different inputs from coinjoin cycles. Therefore, it should be handled with caution. We will discuss the management of these toxic UTXOs in more detail in the last section of this chapter.

### The Initial Mix

After the `Tx0` is completed, the equalized UTXOs are sent to the **premix** account in our portfolio, ready to be introduced into their first coinjoin cycle, also called "initial mix." If, as in our example, `Tx0` generates several UTXOs intended for mixing, each of them will be integrated into a separate initial mix.

At the end of these first mixes, the **premix** account will be empty, while our coins, having paid the mining fees for this first coinjoin, will be settled at exactly the amount defined by the chosen pool. In our example, our initial UTXOs of `108,000 sats` will have been reduced to exactly `100,000 sats`.

![BTC204](assets/fr/147.webp)

### The Remixes

After the initial mix, the UTXOs are transferred to the **postmix** account. This account collects both UTXOs that have already been mixed and those awaiting remix. When the Whirlpool client is active, the UTXOs in the **postmix** account are automatically available for remix and will be randomly chosen to participate in these new rounds.

As a reminder, remixes are then completely free: no additional service fees or mining fees are required. Keeping UTXOs in the **postmix** account thus keeps their value intact and simultaneously improves their anonsets. This is why it is important to allow these coins to participate in multiple coinjoin cycles. It costs you absolutely nothing and increases their anonset levels.

When you decide to spend mixed UTXOs, you can do so directly from this **postmix** account. It is advisable to keep mixed UTXOs in this account to benefit from free remixes and to prevent them from leaving the Whirlpool circuit, which may decrease their privacy.

### How to properly manage your postmix account?

After running coinjoin cycles, the best strategy is to keep your UTXOs in the **postmix** account, pending their future use. It is even advisable to let them remix indefinitely until you need to spend them.

Some users may consider transferring their mixed bitcoins to a protected hardware wallet. This is possible, but it is important to meticulously follow Samourai Wallet's recommendations so as not to compromise the confidentiality gained.

Combining UTXOs is the most frequently made mistake. You need to avoid combining mixed UTXOs with unmixed UTXOs in the same transaction to avoid Common-Input-Ownership (CIOH) heuristics. This requires careful management of your UTXOs within your portfolio, especially in terms of labeling.

![BTC204](assets/fr/148.webp)

It is also important to be cautious about consolidating mixed UTXOs together. Moderate consolidations are conceivable if your mixed UTXOs have significant anonsets, but this will inevitably decrease the confidentiality of your coins. Make sure that consolidations are not too significant or performed after an insufficient number of remixes, at the risk of establishing inferred links between your UTXOs before and after coinjoin cycles. When in doubt about these manipulations, the best practice is not to consolidate UTXOs postmix, and transfer them one by one to your hardware wallet, generating a new empty address each time. Still remember to properly label each UTXO received.

It is also not recommended to transfer your UTXO postmixes to a wallet that uses uncommon scripts. For example, if you enter Whirlpool from a multisig wallet that uses `P2WSH` scripts, there is a small chance that you will be mixed with other users who have the same type of wallet originally. If you withdraw your postmixes in this same multisig wallet, the privacy level of your blended bitcoins will be greatly diminished. In addition to scripts, there are many other wallet fingerprints that can fool you.

As with any Bitcoin transaction, it is also important not to reuse receiving addresses. Each new transaction should be received on a new, empty address.

The simplest and safest solution is to let your mixed UTXOs rest in their **postmix** account, allowing them to remix and touching them only to spend them. The Samourai and Sparrow portfolios have additional protections against all these chain analysis risks. These protections help you avoid making mistakes.

### How to properly manage your toxic change?

Next, you must be careful in handling your toxic change, the change that could not enter the coinjoin pool. These toxic UTXOs, resulting from Whirlpool use, pose a risk to your privacy because they establish a link between you and coinjoin use. Therefore, it is imperative to handle them with caution and not combine them with other UTXOs, especially mixed UTXOs.

Here are several strategies to consider for using them:


- Mix them in smaller pools:** If your toxic UTXO is large enough to fit alone in a smaller pool, consider mixing it. This is often the best option. However, mixing several toxic UTXOs together to access a pool is not recommended, as this could link your different entrances.
- Mark them as "non-spendable":** Another approach is to stop using them, mark them as "non-spendable" in their dedicated account and simply hodl. This ensures that you don't accidentally spend them. If the value of bitcoin increases, new pools more suitable for your toxic UTXOs may emerge;
- Making donations:** Consider making donations, even modest ones, to developers working on Bitcoin and its associated software. You can also donate to organizations that accept BTC. If managing your toxic UTXOs seems too complicated, you can simply get rid of them by making a donation.
- Buy Gift Cards:** Platforms such as [Bitrefill](https://www.bitrefill.com/) allow you to exchange bitcoins for gift cards that can be used at various merchants. This can be a way to dispose of your toxic UTXOs without losing the associated value.
- Consolidate them to Monero:** Samourai Wallet offers an atomic swap service between BTC and XMR. This is ideal for managing toxic UTXOs by consolidating them on Monero, without compromising your privacy via KYC, before sending them back to Bitcoin. However, this option can be expensive in terms of mining fees and premiums due to liquidity constraints.
- Send them to the Lightning Network:** Transferring these UTXOs to the Lightning Network to benefit from reduced transaction fees is an attractive option. However, this method may reveal some information depending on your use of Lightning and should therefore be practiced with caution.

### How to use Whirlpool?

Following the arrest of the founders of Samourai Wallet and the seizure of their servers on April 24, 2024, the Whirlpool tool no longer works, even for those who have their own Dojo. Previously, it was available on Samourai Wallet and Sparrow Wallet.

![BTC204](assets/fr/149.webp)

However, it remains possible that this instrument could be put back into service in the coming weeks, depending on the outcome of the trials, or relaunched in a different way. In any case, I believe that the coinjoin market on Bitcoin will not remain without a supply for long, as there is a clear demand. Moreover, the Whirlpool model, being the most advanced in terms of privacy, will surely be used for other implementations in the future.

We are closely following the evolution of this case as well as developments regarding associated tools. Rest assured that we will update this training as new information becomes available.

In the next chapter, we will find out what "anonsets" are, how these indicators are calculated, and how they can help us estimate the effectiveness of coinjoin cycles.

https://planb.network/tutorials/privacy/on-chain/coinjoin-sparrow-wallet-84def86d-faf5-4589-807a-83be60720c8b
https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef
https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2
## Anonymity Set

<chapterId>be1093dc-1a74-40e5-9545-2b97a7d7d431</chapterId>

Having studied how coinjoins work and the challenges associated with effective blending, we will now learn how to measure this effectiveness. How to determine whether a coinjoin process was effective and what degree of anonymity did a coin acquire? This is what we will explore in this chapter with anonymity sets or "anonsets" in English.

### Reminder on the Usefulness of Coinjoin

The usefulness of CoinJoin lies in its ability to produce plausible deniability by immersing your coin within a group of indistinguishable coins. The goal of this action is to break traceability links, both from past to present and from present to past.

In other words, an analyst who knows your initial transaction (`Tx0`) at the entry of CoinJoin cycles should not be able to identify with certainty your UTXO at the exit of remix cycles (analysis from entry to cycle to exit from cycle).

![BTC204](assets/it/55/01.webp)

In contrast, an analyst who knows your UTXO at the output of CoinJoin cycles should be unable to determine the original transaction at the input of cycles (analysis from cycle output to cycle input).

![BTC204](assets/it/55/02.webp)

To assess the difficulty for an analyst to link the past to the present and vice versa, it is necessary to quantify the size of the homogeneous coin groups within which your coin is hidden. This measure tells us the number of analyses that have an identical probability. Thus, if the correct analysis is drowned among 3 other analyses of equal probability, your level of concealment is very low. However, if the correct analysis is within a set of 20,000 analyses all equally likely, your coin is very well hidden. And precisely, the size of these sets represents indicators called anonsets.

### Understanding the Anonsets

Anonsets serve as indicators to assess the degree of privacy of a particular UTXO. More specifically, they measure the number of indistinguishable UTXOs within the set that includes the coin being studied. The requirement for a homogeneous UTXO set means that anonsets are usually calculated on CoinJoin cycles. The use of these indicators is particularly relevant for Whirlpool CoinJoins because of their uniformity.

Anonsets make it possible, when appropriate, to judge the quality of CoinJoins. A large anonset size means a high level of anonymity, as it becomes difficult to distinguish a specific UTXO within the homogeneous set.

There are 2 types of anonsets:


- The prospective anonset;**
- The retrospective anonset.**

### The Prospective Anonset

The forward-looking anonset indicates the size of the group among which the studied UTXO is hidden at the cycle exit, knowing the UTXO at the entry, that is, the number of indistinguishable coins present within this group. In English, the name of this indicator is "forward anonset," or "forward-looking metrics."

This indicator provides a measure of currency privacy resistance against a past-to-present (input to output) analysis.

![BTC204](assets/it/55/03.webp)

This metric estimates the extent to which your UTXO is protected against attempts to reconstruct its history from its entry point to its exit point in the coinjoin process.

For example, if your transaction participated in its first coinjoin cycle and two additional descending cycles were completed, the prospective anonset of your coin would be `13`:

![BTC204](assets/fr/153.webp)

For example, let us imagine that our coin at the entrance of the coinjoin cycle benefits from a prospective anonset of `86,871`. Practically, this means that it is hidden among `86,871` indistinguishable coins. For an outside observer aware of this coin at the beginning of coinjoin cycles and attempting to track its exit, he would be faced with `86,871` possible UTXOs, each with an identical probability of being the coin sought.

![BTC204](assets/it/55/05.webp)

### The Retrospective Anonset

Retrospective anonset indicates the number of possible sources for a given coin, knowing the UTXO at cycle exit. This indicator measures the coin's privacy resistance against a present-to-past analysis (exit to entry), that is, how difficult it is for an analyst to trace the origin of your coin, before coinjoin cycles. In English, the name of this indicator is "backward anonset," or "retrospective metrics."

Knowing your UTXO at the exit of the cycles, the retrospective anonset determines the number of potential Tx0 transactions that could have constituted your entry in the coinjoin cycles. In the diagram below, this corresponds to the sum of all the orange bubbles.

For example, let us imagine that our coin at the exit of the coinjoin cycle benefits from a retrospective anonset of `42,185`. Practically, this means that there are `42,185` possible sources for this UTXO. If an outside observer identifies this coin at the end of cycles and tries to trace its origin, he will be faced with `42,185` possible sources, all with an equal probability of being the origin sought.

### How to concretely calculate anonsets?

You can manually calculate your anonsets using a block explorer for small sets. However, for larger anonsets, the use of a specialized tool becomes imperative. To my knowledge, the only software capable of performing this task is _Whirlpool Stats Tool_, a Python tool developed by the Samourai and OXT teams. Unfortunately, this tool is currently out of service following the arrest of the founders of Samourai and the termination of OXT, which was being used to extract data from the blockchain.

As we have seen in this chapter, anonsets can only be calculated if there is some homogeneity in the coinjoin structure. And precisely, in the next chapter, we will find out how to quantify this homogeneity in a Bitcoin transaction, whether it is a coinjoin or a more traditional transaction.

https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375
## Entropy

<chapterId>e4fe289d-618b-49a2-84c9-68c562e708b4</chapterId>

As we have seen in this part on coinjoins, the homogeneity of UTXOs in inputs and outputs plays an important role in improving the confidentiality of a Bitcoin transaction. This parameter allows plausible deniability against chain analysis. Several methods can measure this homogeneity, but one of the most effective, in my opinion, is the use of indicators provided by the _Boltzmann_ tool, developed by the OXT and Samourai Wallet teams, specifically transaction entropy. This is what we will study in detail in this chapter.

Unlike anonsets, which are calculated on a set of transactions, the indicators we will present here focus exclusively on a single transaction, whether it is a coinjoin or a more traditional transaction.

### The number of interpretations

The first indicator that can be observed in a Bitcoin transaction is the total number of possible interpretations in the eyes of an outside observer analyzing the transaction. Taking into consideration the values of the UTXOs involved in the transaction, this indicator indicates the number of ways in which inputs can be associated with outputs. In other words, it determines the number of possible interpretations that a transaction can generate in the bitcoin stream from the perspective of an outside observer analyzing it.

For example, a simple payment transaction with 1 input and 2 outputs will have only one interpretation, namely that input #0 funded output #0 and output #1. There are no other possible interpretations:

![BTC204](assets/fr/159.webp)

In contrast, a coinjoin structured according to the Whirlpool 5x5 model has $1,496 possible combinations:

![BTC204](assets/fr/160.webp)

A Whirlpool Surge Cycle 8x8 coinjoin comes up with $9,934,563 possible interpretations:

![BTC204](assets/fr/161.webp)

### Entropy

From the number of interpretations of a Bitcoin transaction, we can calculate its entropy.

In the general context of cryptography and information, entropy is a quantitative measure of the uncertainty or unpredictability associated with a data source or random process. In other words, entropy is a way to measure how difficult it is to predict or guess information.

In the specific context of chain analysis, entropy is also the name of an indicator, derived from Shannon's entropy and [invented by LaurentMT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf), that can be calculated on a Bitcoin transaction.

When a transaction has a high number of possible interpretations, it is often more relevant to refer to its entropy. This indicator provides a measure of analysts' lack of knowledge about the exact configuration of the transaction. In other words, the higher the entropy, the more difficult it becomes for analysts to identify bitcoin flows between inputs and outputs.

In practice, entropy reveals whether, from the perspective of an outside observer, a transaction has multiple possible interpretations, based solely on input and output quantities, without considering other external or internal patterns and heuristics. High entropy is thus synonymous with higher confidentiality for the transaction.

Entropy is defined as the binary logarithm of the number of possible combinations. Here is the formula used with $E$ representing the entropy of the transaction and $C$ the number of possible interpretations:

$$
E = \log_2(C)
$$

In mathematics, the binary logarithm (logarithm to base 2) corresponds to the inverse operation of raising 2 to a certain power. In other words, the binary logarithm of $x$ is the exponent to which $2$ must be raised to obtain $x$. This indicator is thus expressed in bits.

Take the example of the entropy calculation for a coinjoin transaction structured according to the 5x5 Whirlpool model, which, as mentioned in the previous section, has a number of possible interpretations of $1,496:

$$
\begin{align*}
C &= 1.496 \\
E &= \log_2(1.496) \\
E &= 10.5469 \text{ bit}
\end{align*}
$$

Thus, this coinjoin transaction shows an entropy of $10.5469$ bits, which is considered very satisfactory. The higher this value, the more different interpretations the transaction admits, thus improving its level of privacy.

For an 8x8 coinjoin transaction that has $9,934,563 interpretations, the entropy would be:

$$
\begin{align*}
C &= 9.934.563 \\
E &= \log_2(9.934.563) \\
E &= 23,244 \text{ bit}
\end{align*}
$$

Let's take another example with a standard payment transaction, with 1 input and 2 outputs: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://mempool.space/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce)

![BTC204](assets/fr/162.webp)

In the case of this transaction, the only possible interpretation is: `(In.0) > (Out.0 ; Out.1)`. Consequently, its entropy is set to $0$:

$$
\begin{align*}
C &= 1 \\
E &= \log_2(1) \\
E &= 0 \text{ bit}
\end{align*}
$$

### Efficiency

From the entropy of the transaction, we can also calculate its privacy efficiency. This indicator evaluates the efficiency of the transaction by comparing it with the optimal transaction conceivable in an identical configuration.

This leads us to discuss the concept of maximum entropy, which corresponds to the highest entropy that a specific transaction structure could theoretically achieve. The efficiency of the transaction is then calculated by comparing this maximum entropy with the actual entropy of the analyzed transaction.

The formula used is as follows with:


- $E_R$: the actual entropy of the transaction expressed in bits;
- $E_M$: the maximum possible entropy for a transaction structure also expressed in bits;
- $Ef$: the efficiency of the transaction in bits:

$$
Ef = E_R - E_M
$$

For example, for a coinjoin structure of type Whirlpool 5x5, the maximum entropy is $10.5469$:

$$
\begin{align*}
E_R &= 10,5469 \\
E_M &= 10,5469 \\
Ef &= E_R - E_M \\
Ef &= 10,5469 - 10,5469 \\
Ef &= 0 \text{ bit}
\end{align*}
$$

This indicator is also expressed as a percentage. The formula used is as follows with:


- $C_R$: the number of possible real interpretations;
- $C_M$: the maximum number of possible interpretations with the same structure;
- $Ef$: efficiency expressed as a percentage:

$$
\begin{align*}
E_f &= \frac{C_R}{C_M} \\
E_f &= \frac{1.496}{1.496} \\
E_f &= 100\%
\end{align*}
$$

An efficiency of $100\%$ thus indicates that the transaction maximizes its potential for privacy based on its structure.

### The Entropy Density

Entropy is a good indicator for measuring the privacy of a transaction, but it depends in part on the number of inputs and outputs in the transaction. To compare the entropy of 2 different transactions that do not have the same number of inputs and outputs, the entropy density can be calculated. This indicator provides a perspective on the entropy relative to each input or output in the transaction. The density proves useful in evaluating and comparing the efficiency of transactions of different sizes.

To calculate it, simply divide the total entropy of the transaction by the total number of inputs and outputs involved in the transaction:


- $E_D$: the entropy density expressed in bits;
- $E$: the entropy of the transaction expressed in bits;
- $T$: the total number of inputs and outputs in the transaction:

$$
E_D = \frac{E}{T}
$$

Take the example of a 5x5 Whirlpool coinjoin:

$$
\begin{align*}
T &= 5 + 5 = 10 \\
E &= 10.5469 \\
E_D &= \frac{E}{T} \\
E_D &= \frac{10.5469}{10} \\
E_D &= 1.054 \text{ bit}
\end{align*}
$$

We also calculate the entropy density of an 8x8 Whirlpool coinjoin:

$$
\begin{align*}
T &= 8 + 8 = 16 \\
E &= 23.244 \\
E_D &= \frac{E}{T} \\
E_D &= \frac{23.244}{16} \\
E_D &= 1.453 \text{ bit}
\end{align*}
$$

By analyzing the entropy density of these two types of coinjoins, it becomes evident that even when normalizing the entropy for the number of elements, the "Surge Cycle 8x8" coinjoin generates more uncertainty for analysis.

### The Boltzmann Score

Another piece of information analyzed in a transaction is the Boltzmann score of each element relative to another. This is a table of probabilities of correspondence between inputs and outputs. This table indicates, through the Boltzmann score, the conditional probability that a specific input is related to a given output. It is thus a quantitative measure of the conditional probability that an association between an input and an output in a transaction will occur, determined on the ratio of the number of favorable occurrences of this event to the total number of possible occurrences, in a set of interpretations.

Taking the example of a Whirlpool coinjoin, the conditional probability table would highlight the possibilities of a link between each input and output, providing a quantitative measure of the ambiguity of associations in the transaction:

| % | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |

| ------- | -------- | -------- | -------- | -------- | -------- |











Here, it is clear that each input has the same probability of being associated with any output, which increases the confidentiality of the transaction.

Calculating the Boltzmann score involves dividing the number of interpretations in which a certain event occurs by the total number of interpretations available. Thus, to determine the score by associating input #0 with output #3 (an event present in $512$ interpretations), the process is as follows:

$$
\begin{align*}
\text{Interpretazioni (IN.0 > OUT.3)} &= 512 \\
\text{Interpretazioni Totali} &= 1496 \\
\text{Punteggio} &= \frac{512}{1496} \\
\text{Punteggio} &= 34\%
\end{align*}
$$

If we reconsider the example of a Surge 8x8 Whirlpool coinjoin cycle, the Boltzmann table would look like this:

| | OUT.0 | OUT.1 | OUT.2 | OUT.3 | OUT.4 | OUT.5 | OUT.6 | OUT.7 | OUT.7 |

| ---- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |

| IN.0 | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% |

| IN.1 | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% |

| IN.2 | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% |

| IN.3 | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% |

| IN.4 | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% |

| IN.5 | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% |

| IN.6 | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% |

| IN.7 | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% | 23% |

However, in the case of a simple transaction involving a single input and 2 outputs, the situation is different:

| % | Output 0 | Output 1 |

| ------- | -------- | -------- |

| Input 0 | 100% | 100% |

Here, we observe that the probability of each output coming from input #0 is 100%. A lower probability thus results in greater privacy by diluting the direct links between inputs and outputs.

### Deterministic Links

It is also possible to calculate the number of deterministic links in a transaction. This indicator reveals how many links between inputs and outputs in the analyzed transaction are unquestionable, with 100% probability. This indicator can then be completed by calculating the ratio of deterministic links. The ratio provides a perspective on the weight of these deterministic links within all links in the transaction.

For example, a Whirlpool coinjoin transaction shows no deterministic linkage between inputs and outputs, thus showing an indicator of 0 linkages and a ratio of 0%. In contrast, in our second simple payment transaction examined (with one input and 2 outputs), the indicator tells us that there are 2 deterministic links and the ratio reaches 100%. Thus, a null indicator signals excellent privacy because of the absence of direct and indisputable connections between inputs and outputs.

### How to calculate these indicators?

Calculating these indicators manually using the equations I have provided is relatively simple. The main difficulty lies in determining the number of possible interpretations of a transaction. For a standard transaction, this calculation can be done by hand. However, for a coinjoin, the task is significantly more complex.

Previously, there was a Python tool called _Boltzmann Calculator_, developed by the teams at OXT and Samourai, which allowed for the automatic calculation of all these indicators for a Bitcoin transaction:

![BTC204](assets/fr/163.webp)

It was also possible to use the KYCP.org website for these analyses:

![BTC204](assets/fr/164.webp)

Unfortunately, following the arrest of Samourai's founders, these tools are currently not operational.

Now that we have discussed coinjoins in detail, we will explore other privacy techniques available on Bitcoin in the last section of our training. We will examine payjoin transactions, specific pseudo-coinjoin transaction types, static address protocols, as well as measures to improve privacy not at the transaction level, but at the level of the network of nodes.

https://planb.network/tutorials/privacy/analysis/boltzmann-entropy-738e45af-18a6-4ce6-af1a-1bf58e15f1fe
# Understand the stakes of other advanced privacy techniques

<partId>19989ae6-d608-4acf-b698-2cf1e7e5e6ae</partId>

## Payjoin Transactions

<chapterId>c1e90b95-f709-4574-837b-2ec26b11286f</chapterId>

Currently, coinjoin is the most effective method for introducing uncertainty into coin tracking during a chain analysis. As we have seen in previous chapters, to achieve effective mixing, the inputs and outputs need to be as homogeneous as possible. In addition, it is crucial that coinjoins be integrated into as large a group as possible to maximize anonsets. Thus, for coinjoins to be effective, they must involve a large number of uniform coins. This multitude of requirements means that coinjoin transactions have a very rigid structure: amounts are predetermined and all participants must adhere to them to ensure uniformity of the process. In addition, coinjoins require synchronization between all participants and the coordinator during the construction of the transaction.

These requirements make coinjoin unsuitable for direct payments. For example, if you own a 1M sats piece in a coinjoin pool, using it directly as a payment would be complex. It would require synchronization with other participants and the coordinator to build exactly at the time you need to make a payment the collaborative transaction, and the purchase amount would have to exactly match the value of your piece, which is practically unfeasible. Therefore, a coinjoin transaction is by nature a collaborative cleanup transaction, which means that generally it is the same owners of the inputs that are in the outputs.

However, it would be interesting to have transaction structures that allow for practical payments by introducing doubt into the chain analysis. This is exactly what we will explore in this chapter and the next.

### What is a payjoin transaction?

Payjoin is a specific Bitcoin transaction structure that enhances user privacy during a spend by collaborating with the payment recipient.

In 2015, LaurentMT first mentioned this method under the name "steganographic transactions," according to an accessible paper [here](https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt). This technique was later adopted by Samourai Wallet, which in 2018, was the first client to implement it with the Stowaway tool. The concept of payjoin is also found in [BIP79](https://github.com/bitcoin/bips/blob/master/bip-0079.mediawiki) and [BIP78](https://github.com/bitcoin/bips/blob/master/bip-0078.mediawiki). Several terms are thus used to designate a payjoin:


- Payjoin;
- Stowaway;
- P2EP (_Pay-to-End-Point_);
- Steganographic transaction.

The uniqueness of the payjoin lies in its ability to generate a transaction that appears ordinary at first glance, but is actually a mini Coinjoin between two people. For this, the structure of the transaction involves the recipient of the payment in the inputs along with the actual sender. The recipient then includes a payment to himself in the middle of the transaction that allows him to be paid.

Let us take an example to better understand this process. Alice buys a baguette for 4,000 sats using a UTXO of 10,000 sats and opts for a payjoin. Her baker, Bob, adds a UTXO of 15,000 sats of his own in input, which he recovers entirely in output, in addition to Alice's 4,000 sats.

In the example, Bob the baker inputs 15,000 sats and comes out with 19,000 sats, the difference is exactly 4,000 sats, which is the price of the baguette. For her part, Alice enters with 10,000 sats and ends up with 6,000 sats in output, which represents a balance of -4,000 sats, which is the price of the baguette. To simplify the example, I deliberately omitted the mining fees in this transaction.

### What is the purpose of the payjoin?

The payjoin transaction fulfills two goals that allow users to improve the privacy of their payment.

First, the payjoin aims to fool an outside observer by creating a diversion in the chain analysis. This is made possible through the _Common Input Ownership Heuristic_ (CIOH). As we saw in Part 3, usually when a transaction on the blockchain has multiple inputs, it is assumed that all these inputs belong to the same entity or user.

Thus, when an analyst examines a payjoin transaction, he or she is led to believe that all inputs come from the same person. However, this perception is incorrect, since the payee also contributes inputs along with the actual payer. The chain analysis is thus skewed toward an interpretation that turns out to be false.

Let us return to our example of a payjoin transaction to pay for a baguette:

Seeing this transaction on the blockchain, an outside observer following the usual heuristics of chain analysis would interpret it this way, "Alice joined 2 UTXOs in transaction input to pay 19,000 sats to Bob."

This interpretation is clearly wrong; as you already know, the two UTXOs in input do not belong to the same person. One is from Alice, the baguette buyer, and the other is from Bob, the baker.

Thus, the external observer's analysis is directed toward an erroneous conclusion, which ensures the preservation of stakeholder confidentiality.

### The steganographic transaction

The second goal of the payjoin is to deceive an outside observer about the actual amount of the payment made. By examining the structure of the transaction, the analyst might believe that the payment is equivalent to the amount of one of the outputs.

If we take our example of buying a baguette, the analyst will think that the payment amount corresponds to either the UTXO of 6,000 sats or the UTXO of 19,000 sats. In this case, the analyst is more likely to think that the payment amount is 19,000 sats because there are 2 UTXOs in the output, at least one of which is greater than 6,000 sats (there is no logical reason to use 2 UTXOs to pay 6,000 sats when a single UTXO would have been sufficient for this payment).

But in reality, this analysis is incorrect. The payment amount does not match any of the outputs. It is actually the difference between the UTXO of the output recipient and the UTXO of the input recipient.

In this, the payjoin transaction falls into the realm of steganography. It allows the real amount of a transaction to be hidden within a fake transaction that serves as a diversion.

Steganography is a technique for hiding information within other data or objects so that the presence of the hidden information is not discernible. For example, a secret message can be hidden within a point in unrelated text, making it undetectable to the naked eye (this is the [micropoint](https://fr.wikipedia.org/wiki/Micropoint) technique).

Unlike encryption, which renders information unintelligible without the decryption key, steganography does not alter the information. They remain in view. Rather, its goal is to hide the very existence of the secret message, whereas cryptography clearly reveals the presence of hidden information, although inaccessible without the key. This is why the initial name for payjoin was "steganographic transactions."

An analogy could be made between cryptography and coinjoin, as well as between steganography and payjoin. In fact, coinjoin has attributes similar to those of cryptography: the method is recognizable, but the information is indecipherable. In contrast, payjoin is akin to steganography: the information is theoretically accessible, but because its method of concealment is not recognizable, it becomes inaccessible.

### How to use payjoin?

Known software that support payjoin include Sparrow Wallet, Wasabi Wallet, Mutiny, BitMask, BlueWallet, and JoinMarket, as well as the BTCPay payment processor.

The most advanced implementation of payjoin was only the Stowaway on Samourai Wallet. However, since the shutdown of the software founders, this tool now works only partially. The advantage of Stowaway is that it is a complete and very easy-to-use protocol that supports both receiving and sending payjoins. Partially signed transactions can be exchanged manually by scanning multiple QR codes or automatically through Tor via Soroban. It is the latter communication option that is not currently in service.

The difficulty in using payjoin lies in its dependence on merchant participation. As a customer, using a payjoin is impossible if the merchant does not support it. This adds an additional difficulty during a purchase: not only is it complicated to find merchants that accept bitcoin, but if you also look for those that support payjoins, it becomes even more complicated.

One solution could be the use of transactional structures that introduce ambiguity into the chain analysis without requiring the cooperation of the recipient. This would allow us to improve the privacy of our payments without depending on the active participation of merchants. This is precisely what we will study in the next chapter.

https://planb.network/tutorials/privacy/on-chain/payjoin-sparrow-wallet-087a0e49-61cd-41f5-8440-ac7b157bdd62
https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab
## Mini-coinjoin payment

<chapterId>300777ee-30ae-43d7-ab00-479dac3522c1</chapterId>

When looking to make a payment transaction while preserving some degree of privacy, payjoin is a good option. But as we have seen, payjoin requires the involvement of the recipient. So what to do if the latter refuses to participate in a payjoin, or if you simply prefer not to involve him? One alternative is to use a Stonewall or Stonewall x2 transaction. Let's take a closer look at these two types of transactions.

### The Stonewall Transaction

Stonewall is a specific form of Bitcoin transaction aimed at increasing user privacy during a shopping spree by mimicking a pseudo-coinjoin between two people, but without actually being one. In fact, this transaction is not collaborative. A user can build it by himself, involving only the UTXOs he owns as input. You can then create a Stonewall transaction for any occasion, without the need to synchronize with another user or the recipient.

The operation of the Stonewall transaction is as follows: in the input of the transaction, the sender uses 2 UTXOs that belong to him. In the output, the transaction produces 4 UTXOs, 2 of which will be exactly the same amount. The other 2 UTXOs will constitute the remainder. Among the 2 outputs of the same amount, only one will actually go to the recipient of the payment.

There are only 2 roles in a Stonewall transaction:


- The sender, who makes the payment;
- The recipient, who may be unaware of the specific nature of the transaction and is simply waiting for payment from the sender.

Let us take an example to understand this transaction structure. Alice is at baker Bob's to buy her baguette, which costs 4,000 sats. She wants to pay in bitcoin while maintaining some level of privacy about her payment. Therefore, she decides to construct a Stonewall transaction for payment.

Analyzing this transaction, we can see that Bob the baker actually received 4,000 sats in payment for the baguette. Alice used 2 UTXOs as inputs: one of 10,000 sats and one of 15,000 sats. In outputs, she received 3 UTXOs: one of 4,000 sats, one of 6,000 sats and one of 11,000 sats. Alice thus has a net balance of -4,000 sats on this transaction, which is exactly the same as the price of the baguette.

In this example, I have intentionally neglected mining fees for ease of understanding. In reality, transaction fees are entirely borne by the sender.

### What are the goals of a Stonewall transaction?

The Stonewall structure adds much entropy to the transaction and confuses the traces of the chain analysis. From the outside, such a transaction can be interpreted as a mini-coinjoin between two people. But in reality, it is a payment. Thus, this method generates uncertainties in the chain analysis, or even leads to false traces.

Let us return to the example of Alice at Bob the Baker's. The transaction on the blockchain would look like this:

![BTC204](assets/fr/174.webp)

An outside observer relying on the common heuristics of chain analysis might mistakenly conclude that "_two people made a small coinjoin, with one UTXO each in input and two UTXOs each in output_." Analysis of this transaction from the outside does not lead to the application of Common Ownership Heuristics of Input (CIOH), because the presence of two outputs of the same amount suggests a coinjoin pattern. From an external perspective, CIOH therefore does not apply in this particular case.

![BTC204](assets/fr/175.webp)

This interpretation is inaccurate, because, as you know, one UTXO was sent to Bob the Baker, the 2 UTXOs in input came from Alice, and she retrieved 3 rest outputs.

![BTC204](assets/fr/176.webp)

And what is particularly interesting about the structure of the Stonewall transaction is that, from the perspective of an outside observer, it looks exactly like that of a Stonewall x2 transaction.

### The Stonewall Transaction x2

Stonewall x2 is another specific form of Bitcoin transaction that also aims to increase user privacy during a spend, but this time by collaborating with a third party not involved in the spend. This method functions as a pseudo-coinjoin between two participants while making a payment to a third party.

The operation of the Stonewall x2 transaction is relatively simple: one uses a UTXO in one's possession to make the payment and enlists the help of a third party that also contributes a UTXO of its own. The transaction ends with four outputs: two of them of equal amounts, one going to the address of the payment recipient, the other to an address belonging to the contributor. A third UTXO is sent to another address of the contributor, allowing them to recover the initial amount (a neutral action for them, minus mining fees), and a final UTXO returns to an address belonging to us, which constitutes the remainder of the payment.

Thus, three different roles are defined in Stonewall x2 transactions:


- The sender, who makes the actual payment;
- The recipient, who may be unaware of the specific nature of the transaction and simply awaits payment from the sender;
- The collaborator, who provides bitcoin to cast doubt in the transaction analysis, fully recovering their funds at the end (a neutral action for them, net of mining fees).

Let us return to our example with Alice who is at Bob the Baker's to buy her baguette that costs 4,000 sats. She wants to pay in bitcoin while maintaining some level of privacy about her payment. So, she calls her friend Charles, who will help her in this process.

![BTC204](assets/fr/177.webp)

Analyzing this transaction, we can see that Bob the baker actually received 4,000 sats in payment for the baguette. Alice used 10,000 sats in input and recovered 6,000 sats in output, resulting in a net balance of -4,000 sats, which corresponds to the price of the baguette. As for Charles, he provided 15,000 sats in input and received two outputs: one of 4,000 sats and the other of 11,000 sats, resulting in a balance of 0.

In this example, I have intentionally neglected commissions to facilitate understanding. In reality, mining fees are generally shared equally between the issuer of the payment and the contributor.

### What are the goals of a Stonewall x2 transaction?

Like the Stonewall structure, the Stonewall x2 structure adds a significant amount of entropy to the transaction and obscures the traces of chain analysis. From an external point of view, such a transaction could be interpreted as a small coinjoin between two people. But in reality, it is a payment. This method, therefore, generates uncertainties in chain analysis, also leading to false traces.

Let us review the example of Alice, Bob the Baker, and Charles. The transaction on the blockchain would look like this:

![BTC204](assets/fr/178.webp)

An outside observer relying on the common heuristics of chain analysis might mistakenly conclude that "_Alice and Charles conducted a small coinjoin, with one UTXO each in input and two UTXOs each in output_." Again, analyzing this transaction from the outside does not lead to the application of Common Ownership Heuristics of Input (CIOH), because the presence of two outputs of the same amount suggests a coinjoin pattern. From an external perspective, CIOH therefore does not apply in this particular case.

![BTC204](assets/fr/179.webp)

This interpretation is inaccurate because, as you know, one UTXO was sent to Bob the Baker, Alice has only one rest output, and Charles has two.

![BTC204](assets/fr/180.webp)

And again, what is particularly interesting with the Stonewall x2 transaction structure is that from the perspective of an outside observer, it looks exactly like that of a Stonewall transaction.

### What is the difference between Stonewall and Stonewall x2?

A StonewallX2 transaction works exactly like a Stonewall transaction, except that the former is collaborative, while the latter is not. As we have seen, a Stonewall x2 transaction involves the participation of a third party (Charles), who is external to the payment, and who provides his bitcoins to increase the confidentiality of the transaction. In a classic Stonewall transaction, the role of the contributor is assumed by the sender.

![BTC204](assets/fr/181.webp)

From an external point of view, therefore, the transaction model is exactly the same.

The fact that these two transaction structures share exactly the same pattern implies that even if an outside observer can identify a "Stonewall(x2)" pattern, he will not have all the information. He will not be able to determine which of the two UTXOs of the same amounts corresponds to the payment. It also will not be able to determine whether the two input UTXOs came from two different people (Stonewall x2) or whether they belonged to a single person who joined them (Stonewall).

This last point is due to the fact that Stonewall x2 transactions follow exactly the same pattern as Stonewall transactions. From the outside and without additional context information, it is impossible to differentiate a Stonewall transaction from a Stonewall x2 transaction. However, the former are not collaborative transactions, while the latter are. This adds even more doubt in the analysis of one such transaction.

### When to use Stonewall and Stonewall x2 transactions?

The logic should be as follows when you want to use a privacy tool for a transaction:


- As a priority, you can choose to make a payjoin;
- If the merchant does not support payjoins, a collaborative transaction can be made with another person outside of payment using the Stonewall x2 structure;
- If you cannot find anyone to do a Stonewall x2 transaction with, you can do a Stonewall transaction on your own, which will mimic the behavior of a Stonewall x2 transaction.

### How to use Stonewall and Stonewall x2 transactions?

Stonewall and Stonewall x2 transactions are available on both the Samourai Wallet app and Sparrow Wallet software.

However, just as with payjoins, following the arrest of Samourai's founders, Stonewall x2 transactions now work only by manually exchanging PSBTs between the parties involved. Automatic exchange via Soroban is unfortunately not available at the moment.

You can also perform this type of transaction manually from any Bitcoin wallet software.

In the next chapter, we will study another relatively unknown but very useful privacy technique in addition to what we have already studied.

https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4
https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b
## Rebounds

<chapterId>db9a20ac-a149-443d-884b-ea6c03f28499</chapterId>

The use of Bitcoin transaction structures that add ambiguity in chain analysis, such as coinjoin, is particularly beneficial for privacy protection. However, as we discussed in the chapter on payjoins, coinjoin transactions are naturally identifiable in the chain. Remember the analogy we established between cryptography and coinjoins: when encrypting a file, a third party discovering this encrypted file cannot access its contents, but can clearly identify that there has been a modification of the file to hide its contents. The same is true for coinjoins: when an analyst examines a coinjoin transaction, even if he or she cannot establish direct links between inputs and outputs (and vice versa), he or she can still recognize that the observed transaction is a coinjoin.

Depending on the intended use of your coin after undergoing coinjoin cycles, the fact that it has undergone this process can be problematic. For example, if you plan to sell your coin on a regulated exchange platform, but it has recently undergone a coinjoin, the platform's chain analysis tool will detect this fact. The platform may then refuse to accept your UTXO that has suffered a coinjoin, or even demand explanations from you, with the risk of having your account suspended or your funds frozen. In some cases, the platform may also report your behavior to state authorities (for example, this is what TRACFIN requires of Digital Asset Service Providers (PSANs) in France).

What we would need to avoid this is a tool capable of blurring the traces of a Bitcoin coin's past in order to restore some form of fungibility. This is precisely the goal of ricochet.

### What is a ricochet?

Ricochet is a technique that involves performing several dummy transactions to oneself (sweeping) to simulate a transfer of bitcoin ownership. This tool is different from other transaction structures we have discussed because it does not allow for prospective anonymity, but rather a form of retrospective anonymity. In fact, ricochet allows for the blurring of specificities that might compromise the fungibility of a bitcoin coin because of its past.

To obfuscate the imprint left by a past event on a coin, such as coinjoin cycles, for example, ricochet performs four successive transactions in which the user transfers funds to himself at different addresses.

After this sequence of transactions, the ricochet tool finally routes the bitcoins to their final destination as an exchange platform.

The goal is to create a distance that affects the fungibility of the coin, such as a coinjoin transaction, and the final act of spending that might reject this coin because of its past. Thus, chain analysis tools might conclude that there was probably a change of ownership after the event, and consider that this coin is fungible. In the case of a coinjoin, the chain analysis tools could then assume that it is not the same person who sent the bitcoins and executed the coinjoin, and thus it is useless to initiate actions against the sender.

### Why does it work?

Faced with this ricochet method, one might imagine that the chain analysis software would deepen their examination beyond four hops. However, these platforms face a dilemma in optimizing the detection threshold. They need to set a limit on the number of hops after which they admit that a change in ownership has probably occurred and that the link to a previous event (such as a coinjoin) should be ignored.

However, determining this threshold proves risky: each extension of the observed number of skips exponentially increases the volume of false positives, i.e., individuals incorrectly marked as participants in an event when the transaction was performed by someone else. This scenario poses a greater risk to these companies, as false positives lead to dissatisfaction, which can drive affected customers to competitors. In the long run, too large a detection threshold leads a platform to lose more customers than its competitors, which could threaten its survival. Therefore, it is complicated for these platforms to increase the number of jumps observed, and 4 is often a sufficient number to counter their analysis.

The phenomenon observed here is somewhat analogous to the six degrees of separation theory.

The theory of six degrees of separation suggests that any person on Earth is connected to any other through a chain of knowledge that includes no more than six intermediaries. It would be enough to go through a series of six people, each knowing the next personally, to reach any individual in the world.

For Bitcoin transactions, one finds a similar phenomenon. By tracking back a sufficient number of Bitcoin transactions, one inevitably ends up encountering a coinjoin. The ricochet method exploits this principle by using more hops than the exchange platforms can reasonably follow. If platforms decide to follow more transactions, it is then possible to simply add an additional hop to circumvent this measure.

### When and how to use ricochet?

The most common use case for ricochet occurs when it is necessary to hide previous participation in a coinjoin on a UTXO that you own. Ideally, it is best to avoid transferring bitcoins that have undergone a coinjoin to regulated entities. However, in the event that one finds oneself without other options, especially in the urgency of liquidating bitcoin into fiat currency, ricochet offers an effective solution.

This method is effective not only for coinjoins but also for any other marks that might compromise the fungibility of a coin.

The idea for this ricochet method originally came from the Samourai Wallet teams, who integrated it into their application to automate the process. There is a charge for the service on Samourai, as a ricochet carries a service fee of 100,000 sats, in addition to mining fees. Therefore, its use is rather recommended for transfers of significant amounts.

The Samourai application offers two variations of the ricochet:


- Advanced ricochet, or "staggered delivery," which has the advantage of spreading Samourai's service fees over five successive transactions. This option also ensures that each transaction is transmitted at a separate time and recorded in a different block, which allows it to mimic the behavior of a change of ownership as closely as possible. Although slower, this method is preferable for those who are not in a hurry, as it maximizes the efficiency of the ricochet by strengthening its resistance to chain analysis;
- The classic ricochet, which is designed to perform the operation quickly by transmitting all transactions in a short period of time. This method, therefore, offers less privacy and less resistance to analysis than the advanced method. It should be used only for urgent submissions.

Recochet consists simply of sending bitcoin to oneself. It is entirely possible to perform a ricochet manually on any wallet software, without using a specialized tool. Simply transfer the same coin to yourself later, using a new empty address each time.

In the following chapter, we explore several techniques for secret property transfers. These methods differ radically from those we have examined so far, both in terms of how they work and their results.

https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589
## Secret Property Transfers

<chapterId>a2067036-849c-4d6b-87d2-44235cfae7a1</chapterId>

Among the privacy techniques on bitcoin is the secret transfer of ownership. This method aims to transfer ownership of bitcoins from one person to another, and vice versa, without this transaction being explicitly visible on the blockchain. Let us study together the different techniques available as well as their advantages and disadvantages.

### The CoinSwap

CoinSwap is based on a relatively simple concept: it uses smart contracts to facilitate a transfer of bitcoin ownership between two users, without the need for trust and without this transfer being explicitly visible on the blockchain.

Let us imagine a simplified example with Alice and Bob. Alice holds 1 BTC secured with private key $A$, and Bob also holds 1, secured with private key $B$. Theoretically, they could exchange their private keys via an external communication channel to perform a secret transfer.

However, this naive method presents a high risk in terms of trust. Nothing prevents Alice from keeping a copy of the $A$ private key after the exchange and using it later to steal bitcoins once the key is in Bob's possession.

Moreover, there is no guarantee that prevents Alice from receiving Bob's private key $B$ and never sending his private key $A$ in return. This exchange, therefore, relies on excessive trust between the parties and proves to be inefficient in ensuring a secret transfer of ownership in a secure manner.

To solve these problems and allow exchanges between parties who do not trust each other, we can instead use smart contract systems. A smart contract is a program that runs automatically when predefined conditions are met, which, in our case, ensures that the exchange of property occurs automatically without requiring mutual trust.

To do this, we can use HTLC (_Hash Time-Locked Contracts_) or PTLC (_Point Time-Locked Contracts_). These two protocols work similarly using a time-lock system that ensures that the exchange is successfully completed or completely canceled, thus protecting the integrity of both parties' funds. The main difference between HTLC and PTLC is that HTLCs use hashes and preimages to secure the transaction, while PTLCs use Adaptive Signatures.

In a CoinSwap scenario using an HTLC or a PTLC between Alice and Bob, the exchange takes place in a secure manner: either it succeeds, and each receives the other's BTC, or it fails, and each keeps its own BTC. It is therefore impossible for either party to cheat or steal the other's BTC.

> _The HTLCs are also the mechanism used to route payments securely through the two-way channels of the Lightning Network._
> The use of Adaptive Signatures is particularly interesting in this context, as it allows traditional scripts to be bypassed (this is a mechanism sometimes referred to as "_scriptless scripts_"). This feature helps reduce the fees associated with the exchange. Another major advantage of Adaptive Signatures is that they do not require the use of a common hash for both sides of the transaction, thus avoiding revealing a direct link between them in certain types of exchanges.
### Adaptive Signatures

Adaptive Signatures are a cryptographic method that integrates a valid signature with an additional signature, called an "_adaptive signature_," to reveal a secret piece of data. This mechanism is designed in such a way that knowing 2 of the following 3 elements: the valid signature, the adaptive signature and the secret, allows the third missing element to be deduced. An interesting property of this method is that if we know the adaptive signature of our counterpart and the specific point on the elliptic curve associated with the secret used to compute this adaptive signature, we can derive our own adaptive signature that will be compatible with that same secret, without ever having direct access to the secret itself.

In coin exchanges, the use of Adaptive Signatures allows the simultaneous disclosure of two pieces of sensitive information between participants, thus avoiding the need for mutual trust. Let us take an example to illustrate this process with Alice and Bob, who wish to exchange ownership of 1 BTC each, but do not trust each other. They use Adaptive Signatures to eliminate the need for trust in this exchange. Here is how they proceed:


- Alice initiates the exchange by creating a transaction $m_A$ that sends 1 BTC to Bob. She generates a signature $s_A$, which validates this transaction, using her private key $p_A$ ($P_A = p_A \cdot G$), a nonce $n_A$ ($N_A = n_A \cdot G$), and a secret $t$ ($T = t \cdot G$):

$$s_A = n_A + t + H(N_A + T \parallel P_A \parallel m_A) \cdot p_A$$


- Alice computes the adaptive signature $s_A'$ by subtracting the secret $t$ from her true signature $s_A$:

$$s_A' = s_A - t$$


- Alice sends Bob her adaptive signature $s'_A$, her unsigned transaction $m_A$, the point corresponding to the secret ($T$), and the point corresponding to the nonce ($N_A$). These elements constitute what is called an "_adapter_." It is important to note that with only this information, Bob cannot retrieve Alice's BTC.
- However, Bob has the ability to verify that Alice is not trying to steal from him. To do this, he checks whether Alice's adaptive signature $s_A'$ actually matches the proposed transaction $m_A$. If the following equation is correct, he can then be sure that Alice's adaptive signature is valid:

$$s_A' \cdot G = N_A + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$


- This verification provides Bob with sufficient assurance to proceed with the exchange in a confident manner. He then creates his own transaction $m_B$, intended to send 1 BTC to Alice, and generates his adaptive signature $s_B'$, which will also be linked to the same secret $t$. At this point, only Alice knows the value of $t$; Bob knows only the corresponding point $T$ that Alice transmitted to him:

$$s_B' = n_B + H(N_B + T \parallel P_B \parallel m_B) \cdot p_B$$


- Bob transmits to Alice his adaptive signature $s_B'$, his unsigned transaction $m_B$, as well as the point corresponding to the secret ($T$) and the point corresponding to the nonce ($N_B$). Alice, who knows the secret $t$, can now combine Bob's adaptive signature $s_B'$ with this secret to generate a valid signature $s_B$ for the transaction $m_B$ that will transfer Bob's BTC to her:

$$s_B = s_B' + t$$

$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \parallel P_B \parallel m_B) \cdot P_B$$


- Alice transmits this signed transaction $m_B$ on the Bitcoin blockchain to retrieve the BTC promised by Bob. When Bob sees this transaction on the blockchain, he can extract the signature $s_B = s_B' + t$. With this information, Bob is then able to isolate the famous $t$ secret he needed:

$$t = (s_B' + t) - s_B' = s_B - s_B'$$


- And in fact, this secret $t$ was the only missing element for Bob to generate the valid signature $s_A$ from Alice's adapter signature $s_A'$. This signature allows the transaction $m_A$ that sends a BTC from Alice to Bob to be validated. Bob then computes $s_A$ and in turn transmits the $m_A$ transaction on the blockchain:

$$s_A = s_A' + t$$

$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$

Let us summarize how a Signature Adapter works in a coin exchange. Initially, Alice sends Bob an unsigned transaction along with an adapter, which allows Bob to verify that the secret revealed later will give him access to bitcoins. In return, Bob sends Alice his unsigned transaction and adapter. Alice can then finalize Bob's transaction and recover the bitcoins by transmitting a valid transaction using the secret. When this transaction is published on the blockchain, Bob has the ability to extract the secret and thus unlock Alice's transaction. Consequently, if Alice initiates a transfer of Bob's bitcoins, he can, in turn, access Alice's bitcoins without requiring mutual trust.

It is important to note that coin exchanges were first proposed by [Gregory Maxwell in October 2013 on BitcoinTalk](https://bitcointalk.org/index.php?topic=321228.0).

### The Atomic Exchange

Similar to the coin exchange and using the same types of smart contracts, it is also possible to perform atomic exchanges. An atomic exchange allows a direct exchange of different cryptocurrencies, such as BTC and XMR, between two users without requiring trust or the intervention of an intermediary. These exchanges are called "atomic" exchanges because they have only two possible outcomes: either the exchange succeeds and both parties are satisfied, or it fails and each retains their original cryptocurrencies, thus eliminating the need for trust in the other party.

![BTC204](assets/fr/197.webp)

Atomic exchange and coin exchange share a similar method of operation and offer the same advantages and disadvantages in terms of privacy. In fact, from Bitcoin's perspective, an atomic exchange is comparable to a coin exchange performed in two steps. First, we exchange our BTC for another cryptocurrency, and then this cryptocurrency can be exchanged for other BTC. Finally, we retrieve another user's BTC. This is why, in the analysis of privacy issues, I group these two protocols under the category of secret exchanges of property.

![BTC204](assets/fr/198.webp)

However, unlike coin exchange, atomic exchange can have imbalances in terms of available liquidity, especially in BTC/XMR exchanges. Generally, it is easier to exchange bitcoin for altcoin because there is a large demand for bitcoin, which keeps the premiums for this direction of conversion low. However, trading altcoin to get BTC can be more complex because of lower demand, often resulting in very high premiums.

Finally, when an atomic exchange involves onchain bitcoin and bitcoin on the Lightning network, we refer to it as a "_submersible exchange_."

### Is it Really Useful?

Secret transfers of ownership, such as coin exchanges and atomic exchanges, have the advantage of fooling chain analysis heuristics. These methods can give the impression that transactions involve the same user, even if the actual ownership has changed hands. However, the main disadvantage of these methods is that they are very risky without the use of an additional technique to disrupt the coin history.

Effectively, when Alice makes a coin exchange or atomic swap with Bob, she exchanges the ownership of her bitcoins for Bob's bitcoins. In the case of an atomic swap, the exchange includes an altcoin, but the principle remains the same. Thus, Alice ends up with coin $B$ and Bob with coin $A$. This adds doubt in the chain analysis, but the history of the coins remains traceable. If an analyst examines coin $A$, he or she can trace Alice's previous activities, and vice versa for coin $B$.

From Alice's point of view, the risk is that the history of the $B$ coin could be considered suspicious by certain entities. If, for example, Bob had acquired the $B$ coin in a criminal act such as hacking, this coin would remain linked to his illegal activities. Alice could then find herself in possession of a coin that she could not transfer to regulated trading platforms without risking having her funds frozen, or even being accused of Bob's crimes, although she had nothing to do with them.

And of course, privacy methods such as coin swapping or atomic swapping are favored by criminals whose funds are monitored by authorities. These protocols give them the opportunity to dispose of their monitored bitcoins in exchange for perfectly fungible bitcoins. This also allows them to create diversion by directing authorities to other users. There is thus a dual utility for these people.

With coinjoin, even if your coin is mixed with monitored bitcoins, the coin's history is broken, which provides a form of plausible deniability that is nonexistent in secret property transfer protocols such as coin exchange or atomic swap.

If Alice wants to avoid any risk, she must necessarily use a method to disrupt the history of the $B$ coin, such as running it through coinjoins, for example. This raises a question about the usefulness of combining secret transfer of ownership and coinjoin. The coinjoin, by interrupting the history of a coin, already provides a sufficient level of privacy for Alice. Thus, my view is that if Alice seeks to protect her privacy, it would be more prudent to proceed directly with a coinjoin than to engage in a coin exchange followed by a coinjoin.

For methods of secret transfer of ownership to be truly effective and avoid the risk of linking the history of an $A$ user to a $B$ user, it would be paradoxically necessary for their use to be widely known. If coin exchange is used massively and authorities are aware of this common practice, then a plausible form of deniability could be established. However, as long as the use of these transfers remains marginal, I believe these methods will remain too risky for users.

So far, we have mainly studied privacy methods at the transaction level itself. In the next chapter, we will explore issues at the network level and transaction diffusion.

## Privacy on the P2P Network

<chapterId>04a2467b-db84-4076-a9ff-919be5135106</chapterId>

In Part 4, we discussed the importance of using a full node to protect the privacy of your transactions. However, it is important to understand that your node itself can be subject to attacks that seek to extract information about your activities. In this chapter, we will therefore look at different privacy protection measures, not at the level of the transactions themselves or the bitcoin streams, but at the network level.

### Dandelion

One way to avoid various deanonymization attacks is to use the proposed Dandelion. This transmission protocol was formalized in BIP156, but has never been implemented on Bitcoin. The idea of Dandelion is to improve the privacy of transaction routing in the Bitcoin network to thwart various forms of attacks. Its main goal is to hide the source node that initially transmits a transaction on the network. Disclosure of this node could link a Bitcoin transaction to a specific IP address (if the node operates on the unencrypted network), thus providing an entry point for chain analysis.

This association between an activity on Bitcoin and an IP address poses a significant risk to user privacy. In fact, numerous entities can easily link an IP address to a personal identity. This remarkably includes governments and Internet service providers. In addition, this information can become publicly accessible, for example, if your IP address and personal data are exposed due to a data leak during a website database hack.

In the standard operation of Bitcoin, transactions built by a user on their software wallet are transmitted to their personal node. This node immediately transmits the new transaction to all peers to which it is connected.

These peers then verify the transaction to ensure that it meets consensus rules and local standardization rules. Once validated, each peer in turn forwards the transaction to its peers, and so on.

The distribution of transactions awaiting integration in a block happens in a fairly balanced and statistically predictable manner. This vulnerability can be exploited by colluding spy nodes, which collaborate to monitor and analyze the network in order to identify the first node to transmit a transaction. If an observer can locate the source node, they can assume that the transaction came from the operator of that node. This type of observation can link transactions, normally anonymous, to specific IP addresses.

The goal of BIP156 is to address this problem. To do so, it introduces an additional stage in the transmission of a new transaction to preserve anonymity before large-scale public dissemination. Dandelion first uses a "stem" phase where the transaction is sent through a random path of nodes.

The transaction is then transmitted to the entire network in the "fluff" (blowhole) stage.

The stem and the dandelion are references to the behavior of the propagation of the transaction through the network, which resembles the shape of a dandelion.

Thus, spy nodes can potentially trace the transaction back to the node that initiated the blowing phase (the massive transmission), but this node is not the one that first transmitted the transaction, since it received it from the last node in the stem. If the spy nodes cannot trace the stem, they cannot identify the source node either.

Even in the presence of spy nodes during the stem phase, doubt always remains because as soon as they encounter an honest node in the diffusion graph, the spies cannot determine whether this node is the original source or simply an intermediary.

This routing method makes it more difficult to track back to the source node, making it complicated to trace a transaction through the network to its origin. Dandelion thus improves privacy by limiting the ability of adversaries to deanonymize the network. This method is even more effective when the transaction, during the "stem" phase, traverses a node that encrypts its network communications, as with Tor or P2P Transport V2.

BIP156 has not been integrated into Bitcoin Core and is currently classified with the status "rejected." A major concern about this protocol lies in the fact that, during the stem phase, transactions must be forwarded by intermediate nodes before being verified. As we have seen, in the normal Bitcoin model, each node first verifies the transaction before forwarding it to its peers. If a transaction does not meet the node's consensus or local standardization rules, it is ignored and not forwarded. This process is important in thwarting DoS attacks, since only valid transactions are transmitted to the entire network. Invalid transactions, potentially generated en masse to overload the network, are stopped at the first node encountered and do not propagate. The main risk with Dandelion is that this new protocol could introduce new vectors for DoS attacks by allowing invalid transactions to be transmitted through part of the network.

### P2P Transport V2

P2P Transport V2 is another network protocol presented in BIP324. It is a new version of Bitcoin's P2P transport protocol that incorporates opportunistic cryptography to improve the confidentiality and security of communications between nodes.

This improvement aims to solve several problems with the basic version of the P2P protocol. For one thing, it makes exchanged data indistinguishable from other types of data circulating on the Internet to a passive observer. The main goal is to prevent governments, Internet service providers, or VPN providers from massively monitoring Bitcoin users. This also complicates the task for these entities to determine whether an Internet user is also a Bitcoin user, i.e., whether they are operating a full node.

P2P V2 also helps reduce the risks of censorship and attacks by detecting specific patterns in data packets. It complicates and makes it more costly to execute various types of Sybil attacks at the network level. A Sybil attack occurs when an actor creates multiple false identities to gain undue advantage. In the context of the Bitcoin network, this often manifests as an actor controlling a large number of complete nodes and aggressively using them to multiply connections. Sybil attacks can be passive, aiming to gather information and compromise user confidentiality, or active, in the form of Eclipse attacks. The latter isolate a specific node from the rest of the network, allowing it to censor the user or alter the data it receives. Finally, P2P V2 makes _Man-In-The-Middle_ (MITM) attacks more expensive and easier to detect.

The encryption implemented by P2P V2 does not include authentication so as not to add unnecessary complexity and not to compromise the permissionless nature of the network connection. However, this new P2P transport protocol provides better security against passive attacks and makes active attacks significantly more costly and detectable. The introduction of a pseudo-random data stream in network messages complicates the task for attackers who wish to censor or manipulate communications.

P2P V2 transport was included as an option (disabled by default) in version 26.0 of Bitcoin Core, deployed in December 2023. It was then enabled by default in version 27.0 in April 2024. It can be changed with the `v2transport=` option in the configuration file.

### Tor

A relatively simple solution to avoid the risks of loss of confidentiality for a network-level node is to run it entirely under Tor. Tor is a network of relay servers (nodes) that anonymizes the origin of TCP connections over the Internet. It works by encapsulating data in multiple layers of encryption. Each relay node removes one layer to reveal the address of the next node, until the final destination is reached. The Tor network ensures anonymity by preventing intermediate nodes from knowing both the origin and destination of the data, making it very difficult for an observer to track user activity.

Tor therefore not only encrypts the data communicated but also allows the origin and destination of communications to be masked. By using Tor for one's personal node communications, we improve the privacy of our transactions: the Internet Service Provider (ISP) cannot decrypt the communications, and other nodes in the Bitcoin network cannot identify the IP address of the source node. In addition, Tor also hides the use of Bitcoin from one's ISP.

The main risk associated with this method is that Tor is a Bitcoin-independent protocol. If you have a Bitcoin node under Tor and Tor stops working, then your Bitcoin node will no longer be able to communicate.

Also, it is important to note that communications on Tor are slower. This latency is particularly troublesome during the initial launch of a node, as Initial Block Download (IBD) requires a lot of communication. As a result, the initial synchronization with the Bitcoin network could be significantly longer using Tor. It is also possible to perform IBD on the open network and then activate Tor later. Although this method reveals the existence of your Bitcoin node to your ISP, it protects your personal transaction information once you switch to Tor.

Having explored the different privacy methods at the network level, I also want to introduce in the next chapters two elegant solutions to avoid address reuse: BIP47 and Silent Payments.

## BIP47 and Reusable Payment Codes

<chapterId>ad88e076-a04b-4aec-b3b2-7b4760175504</chapterId>

As we saw in Part 3, address reuse is a serious obstacle to user privacy on the Bitcoin protocol. To mitigate these risks, it is strongly recommended to generate a new receiving address for each new payment received in a wallet. Although today the generation of a new address is simplified by the use of modern software and hierarchical deterministic wallets, this practice may seem counterintuitive.

In the traditional banking system, for example, we are used to sharing our IBAN, which always remains the same. Once we tell someone, they can send us multiple payments without having to interact with us again. Neo-banks also offer more modern possibilities such as the use of unique email addresses on PayPal or RevTags on Revolut. Even outside the financial domain, our daily identifiers such as mailing address, phone number, and email address are unique and permanent. We do not have to renew them with each new interaction.

However, how Bitcoin works is different: it is imperative to generate a new receiving address for each incoming transaction. This trade-off between ease of use and privacy goes back to the very origins of Bitcoin's white paper. Since the publication of the first version of his paper in late 2008, Satoshi Nakamoto had already warned us of this risk:

**"_As an additional firewall, a new key pair could be used for each transaction to keep them unlinked to a common owner._"**

There are numerous methods for receiving multiple payments on a single identifier without causing address reuse. Each of these methods has its own tradeoffs and disadvantages. Among these methods is BIP47, a proposal developed by Justus Ranvier and published in 2015. This proposal aims to create reusable payment codes that allow multiple transactions to the same person while avoiding address reuse. In essence, BIP47 seeks to offer an intuitive payment system as a unique identifier while preserving transaction privacy.

![BTC204](assets/fr/212.webp)

BIP47 does not directly improve user privacy, since a BIP47 payment offers the same level of privacy as a classic Bitcoin transaction using fresh addresses. However, it does make the use of Bitcoin more convenient and intuitive, an ease that would normally have to compromise privacy. Thanks to BIP47, this ease of use achieves the same level of privacy as a classic transaction. This is why BIP47 is a valuable tool for privacy preservation.

Initially, BIP47 was a proposal formulated to be integrated into Bitcoin Core, but it was never adopted. However, some software chose to implement it independently at the application level. Thus, the Samourai Wallet teams developed their own implementation of BIP47 called "PayNym."

### General Principle of BIP47 and PayNym

The goal of BIP47 is to enable the receipt of numerous payments without causing address reuse. It is based on the use of a reusable payment code, which allows different senders to send multiple payments to a single code belonging to another user. Thus, the recipient does not have to provide a fresh address for each transaction, which greatly facilitates their exchanges while preserving their privacy.

![BTC204](assets/it/66/4.webp)

A user can then freely share his or her payment code, either on social networks or on his or her own website, without risking loss of privacy, unlike what would happen with a classic receiving address or public key.

To conduct a transaction, both parties must have a Bitcoin wallet with an implementation of BIP47, such as PayNym on Samourai Wallet or Sparrow Wallet. The joint use of their payment codes creates a secret channel between them. To establish this channel efficiently, the sender must perform a specific transaction on the Bitcoin blockchain, known as a "notification transaction" (I will provide more details on this later).

The combination of both users' payment codes generates shared secrets, which in turn allow the creation of a large number of unique Bitcoin receiving addresses (exactly 2^32, or about 4 billion). Thus, payments made through BIP47 are not actually addressed to the payment code itself, but rather to classic receiving addresses derived from the payment codes of the users involved.

The payment code then serves as a virtual identifier derived from the seed of the wallet. In the hierarchical derivation structure of the portfolio, the payment code is placed at level 3, that is, at the account level.

![BTC204](assets/it/66/5.webp)

The derivation target for BIP47 is identified by the index `47'` (`0x8000002F`), which refers to BIP47. An example of a derivation path for a reusable payment code would be as follows:

```plaintext
m/47'/0'/0'/
```

To give you an idea of what a payment code looks like, here is mine:

```plaintext
M8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```

This code can also be encoded into a QR code for easy communication, just like a classic receiving address.

As for PayNym Bots, these robots sometimes seen on Twitter are visual representations of payment code, created by Samourai Wallet. They are generated through a hashing function, which gives them almost uniqueness. They appear as a small string of characters beginning with `+`:

```plaintext
+throbbingpond8B1
+twilightresonance487
+billowingfire340
```

These avatars can also be represented as images:

![BTC204](assets/fr/215.webp)

Although these robots do not have a specific technical functionality within the BIP47 framework, they play a role in facilitating interactions between users by offering an easily recognizable visual identity.

---
*In the following sections of this chapter devoted to BIP47, we will examine its operation in detail, focusing in particular on the cryptographic methods used. To fully understand these rather technical explanations, it is first essential to understand the structure of HD wallets, key derivation processes, and the basic principles of elliptic curve-based cryptography. If you would like to learn more about these concepts, another free course is available from Plan ₿ Network:*

https://planb.network/courses/cyp201
*I highly recommend you follow it, because understanding the technical workings of BIP47 will help you much more easily understand other similar proposals that we will discuss in the coming chapters.*

---
### Reusable Payment Code

As mentioned earlier, the reusable payment code is located at level 3 of the HD wallet, making it comparable to an `xpub`, both in its position within the wallet structure and in its role.

The 80-byte payment code is divided as follows:


- Byte `0`: Version**. For the first version of BIP47, this byte is set to `0x01`;
- Byte `1`: The bit field**. This space is reserved for incorporating additional indications during specific uses. For standard use with PayNym, this byte is defined as `0x00`;
- Byte `2`: The parity of `y`**. This byte is `0x02` or `0x03`, indicating whether the ordinate of the public key is even or odd, since a compressed public key is used;
- From byte `3` to byte `34`: The value of `x`**. These bytes represent the abscissa of the public key. The concatenation of `x` and the parity of `y` forms the complete compressed public key;
- From byte `35` to byte `66`: Chain code**. This space contains the chain code associated with the public key;
- From byte `67` to byte `79`: Filling**. This space is intended for possible future development. For the current version, zeros are simply placed here to achieve the 80 byte size required for an `OP_RETURN` output.

Here is the hexadecimal representation of my reusable payment code already presented in the previous section:

```plaintext
0x010002a0716529bae6b36c5c9aa518a52f9c828b46ad8d907747f0d09dcd4d9a39e97c3c5f37c470c390d842f364086362f6122f412e2b0c7e7fc6e32287e364a7a36a00000000000000000000000000
```

![BTC204](assets/it/66/7.webp)

First of all, it is necessary to add the prefix byte `P` at the beginning to clearly indicate that it is a payment code. This byte is represented by `0x47`:

```plaintext
0x47010002a0716529bae6b36c5c9aa518a52f9c828b46ad8d907747f0d09dcd4d9a39e97c3c5f37c470c390d842f364086362f6122f412e2b0c7e7fc6e32287e364a7a36a00000000000000000000000000
```

Finally, to ensure the integrity of the payment code, a checksum calculation is performed using `HASH256`, which consists of double hashing with the `SHA256` function. The first four bytes resulting from this hash are then concatenated at the end of the payment code:

```plaintext
0x47010002a0716529bae6b36c5c9aa518a52f9c828b46ad8d907747f0d09dcd4d9a39e97c3c5f37c470c390d842f364086362f6122f412e2b0c7e7fc6e32287e364a7a36a00000000000000000000000000567080c4
```

Once these steps are completed, the payment code is ready. The only remaining step is to convert it to base 58 to get its final version:

```plaintext
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```

During this process of creating the payment code, we use a compressed public key and a chain code. Both are derived by deterministic and hierarchical derivation from the wallet seed. The derivation path used to achieve this is:

```plaintext
m/47'/0'/0'/
```

To generate the compressed public key and associated chain code for the reusable payment code, we start by computing the main private key from the wallet seed. We then proceed to derive a daughter key pair using the index `47 + 2^31` (reinforced derivation). This step is followed by two more successive derivations of daughter key pairs, each using the index `2^31` (reinforced derivation).

### The Elliptic-Curve Diffie-Hellman Key Exchange (ECDH)

The cryptographic protocol at the heart of BIP47 is referred to by the acronym ECDH, for _Elliptic-Curve Diffie-Hellman_. This method is a variant of the original Diffie-Hellman key exchange.

Introduced in 1976, Diffie-Hellman is a key agreement protocol that allows two parties, each equipped with a key pair (public and private), to agree on a common secret, even while communicating exclusively through a public, insecure channel.

![BTC204](assets/it/66/10.webp)

This shared secret (here, the blue key), can then be used for other operations. Typically, this shared secret can be used to encrypt and decrypt communication over an insecure network:

![BTC204](assets/fr/220.webp)

To accomplish this exchange, Diffie-Hellman uses modular arithmetic to calculate the shared secret. Here is a simplified explanation of how it works:


- Alice and Bob agree on a common color, here yellow, which constitutes public data (attackers know this color);
- Alice selects a secret color, here red, and mixes the two to get orange;
- Bob also chooses a secret color, here blue, and mixes it with yellow to get green;
- Then they exchange the obtained colors, orange and green. This exchange can take place on an insecure, observed network;
- By mixing Bob's green with his secret color, Alice produces brown;
- Bob, doing the same with Alice's orange and her secret blue, also gets brown.

![BTC204](assets/it/66/12.webp)

In this simplification, the color brown represents the secret shared between Alice and Bob. It is important to understand that, in reality, it is impossible for the attacker to separate the colors orange and green to discover the secret colors of Alice or Bob.

Now, let us examine how this protocol actually works, not with color analogies, but using real numbers and modular arithmetic!

Before discussing Diffie-Hellman mechanisms, let me briefly remind you of two essential mathematical concepts we will need:


- A **prime number** is a natural number that has only two divisors: $1$ and itself. For example, $7$ is a prime number because it can only be divided by $1$ and $7$. On the other hand, $8$ is not a prime number since it is divisible by $1$, $2$, $4$ and $8$. Therefore, it has four positive integer divisors instead of two;
- The **mod** (denoted $mod$ or $\%$) is a mathematical operation that, between two integers, returns the remainder of the Euclidean division of the former by the latter. For example, $16 \bmod 5 = 1$.

**The Diffie-Hellman key exchange between Alice and Bob proceeds as follows:**


- Alice and Bob agree on two common numbers: $p$ and $g$. $p$ is a prime number, and the larger this number, the more secure Diffie-Hellman will be. $g$ is a primitive root of $p$. These two numbers can be communicated openly over an unsecured network. They represent the equivalent of the **yellow color** in the above simplification. It is therefore important that Alice and Bob use exactly the same values for $p$ and $g$.

Once these parameters are defined, Alice and Bob each choose a random secret number. Alice calls her random secret number $a$ (equivalent to **the color red**) and Bob calls his $b$ (equivalent to **the color blue**). These numbers must remain strictly confidential.

Instead of directly exchanging the numbers $a$ and $b$, each side calculates $A$ and $B$ as follows:

$A$ is equal to $g$ raised to the power of $a$ modulo $p$:

$$
A = g^a \bmod p
$$

$B$ is equal to $g$ raised to the power of $b$ modulo $p$:

$$
B = g^b \bmod p
$$

The values $A$ (equivalent to **the color orange**) and $B$ (equivalent to **the color green**) are exchanged between the two parties. This exchange can take place openly over an unsecured network;

Alice, having received $B$, calculates the value of $z$ as follows:

$z$ is equal to $B$ raised to the power of $a$ modulo $p$:

$$
z = B^a \bmod p
$$

Recall:

$$
B = g^b \bmod p
$$

Thus, we get:

$$
z = B^a \bmod p
$$

$$
z = (g^b)^a \bmod p
$$

Applying the rules of exponents:

$$
(x^n)^m = x^{nm}
$$

We thus obtain:

$$
z = g^{ba} \bmod p
$$


- On his side, Bob, having received $A$, also calculates the value of $z$ in the following way:

$z$ is equal to $A$ raised to the power of $b$ modulo $p$:

$$
z = A^b \bmod p
$$

Thus, we get:

$$
z = (g^a)^b \bmod p
$$

$$
z = g^{ab} \bmod p
$$

$$
z = g^{ba} \bmod p
$$

Due to the distributivity of the modulo operator, Alice and Bob get exactly the same $z$ value. This number represents their common secret, equivalent to **the color brown** in the previous simplification with paint pots. They can now use this common secret to symmetrically encrypt their communications over an unsecured network.

An attacker, even in possession of $p$, $g$, $A$ and $B$ (the public values), will not be able to compute $a$, $b$ or $z$ (the private values). To do so would require inverting exponentiation, an impossible task without trying all possibilities one by one, since it is equivalent to computing the discrete logarithm, i.e., the inverse of the exponential in a finite cyclic group.

Therefore, as long as the values of $a$, $b$ and $p$ are sufficiently large, the Diffie-Hellman protocol is safe. Typically, with 2048-bit parameters (a number with 600 digits in decimal), testing all possibilities for $a$ and $b$ would be impractical. To date, with such numbers, this algorithm is considered safe.

This is precisely where the main disadvantage of the Diffie-Hellman protocol lies. To be safe, the algorithm must use large numbers. That is why, nowadays, people prefer the ECDH (_Elliptic Curve Diffie-Hellman_) algorithm, a variant of Diffie-Hellman that is based on an algebraic curve, more precisely an elliptic curve. This approach makes it possible to work with much smaller numbers while maintaining equivalent security, thus reducing the resources required for computation and storage.

The general principle of the algorithm remains the same. However, instead of using a random number $a$ and a number $A$ computed from $a$ by modular exponentiation, we use a key pair established on an elliptic curve. Instead of relying on the distributivity of the modulo operator, we use the group law on elliptic curves, and more specifically the associativity of this law.

To briefly explain the principle of elliptic curve cryptography, a private key is represented by a random number between $1$ and $n-1$, where $n$ represents the order of the curve. The public key, on the other hand, is a specific point on this curve, obtained from the private key by addition and doubling operations of points starting from the generating point, according to the equation:

$$
K = k \cdot G
$$

In this formula, $K$ denotes the public key, $k$ the private key, and $G$ the generating point.

One of the essential features of these keys is the ease of computing $K$ from $k$ and $G$, while it is virtually impossible to find $k$ from $K$ and $G$. This asymmetry creates a one-way function. In other words, it is easy to compute the public key if one knows the private key, but finding the private key from the public key is impossible. This security still relies on the computational difficulty of the discrete logarithm.

We will use this property to adapt our Diffie-Hellman algorithm. **The working principle of ECDH is as follows:**


- Alice and Bob agree together on a cryptographically secure elliptic curve and its parameters. This information is public;
- Alice generates a random number $ka$ that will be her private key. This private key must remain secret. She determines her public key $Ka$ by addition and doubling of points on the chosen elliptic curve:

$$
K_a = k_a \cdot G
$$


- Bob also generates a random number $kb$ that will be his private key. He calculates the associated public key $kb$:

$$
K_b = k_b \cdot G
$$


- Alice and Bob exchange their public keys $Ka$ and $Kb$ on an unsecured public network.
- Alice computes a point $(x,y)$ on the curve by applying her private key $ka$ to Bob's public key $Kb$:

$$
(x,y) = k_a \cdot K_b
$$


- Bob computes a point $(x,y)$ on the curve by applying his private key $kb$ to Alice's public key $Ka$:

$$
(x,y) = k_b \cdot K_a
$$


- Alice and Bob get the same point on the elliptic curve. The shared secret will be the $x$ coordinate of this point.

In fact, they get the same shared secret because:

(x,y) = k_a \cdot K_b = k_a \cdot (k_b \cdot G) = (k_a \cdot k_b) \cdot G = (k_b \cdot k_a) \cdot G = k_b \cdot (k_a \cdot G) = k_b \cdot K_a

$$
Un attaccante che osserva la rete pubblica non protetta può ottenere solo le chiavi pubbliche di ciascuna parte e i parametri della curva ellittica scelta. Come precedentemente spiegato, queste informazioni da sole non sono sufficienti per determinare le chiavi private. Pertanto, l'attaccante non può trovare il segreto condiviso tra Alice e Bob.
ECDH è quindi un algoritmo che consente lo scambio di chiavi. È spesso utilizzato in combinazione con altri metodi crittografici per stabilire un protocollo completo. Ad esempio, ECDH è integrato nel nucleo di TLS (_Transport Layer Security_), un protocollo di crittografia e autenticazione utilizzato per il livello di trasporto di Internet. TLS utilizza ECDHE per lo scambio di chiavi, una variante di ECDH dove le chiavi sono effimere, per garantire la confidenzialità persistente. Inoltre, TLS utilizza algoritmi di autenticazione come ECDSA, algoritmi di crittografia come AES e funzioni hash come SHA256.
TLS è notevolmente responsabile della `s` in `https` così come del lucchetto visibile nella barra degli indirizzi del tuo browser, simboli delle comunicazioni criptate. Seguendo questo corso, stai quindi utilizzando ECDH, ed è molto probabile che lo usi quotidianamente senza nemmeno saperlo.
### La Transazione di Notifica
Come abbiamo visto nella sezione precedente, ECDH è una variante dello scambio Diffie-Hellman che utilizza coppie di chiavi stabilite su una curva ellittica. Convenientemente, possediamo già molte coppie di chiavi aderenti a questo standard nei nostri portafogli Bitcoin! L'idea di BIP47 è di utilizzare le coppie di chiavi dei portafogli Bitcoin gerarchici deterministici di entrambe le parti per stabilire segreti condivisi ed effimeri tra di loro. Nel contesto di BIP47, viene utilizzato ECDHE (_Elliptic Curve Diffie-Hellman Ephemeral_).
ECDHE viene utilizzato per la prima volta in BIP47 per trasmettere il codice di pagamento dal mittente al destinatario. Questo è il famoso **notification transaction**. Questo passaggio è essenziale perché affinché BIP47 funzioni efficacemente, entrambe le parti coinvolte (il mittente e il destinatario) devono conoscere il codice di pagamento dell'altro. Questa conoscenza consente la derivazione di chiavi pubbliche effimere e, di conseguenza, indirizzi di ricezione vuoti associati.
Prima di questo scambio, il mittente è logicamente già a conoscenza del codice di pagamento del destinatario poiché lo ha recuperato off-chain, ad esempio, dal loro sito web, una fattura o i loro social media. Tuttavia, il destinatario potrebbe non conoscere necessariamente il codice di pagamento del mittente. Eppure, questo codice deve essere trasmesso a loro; altrimenti, non saranno in grado di derivare le chiavi effimere necessarie per identificare gli indirizzi dove sono conservati i loro bitcoin, né accedere ai loro fondi. Sebbene questa trasmissione del codice del mittente possa tecnicamente essere effettuata off-chain attraverso altri mezzi di comunicazione, ciò pone un problema se il portafoglio deve essere recuperato solo dal seme.
Infatti, a differenza degli indirizzi convenzionali, gli indirizzi BIP47 non sono derivati direttamente dal seed del destinatario—utilizzare un `xpub` sarebbe più semplice in questo caso—ma risultano da un calcolo che combina i codici di pagamento di entrambi: quello del mittente e quello del destinatario. Pertanto, se il destinatario perde il proprio portafoglio e tenta di ripristinarlo dal proprio seed, recupererà il proprio codice di pagamento, che è derivato direttamente dal loro seed. Tuttavia, per trovare gli indirizzi effimeri, sarà essenziale per loro avere anche i codici di pagamento di tutti coloro che hanno inviato loro bitcoin tramite BIP47. Da qui l'importanza della transazione di notifica, che consente di salvare queste informazioni sulla blockchain di Bitcoin, pur essendo in grado di trovarle molto facilmente senza dover cercare tra il miliardo di transazioni eseguite dal suo lancio nel 2009.
![BTC204](assets/it/66/15.webp)
Pertanto, sarebbe possibile implementare BIP47 senza ricorrere alla transazione di notifica, a condizione che ogni utente conservi un backup dei codici di pagamento dei propri pari. Tuttavia, questo metodo si rivela complesso da gestire finché non viene sviluppata una soluzione semplice, robusta ed efficiente per creare, conservare e aggiornare questi backup. Nello stato attuale delle cose, la transazione di notifica diventa quasi indispensabile.
Nei capitoli seguenti, studieremo altri protocolli con obiettivi simili a quelli di BIP47, ma che non richiedono una transazione di notifica. Queste alternative, tuttavia, introducono i propri compromessi.
Oltre al suo ruolo nel backup dei codici di pagamento, la transazione di notifica serve anche una funzione di notifica per il destinatario, come suggerisce il suo nome. Segnala al client del destinatario che è stato stabilito un nuovo canale di pagamento e suggerisce quindi di monitorare gli indirizzi effimeri risultanti.
### Il Modello di Privacy di BIP47
Prima di dettagliare il funzionamento tecnico della transazione di notifica, è importante discutere il modello di privacy associato a BIP47, che giustifica alcune misure prese durante la creazione di questa transazione iniziale.
Il codice di pagamento, di per sé, non rappresenta un rischio diretto per la privacy. A differenza del modello Bitcoin tradizionale, che mira a rompere il collegamento tra l'identità di un utente e le sue transazioni (che sono pubbliche) preservando l'anonimato di chiavi e indirizzi, il codice di pagamento può essere apertamente associato a un'identità senza rappresentare una minaccia.
Infatti, il codice di pagamento non è utilizzato per derivare direttamente gli indirizzi che ricevono pagamenti BIP47. Questi indirizzi sono invece generati attraverso l'applicazione di ECDH tra le chiavi derivate dai codici di pagamento delle due parti coinvolte.
Così, un codice di pagamento di per sé non porta direttamente a una perdita di privacy, poiché solo l'indirizzo di notifica è derivato da esso. Sebbene questo indirizzo possa rivelare alcune informazioni, normalmente non consente di scoprire le parti con cui si stanno conducendo transazioni, a meno che non si effettui un'analisi approfondita della catena. Infatti, se il mittente utilizza UTXO che possono essere collegati alla loro identità per eseguire la transazione di notifica, allora diventa possibile dedurre che la loro identità è probabilmente collegata ai pagamenti BIP47 al tuo codice di pagamento. Questo non rivelerà le transazioni sottostanti, ma indicherà la loro probabile esistenza.
Pertanto, è essenziale mantenere questa stretta separazione tra i codici di pagamento degli utenti. Verso questo obiettivo, il passo iniziale di comunicazione del codice è un momento critico per la privacy del pagamento, ma obbligatorio per il corretto funzionamento del protocollo. Se uno dei codici di pagamento può essere ottenuto pubblicamente (come su un sito web), il secondo codice, quello del mittente, non deve essere collegato al primo in nessun caso.
Prendiamo un esempio concreto: voglio fare una donazione a un movimento politico tramite BIP47:
- L'organizzazione ha reso pubblico il suo codice di pagamento sul suo sito web o tramite i suoi social network;
- Questo codice è quindi collegato al movimento politico;
- Recupero questo codice di pagamento;
- Prima di procedere con un invio, devo assicurarmi che conoscano il mio codice di pagamento, che è anche collegato alla mia identità poiché lo uso per ricevere transazioni sui miei social network.
Come trasmettere il mio codice senza rischi? L'uso di mezzi di comunicazione convenzionali potrebbe portare a una fuga di informazioni e, di conseguenza, associarmi a questo movimento politico. La transazione di notifica offre una soluzione grazie a uno strato di crittografia che impedisce precisamente questa associazione tra due codici. Sebbene questo non sia l'unico metodo per trasmettere segretamente il codice di pagamento del mittente, si dimostra molto efficace.
Nel diagramma sottostante, le linee arancioni indicano i punti in cui il flusso di informazioni deve essere interrotto, e le frecce nere mostrano le connessioni che potrebbero potenzialmente essere osservate da terze parti:
![BTC204](assets/it/66/16.webp)
In realtà, all'interno del modello tradizionale di privacy di Bitcoin, è spesso complesso dissociare completamente il flusso di informazioni tra la coppia di chiavi e l'utente, specialmente durante le transazioni a distanza. Ad esempio, nel contesto di una campagna di donazione, il destinatario deve inevitabilmente divulgare un indirizzo o una chiave pubblica tramite il loro sito web o social network. L'uso corretto di BIP47, in particolare con la transazione di notifica, permette di aggirare questo problema grazie a ECDHE e allo strato di crittografia che studieremo ulteriormente.
Ovviamente, il modello classico di privacy di Bitcoin si applica ancora alle chiavi pubbliche effimere, che sono derivate dalla combinazione dei due codici di pagamento. I due modelli sono in realtà complementari. Quello che voglio evidenziare qui è che, contrariamente all'uso abituale di una chiave pubblica per ricevere bitcoin, il codice di pagamento può essere collegato a una specifica identità, perché l'informazione "_Alice effettua una transazione con Bob_" viene interrotta in un'altra fase. Il codice di pagamento viene utilizzato per generare indirizzi di pagamento, ma basandosi unicamente sull'osservazione della blockchain, è impossibile collegare una transazione di pagamento BIP47 ai codici di pagamento utilizzati per eseguirla, a meno che gli UTXO coinvolti non fossero già collegati a un'identità precedentemente e gli utenti non abbiano associato i loro codici di pagamento alle rispettive identità.
Per riassumere, il modello di privacy offerto dai pagamenti BIP47 potrebbe essere considerato superiore a quello della base di Bitcoin, anche se non è magico in alcun modo.
### Costruzione della Transazione di Notifica
Ora, vediamo come funziona questa transazione di notifica. Immaginiamo che Alice voglia inviare fondi a Bob con BIP47. Nel mio esempio, Alice agisce come mittente e Bob come destinatario. Quest'ultimo ha pubblicato il suo codice di pagamento sul suo sito web. Pertanto, Alice è già a conoscenza del codice di pagamento di Bob.
**1- Alice calcola un segreto condiviso con ECDH:**
- Seleziona una coppia di chiavi dal suo portafoglio HD situato su un ramo diverso dal suo codice di pagamento. Nota, questa coppia non dovrebbe essere facilmente associata all'indirizzo di notifica di Alice, né all'identità di Alice (vedi sezione precedente);
- Alice seleziona la chiave privata da questa coppia. La chiamiamo $a$ (minuscolo);
$$

a

$$
```text
- Alice recupera la chiave pubblica associata all'indirizzo di notifica di Bob. Questa chiave è la prima figlia derivata dal codice di pagamento di Bob (indice $/0$). Chiamiamo questa chiave pubblica $B$ (maiuscolo). La chiave privata associata a questa chiave pubblica è chiamata $b$ (minuscolo). $B$ è determinata dall'addizione e dal raddoppio dei punti sulla curva ellittica da $G$ (il punto generatore) con $b$ (la chiave privata):
$$ B = b \cdot G $$
- Alice calcola un punto segreto $S$ (maiuscolo) sulla curva ellittica tramite l'addizione e il raddoppio dei punti applicando la sua chiave privata $a$ dalla chiave pubblica di Bob $B$.
$$ S = a \cdot B $$
- Alice calcola il fattore di oscuramento $f$ che le permetterà di criptare il suo codice di pagamento. Per fare ciò, determinerà un numero pseudo-casuale con la funzione HMAC-SHA512. Nel secondo input di questa funzione, utilizza un valore che solo Bob potrà recuperare: $x$ che è l'ascissa del punto segreto precedentemente calcolato. Il primo input è $o$ che è l'UTXO consumato in input di questa transazione (outpoint).
$$ f = \text{HMAC-SHA512}(o, x) $$
**2- Alice converte il suo codice di pagamento personale in base 2 (binario).**
**3- Utilizza questo fattore di oscuramento come chiave per eseguire la crittografia simmetrica sul payload del suo codice di pagamento.** L'algoritmo di crittografia utilizzato è semplicemente un `XOR`. L'operazione eseguita è paragonabile alla cifratura di Vernam, anche denominata "One-Time Pad".
- Alice prima divide il suo fattore di oscuramento in due: i primi 32 byte sono denominati $f1$ e gli ultimi 32 byte sono denominati $f2$. Quindi, abbiamo:
$$ f = f1 || f2 $$
- Alice calcola l'$x'$ criptato dell'ascissa della chiave pubblica $x$ del suo codice di pagamento, e il $c'$ criptato del suo codice catena $c$ separatamente. $f1$ e $f2$ agiscono rispettivamente come chiavi di crittografia. L'operazione utilizzata è il `XOR` (o esclusivo).
$$ x' = x \oplus f1 $$
$$ c' = c \oplus f2 $$
- Alice sostituisce i valori reali dell'ascissa della chiave pubblica $x$ e del codice catena $c$ nel suo codice di pagamento con i valori criptati $x'$ e $c'$.
**4-** Alice ora ha il suo codice di pagamento con un payload criptato. Costruirà e trasmetterà una transazione che coinvolge la sua chiave pubblica $A$ come input, un output all'indirizzo di notifica di Bob, e un output `OP_RETURN` contenente il suo codice di pagamento con il payload criptato. **Questa transazione è la transazione di notifica**.
Un `OP_RETURN` è un opcode che segna un output di una transazione Bitcoin come non valido. Oggi, è utilizzato per trasmettere o ancorare informazioni sulla blockchain di Bitcoin. Fino a 80 byte di dati possono essere memorizzati, che sono scritti sulla catena e quindi visibili a tutti gli altri utenti.
Come abbiamo visto nelle sezioni precedenti, ECDH è utilizzato per generare un segreto condiviso tra due utenti che comunicano su una rete non sicura, potenzialmente osservata da attaccanti. In BIP47, ECDH è utilizzato per la comunicazione sulla rete Bitcoin, che per sua natura è una rete di comunicazione trasparente osservata da molti attaccanti. Il segreto condiviso calcolato tramite lo scambio di chiavi ECDH è poi utilizzato per criptare le informazioni segrete da trasmettere: il codice di pagamento del mittente (di Alice).
Ricapitoliamo i passaggi che abbiamo appena esaminato insieme per eseguire una transazione di notifica:
- Alice recupera il codice di pagamento e l'indirizzo di notifica di Bob;
- Alice seleziona un UTXO che possiede nel suo portafoglio HD con la corrispondente coppia di chiavi;
- Calcola un punto segreto sulla curva ellittica utilizzando ECDH;
- Utilizza questo punto segreto per calcolare un HMAC, che è il fattore di oscuramento;
- Utilizza questo fattore di oscuramento per criptare il payload del suo codice di pagamento personale.
- Lei utilizza un output di transazione `OP_RETURN` per comunicare il codice di pagamento mascherato a Bob.
![BTC204](assets/it/66/17.webp)
### Transazione di Notifica: Studio Concreto
Per comprendere meglio il suo funzionamento, in particolare l'uso di `OP_RETURN`, esaminiamo insieme una vera transazione di notifica. Ho eseguito tale transazione sulla testnet, che potete trovare [cliccando qui](https://mempool.space/fr/testnet/tx/0e2e4695a3c49272ef631426a9fd2dae6ec3a469e3a39a3db51aa476cd09de2e).
![BTC204](assets/fr/227.webp)
Osservando questa transazione, possiamo vedere che ha un singolo input e 4 output:
- Il primo output è l'`OP_RETURN` che contiene il mio codice di pagamento mascherato;
- Il secondo output di 546 sats punta all'indirizzo di notifica del mio destinatario;
- Il terzo output di 15.000 sats rappresenta le commissioni di servizio, poiché ho utilizzato Samourai Wallet per costruire questa transazione;
- Il quarto output di 2 milioni di sats rappresenta il resto, ovvero la differenza rimanente dal mio input che ritorna a un altro indirizzo che mi appartiene.
Il più interessante da studiare è ovviamente l'output 0 che utilizza l'`OP_RETURN`. Vediamo più da vicino cosa contiene. Ecco lo `scriptPubKey` in esadecimale:
6a4c50010002b13b2911719409d704ecc69f74fa315a6cb20fdd6ee39bc9874667703d67b164927b0e88f89f3f8b963549eab2533b5d7ed481a3bea7e953b546b4e91b6f50d800000000000000000000000000
```

```text
In questo script, possiamo sezionare diverse parti. Prima di tutto, gli opcode:
6a4c
```

```text
Tra gli opcode, possiamo riconoscere `0x6a` che designa l'`OP_RETURN` e `0x4c` che designa l'`OP_PUSHDATA1`.
Il byte seguente questo ultimo opcode indica la dimensione del payload che segue. Indica `0x50`, ovvero 80 byte:
6a4c50
```

```text
Poi, abbiamo i metadati del mio codice di pagamento in chiaro:
010002
```

```text
La coordinata x criptata della chiave pubblica del mio codice di pagamento:
b13b2911719409d704ecc69f74fa315a6cb20fdd6ee39bc9874667703d67b164
```

```text
Il codice catena criptato del mio codice di pagamento:
927b0e88f89f3f8b963549eab2533b5d7ed481a3bea7e953b546b4e91b6f50d8
```

```text
E infine, il padding per raggiungere 80 byte, la dimensione standard di un `OP_RETURN`:
00000000000000000000000000
```

```
Per capire meglio, ecco il mio codice di pagamento in chiaro in base 58:
````text
PM8TJQCyt6ovbozreUCBrfKqmSVmTzJ5vjqse58LnBzKFFZTwny3KfCDdwTqAEYVasn11tTMPc2FJsFygFd3YzsHvwNXLEQNADgxeGnMK8Ugmin62TZU
Quando si confronta il mio codice di pagamento in chiaro con l'`OP_RETURN`, è evidente che l'HRP (`0x47`) e il checksum (`0x8604e4db`) non vengono trasmessi. Questo è previsto, poiché queste informazioni sono destinate agli esseri umani.
Successivamente, possiamo identificare la versione (`0x01`), il campo di bit (`0x00`) e la parità della chiave pubblica (`0x02`). E, alla fine del codice di pagamento, i byte vuoti (`0x00000000000000000000000000`) sono utilizzati per riempire il codice fino a un totale di 80 byte. Tutti questi metadati vengono trasmessi in chiaro (non criptati).
Infine, si può osservare che la coordinata x della chiave pubblica (`0x77507c9c17a89cfca2d3af554745d6c2db0e7f6b2721a3941a504933103cc42a`) e il codice catena (`0xdd94881210d6e752a9abc8a9fa0070e85184993c4f643f1121dd807dd556d1dc`) sono stati criptati. Questo costituisce il payload del codice di pagamento.
### Cos'è XOR?
Nelle sezioni precedenti, abbiamo visto che il codice di pagamento è stato trasmesso criptato utilizzando l'operazione XOR. Prendiamoci un momento per capire come funziona questo operatore, poiché è ampiamente utilizzato nella crittografia.
XOR è un operatore logico bit a bit basato sull'algebra booleana. Con due operandi bit, restituisce `1` se i bit dello stesso rango sono diversi, e restituisce `0` se i bit dello stesso rango sono uguali. Ecco la tabella di verità di XOR basata sui valori degli operandi `D` e `E`:
| D   | E   | D XOR E |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 1       |
| 1   | 0   | 1       |
| 1   | 1   | 0       |
Per esempio:
$$

$$
0110 \oplus 1110 = 1000
Oppure:
$$

$$
010011 \oplus 110110 = 100101
Con ECDH, l'uso di XOR come strato di crittografia è particolarmente adatto. Innanzitutto, a causa di questo operatore, la crittografia è simmetrica. Questo consente al destinatario di decifrare il codice di pagamento con la stessa chiave utilizzata per la crittografia. La chiave di crittografia e decrittografia viene calcolata dal segreto condiviso grazie a ECDH. Questa simmetria è resa possibile dalle proprietà commutativa e associativa dell'operatore XOR:
- Altre proprietà:
$$

$$
D \oplus D = 0
D ⊕ 0 = D
- Commutatività:
$$

$$
D \oplus E = E \oplus D
- Associatività:
$$

$$
D \oplus (E \oplus Z) = (D \oplus E) \oplus Z = D \oplus E \oplus Z
Se:
$$

$$
D \oplus E = L
Allora:
$$

$$
D \oplus L = D \oplus (D \oplus E) = D \oplus D \oplus E = 0 \oplus E = E \\
\therefore D \oplus L = E
Successivamente, questo metodo di cifratura assomiglia molto al cifrario di Vernam (One-Time Pad), l'unico algoritmo di cifratura conosciuto fino ad oggi che possiede sicurezza incondizionata (o assoluta). Affinché il cifrario di Vernam abbia questa caratteristica, la chiave di cifratura deve essere perfettamente casuale, deve essere della stessa dimensione del messaggio e deve essere utilizzata una sola volta. Nel metodo di cifratura utilizzato qui per BIP47, la chiave è effettivamente della stessa dimensione del messaggio, il fattore di offuscamento è esattamente della stessa dimensione della concatenazione della coordinata x della chiave pubblica con il codice catena del codice di pagamento. Questa chiave di cifratura è effettivamente utilizzata una sola volta. Tuttavia, questa chiave non è il risultato di una casualità perfetta poiché è un HMAC. È piuttosto pseudo-casuale. Pertanto, non si tratta di un cifrario di Vernam, ma il metodo è simile.
### Ricezione della Transazione di Notifica
Ora che Alice ha inviato la transazione di notifica a Bob, vediamo come lui la interpreta. Come promemoria, Bob deve essere in grado di accedere al codice di pagamento di Alice. Senza queste informazioni, come vedremo nella sezione seguente, non sarà in grado di derivare le coppie di chiavi create da Alice e, quindi, non sarà in grado di accedere ai suoi bitcoin ricevuti tramite BIP47. Per ora, il payload del codice di pagamento di Alice è criptato. Vediamo come Bob lo decifra.
**1-** Bob monitora le transazioni che creano output con il suo indirizzo di notifica.
**2-** Quando una transazione ha un output sul suo indirizzo di notifica, Bob la analizza per vedere se contiene un output OP_RETURN che segue lo standard BIP47.
**3-** Se il primo byte del payload OP_RETURN è `0x01`, Bob inizia la sua ricerca di un possibile segreto condiviso con ECDH:
- Bob seleziona la chiave pubblica nell'input della transazione. Ovvero, la chiave pubblica di Alice denominata $A$ con:
$$ A = a \cdot G $$
- Bob seleziona la chiave privata $b$ associata al suo indirizzo di notifica personale:
$$ b $$
- Bob calcola il punto segreto $S$ (segreto condiviso ECDH) sulla curva ellittica sommando e raddoppiando i punti, applicando la sua chiave privata $b$ alla chiave pubblica di Alice $A$:
$$ S = b \cdot A $$
- Bob determina il fattore di offuscamento $f$ che gli permetterà di decifrare il payload del codice di pagamento di Alice. Nello stesso modo in cui Alice aveva precedentemente calcolato, Bob troverà $f$ applicando HMAC-SHA512 su $x$ la coordinata x del punto segreto $S$, e su $o$ l'UTXO consumato come input in questa transazione di notifica:
$$ f = \text{HMAC-SHA512}(o, x) $$
**4-** Bob interpreta i dati nell'OP_RETURN della transazione di notifica come un codice di pagamento. Egli semplicemente decifra il payload di questo potenziale codice di pagamento usando il fattore di offuscamento $f$:
- Bob divide il fattore di offuscamento $f$ in 2 parti: i primi 32 byte di $f$ saranno $f1$ e gli ultimi 32 byte saranno $f2$;
- Bob decifra la coordinata x cifrata $x'$ della chiave pubblica dal codice di pagamento di Alice:
$$ x = x' \oplus f1 $$
- Bob decifra il valore del codice catena cifrato $c'$ dal codice di pagamento di Alice:
$$ c = c' \oplus f2 $$
**5-** Bob verifica se il valore della chiave pubblica dal codice di pagamento di Alice è effettivamente parte del gruppo secp256k1. Se è così, lo interpreta come un codice di pagamento valido. Altrimenti, ignora questa transazione.
Ora che Bob è a conoscenza del codice di pagamento di Alice, lei può inviargli fino a `2^32` pagamenti, senza mai dover effettuare un'altra transazione di notifica di questo tipo.
Perché funziona? Come fa Bob a determinare lo stesso fattore di offuscamento di Alice, e quindi a decifrare il suo codice di pagamento? Esaminiamo più da vicino il ruolo di ECDH in quello che abbiamo appena descritto.
Prima di tutto, stiamo trattando con la crittografia simmetrica. Questo significa che la chiave di cifratura e la chiave di decifratura sono lo stesso valore. Questa chiave nella transazione di notifica è il fattore di offuscamento:
$$ f = f1 || f2 $$
Pertanto, Alice e Bob devono ottenere lo stesso valore per $f$, senza trasmetterlo direttamente poiché un attaccante potrebbe rubarlo e decifrare le informazioni segrete. Questo fattore di offuscamento si ottiene applicando HMAC-SHA512 su 2 valori:
- la coordinata x di un punto segreto;
- e l'UTXO consumato come input nella transazione.
Bob, quindi, ha bisogno di queste due informazioni per decifrare il payload del codice di pagamento di Alice. Per l'UTXO come input, Bob può semplicemente recuperarlo osservando la transazione di notifica. Per il punto segreto, Bob dovrà usare ECDH. Come visto nella sezione precedente su Diffie-Hellman, semplicemente scambiando le rispettive chiavi pubbliche e applicando segretamente le proprie chiavi private alla chiave pubblica dell'altro, Alice e Bob possono trovare un punto specifico e segreto sulla curva ellittica. La transazione di notifica si basa su questo meccanismo:
- Coppia di chiavi di Bob:
$$ B = b \cdot G $$
- Coppia di chiavi di Alice:
$$ A = a \cdot G $$
- Per un segreto $S (x, y)$:
$$ S = a \cdot B = a \cdot (b \cdot G) = (b \cdot a) \cdot G = b \cdot A $$
Ora che Bob conosce il codice di pagamento di Alice, sarà in grado di rilevare i suoi pagamenti BIP47, e può derivare le chiavi private che bloccano i bitcoin ricevuti.
Ricapitoliamo i passaggi che abbiamo appena esaminato per ricevere e interpretare una transazione di notifica:
- Bob monitora gli output delle transazioni al suo indirizzo di notifica;
- Quando ne rileva uno, recupera le informazioni contenute nell'OP_RETURN;
- Bob seleziona la chiave pubblica in input e calcola un punto segreto usando ECDH;
- Usa questo punto segreto per calcolare un HMAC che è il fattore di offuscamento;
- Usa questo fattore di offuscamento per decifrare il payload del codice di pagamento di Alice contenuto nell'OP_RETURN.
### La Transazione di Pagamento BIP47
Studiamo ora insieme il processo di pagamento con BIP47. Per ricordarvi lo stato attuale delle cose:
- Alice conosce il codice di pagamento di Bob, che ha semplicemente recuperato dal suo sito web;
- Bob conosce il codice di pagamento di Alice grazie alla transazione di notifica;
- Alice effettuerà un primo pagamento a Bob. Potrà effettuarne molti altri allo stesso modo.
Prima di spiegare questo processo, penso sia importante ricordare gli indici su cui stiamo attualmente lavorando. Il percorso di derivazione di un codice di pagamento è descritto come segue: `m/47'/0'/0'`. La profondità successiva distribuisce gli indici in questo modo:
- La prima coppia di chiavi figlio normali (non rinforzate) è quella utilizzata per generare l'indirizzo di notifica di cui abbiamo parlato nella parte precedente: `m/47'/0'/0'/0`;
- Le coppie di chiavi figlio normali sono utilizzate all'interno di ECDH per generare indirizzi di ricezione dei pagamenti BIP47 come vedremo in questa sezione: da `m/47'/0'/0'/0` a `m/47'/0'/0'/2 147 483 647`;
- Le coppie di chiavi figlio rinforzate sono codici di pagamento effimeri: da `m/47'/0'/0'/0'` a `m/47'/0'/0'/2 147 483 647'`.
Ogni volta che Alice desidera inviare un pagamento a Bob, deriva un nuovo indirizzo vergine unico, grazie ancora al protocollo ECDH:
- Alice seleziona la prima chiave privata derivata dal suo codice di pagamento personale riutilizzabile:
$$ a $$
- Alice seleziona la prima chiave pubblica inutilizzata derivata dal codice di pagamento di Bob. Questa chiave pubblica, la chiameremo $B$. È associata alla chiave privata $b$ che solo Bob conosce:
$$ B = b \cdot G $$
- Alice calcola un punto segreto $S$ sulla curva ellittica tramite addizione e raddoppio di punti applicando la sua chiave privata $a$ alla chiave pubblica $B$ di Bob:
$$ S = a \cdot B $$
- Da questo punto segreto, Alice calcolerà il segreto condiviso $s$ (minuscolo). Per fare ciò, seleziona la coordinata x del punto segreto $S$ denominata $Sx$, e passa questo valore attraverso la funzione hash SHA256:
$$ S = (Sx, Sy) $$
$$ s = \text{SHA256}(Sx) $$
- Alice utilizza questo segreto condiviso $s$ per calcolare un indirizzo Bitcoin di ricezione dei pagamenti. Inizialmente, verifica che $s$ sia contenuto nell'ordine della curva secp256k1. In caso contrario, incrementa l'indice della chiave pubblica di Bob per derivare un altro segreto condiviso;
- In secondo luogo, calcola una chiave pubblica $K0$ aggiungendo sulla curva ellittica i punti $B$ e $s·G$. In altre parole, Alice aggiunge la chiave pubblica derivata dal codice di pagamento di Bob $B$ con un altro punto calcolato sulla curva ellittica tramite addizione e raddoppio con il segreto condiviso $s$ dal punto generatore della curva secp256k1 $G$. Questo nuovo punto rappresenta una chiave pubblica, e lo chiamiamo $K0$:
$$ K0 = B + s \cdot G $$
- Con questa chiave pubblica $K0$, Alice può derivare un indirizzo vergine standard di ricezione (per esempio, SegWit V0 in bech32).
Una volta che Alice ha ottenuto l'indirizzo di ricezione di Bob $K0$, può eseguire una transazione Bitcoin in modo standard. Per fare ciò, seleziona un UTXO di sua proprietà, assicurato da una coppia di chiavi di un ramo diverso del suo portafoglio HD, e lo spende per soddisfare un output all'indirizzo di Bob $K0$. È importante notare che questo pagamento, una volta derivato l'indirizzo, segue un processo convenzionale e non dipende più dalle chiavi associate a BIP47.
Ricapitoliamo i passaggi che abbiamo appena eseguito insieme per inviare un pagamento BIP47:
- Alice seleziona la prima chiave privata derivata dal suo codice di pagamento personale;
- Calcola un punto segreto sulla curva ellittica utilizzando ECDH dalla prima chiave pubblica derivata non utilizzata dal codice di pagamento di Bob;
- Utilizza questo punto segreto per calcolare un segreto condiviso con SHA256;
- Utilizza questo segreto condiviso per calcolare un nuovo punto segreto sulla curva ellittica;
- Aggiunge questo nuovo punto segreto alla chiave pubblica di Bob;
- Ottiene una nuova chiave pubblica effimera per la quale solo Bob ha la chiave privata associata;
- Alice può effettuare una transazione standard a Bob con l'indirizzo di ricezione effimero derivato.
![BTC204](assets/it/66/21.webp)
Se Alice desidera effettuare un secondo pagamento, seguirà gli stessi passaggi di prima, eccetto che questa volta selezionerà la seconda chiave pubblica derivata dal codice di pagamento di Bob. Specificamente, utilizzerà la prossima chiave non utilizzata. Otterrà così un nuovo indirizzo di ricezione appartenente a Bob, designato $K1$:
![BTC204](assets/it/66/22.webp)
Può continuare in questo modo e derivare fino a `2^32` indirizzi non utilizzati appartenenti a Bob.
Da un punto di vista esterno, osservando la blockchain, è teoricamente impossibile differenziare un pagamento BIP47 da un pagamento standard. Ecco un esempio di transazione di pagamento BIP47 sul Testnet:
```

94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254
````
Questo sembra una transazione standard con un input consumato, un output di pagamento e un resto:
![BTC204](assets/fr/232.webp)
### Ricevere il Pagamento BIP47 e Derivare la Chiave Privata
Alice ha appena effettuato il suo primo pagamento a un nuovo indirizzo BIP47 appartenente a Bob. Ora vediamo come Bob riceve questo pagamento. Vedremo anche perché Alice non ha accesso alla chiave privata dell'indirizzo che ha appena generato da sola, e come Bob recupera questa chiave per spendere i bitcoin che ha appena ricevuto.
Non appena Bob riceve la transazione di notifica da Alice, deriva la chiave pubblica BIP47 $K0$ anche prima che lei abbia inviato qualsiasi pagamento. Poi monitora qualsiasi pagamento all'indirizzo associato. Infatti, deriva immediatamente diversi indirizzi che monitorerà ($K0$, $K1$, $K2$, $K3$...). Ecco come deriva questa chiave pubblica $K0$:
- Bob seleziona la prima chiave privata derivata dal suo codice di pagamento. Questa chiave privata è denominata $b$. È associata alla chiave pubblica $B$ con cui Alice aveva fatto i suoi calcoli nel passaggio precedente:
$$ b $$
- Bob seleziona la prima chiave pubblica di Alice derivata dal suo codice di pagamento. Questa chiave è denominata $A$. È associata alla chiave privata $a$ con cui Alice aveva fatto i suoi calcoli, e di cui solo Alice è a conoscenza. Bob può eseguire questo processo poiché è a conoscenza del codice di pagamento di Alice che le è stato trasmesso con la transazione di notifica:
$$ A = a \cdot G $$
- Bob calcola il punto segreto $S$, mediante addizione e raddoppio di punti sulla curva ellittica, applicando la sua chiave privata $b$ alla chiave pubblica di Alice $A$. Qui troviamo l'uso di ECDH che garantisce che questo punto $S$ sarà lo stesso sia per Bob che per Alice:
$$ S = b \cdot A $$
- Proprio come ha fatto Alice, Bob isola la coordinata x di questo punto $S$. Abbiamo chiamato questo valore $Sx$. Egli passa questo valore attraverso la funzione SHA256 per trovare il segreto condiviso $s$ (minuscolo):
$$ s = \text{SHA256}(Sx) $$
- Proprio come Alice, Bob calcola il punto $s·G$ sulla curva ellittica. Poi, aggiunge questo punto segreto alla sua chiave pubblica $B$. Ottiene così un nuovo punto sulla curva ellittica che interpreta come una chiave pubblica $K0$:
$$ K0 = B + s \cdot G $$
Una volta che Bob ha questa chiave pubblica $K0$, può derivare la chiave privata associata per essere in grado di spendere i suoi bitcoin. È l'unico che può generare questa chiave privata:
- Bob aggiunge la sua chiave privata figlio $b$ derivata dal suo codice di pagamento personale. È l'unico che può ottenere il valore di $b$. Poi, aggiunge $b$ con il segreto condiviso $s$ per ottenere $k0$, la chiave privata di $K0$:
$$ k0 = b + s $$
Grazie alla legge di gruppo della curva ellittica, Bob ottiene esattamente la chiave privata corrispondente alla chiave pubblica usata da Alice. Abbiamo quindi:
$$ K0 = k0 \cdot G $$
Riassumerò i passaggi che abbiamo appena esaminato insieme per ricevere un pagamento BIP47 e calcolare la chiave privata corrispondente:
- Bob seleziona la prima chiave privata figlio derivata dal suo codice di pagamento personale;
- Calcola un punto segreto sulla curva ellittica usando ECDH dalla prima chiave pubblica figlio derivata dal codice catena di Alice;
- Usa questo punto segreto per calcolare un segreto condiviso con SHA256;
- Usa questo segreto condiviso per calcolare un nuovo punto segreto sulla curva ellittica;
- Aggiunge questo nuovo punto segreto alla sua chiave pubblica personale;
- Ottiene una nuova chiave pubblica effimera, alla quale Alice invierà il suo primo pagamento;
- Bob calcola la chiave privata associata a questa chiave pubblica effimera aggiungendo la sua chiave privata figlio derivata dal suo codice di pagamento e il segreto condiviso.
![BTC204](assets/it/66/24.webp)
Poiché Alice non può ottenere $b$ (la chiave privata di Bob), lei non è in grado di determinare $k0$ (la chiave privata associata all'indirizzo di ricezione BIP47 di Bob). Schematicamente, possiamo rappresentare il calcolo del segreto condiviso $S$ così:
![BTC204](assets/it/66/19.webp)
Una volta trovato il segreto condiviso con ECDH, Alice e Bob calcolano la chiave pubblica di pagamento BIP47 $K0$, e Bob calcola anche la chiave privata associata $k0$:
![BTC204](assets/it/66/25.webp)
### Rimborsare il Pagamento BIP47
Poiché Bob è a conoscenza del codice di pagamento riutilizzabile di Alice, ha già tutte le informazioni necessarie per inviarle un rimborso. Non avrà bisogno di contattare nuovamente Alice per chiedere informazioni. Dovrà semplicemente notificarla con una transazione di notifica, specialmente affinché lei possa recuperare i suoi indirizzi BIP47 con il suo seed, e poi potrà anche inviarle fino a `2^32` pagamenti.
La funzionalità di rimborso è specifica per BIP47 ed è uno dei suoi vantaggi rispetto ad altri metodi che studieremo nei prossimi capitoli, come i Pagamenti Silenziosi.
Bob può quindi rimborsare Alice nello stesso modo in cui lei gli ha inviato i pagamenti. I ruoli si invertono:
![BTC204](assets/it/66/26.webp)
_Un grande ringraziamento a [Fanis Michalakis](https://x.com/FanisMichalakis) per la sua revisione e preziosi consigli esperti sull'articolo che ha ispirato la scrittura di questo capitolo!_
https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093
## Pagamenti Silenziosi
<chapterId>2871d594-414e-4598-a830-91c9eb84dfb8</chapterId>
Il BIP47 è stato criticato per la sua inefficienza sulla blockchain. Come spiegato nel capitolo precedente, richiede una transazione di notifica per ogni nuovo destinatario. Questo vincolo diventa trascurabile se si prevede di stabilire un canale di pagamento duraturo con questo destinatario. Infatti, una singola transazione di notifica apre la strada a un numero quasi infinito di pagamenti BIP47 successivi.
Tuttavia, in determinate situazioni, la transazione di notifica può rappresentare un ostacolo per l'utente. Prendiamo l'esempio di una donazione una tantum a un destinatario: con un indirizzo Bitcoin classico, una singola transazione è sufficiente per effettuare la donazione. Ma con il BIP47, sono necessarie due transazioni: una per la notifica e un'altra per il pagamento effettivo. Quando la domanda di spazio nel blocco è bassa e le commissioni di transazione sono minime, questo passaggio aggiuntivo generalmente non rappresenta un problema. Tuttavia, durante i periodi di congestione, le commissioni di transazione possono diventare esorbitanti per un singolo pagamento, potenzialmente raddoppiando il costo per l'utente rispetto a una transazione Bitcoin standard, il che può essere inaccettabile per l'utente.
Per situazioni in cui l'utente prevede di effettuare solo pochi pagamenti a un identificatore statico, sono state sviluppate altre soluzioni. Tra queste ci sono i Pagamenti Silenziosi, descritti nel [BIP352](https://github.com/bitcoin/bips/blob/master/bip-0352.mediawiki). Questo protocollo consente l'uso di un identificatore statico per ricevere pagamenti senza generare riutilizzo dell'indirizzo e senza richiedere l'uso di transazioni di notifica. Esaminiamo come funziona questo protocollo.
---
_Per comprendere appieno questo capitolo, è essenziale essere familiari con il funzionamento di ECDH (Elliptic Curve Diffie-Hellman) e la derivazione delle chiavi crittografiche in un portafoglio HD. Questi concetti sono stati dettagliati nel capitolo precedente sul BIP47. Non li ripeterò qui. Se non sei ancora familiare con queste nozioni, ti consiglio di consultare il capitolo precedente prima di continuare con questo. Non riprenderò nemmeno i rischi associati al riutilizzo degli indirizzi di ricezione, né l'importanza di avere un identificatore unico per ricevere pagamenti._
---
### Perché non spostare la notifica?
Come discusso nel capitolo sul BIP47, la transazione di notifica svolge principalmente due funzioni:
- Notifica il destinatario;
- Trasmette il codice di pagamento del mittente.
Si potrebbe ingenuamente pensare che questo processo di notifica potrebbe essere effettuato off-chain. In teoria, ciò è completamente fattibile: sarebbe sufficiente per il destinatario indicare un mezzo di comunicazione per ricevere i codici di pagamento BIP47 dai mittenti. Tuttavia, questo approccio presenta due problemi principali:
- Primo, ciò sposterebbe il processo di trasmissione del codice su un altro protocollo di comunicazione. Le questioni relative ai costi e alla privacy dello scambio rimarrebbero, ma sarebbero semplicemente trasferite a questo nuovo protocollo. In termini di privacy, ciò potrebbe anche creare un collegamento tra l'identità di un utente e l'attività sulla blockchain, cosa che cerchiamo di evitare eseguendo la notifica direttamente sulla blockchain. Inoltre, effettuare la notifica fuori dalla blockchain introdurrebbe rischi di censura (come il blocco dei fondi) che non esistono su Bitcoin;
Successivamente, ciò porrebbe un problema di recupero. Con BIP47, il destinatario deve assolutamente conoscere i codici di pagamento dei mittenti per accedere ai fondi. Questo è vero al momento della ricezione, ma anche in caso di recupero dei fondi tramite il seed in caso di perdita del portafoglio. Con le notifiche onchain, questo rischio viene evitato, poiché l'utente può trovare e decifrare le transazioni di notifica semplicemente conoscendo il proprio seed. Tuttavia, se la notifica viene eseguita fuori dalla blockchain, l'utente dovrebbe mantenere un backup dinamico di tutti i codici di pagamento ricevuti, il che è impraticabile per l'utente medio.
Tutti questi vincoli rendono l'uso della notifica onchain indispensabile nel contesto di BIP47. Eppure, i Pagamenti Silenziosi cercano specificamente di evitare questo passaggio di notifica onchain a causa del suo costo. Pertanto, la soluzione adottata non è spostare la notifica, ma eliminarla completamente. Per raggiungere questo obiettivo, deve essere accettato un compromesso: quello della scansione. A differenza di BIP47, dove l'utente sa esattamente dove trovare i propri fondi grazie alle transazioni di notifica, nel contesto dei Pagamenti Silenziosi, l'utente deve esaminare tutte le transazioni Bitcoin esistenti per rilevare eventuali pagamenti che potrebbero essere destinati a loro. Per ridurre questo onere operativo, la ricerca di Pagamenti Silenziosi è limitata solo alle transazioni che probabilmente contengono tali pagamenti, ovvero quelle che includono almeno un output Taproot P2TR. La scansione si concentra esclusivamente anche sulle transazioni dalla data di creazione del portafoglio (non c'è bisogno di scandire transazioni risalenti al 2009 se il portafoglio è stato creato nel 2024).
Pertanto, potete vedere perché BIP47 e Pagamenti Silenziosi, sebbene mirino a un obiettivo simile, comportano compromessi diversi e **quindi si rivolgono effettivamente a casi d'uso distinti**. Per i pagamenti una tantum, come le donazioni occasionali, i Pagamenti Silenziosi sono più appropriati a causa del loro costo inferiore. Al contrario, per le transazioni regolari allo stesso destinatario, come nel caso delle piattaforme di scambio o dei pool di mining, BIP47 potrebbe essere preferito.
Esploriamo insieme il funzionamento tecnico dei Pagamenti Silenziosi per capirne meglio le implicazioni. Per fare ciò, suggerisco di adottare lo stesso approccio del documento esplicativo di BIP352. Scomporremo gradualmente i calcoli da eseguire, elemento per elemento, giustificando ogni nuova aggiunta.
### Alcuni concetti da comprendere
Prima di iniziare, è importante chiarire che i Pagamenti Silenziosi si basano esclusivamente sull'uso di tipi di script P2TR (_Pay to Taproot_). A differenza di BIP47, non è necessario derivare gli indirizzi di ricezione dalle chiavi pubbliche figlie tramite hashing. Infatti, nello standard P2TR, la chiave pubblica modificata viene utilizzata direttamente e apertamente nell'indirizzo. Così, un indirizzo di ricezione Taproot è essenzialmente una chiave pubblica accompagnata da alcuni metadati. Questa chiave pubblica modificata è l'aggregazione di altre due chiavi pubbliche: una che consente la spesa diretta e tradizionale tramite una semplice firma, e l'altra che rappresenta la radice di Merkle del MAST, che autorizza la spesa soggetta alla soddisfazione di una delle condizioni potenzialmente iscritte nell'albero di Merkle.
![BTC204](assets/it/67/01.webp)
La decisione di limitare i Pagamenti Silenziosi esclusivamente a Taproot è motivata da due ragioni principali:
- Primo, facilita significativamente l'implementazione e gli aggiornamenti futuri nel software del portafoglio, poiché è necessario aderire a un solo standard;
- In secondo luogo, questo approccio aiuta a migliorare l'insieme di anonimato degli utenti incoraggiandoli a non disperdersi tra diversi tipi di script, che generano impronte di portafoglio distinte nell'analisi della catena (per maggiori informazioni su questo concetto, vi invito a consultare il capitolo 4 della parte 2).
### Derivazione naive di una chiave pubblica di Pagamenti Silenziosi
Iniziamo con un semplice esempio che ti aiuterà a comprendere il funzionamento di base dei Pagamenti Silenziosi (SP, Silent Payments). Prendiamo Alice e Bob, due utenti Bitcoin. Alice vuole inviare bitcoin a Bob su un nuovo indirizzo di ricezione. Tre obiettivi devono essere raggiunti in questo processo:
- Alice deve essere in grado di generare un nuovo indirizzo;
- Bob deve essere in grado di identificare un pagamento inviato a questo specifico indirizzo;
- Bob deve essere in grado di ottenere la chiave privata associata a questo indirizzo per poter spendere i suoi fondi.
Alice ha un UTXO nel suo portafoglio Bitcoin protetto con la seguente coppia di chiavi:
- $a$: la chiave privata;
- $A$: la chiave pubblica ($A = a \cdot G$)
Bob ha un indirizzo SP che ha pubblicato su internet con:
- $b$: la chiave privata;
- $B$: la chiave pubblica ($B = b \cdot G$)
Recuperando l'indirizzo di Bob, Alice è in grado di calcolare un nuovo indirizzo vuoto che appartiene a Bob usando ECDH. Chiamiamo questo indirizzo $P$:
$$ P = B + \text{hash}(a \cdot B) \cdot G $$
In questa equazione, Alice ha semplicemente calcolato il prodotto scalare della sua chiave privata $a$ e della chiave pubblica di Bob $B$. Ha passato questo risultato attraverso una funzione hash conosciuta da tutti. Il valore di output è poi moltiplicato scalarmente per il punto generatore $G$ della curva ellittica `secp256k1`. Infine, Alice aggiunge il punto ottenuto alla chiave pubblica di Bob $B$. Una volta che Alice ha questo indirizzo $P$, lo usa come output in una transazione, il che significa che invia bitcoin ad esso.
> _Nel contesto dei Pagamenti Silenziosi, la funzione "hash" corrisponde a una funzione hash SHA256 etichettata specificamente con `BIP0352/SharedSecret`, assicurando che gli hash generati siano unici per questo protocollo e non possano essere riutilizzati in altri contesti, fornendo anche una protezione aggiuntiva contro il riutilizzo di nonce nelle firme. Questo standard corrisponde a quello [specificato nel BIP340 per le firme Schnorr](https://github.com/bitcoin/bips/blob/master/bip-0340.mediawiki) su `secp256k1`._
Grazie alle proprietà della curva ellittica su cui si basa ECDH, sappiamo che:
$$ a \cdot B = b \cdot A $$
Bob sarà quindi in grado di calcolare l'indirizzo di ricezione su cui Alice ha inviato i bitcoin. Per fare ciò, monitora tutte le transazioni Bitcoin che soddisfano i criteri dei Pagamenti Silenziosi e applica il seguente calcolo a ciascuna di esse per vedere se il pagamento è indirizzato a lui (_scanning_):
$$ P' = B + \text{hash}(b \cdot A) \cdot G $$
Quando esamina la transazione di Alice, si rende conto che $P'$ è uguale a $P$. Sa quindi che questo pagamento è indirizzato a lui:
$$ P' = B + \text{hash}(b \cdot A) \cdot G = B + \text{hash}(a \cdot B) \cdot G = P $$
Da qui, Bob sarà in grado di calcolare la chiave privata $p$ che consente di spendere l'indirizzo $P$:
$$ p = (b + \text{hash}(b \cdot A)) \bmod n $$
Come puoi vedere, per calcolare questa chiave privata $p$, è necessario avere la chiave privata $b$. Solo Bob ha questa chiave privata $b$. Sarà quindi effettivamente l'unico in grado di spendere i bitcoin inviati al suo indirizzo di Pagamenti Silenziosi.
![BTC204](assets/fr/236.webp)
_Didascalia:_
- $B$: La chiave pubblica / indirizzo statico pubblicato da Bob
- $b$: La chiave privata di Bob
- $A$: La chiave pubblica dell'UTXO di Alice usata come input per la transazione
- $a$: La chiave privata di Alice
- $G$: Il punto generatore della curva ellittica `secp256k1`
- $\text{SHA256}$: La funzione di hashing SHA256 etichettata con `BIP0352/SharedSecret`
- $s$: Il segreto comune ECDH
- $P$: La chiave pubblica / indirizzo unico per il pagamento a Bob
Ecco un approccio inizialmente piuttosto ingenuo nell'uso dell'indirizzo statico di Bob, denotato $B$, per derivare un indirizzo unico $P$ per inviare bitcoin. Tuttavia, questo metodo è troppo semplicistico e presenta diversi difetti che necessitano di correzione. Il primo problema è che, in questo schema, Alice non può creare molteplici output per Bob all'interno della stessa transazione.
### Come creare molteplici output?
Nell'esempio della sezione precedente, Alice crea un singolo output che andrà a Bob al suo indirizzo unico $P$. Con lo stesso input selezionato, è impossibile per Alice creare due indirizzi vergini distinti per Bob, poiché il metodo utilizzato porterebbe sempre allo stesso risultato per $P$, quindi allo stesso indirizzo. Tuttavia, ci possono essere molte situazioni in cui Alice desidera dividere il suo pagamento a Bob in diverse piccole somme, creando così molteplici UTXO. È quindi necessario trovare un metodo che permetta di farlo.
Per raggiungere questo obiettivo, modificheremo leggermente il calcolo che Alice esegue per derivare $P$, in modo che possa generare due indirizzi distinti per Bob, ovvero $P_0$ e $P_1$.
Per modificare il calcolo e ottenere 2 indirizzi diversi, è sufficiente aggiungere un intero che modifica il risultato. Così, Alice aggiungerà $0$ nel suo calcolo per ottenere l'indirizzo $P_0$ e $1$ per ottenere l'indirizzo $P_1$. Chiamiamo questo intero $i$:
$$ P_i = B + \text{hash}(a \cdot B \text{ ‖ } i) \cdot G $$
Il processo di calcolo rimane invariato rispetto al metodo precedente, eccetto che questa volta Alice concatenerà $a \cdot B$ con $i$ prima di procedere al hash. È quindi sufficiente cambiare $i$ per avere un nuovo indirizzo appartenente a Bob. Ad esempio:
$$ P_0 = B + \text{hash}(a \cdot B \text{ ‖ } 0) \cdot G $$
$$ P_1 = B + \text{hash}(a \cdot B \text{ ‖ } 1) \cdot G $$
Quando Bob esamina la blockchain per i Pagamenti Silenziosi destinati a lui, inizia utilizzando $i = 0$ per l'indirizzo $P_0$. Se non trova nessun pagamento su $P_0$, conclude che questa transazione non contiene nessun Pagamento Silenzioso per lui e smette di analizzarla. Tuttavia, se $P_0$ è valido e contiene un pagamento per lui, procede con $P_1$ nella stessa transazione per verificare se Alice ha effettuato un secondo pagamento. Se $P_1$ risulta essere invalido, interrompe la sua ricerca per questa transazione; altrimenti, continua a testare valori successivi di $i$.
$$ P_1 = B + \text{hash}(b \cdot A \text{ ‖ } 1) \cdot G $$
Poiché Bob si ferma immediatamente a $i = 0$ se $P_0$ non produce risultati, l'uso di questo intero aggiunge quasi nessun onere operativo aggiuntivo a Bob per la fase di scansione delle transazioni.
Bob può quindi calcolare le chiavi private nello stesso modo:
$$

p_0 = (b + \text{hash}(b \cdot A \text{ ‖ } 0)) \bmod n

$$
p_1 = (b + \text{hash}(b \cdot A \text{ ‖ } 1)) \bmod n

$$
_Didascalia:_
- $B$: La chiave pubblica / indirizzo statico pubblicato da Bob
- $b$: La chiave privata di Bob
- $A$: La chiave pubblica dell'UTXO di Alice usata come input per la transazione
- $a$: La chiave privata di Alice
- $G$: Il punto generatore della curva ellittica `secp256k1`
- $\text{SHA256}$: La funzione di hash SHA256 etichettata con `BIP0352/SharedSecret`
- $s_0$: Il primo segreto condiviso ECDH
- $s_1$: Il secondo segreto condiviso ECDH
- $P_0$: La prima chiave pubblica / indirizzo unico per il pagamento a Bob
- $P_1$: La seconda chiave pubblica / indirizzo unico per il pagamento a Bob
Con questo metodo, iniziamo ad avere un bel protocollo, ma ci sono ancora alcune sfide da superare, in particolare la prevenzione del riutilizzo degli indirizzi.
### Come evitare il riutilizzo degli indirizzi?
Come abbiamo visto nelle sezioni precedenti, Alice utilizza la coppia di chiavi che proteggono il suo UTXO, che spenderà per calcolare il segreto condiviso ECDH con Bob. Questo segreto le permette di derivare l'indirizzo unico $P_0$. Tuttavia, la coppia di chiavi ($a$, $A$) usata da Alice può proteggere più UTXO se ha riutilizzato questo indirizzo diverse volte. Nel caso in cui Alice effettui due pagamenti all'indirizzo statico $B$ di Bob utilizzando due UTXO protetti dalla stessa chiave $A$, ciò comporterebbe un riutilizzo dell'indirizzo per Bob.
> _Il riutilizzo degli indirizzi è una pratica molto negativa per la privacy degli utenti. Per capire perché, vi consiglio di rivedere le prime parti di questa formazione._
Infatti, poiché l'indirizzo unico $P_0$ è derivato da $A$ e $B$, se Alice deriva un secondo indirizzo per un secondo pagamento a $B$, con la stessa chiave $A$, finirà per ottenere lo stesso indirizzo $P_0$. Per evitare questo rischio e prevenire il riutilizzo degli indirizzi all'interno dei Pagamenti Silenziosi, dobbiamo modificare leggermente i nostri calcoli.
Quello che vogliamo è che ogni UTXO consumato da Alice come input di un pagamento dia un indirizzo unico dal lato di Bob, anche se più UTXO sono protetti dalla stessa coppia di chiavi. È quindi sufficiente aggiungere un riferimento all'UTXO nel calcolo dell'indirizzo unico $P_0$. Questo riferimento sarà semplicemente l'hash dell'UTXO consumato come input:
$$ \text{inputHash} = \text{hash}(\text{outpoint} \text{ ‖ } A) $$
E questo riferimento di input, Alice lo aggiungerà nel suo calcolo dell'indirizzo unico $P_0$:
Durante la sua scansione, Bob può anche aggiungere $\text{inputHash}$, poiché tutto ciò che deve fare è osservare la transazione per dedurre $\text{outpoint}$:
$$ P_0 = B + \text{hash}(\text{inputHash} \cdot b \cdot A \text{ ‖ } 0) \cdot G $$
Quando trova un valido $P_0$, può calcolare la corrispondente chiave privata $p_0$:
$$

p_0 = (b + \text{hash}(\text{inputHash} \cdot b \cdot A \text{ ‖ } 0)) \bmod n

$$
```text
_Legenda:_
- $B$: La chiave pubblica / indirizzo statico pubblicato da Bob
- $b$: La chiave privata di Bob
- $A$: La chiave pubblica dell'UTXO di Alice usata come input per la transazione
- $a$: La chiave privata di Alice
- $H$: L'hash dell'UTXO usato come input
- $G$: Il punto generatore della curva ellittica `secp256k1`
- $\text{SHA256}$: La funzione di hash SHA256 etichettata con `BIP0352/SharedSecret`
- $s_0$: Il primo segreto condiviso ECDH
- $P_0$: La prima chiave pubblica / indirizzo unico per il pagamento a Bob
Al momento, i nostri calcoli presuppongono che Alice utilizzi un singolo input per la sua transazione. Tuttavia, dovrebbe essere in grado di utilizzare più input. Di conseguenza, da parte di Bob, per ogni transazione contenente più input, teoricamente avrebbe bisogno di calcolare l'ECDH per ogni input per determinare se un pagamento è destinato a lui. Questo metodo non è soddisfacente, quindi abbiamo bisogno di trovare una soluzione per ridurre il carico di lavoro!
### Modificare le chiavi pubbliche negli input
Per risolvere questo problema, invece di utilizzare la coppia di chiavi che protegge un input specifico da parte di Alice, useremo la somma di tutte le coppie di chiavi utilizzate negli input della transazione. Questa somma sarà quindi considerata come una nuova coppia di chiavi. Questa tecnica è nota come "tweak".
Per esempio, immagina che la transazione di Alice abbia 3 input, ognuno protetto con una coppia di chiavi diversa:
- $a_0$ protegge l'input #0;
- $a_1$ protegge l'input #1;
- $a_2$ protegge l'input #2.
Seguendo il metodo descritto sopra, Alice dovrebbe scegliere una singola coppia di chiavi tra $a_0$, $a_1$ e $a_2$ per calcolare il segreto ECDH e generare l'indirizzo di pagamento unico $P$ dall'indirizzo statico $B$ di Bob. Tuttavia, questo approccio richiede a Bob di testare ogni possibilità sequenzialmente, partendo da $a_0$, poi $a_1$, e così via, fino all'identificazione di una coppia che genera un indirizzo valido $P$. Questo processo richiede che Bob esegua il calcolo ECDH su tutti gli input di tutte le transazioni, aumentando significativamente il carico di lavoro operativo di scansione.
Per evitare ciò, chiederemo ad Alice di eseguire il suo calcolo di $P$ utilizzando la somma di tutte le chiavi in input. Prendendo il nostro esempio, la chiave privata modificata $a$ sarebbe calcolata come segue:
$$ a = a_0 + a_1 + a_2 $$
Allo stesso modo, Alice e Bob saranno in grado di calcolare la chiave pubblica modificata:
$$ A = A_0 + A_1 + A_2 $$
Grazie a questo metodo, a Bob basta calcolare la somma delle chiavi pubbliche della transazione, poi calcolare il segreto ECDH da $A$ soltanto, il che riduce notevolmente il numero di calcoli da fare per la fase di scansione. Tuttavia, ricorda dalla sezione precedente. Avevamo incluso nel nostro calcolo l'hash $\text{inputHash}$ che viene usato come nonce per prevenire il riutilizzo degli indirizzi:
$$ \text{inputHash} = \text{hash}(\text{outpoint} \text{ ‖ } A) $$
Ma se ci sono più input in una transazione, è necessario determinare quale $\text{outpoint}$ viene scelto in questo calcolo. Secondo il BIP352, il criterio di selezione per $\text{outpoint}$ da usare è scegliere il più piccolo lessicograficamente, il che significa selezionare l'UTXO che appare per primo in ordine alfabetico. Questo metodo standardizza l'UTXO da scegliere in ogni transazione. Ad esempio, se questo $\text{outpoint}$ più piccolo lessicograficamente è $\text{outpoint}_L$, il calcolo di $\text{inputHash}$ sarà:
$$ \text{inputHash} = \text{hash}(\text{outpoint}\_L \text{ ‖ } A) $$
I calcoli rimangono quindi identici a quelli presentati nella sezione precedente, eccetto che la chiave privata $a$ e la sua corrispondente chiave pubblica $A$ non rappresentano più una coppia che protegge un singolo input, ma ora rappresentano la modifica di tutte le coppie di chiavi negli input.
### Separare le Chiavi di Spesa e di Scansione
Finora, abbiamo discusso dell'indirizzo statico di Pagamento Silenzioso $B$ come di una chiave pubblica unica. Ricorda, è questa chiave pubblica $B$ che viene usata da Alice per creare il segreto condiviso ECDH, che a sua volta viene usato per calcolare l'indirizzo di pagamento unico $P$. Bob usa questa chiave pubblica $B$ e la corrispondente chiave privata $b$ per la fase di scansione. Ma userà anche la chiave privata $b$ per calcolare la chiave privata $p$ che consente di spendere dall'indirizzo $P$.
Lo svantaggio di questo metodo è che la chiave privata $b$, che viene usata per calcolare tutte le chiavi private per gli indirizzi che ricevono Pagamenti Silenziosi, viene anche usata da Bob per scansionare le transazioni. Questo passaggio richiede che la chiave $b$ sia disponibile su un software di portafoglio connesso a Internet, il che la espone a un rischio maggiore di furto rispetto al mantenerla su un portafoglio freddo. Idealmente, sarebbe vantaggioso poter approfittare dei Pagamenti Silenziosi mantenendo la chiave privata $b$, che controlla l'accesso a tutte le altre chiavi private, al sicuro su un portafoglio hardware. Fortunatamente, il protocollo è stato adattato per permettere esattamente questo.
Per raggiungere questo obiettivo, il BIP352 specifica che il ricevente usa 2 diverse coppie di chiavi:
- $B_{\text{spend}}$: per calcolare le chiavi private degli indirizzi di pagamento unici;
- $B_{\text{scan}}$: per trovare indirizzi di pagamento unici.
In questo modo, Bob può mantenere la chiave privata $b_{\text{spend}}$ su un portafoglio hardware e usare la chiave privata $b_{\text{scan}}$ su software online per trovare i suoi Pagamenti Silenziosi, senza rivelare $b_{\text{spend}}$. Tuttavia, le chiavi pubbliche $B_{\text{scan}}$ e $B_{\text{spend}}$ sono entrambe pubblicamente rivelate, poiché si trovano nell'indirizzo statico di Bob $B$:
Per calcolare un indirizzo di pagamento unico $P_0$ appartenente a Bob, Alice eseguirà il seguente calcolo:
$$ P*0 = B*{\text{spend}} + \text{hash}(\text{inputHash} \cdot a \cdot B\_{\text{scan}} \text{ ‖ } 0) \cdot G $$
Per trovare i pagamenti indirizzati a lui, Bob eseguirà il seguente calcolo:
$$ P*0 = B*{\text{spend}} + \text{hash}(\text{inputHash} \cdot b\_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$
Come puoi vedere, fino a questo momento, Bob non ha avuto bisogno di usare $b_{\text{spend}}$ che si trova sul suo portafoglio hardware. Quando desidera spendere $P_0$, può quindi eseguire il seguente calcolo per trovare la chiave privata $p_0$:
$$ p*0 = (b*{\text{spend}} + \text{hash}(\text{inputHash} \cdot b\_{\text{scan}} \cdot A \text{ ‖ } 0)) \bmod n $$
_Didascalia:_
- $B_{\text{scan}}$: Chiave pubblica di scansione di Bob (indirizzo statico)
- $b_{\text{scan}}$: Chiave privata di scansione di Bob
- $B_{\text{spend}}$: Chiave pubblica di spesa di Bob (indirizzo statico)
- $b_{\text{spend}}$: Chiave privata di spesa di Bob
- $A$: La somma delle chiavi pubbliche in input (tweak)
- $a$: La chiave privata corrispondente alla chiave pubblica modificata
- $H$: L'hash dell'UTXO più piccolo (lessicograficamente) usato in input
- $G$: Il punto generatore della curva ellittica `secp256k1`
- $\text{SHA256}$: La funzione di hashing SHA256 etichettata con `BIP0352/SharedSecret`
- $s_0$: Il primo segreto condiviso ECDH
- $P_0$: La prima chiave pubblica / indirizzo di pagamento unico per Bob
### Utilizzando indirizzi SP con un'etichetta
Bob ha quindi un indirizzo statico $B$ per i Pagamenti Silenziosi come segue:
$$ B = B*{\text{scan}} \text{ ‖ } B*{\text{spend}} $$
Il problema con questo metodo è che non permette di segregare i diversi pagamenti inviati a questo indirizzo. Ad esempio, se Bob ha 2 clienti diversi per la sua attività e vuole differenziare chiaramente i pagamenti da ciascuno, avrebbe bisogno di 2 indirizzi statici diversi. Una soluzione ingenua, con l'approccio attuale, sarebbe che Bob crei due portafogli separati, ognuno con il proprio indirizzo statico, o addirittura stabilisca due indirizzi statici diversi all'interno dello stesso portafoglio. Tuttavia, questa soluzione richiede la scansione dell'intera blockchain due volte (una per ciascun indirizzo) per rilevare rispettivamente i pagamenti destinati a ciascun indirizzo. Questa doppia scansione aumenta in modo irragionevole l'onere operativo per Bob.
Per risolvere questo problema, BIP352 utilizza un sistema di etichettatura che consente di avere diversi indirizzi statici senza aumentare in modo irragionevole il carico di lavoro per trovare Pagamenti Silenziosi sulla blockchain. Per fare ciò, viene aggiunto un intero $m$ alla chiave pubblica di spesa $B_{\text{spend}}$. Questo intero può assumere il valore di $1$ per il primo indirizzo statico, poi $2$ per il secondo, e così via. Le chiavi di spesa $B_{\text{spend}}$ saranno d'ora in poi chiamate $B_m$ e saranno costruite in questo modo:
$$ B*m = B*{\text{spend}} + \text{hash}(b\_{\text{scan}} \text{ ‖ } m) \cdot G $$
Per esempio, per la prima chiave di spesa con l'etichetta $1$:
$$ B*1 = B*{\text{spend}} + \text{hash}(b\_{\text{scan}} \text{ ‖ } 1) \cdot G $$
L'indirizzo statico pubblicato da Bob consisterà ora di $B_{\text{scan}}$ e $B_m$. Per esempio, il primo indirizzo statico con l'etichetta $1$ sarà:
$$ B = B\_{\text{scan}} \text{ ‖ } B_1 $$
> _Iniziamo solo dall'etichetta 1 perché l'etichetta 0 è riservata per il resto._
Alice, da parte sua, deriverà l'indirizzo di pagamento unico $P$ nello stesso modo di prima, ma utilizzando il nuovo $B_1$ invece di $B_{\text{spend}}$.
$$ P*0 = B_1 + \text{hash}(\text{inputHash} \cdot a \cdot B*{\text{scan}} \text{ ‖ } 0) \cdot G $$
In realtà, Alice potrebbe non sapere nemmeno che Bob ha un indirizzo etichettato, poiché lei semplicemente utilizza la seconda parte dell'indirizzo statico che lui le ha fornito, che in questo caso, è il valore $B_1$ piuttosto che $B_{\text{spend}}$.
Per scansionare i pagamenti, Bob utilizzerà sempre il valore del suo indirizzo statico iniziale con $B_{\text{spend}}$ in questo modo:
$$ P*0 = B*{\text{spend}} + \text{hash}(\text{inputHash} \cdot b\_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$
Poi, semplicemente sottrae il valore che trova per $P_0$ da ogni output uno per uno. Poi controlla se uno dei risultati di queste sottrazioni corrisponde al valore di una delle etichette che usa nel suo portafoglio. Se corrisponde, per esempio, per l'output #4 con l'etichetta $1$, ciò significa che questo output è un Pagamento Silenzioso associato al suo indirizzo statico etichettato $B_1$:
$$ Out*4 - P_0 = \text{hash}(b*{\text{scan}} \text{ ‖ } 1) \cdot G $$
Questo funziona perché:
$$ B*1 = B*{\text{spend}} + \text{hash}(b*{\text{scan}} \text{ ‖ } 1) \cdot G $$
Grazie a questo metodo, Bob può utilizzare una moltitudine di indirizzi statici ($B_1$, $B_2$, $B_3$...), tutti derivati dal suo indirizzo statico base ($B = B*{\text{scan}} \text{ ‖ } B*{\text{spend}}$), al fine di separare correttamente gli usi.
Tuttavia, questa separazione degli indirizzi statici è valida solo da una prospettiva di gestione personale del portafoglio e non consente la separazione delle identità. Poiché tutti hanno lo stesso $B*{\text{scan}}$, è molto facile associare tutti gli indirizzi statici insieme e dedurre che appartengono a una singola entità.
_Didascalia:_
- $B_{\text{scan}}$: chiave pubblica di scansione di Bob (indirizzo statico)
- $b_{\text{scan}}$: chiave privata di scansione di Bob
- $B_{\text{spend}}$: chiave pubblica di spesa di Bob (indirizzo iniziale)
- $B_m$: chiave pubblica di spesa etichettata di Bob (indirizzo statico)
- $b_m$: chiave privata di spesa etichettata di Bob
- $A$: La somma delle chiavi pubbliche in input (tweak)
- $a$: La chiave privata corrispondente alla chiave pubblica modificata
- $H$: L'hash del più piccolo UTXO (lessicograficamente) utilizzato come input
- $G$: Il punto generatore della curva ellittica `secp256k1`
- $\text{SHA256}$: La funzione di hashing SHA256 etichettata con `BIP0352/SharedSecret`
- $s_0$: Il primo segreto condiviso ECDH
- $P_0$: La prima chiave pubblica / indirizzo unico per il pagamento a Bob
- $p_0$: La chiave privata del primo indirizzo di pagamento unico a Bob
- $X$: L'hash della chiave privata di scansione con l'etichetta
### Come Costruire un Indirizzo per Pagamenti Silenziosi?
Per costruire un indirizzo dedicato ai Pagamenti Silenziosi, è necessario prima derivare 2 coppie di chiavi nel proprio portafoglio Bitcoin HD:
- La coppia $b_{\text{scan}}$, $B_{\text{scan}}$ per cercare i pagamenti indirizzati a noi;
- La coppia $b_{\text{spend}}$, $B_{\text{spend}}$ per spendere i bitcoin che abbiamo ricevuto.
Queste coppie sono derivate seguendo questi percorsi (_Bitcoin Mainnet_):
scan: m / 352' / 0' / 0' / 1' / 0
spend: m / 352' / 0' / 0' / 0' / 0
```

```text
Una volta disponibili queste 2 coppie di chiavi, si concatenano semplicemente (una di seguito all'altra) per creare il payload dell'indirizzo statico:
$$ B = B*{\text{scan}} \text{ ‖ } B*{\text{spend}} $$
Se si desidera utilizzare etichette, $B_{\text{spend}}$ viene sostituito con $B_m$:
$$ B = B\_{\text{scan}} \text{ ‖ } B_m $$
Con l'etichetta $m$:
$$ B*m = B*{\text{spend}} + \text{hash}(b\_{\text{scan}} \text{ ‖ } m) \cdot G $$
Una volta disponibile questo payload, si aggiunge la HRP (_Human-Readable Part_) `sp` e la versione `q` (= versione 0). Viene anche aggiunto un checksum, e l'indirizzo è formattato in bech32m.
Ad esempio, ecco il mio indirizzo statico per i Pagamenti Silenziosi:
sp1qqvhjvsq2vz8zwrw372vuzle7472zup2ql3pz64yn5cpkw5ngv2n6jq4nl8cgm6zmu48yk3eq33ryc7aam6jrvrg0d0uuyzecfhx2wgsumcurv77e
```