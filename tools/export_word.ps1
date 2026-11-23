param([switch]$TemplatesOnly,[switch]$Mla,[switch]$JavaOnly)
$ErrorActionPreference = 'Stop'
$workspacePath = Split-Path -Parent $PSScriptRoot
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0
$word.AutomationSecurity = 3
try {
    $documentNames = @('Engineering_Impact_Framework','Engineering_Impact_Framework_Templates')
    if ($TemplatesOnly) { $documentNames = @('Engineering_Impact_Framework_Templates') }
    if ($Mla) { $documentNames = $documentNames | ForEach-Object { $_ + '_MLA' } }
    if ($JavaOnly) { $documentNames = @('Engineering_Impact_Framework_Java_Workflow_MLA') }
    foreach ($name in $documentNames) {
        $documentPath = Join-Path $workspacePath "outputs\$name.docx"
        $renderPath = Join-Path $workspacePath "tmp\qa\$name"
        New-Item -ItemType Directory -Path $renderPath -Force | Out-Null
        $pdfPath = Join-Path $renderPath "$name.pdf"
        $document = $word.Documents.Open($documentPath, $false, $false, $false)
        try {
            $document.Fields.Update() | Out-Null
            foreach ($toc in $document.TablesOfContents) { $toc.Update() }
            $document.Repaginate()
            $document.Save()
            $document.ExportAsFixedFormat($pdfPath, 17)
            Write-Output $pdfPath
        } finally { $document.Close(0) }
    }
} finally {
    $word.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
}
