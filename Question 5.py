from typing import List
import numpy as np
import matplotlib.pyplot as plt


class Packet:
    def __init__(self, arrival_time, size=1, color=2):
        self.arrival_time = arrival_time
        self.size = size  # Packet size can vary
        self.color = color  # Default to red (non-conforming)

    def __repr__(self):
        return f"Packet(arrival_time={self.arrival_time}, size={self.size}, color={self.color})"


def three_color_token_bucket(packets: List[Packet], PIR: float, PBS: int, CIR: float, CBS: int) -> List[Packet]:
    """
    Implements the two-rate three-color token bucket algorithm (trTCM).

    Args:
        packets (List[Packet]): The sequence of packets to process.
        PIR (float): Peak Information Rate (tokens per unit time) for the peak bucket.
        PBS (int): Peak Burst Size (capacity of the peak bucket).
        CIR (float): Committed Information Rate (tokens per unit time) for the committed bucket.
        CBS (int): Committed Burst Size (capacity of the committed bucket).

    Returns:
        List[Packet]: The sequence of packets with updated color markings.
    """
    token_bucket_P = PBS  # Initialize peak bucket with capacity PBS
    token_bucket_C = CBS  # Initialize committed bucket with capacity CBS
    last_time = packets[0].arrival_time if packets else 0.0  # Initialize last update time

    for packet in packets:
        # Update tokens based on time elapsed since last packet
        time_elapsed = packet.arrival_time - last_time
        last_time = packet.arrival_time

        # Add tokens to committed bucket
        tokens_added_C = time_elapsed * CIR
        token_bucket_C = min(token_bucket_C + tokens_added_C, CBS)

        # Add tokens to peak bucket
        tokens_added_P = time_elapsed * PIR
        token_bucket_P = min(token_bucket_P + tokens_added_P, PBS)

        # Check committed bucket for green marking
        if token_bucket_C >= packet.size:
            packet.color = 0  # Green
            token_bucket_C -= packet.size  # Consume tokens from committed bucket
            token_bucket_P -= packet.size  # Also consume from peak bucket
        # Check peak bucket for yellow marking
        elif token_bucket_P >= packet.size:
            packet.color = 1  # Yellow
            token_bucket_P -= packet.size  # Consume tokens from peak bucket only
            # Committed bucket remains unchanged
        else:
            packet.color = 2  # Red
            # Tokens remain unchanged

    return packets


def two_color_token_bucket(packets: List[Packet], r: float, B: int) -> List[Packet]:
    """
    Implements the two-color token bucket algorithm with variable packet sizes.

    Args:
        packets (List[Packet]): The sequence of packets to process.
        r (float): The rate at which tokens are added to the bucket.
        B (int): The maximum capacity of the token bucket.

    Returns:
        List[Packet]: The sequence of packets with updated color markings.
    """
    token_bucket = B  # Initialize token bucket with capacity B
    last_time = 0.0  # Initialize last update time

    for packet in packets:
        # Update tokens based on time elapsed since last packet
        time_elapsed = packet.arrival_time - last_time
        tokens_added = time_elapsed * r
        token_bucket = min(token_bucket + tokens_added, B)
        last_time = packet.arrival_time

        # Check if there are enough tokens for the packet
        if token_bucket >= packet.size:
            packet.color = 0  # Mark as conforming (green)
            token_bucket -= packet.size  # Consume tokens equal to packet size
        else:
            packet.color = 2  # Mark as non-conforming (red)
            # Token bucket remains unchanged

    return packets


def section1():
    print("------------------Section A-------------------")
    # Define the token bucket parameters
    r = 1.0  # tokens per unit time
    B = 5  # maximum number of tokens in the bucket

    # Create a sequence of packets with varying sizes and arrival times
    packets = [
        Packet(arrival_time=0.5),
        Packet(arrival_time=0.515),
        Packet(arrival_time=0.52),
        Packet(arrival_time=0.53),
        Packet(arrival_time=0.54),
        Packet(arrival_time=0.55),
        Packet(arrival_time=0.56),
        Packet(arrival_time=0.7),
        Packet(arrival_time=0.8),
        Packet(arrival_time=1.6),
    ]

    # Process the packets through the token bucket
    processed_packets = two_color_token_bucket(packets, r, B)

    # Output the results
    for i, packet in enumerate(processed_packets):
        color = "Green" if packet.color == 0 else "Red"
        print(f"Packet {i + 1}: Arrival Time = {packet.arrival_time}, Size = {packet.size}, Color = {color}")


def section2():
    print("------------------Section B-------------------")
    # Define the token bucket parameters
    PIR = 1.0  # Peak Information Rate (tokens per unit time)
    PBS = 5  # Peak Burst Size (tokens)
    CIR = 0.5  # Committed Information Rate (tokens per unit time)
    CBS = 3  # Committed Burst Size (tokens)

    # Create a sequence of packets with varying sizes and arrival times
    packets = [
        Packet(arrival_time=0.5),
        Packet(arrival_time=0.515),
        Packet(arrival_time=0.52),
        Packet(arrival_time=0.53),
        Packet(arrival_time=0.54),
        Packet(arrival_time=0.55),
        Packet(arrival_time=0.56),
        Packet(arrival_time=0.7),
        Packet(arrival_time=0.8),
        Packet(arrival_time=1.6),
    ]

    # Process the packets through the token bucket
    processed_packets = three_color_token_bucket(packets, PIR, PBS, CIR, CBS)

    # Output the results
    color_mapping = {0: "Green", 1: "Yellow", 2: "Red"}
    for i, packet in enumerate(processed_packets):
        color = color_mapping[packet.color]
        print(f"Packet {i + 1}: Arrival Time = {packet.arrival_time}, Size = {packet.size}, Color = {color}")


def section3():
    def three_color_token_bucket_C(packets, PIR, PBS, CIR, CBS):
        token_bucket_P = PBS  # Initialize peak bucket with capacity PBS
        token_bucket_C = CBS  # Initialize committed bucket with capacity CBS
        last_time = packets[0].arrival_time if packets else 0.0  # Initialize last update time

        # Lists to store cumulative percentages over time
        time_points = []
        cumulative_green = []
        cumulative_yellow = []
        cumulative_red = []

        total_packets = 0
        green_packets = 0
        yellow_packets = 0
        red_packets = 0

        for packet in packets:
            # Update tokens based on time elapsed since last packet
            time_elapsed = packet.arrival_time - last_time
            last_time = packet.arrival_time

            # Add tokens to committed bucket
            tokens_added_C = time_elapsed * CIR
            token_bucket_C = min(token_bucket_C + tokens_added_C, CBS)

            # Add tokens to peak bucket
            tokens_added_P = time_elapsed * PIR
            token_bucket_P = min(token_bucket_P + tokens_added_P, PBS)

            # Check committed bucket for green marking
            if token_bucket_C >= packet.size:
                packet.color = 0  # Green
                token_bucket_C -= packet.size  # Consume tokens from committed bucket
                token_bucket_P -= packet.size  # Also consume from peak bucket
                green_packets += 1
            # Check peak bucket for yellow marking
            elif token_bucket_P >= packet.size:
                packet.color = 1  # Yellow
                token_bucket_P -= packet.size  # Consume tokens from peak bucket only
                yellow_packets += 1
            else:
                packet.color = 2  # Red
                red_packets += 1

            total_packets += 1

            # Record cumulative percentages
            time_points.append(packet.arrival_time)
            cumulative_green.append(green_packets / total_packets * 100)
            cumulative_yellow.append(yellow_packets / total_packets * 100)
            cumulative_red.append(red_packets / total_packets * 100)

        return packets, time_points, cumulative_green, cumulative_yellow, cumulative_red

    def generate_on_off_mmpp(B, r, total_time):
        """
        Generates packet arrival times using an ON-OFF MMPP process.

        Args:
            B (float): Burst rate during the ON state (packets per unit time).
            r (float): Average rate over the entire simulation (packets per unit time).
            total_time (float): Total simulation time.

        Returns:
            List[Packet]: A list of Packet objects with arrival times.
        """
        if r >= B:
            raise ValueError("Average rate r must be less than burst rate B.")

        # Calculate the fraction of time spent in the ON state
        p_on = r / B

        # Choose mean durations for ON and OFF periods
        mean_on_duration = 1.0  # Adjust as needed
        mean_off_duration = mean_on_duration * (1 - p_on) / p_on

        current_time = 0.0
        state = 'OFF'
        packets = []
        on_times = []
        while current_time < total_time:
            if state == 'ON':
                # Duration in ON state
                on_duration = np.random.exponential(mean_on_duration)
                end_time = current_time + on_duration
                if end_time > total_time:
                    on_duration = total_time - current_time
                    end_time = total_time
                on_times.append(on_duration)
                # Generate packet arrival times during ON state
                num_packets = np.random.poisson(B * on_duration)
                arrival_times = np.random.uniform(current_time, end_time, num_packets)
                arrival_times.sort()
                packets.extend([Packet(arrival_time=at) for at in arrival_times])

                current_time = end_time
                state = 'OFF'
            else:
                # Duration in OFF state
                off_duration = np.random.exponential(mean_off_duration)
                current_time += off_duration
                state = 'ON'

        # Sort packets by arrival time
        packets.sort(key=lambda p: p.arrival_time)
        return packets, on_times

    print("---------------Section C-------------------")
    # (i) Number of time slots simulated
    total_time = 1000.0  # Total simulation time

    # (ii) MMPP parameters
    B = 15.0  # Burst rate during ON state
    r = 3.0  # Average rate over the simulation
    on_times = []

    # Generate packets using the corrected MMPP code
    packets, on_times = generate_on_off_mmpp(B, r, total_time)


    # Expected burst size
    mean_on_duration = 1.0  # As set in the MMPP function
    expected_burst_size = mean_on_duration * B

    # (iv) Token Bucket parameters
    CIR = 3  # Committed Information Rate (tokens per unit time)
    CBS = 15  # Committed Burst Size (tokens)
    PIR = 5  # Peak Information Rate (tokens per unit time)
    PBS = 30  # Peak Burst Size (tokens)

    # Process packets through the three-color token bucket
    processed_packets, time_points, cumulative_green, cumulative_yellow, cumulative_red = three_color_token_bucket_C(
        packets, PIR, PBS, CIR, CBS)

    # Count the number of packets in each color
    color_counts = {0: 0, 1: 0, 2: 0}
    for packet in processed_packets:
        color_counts[packet.color] += 1

    total_packets = len(processed_packets)
    green_percentage = color_counts[0] / total_packets * 100
    yellow_percentage = color_counts[1] / total_packets * 100
    red_percentage = color_counts[2] / total_packets * 100

    average_rate = total_packets/total_time  # Since we set it as desired average rate
    average_burst = total_packets/sum(on_times)

    print("MMPP Parameters:")
    print(f"Burst during ON state (B): {B}")
    print(f"Rate (r): {r}")
    print(f"Average Arrival Rate: {average_rate:} packets/unit time")
    print(f"Expected Burst Size: {average_burst:} packets\n")

    # Output the percentages
    print("Token Bucket Parameters:")
    print(f"Committed Information Rate (CIR): {CIR}")
    print(f"Committed Burst Size (CBS): {CBS}")
    print(f"Peak Information Rate (PIR): {PIR}")
    print(f"Peak Burst Size (PBS): {PBS}\n")

    print(f"Total packets: {total_packets}")
    print(f"Green packets: {color_counts[0]} ({green_percentage:.2f}%)")
    print(f"Yellow packets: {color_counts[1]} ({yellow_percentage:.2f}%)")
    print(f"Red packets: {color_counts[2]} ({red_percentage:.2f}%)\n")

    # Plotting the cumulative percentage of traffic for each color over time
    plt.figure(figsize=(12, 6))
    plt.plot(time_points, cumulative_green, label='Green', color='green')
    plt.plot(time_points, cumulative_yellow, label='Yellow', color='orange')
    plt.plot(time_points, cumulative_red, label='Red', color='red')
    plt.xlabel('Time')
    plt.ylabel('Cumulative Percentage of Traffic (%)')
    plt.title('Cumulative Percentage of Traffic by Color Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()


# Example usage:
if __name__ == "__main__":
    section1()
    section2()
    section3()
