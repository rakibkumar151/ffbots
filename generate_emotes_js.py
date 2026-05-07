import json
import os

def generate():
    try:
        with open('emotes.json', 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading emotes.json: {e}")
        return

    numbers = data.get("EMOTES", {}).get("numbers", {})
    names_dict = data.get("EMOTES", {}).get("names", {})
    
    unique_emotes = {}
    
    # Process numbers
    for k, v in numbers.items():
        unique_emotes[v] = f"Emote {k}"
        
    # Process names
    for k, v in names_dict.items():
        if v in unique_emotes:
            # Prefer readable names over "Emote X"
            if unique_emotes[v].startswith("Emote "):
                unique_emotes[v] = k.replace("_", " ").title()
        else:
            unique_emotes[v] = k.replace("_", " ").title()

    # Create JS array
    js_content = "export const EMOTES = [\n"
    for eid, label in unique_emotes.items():
        js_content += f"  {{ id: '{eid}', name: '{label.lower()}', label: '{label}' }},\n"
    js_content += "];\n"
    
    with open('frontend/src/emotesData.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
        
    print(f"Generated {len(unique_emotes)} emotes in frontend/src/emotesData.js")

if __name__ == "__main__":
    generate()
