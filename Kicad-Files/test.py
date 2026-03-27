import pcbnew, json

board = pcbnew.GetBoard()
data = {}

for fp in board.GetFootprints():
    ref = fp.Reference()
    val = fp.Value()
    data[fp.GetReference()] = {
        "ref": {
            "x": ref.GetX(),
            "y": ref.GetY(),
            "size_x": ref.GetTextSize().x,
            "size_y": ref.GetTextSize().y,
            "angle": ref.GetTextAngle().AsDegrees(),
            "visible": ref.IsVisible(),
            "bold": ref.IsBold(),
            "italic": ref.IsItalic(),
            "thickness": ref.GetTextThickness(),
            "mirrored": ref.IsMirrored(),
        },
        "val": {
            "x": val.GetX(),
            "y": val.GetY(),
            "size_x": val.GetTextSize().x,
            "size_y": val.GetTextSize().y,
            "angle": val.GetTextAngle().AsDegrees(),
            "visible": val.IsVisible(),
            "bold": val.IsBold(),
            "italic": val.IsItalic(),
            "thickness": val.GetTextThickness(),
            "mirrored": val.IsMirrored(),
        }
    }

# Zapisz do pliku obok .kicad_pcb
path = board.GetFileName().replace(".kicad_pcb", "_silk_backup.json")
with open(path, "w") as f:
    json.dump(data, f, indent=2)

print(f"Zapisano {len(data)} komponentów do: {path}")