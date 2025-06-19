# ===================================
# PowerShell Build Script for HKit
# ===================================

# === ANSI Bold Color Codes ===
$ESC    = [char]27
$Reset  = "$ESC[0m"
$Bold   = "$ESC[1m"
$Green  = "$ESC[1;32m"
$Red    = "$ESC[1;31m"
$Cyan   = "$ESC[1;36m"

# === Header ===
Write-Host "${Cyan}=====================================${Reset}"
Write-Host "${Red}${Bold}PowerShell Build Script for HKit${Reset}"
Write-Host "${Cyan}=====================================${Reset}"

# === Configuration ===
$ScriptName  = "app.py"
$AppName     = "HKit"
$IconFile    = "assets\icon.ico"
$VersionFile = "version_info.txt"
$DataFolders = @(
    "assets\*;assets",
    "Scripts\*;Scripts"
)

# === Clean Previous Builds ===
Write-Host "${Cyan}${Bold}Cleaning old builds...${Reset}"
Remove-Item -Recurse -Force build, dist, *.spec -ErrorAction SilentlyContinue

# === Build Data Flags ===
Write-Host "${Cyan}${Bold}Generating --add-data arguments...${Reset}"
$AddDataArgs = ($DataFolders | ForEach-Object { "--add-data `"$($_)`"" }) -join " "

# === Build Command ===
Write-Host "${Cyan}${Bold}Building executable with PyInstaller...${Reset}"
$Command = "pyinstaller --noconsole --name `"$AppName`" --icon `"$IconFile`" --version-file `"$VersionFile`" --noconfirm $AddDataArgs `"$ScriptName`""
Invoke-Expression $Command

# === Result ===
if (Test-Path "dist\$AppName") {
    Write-Host "`n${Green}${Bold}Build complete. Executable located in 'dist\$AppName\'${Reset}`n"
} else {
    Write-Host "`n${Red}${Bold}Build failed. Please check the output above for details.${Reset}`n"
}