# Zollo Documentation

Zollo is a hybrid bundler for Python and Node.js.

## How It Works

- Scans the user Python folder (`py/Zollo/backend/files/py/`) and copies `.py` files to `.zollo_build/backend_bundle/`.
- Scans the user Node folder (`node/Zollo/frontend/files/js/`) and runs `npm install` and `npm run build`, then copies the output to `.zollo_build/frontend_bundle/`.
- Hidden builds can be unhidden with `zollo unhide`.
- Cleanup with `zollo clean`.

## Folder Overview

- `zollo/`: Internal package code.
- `py/...`: User Python scripts.
- `node/...`: User Node projects.
- `.zollo_build/`: Bundled output.
