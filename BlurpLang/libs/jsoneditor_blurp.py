def importer(env):
    import os, json
    def ouvrir_json(chemin_widget, contenu_widget):
        chemin = chemin_widget.get("1.0", "end").strip()
        if os.path.exists(chemin):
            with open(chemin, "r", encoding="utf-8") as f:
                contenu_widget.delete("1.0", "end")
                contenu_widget.insert("1.0", f.read())
        else:
            contenu_widget.delete("1.0", "end")
            contenu_widget.insert("1.0", "{}")
    def sauvegarder_json(chemin_widget, contenu_widget):
        chemin = chemin_widget.get("1.0", "end").strip()
        texte = contenu_widget.get("1.0", "end")
        try:
            obj = json.loads(texte)
            with open(chemin, "w", encoding="utf-8") as f:
                f.write(json.dumps(obj, indent=2, ensure_ascii=False))
        except Exception as e:
            contenu_widget.delete("1.0", "end")
            contenu_widget.insert("1.0", f"[erreur] {e}")
    env["ouvrir_json"] = ouvrir_json
    env["sauvegarder_json"] = sauvegarder_json
