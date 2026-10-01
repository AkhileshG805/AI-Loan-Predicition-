# LoanAI — PowerShell Launcher Script
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  LoanAI — Credit Underwriting Decision Support System  " -ForegroundColor Green
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host ""

$portablePy = Join-Path (Split-Path $scriptDir -Parent) "python_embed\python.exe"

if (Test-Path $portablePy) {
    Write-Host "[INFO] Detected portable Python runtime at $portablePy" -ForegroundColor Green
    Start-Process "http://127.0.0.1:5000"
    & $portablePy app.py
} else {
    try {
        $sysPy = (Get-Command python -ErrorAction Stop).Source
        Write-Host "[INFO] Detected system Python at $sysPy" -ForegroundColor Green
        Start-Process "http://127.0.0.1:5000"
        python app.py
    } catch {
        Write-Host "[ERROR] Python could not be located on this system." -ForegroundColor Red
        Write-Host "Please install Python 3.x and run: python app.py" -ForegroundColor Yellow
        Read-Host "Press Enter to exit..."
    }
}
