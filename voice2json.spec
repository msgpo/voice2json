# -*- mode: python -*-
import os
from pathlib import Path

block_cipher = None

venv = Path.cwd() / ".venv"
bin_dir = Path(os.environ.get("spec_bin_dir", venv / "bin"))
lib_dir = Path(os.environ.get("spec_lib_dir", venv / "lib"))

a = Analysis(
    [Path.cwd() / "voice2json" "/__main__.py"],
    pathex=["."],
    binaries=[
        (
            lib_dir
            / "python3.6/site-packages/pywrapfst.cpython-36m-x86_64-linux-gnu.so",
            ".",
        ),
        (lib_dir / "libfstfarscript.so.13", "."),
        (lib_dir / "libfstscript.so.13", "."),
        (lib_dir / "libfstfar.so.13", "."),
        (lib_dir / "libfst.so.13", "."),
        (lib_dir / "libngram.so.134", "."),
        (bin_dir / "ngramread", "."),
        (bin_dir / "ngramcount", "."),
        (bin_dir / "ngrammake", "."),
        (bin_dir / "ngrammerge", "."),
        (bin_dir / "ngramprint", "."),
        (bin_dir / "ngramsymbols", "."),
        (bin_dir / "ngramperplexity", "."),
        (bin_dir / "farcompilestrings", "."),
        (bin_dir / "phonetisaurus-apply", "."),
    ],
    datas=[],
    hiddenimports=["doit", "dbm.gnu", "antlr4-python3-runtime", "networkx", "numbers"],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="voice2json",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
)
coll = COLLECT(
    exe, a.binaries, a.zipfiles, a.datas, strip=False, upx=True, name="voice2json"
)
