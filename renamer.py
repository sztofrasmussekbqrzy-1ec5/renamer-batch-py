#!/usr/bin/env python3
"""Batch rename: prefix + urutan nomor, preserve extension."""
import os, argparse
def main():
      ap = argparse.ArgumentParser(); ap.add_argument("folder"); ap.add_argument("prefix"); ap.add_argument("--dry-run", action="store_true")
      a = ap.parse_args()
      files = sorted(f for f in os.listdir(a.folder) if os.path.isfile(os.path.join(a.folder, f)))
      for i, name in enumerate(files, 1):
                ext = os.path.splitext(name)[1]
                new = f"{a.prefix}_{i:03d}{ext}"
                if not a.dry_run: os.rename(os.path.join(a.folder, name), os.path.join(a.folder, new))
                          print(f"{name} -> {new}")
        if __name__ == "__main__": main()
          
