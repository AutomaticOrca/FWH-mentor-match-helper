import csv

def get_mentor_dict():
    # Load mentor ID to name mapping and capacity
    mentor_info_mapping = {}
    with open('origin_mentor.csv', 'r') as name_file:
        for line in name_file:
            if not line.strip():  # Skip empty lines
                continue
            parts = line.strip().split('\t')
            if len(parts) >= 2:
                mentor_id, mentor_name = parts[0], parts[1]
                max_capacity = int(parts[-1]) if parts[-1].isdigit() else 0  # Get max mentee capacity
                mentor_info_mapping[mentor_id.zfill(2)] = {
                    'name': mentor_name,
                    'capacity': max_capacity
                }

    # Process mentor-mentee relationships
    with open('origin_miniapp.csv', 'r') as file:
        lines = file.readlines()

    result = {}

    for line in lines:
        if not line.strip():  # Skip empty lines
            continue
        key, value = line.strip().split('\t')
        key = key.zfill(2)  # Preserve leading zeros
        if key not in mentor_info_mapping:  # Skip invalid mentor IDs
            continue
        try:
            value = value.zfill(2) if value.isdigit() else value
        except ValueError:
            pass

        if key not in result:
            result[key] = []
        result[key].append(value)

    # Ensure all valid mentors are in the result, even those without mentees
    for mentor_id in mentor_info_mapping.keys():
        if mentor_id not in result:
            result[mentor_id] = []

    # Sort mentors by mentor_id numerically in ascending order
    sorted_result = sorted(result.items(), key=lambda item: int(item[0]))

    # Write combined data to CSV
    with open('result.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the header
        writer.writerow(['mentor_id', 'mentor_name', 'mentee1', 'mentee2', 'mentee3', 'mentee4', 'remaining_slots', 'unselected'])

        # Write the data rows
        for key, mentees in sorted_result:
            mentor_info = mentor_info_mapping.get(key, {'name': 'Unknown', 'capacity': 0})
            mentor_name = mentor_info['name']
            max_capacity = mentor_info['capacity']
            mentees += [''] * (4 - len(mentees))  # Pad with empty strings if fewer than 4 mentees
            remaining_slots = max_capacity - len([m for m in mentees if m])
            remaining_slots = max(remaining_slots, 0)  # Ensure non-negative
            unselected = 'Yes' if len([m for m in mentees if m]) == 0 else 'No'  # Mark unselected mentors
            writer.writerow([key, mentor_name] + mentees[:4] + [remaining_slots, unselected])

if __name__ == '__main__':
    get_mentor_dict()
