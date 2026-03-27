import pcbnew, json
from pcbnew import VECTOR2I, EDA_ANGLE

board = pcbnew.GetBoard()

path = board.GetFileName().replace(".kicad_pcb", "_silk_backup.json")
with open(path, "r") as f:
    data = json.load(f)

restored = 0
skipped = []

for fp in board.GetFootprints():
    ref_des = fp.GetReference()
    if ref_des not in data:
        skipped.append(ref_des)
        continue

    d = data[ref_des]

    # --- Reference ---
    ref = fp.Reference()
    r = d["ref"]
    ref.SetX(r["x"])
    ref.SetY(r["y"])
    ref.SetTextSize(VECTOR2I(r["size_x"], r["size_y"]))
    ref.SetTextAngle(EDA_ANGLE(r["angle"], pcbnew.DEGREES_T))
    ref.SetVisible(r["visible"])
    ref.SetBold(r["bold"])
    ref.SetItalic(r["italic"])
    ref.SetTextThickness(r["thickness"])
    ref.SetMirrored(r["mirrored"])

    # --- Value ---
    val = fp.Value()
    v = d["val"]
    val.SetX(v["x"])
    val.SetY(v["y"])
    val.SetTextSize(VECTOR2I(v["size_x"], v["size_y"]))
    val.SetTextAngle(EDA_ANGLE(v["angle"], pcbnew.DEGREES_T))
    val.SetVisible(v["visible"])
    val.SetBold(v["bold"])
    val.SetItalic(v["italic"])
    val.SetTextThickness(v["thickness"])
    val.SetMirrored(v["mirrored"])

    restored += 1

# Odśwież widok
pcbnew.Refresh()

print(f"Przywrócono: {restored} komponentów")
if skipped:
    print(f"Pominięto (brak w backupie): {skipped}")