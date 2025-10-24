def main(input):
    with open(f"{input}.txt") as f:
        jet_pattern = f.read().strip()

    # Rock shapes as coordinate offsets from top-left corner
    PIECES = [
        [0, 1, 2, 3],  # Horizontal line: ####
        [-1j, 1, 1 - 1j, 1 - 2j, 2 - 1j],  # Plus: +
        [-2j, 1 - 2j, 2, 2 - 1j, 2 - 2j],  # Reverse L: ⅃
        [0, -1j, -2j, -3j],  # Vertical line: |
        [0, -1j, 1, 1 - 1j],  # Square: ■
    ]

    HEIGHTS = [1, 3, 3, 4, 2]
    WIDTHS = [4, 3, 3, 1, 2]
    CHAMBER_WIDTH = 7

    def solve(num_pieces):
        # Initialize game state
        settled_rocks = set(range(CHAMBER_WIDTH))  # Floor at y=0
        max_height = 0
        column_tops = {i: 0 for i in range(CHAMBER_WIDTH)}

        # For cycle detection (part 2)
        seen_states = {}
        skipped = False
        rocks_added_from_skip = 0

        rock_count = 0
        jet_index = 0

        while rock_count < num_pieces:
            # Select current piece
            piece_type = rock_count % 5
            piece_height = HEIGHTS[piece_type]
            piece_width = WIDTHS[piece_type]
            piece_offsets = PIECES[piece_type]

            # Spawn rock at starting position (2 units from left, 3 units above highest rock)
            rock_pos = 2 + (max_height + piece_height + 3) * 1j

            # Simulate rock falling
            while True:
                # Push by jet
                jet_dir = jet_pattern[jet_index % len(jet_pattern)]
                jet_index += 1

                if jet_dir == ">":
                    # Try to push right
                    new_pos = rock_pos + 1
                    rock_coords = {new_pos + offset for offset in piece_offsets}

                    # Check if move is valid (not hitting wall or settled rocks)
                    if (
                        not (rock_coords & settled_rocks)
                        and (piece_width + new_pos.real) <= CHAMBER_WIDTH
                    ):
                        rock_pos = new_pos
                else:  # jet_dir == "<"
                    # Try to push left
                    new_pos = rock_pos - 1
                    rock_coords = {new_pos + offset for offset in piece_offsets}

                    # Check if move is valid
                    if not (rock_coords & settled_rocks) and new_pos.real >= 0:
                        rock_pos = new_pos

                # Try to fall down
                new_pos = rock_pos - 1j
                rock_coords = {new_pos + offset for offset in piece_offsets}

                # Check if rock hits something below
                if rock_coords & settled_rocks:
                    # Rock has settled - add it to the grid
                    final_coords = {rock_pos + offset for offset in piece_offsets}

                    # Update column tops
                    for coord in final_coords:
                        column_tops[coord.real] = max(
                            column_tops[coord.real], coord.imag
                        )

                    # Add to settled rocks
                    settled_rocks |= final_coords

                    # Update max height
                    max_height = max(
                        max_height, max(coord.imag for coord in final_coords)
                    )

                    # Cycle detection for part 2
                    if not skipped:
                        min_top = min(column_tops.values())
                        state = (
                            piece_type,
                            (jet_index - 1) % len(jet_pattern),
                            tuple(
                                column_tops[i] - min_top for i in range(CHAMBER_WIDTH)
                            ),
                        )

                        if state in seen_states:
                            # Found a cycle! Skip ahead
                            print("Skipping ahead")
                            skipped = True
                            prev_rock_count, prev_height = seen_states[state]

                            cycle_length = rock_count - prev_rock_count
                            cycle_height = max_height - prev_height

                            num_cycles_to_skip = (
                                num_pieces - rock_count
                            ) // cycle_length
                            rock_count += cycle_length * num_cycles_to_skip
                            rocks_added_from_skip = num_cycles_to_skip * cycle_height
                            print(f"Skipped {rocks_added_from_skip} rocks")

                        seen_states[state] = (rock_count, max_height)

                    break
                else:
                    # Rock continues falling
                    rock_pos = new_pos

            rock_count += 1

        return max_height + rocks_added_from_skip

    # Part 1: Height after 2022 rocks
    print(f"Part 1: {solve(2022)}")

    # Part 2: Height after 1 trillion rocks
    print(f"Part 2: {solve(1000000000000)}")


if __name__ == "__main__":
    main("sample")
