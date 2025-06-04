# Productions_max_profit

This repository provides Python implementations for solving a production optimization problem using both brute-force and Branch and Bound algorithms. The goal is to maximize profit given resource constraints and production limitations.

## Problem Description

The optimization problem focuses on determining the optimal quantities of three products (A, B, and C) to maximize total profit. The objective function and constraints are as follows:

**Objective Function:**

Maximize: `p1*x1 + p2*x2 + p3*x3`

**Subject to:**

* `l1*x1 + l2*x2 + l3*x3 <= L` (Labor constraint)
* `m1*x1 + m2*x2 + m3*x3 <= M` (Material constraint)
* `x1 >= 0` (Real number)
* `x2, x3 ∈ {0,1,2,...}` (Integers)

In cases where multiple solutions yield the same profit, the solution with the larger `x2` is preferred. If `x2` values are equal, the solution with the larger `x3` is chosen.

## Repository Structure

* `Productions_max_profit.py`: Implements the brute-force approach to solve the optimization problem.
* `Second_version.py`: Implements the Branch and Bound algorithm for a more efficient solution.

## Getting Started

### Prerequisites

* Python 3.x

### Running the Code

1. Clone the repository:

   ```bash
   git clone https://github.com/mahajialirezaei/Productions_max_profit.git
   cd Productions_max_profit
   ```



2. Run the desired Python script:

   * For brute-force approach:

     ```bash
     python Productions_max_profit.py
     ```

   * For Branch and Bound approach:

     ```bash
     python Second_version.py
     ```

3. Input the required parameters when prompted:

   * Profit coefficients: `p1 p2 p3`
   * Labor coefficients: `l1 l2 l3`
   * Material coefficients: `m1 m2 m3`
   * Available resources: `L M`

## Example

```bash
Enter profit coefficients (p1 p2 p3): 50 40 30
Enter labor coefficients (l1 l2 l3): 2 1 1
Enter material coefficients (m1 m2 m3): 1 2 1
Enter available labor and material (L M): 60 50
```



The program will output the optimal quantities of products A, B, and C, along with the total profit.


## 🛠 Developer

Developed by [Mohammad Amin Haji Alirezaei](https://github.com/mahajialirezaei)
Feel free to ⭐️ this repo or open an issue if you'd like to contribute or have questions!
