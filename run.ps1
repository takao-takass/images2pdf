if (-not (Test-Path .venv)) {
    python -m venv .venv
    Write-Host ".venvディレクトリを作成し、Pythonの仮想環境を設定しました。"
} else {
    Write-Host ".venvディレクトリは既に存在します。"
}

.venv\Scripts\Activate.ps1

pip install -r requirements.txt

python main.py