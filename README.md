VIDEO DEMONSTARTION LINK : https://drive.google.com/file/d/1eLwKiZwRWwx3nOeHXpHroZrcTYwpgxTp/view?usp=sharing
# 🔗 Chord Distributed Hash Table (DHT) Simulator

An interactive and visually rich simulation of the **Chord Protocol**, built using **Python, Streamlit, and Plotly**, to demonstrate how decentralized systems efficiently locate data using consistent hashing.

---

## 📌 Overview

Chord is a **peer-to-peer distributed lookup protocol** that maps keys to nodes in a network using a circular identifier space. It enables efficient data retrieval in **O(log N)** time.

This project provides a **complete visualization and simulation environment** to understand:

- Node organization in a circular ring
- Finger table routing mechanism
- Key lookup process (hop-by-hop)
- Performance metrics and scalability

---

## 🚀 Features

### 🌐 1. Ring Topology Visualization
- Displays nodes arranged in a circular Chord ring
- Shows node IDs based on consistent hashing
- Helps understand the structure of distributed systems

---

### 📊 2. Finger Table Explorer
- Displays finger table for any selected node
- Shows:
  - Start value `(n + 2^i)`
  - Successor node
- Demonstrates how routing is optimized

---

### 🔍 3. Lookup Simulation
- Perform real-time key lookup
- Displays:
  - Path taken across nodes
  - Number of hops
- Shows how Chord avoids linear search

---

### ⚡ 4. Performance Simulation
- Runs multiple lookup requests
- Measures:
  - Average hops
  - Maximum hops
  - Latency
- Validates efficiency of the protocol

---

### 📈 5. Scalability Analysis
- Compares actual lookup hops with **log₂(N)**
- Demonstrates:
  - Logarithmic growth
  - High scalability of Chord

---

## 🧠 Core Concepts

### 🔹 Consistent Hashing
- Maps nodes and keys into the same ID space
- Ensures uniform distribution

---

### 🔹 Circular Ring Structure
- Nodes are arranged in a ring of size `2^m`
- Each node maintains a successor

---

### 🔹 Finger Tables
- Each node maintains `m` entries
- Allows exponential jumps across the ring
- Reduces lookup complexity

---

### 🔹 Lookup Algorithm
1. Start from a node
2. Check if key lies between current and successor
3. Otherwise jump using closest finger
4. Repeat until destination is found

---

## 🏗️ Project Structure

```

├── app.py              # Streamlit UI (Complete dashboard)
├── chord.py            # Core Chord protocol implementation
├── simulation.py       # Lookup simulation & scalability logic
├── requirements.txt    # Dependencies
└── README.md           # Documentation

````

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone <your-repo-link>
cd chord-dht-simulator
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Then open in browser:

```
http://localhost:8501
```

---

## 🖥️ How to Use

1. Select:

   * Bit size `m`
   * Number of nodes

2. Click **Build Network**

3. Navigate through tabs:

   * **Topology** → View ring
   * **Finger Table** → Analyze routing
   * **Lookup** → Perform search
   * **Simulation** → Measure performance
   * **Scalability** → Validate O(log N)

---

## 📊 Example Output

* Lookup hops ≈ **log₂(N)**
* Efficient routing across nodes
* Minimal latency even with increased nodes

---

## 🎯 Learning Outcomes

By using this project, you will understand:

* How distributed systems locate data efficiently
* Why consistent hashing is important
* How Chord achieves scalability
* Real-world applications of DHTs

---

## 🔥 Applications of Chord

* Peer-to-peer networks (e.g., BitTorrent)
* Distributed storage systems
* Blockchain and decentralized apps
* DNS systems

---

## ⚠️ Limitations

* Single-machine simulation (not real networked nodes)
* No fault tolerance simulation
* No real network latency modeling

---

## 🚀 Future Enhancements

* 🌐 Multi-node distributed simulation
* 🔁 Node join/leave dynamics
* 🎬 Animated lookup visualization
* ☁️ Cloud deployment
* 📡 Network delay simulation

---

## 👨‍💻 Author

**Suriya Kumari P**
M.Tech Integrated CSE – VIT

---

## ⭐ Acknowledgment

Inspired by the original **Chord Protocol (MIT Research)** for distributed systems.

---

## 📌 Conclusion

This project demonstrates how **Chord efficiently solves distributed lookup problems** using structured peer-to-peer architecture, achieving **logarithmic complexity and high scalability**, making it a fundamental concept in modern distributed computing.

```
```
