COMPANY: CODTECH IT SOLUTIONS

NAME: Marachu Ganesh

INTERN ID:CT06DL1050

DOMAIN: SQL

DURATION: 6 WEEEKS

MENTOR: NEELA SANTOSH

# FILE-INTEGRITY-CHECKER

This project is a simple Python-based tool developed to monitor the integrity of important files by calculating and comparing their SHA-256 hash values. The idea behind this tool is straightforward but important: any change in a file’s contents, no matter how small, will result in a different hash value. By storing the original hash of each file and comparing it during future runs, the tool can detect whether the file has been altered, added, or left unchanged. This functionality can play a crucial role in environments where the consistency and security of files are essential.

The tool was developed as part of a cybersecurity internship with the intention of applying theoretical concepts in a practical way. File integrity monitoring is a foundational concept in digital security, and this script aims to demonstrate how simple techniques can still be effective when it comes to protecting digital assets. It uses Python’s built-in `hashlib` and `json` modules to calculate and store the hash values. The first time the script is run, it records the hash values of the specified files and saves them in a JSON file. On subsequent runs, the script checks each file again, recalculates the hash, and compares it to the previously stored value. Based on the comparison, it reports whether the file has been modified, remains unchanged, or is new.

The tool is easy to set up. The user only needs to specify the list of files they want to monitor. It doesn’t rely on any external libraries, so it runs in any environment where Python is available. This makes it lightweight and highly portable. Its simplicity also means it can be easily modified or extended in the future to monitor folders, send alerts, or even integrate into automated workflows or task schedulers.

This kind of monitoring is especially useful for configuration files, log files, scripts, or any documents that must not be changed without proper authorization. Even developers and IT professionals can benefit from using this script to keep an eye on important files in their local or server environments. Although this project focuses on the basic concept of hashing and file comparison, the idea has broader applications in real-world cybersecurity tools and intrusion detection systems.

Overall, building this file integrity checker was a valuable experience that strengthened both programming and security fundamentals. It involved thinking carefully about how changes can be tracked over time in a reliable and secure way. While the script is small, its usefulness lies in its ability to highlight how simple tools can support essential security tasks. It reflects the importance of attention to detail in cybersecurity and demonstrates how a basic concept like hashing can be turned into a working solution with real-world applications.
