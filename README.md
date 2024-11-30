
# 3-Color Marking Module and Token Bucket Implementation

This project implements Python modules for 3-color marking using a two-rate token bucket (trTCM) and a single-rate token bucket, in addition to analyzing their performance with MMPP (Markov Modulated Poisson Process) traffic.

## Features

- **Two-Color Token Bucket**:
  - Implements a single-rate token bucket for unit-sized packets.
  - Marks packets as conforming (green) or non-conforming (red).

- **Three-Color Token Bucket (trTCM)**:
  - Implements a two-rate token bucket for 3-color marking.
  - Marks packets as green, yellow, or red based on committed and peak rates.

- **MMPP Traffic**:
  - Generates ON-OFF MMPP traffic with configurable parameters.
  - Analyzes performance of token buckets with MMPP traffic.

## Code Structure

### Main Functions

- **`two_color_token_bucket(packets, r, B)`**:
  - Simulates a single-rate token bucket.
  - Marks packets as conforming (green) or non-conforming (red).

- **`three_color_token_bucket(packets, PIR, PBS, CIR, CBS)`**:
  - Implements a two-rate token bucket for 3-color marking.

- **`generate_on_off_mmpp(B, r, total_time)`**:
  - Generates packet arrival times using an ON-OFF MMPP process.

### Analysis

1. **Single-Rate Token Bucket**:
   - Processes a sequence of packets through a single-rate token bucket.
   - Outputs the color marking for each packet.

2. **Three-Color Token Bucket**:
   - Processes a sequence of packets through a two-rate token bucket.
   - Marks packets with green, yellow, or red colors based on token availability.

3. **MMPP with Token Buckets**:
   - Generates MMPP traffic and feeds it into a three-color token bucket.
   - Provides detailed statistics on token bucket performance, including:
     - Percentages of packets marked green, yellow, and red.
     - Cumulative percentage plots for each color over time.

## How to Run

1. Install dependencies:
   ```bash
   pip install numpy matplotlib
   ```
2. Run the script:
   ```bash
   python Question5.py
   ```

## Results

1. **Token Bucket Statistics**:
   - Displays statistics on the number and percentage of packets marked green, yellow, and red.
   - Analyzes how token bucket parameters influence marking decisions.

2. **MMPP Parameters**:
   - Configurable burst size (`B`) and average rate (`r`).
   - Displays expected burst size and arrival rate.

3. **Cumulative Traffic Plots**:
   - Visualizes cumulative percentages of traffic marked as green, yellow, and red over time.

## Dependencies

- Python 3.9 or higher
- NumPy
- Matplotlib