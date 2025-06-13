# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules

hiddenimports = []
hiddenimports += collect_submodules('PIL')


a = Analysis(
    ['check_out_check_in_2_2.py'],
    pathex=[],
    binaries=[],
    datas=[('icons/admin_icon.ico', 'icons'), ('icons/reload.ico', 'icons'), ('icons/search_icon.ico', 'icons'), ('env/lib/python3.11/site-packages/face_recognition_models/models/dlib_face_recognition_resnet_model_v1.dat', 'face_recognition_models/models'), ('env/lib/python3.11/site-packages/face_recognition_models/models/mmod_human_face_detector.dat', 'face_recognition_models/models'), ('env/lib/python3.11/site-packages/face_recognition_models/models/shape_predictor_5_face_landmarks.dat', 'face_recognition_models/models'), ('env/lib/python3.11/site-packages/face_recognition_models/models/shape_predictor_68_face_landmarks.dat', 'face_recognition_models/models'), ('haarcascade_eye.xml', 'cv2/data'), ('haarcascade_frontalface_default.xml', 'cv2/data')],
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='check_out_check_in_2_2',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
