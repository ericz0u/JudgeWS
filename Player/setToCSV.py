import os
import csv


def extract_card_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Ensure the file has enough lines
        if len(lines) < 9:
            raise ValueError(f"File {file_path} does not have enough lines.")

        # Extract data from lines
        name = lines[0].strip()
        card_no_line = lines[2].split('Card No.: ')
        if len(card_no_line) < 2:
            raise ValueError(f"Card No. not found in file {file_path}")
        card_no = card_no_line[1].split(' ')[0].strip()

        rarity_line = lines[2].split('Rarity: ')
        if len(rarity_line) < 2:
            raise ValueError(f"Rarity not found in file {file_path}")
        rarity = rarity_line[1].strip()

        color_line = lines[3].split('Color: ')
        if len(color_line) < 2:
            raise ValueError(f"Color not found in file {file_path}")
        color = color_line[1].split(' ')[0].strip()

        card_type = lines[3].split()[-1].strip()

        level_line = lines[4].split('Level: ')
        if len(level_line) < 2:
            raise ValueError(f"Level not found in file {file_path}")
        level = level_line[1].split(' ')[0].strip()

        cost_line = lines[4].split('Cost: ')
        if len(cost_line) < 2:
            raise ValueError(f"Cost not found in file {file_path}")
        cost = cost_line[1].split(' ')[0].strip()

        power_line = lines[4].split('Power: ')
        if len(power_line) < 2:
            raise ValueError(f"Power not found in file {file_path}")
        power = power_line[1].split(' ')[0].strip()

        soul_line = lines[4].split('Soul: ')
        if len(soul_line) < 2:
            raise ValueError(f"Soul not found in file {file_path}")
        soul = soul_line[1].strip()

        traits_line = lines[5].split('Traits: ')
        if len(traits_line) < 2:
            raise ValueError(f"Traits not found in file {file_path}")
        traits = traits_line[1].strip()

        triggers_line = lines[6].split('Triggers: ')
        if len(triggers_line) < 2:
            raise ValueError(f"Triggers not found in file {file_path}")
        triggers = triggers_line[1].strip()

        # Check if there's a "Flavor:" line, and find where "TEXT:" starts
        text_start_idx = 7
        if 'Flavor:' in lines[7]:
            text_start_idx = 8

        text_line = ''.join(lines[text_start_idx:])
        if 'TEXT: ' not in text_line:
            raise ValueError(f"TEXT not found in file {file_path}")
        text = text_line.split('TEXT: ')[1].strip()

        return [name, card_no, rarity, color, card_type, level, cost, power, soul, traits, triggers, text]
    except IndexError as e:
        raise ValueError(f"Error parsing file {file_path}: {e}")
    except Exception as e:
        raise ValueError(f"Unexpected error with file {file_path}: {e}")


def process_directory(directory_path, output_csv_path):
    # Prepare the CSV file
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        # Write header
        csvwriter.writerow(
            ['Name', 'Card No.', 'Rarity', 'Color', 'Card Type', 'Level', 'Cost', 'Power', 'Soul', 'Traits', 'Triggers',
             'Text'])

        # Process each file in the directory
        for filename in os.listdir(directory_path):
            if filename.endswith('.txt'):
                file_path = os.path.join(directory_path, filename)
                try:
                    card_data = extract_card_data(file_path)
                    csvwriter.writerow(card_data)
                except ValueError as e:
                    print(e)
# Example usage:
directory_path = 'MTI_MushokuTenseiSet'  # Update this path to your directory
output_csv_path = 'output.csv'  # Update this path to your desired output CSV path
process_directory(directory_path, output_csv_path)






