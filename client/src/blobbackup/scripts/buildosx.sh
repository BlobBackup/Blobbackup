#!/bin/bash

src/blobbackup/scripts/buildrestic.sh
src/blobbackup/scripts/generateui.sh
pip install .
pyinstaller --clean --noconfirm package/blobbackup.spec
rm -rf dist/blobbackup build