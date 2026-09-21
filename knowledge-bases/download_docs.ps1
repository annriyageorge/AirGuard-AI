$docsDir = Join-Path $PSScriptRoot "docs"

if (-not (Test-Path $docsDir)) {
    New-Item -ItemType Directory -Path $docsDir | Out-Null
}

$sources = @(
    @{ File = "cpcb_aqi_india.html"; Url = "https://app.cpcbccr.com/AQI_India/" },
    @{ File = "cpcb_naaqs.html"; Url = "https://cpcb.nic.in/naaqs/" },
    @{ File = "cpcb_air_pollution_control.html"; Url = "https://cpcb.nic.in/air-pollution-control/" },
    @{ File = "who_ambient_air_quality.html"; Url = "https://www.who.int/news-room/fact-sheets/detail/ambient-(outdoor)-air-quality-and-health" },
    @{ File = "who_air_pollution_topics.html"; Url = "https://www.who.int/health-topics/air-pollution" },
    @{ File = "epa_pm_basics.html"; Url = "https://www.epa.gov/pm-pollution/particulate-matter-pm-basics" },
    @{ File = "epa_no2_basics.html"; Url = "https://www.epa.gov/no2-pollution/basic-information-about-no2" },
    @{ File = "epa_so2_basics.html"; Url = "https://www.epa.gov/so2-pollution/sulfur-dioxide-basics" },
    @{ File = "epa_co_basics.html"; Url = "https://www.epa.gov/co-pollution/basic-information-about-carbon-monoxide-co-outdoor-air-pollution" },
    @{ File = "epa_ozone_basics.html"; Url = "https://www.epa.gov/ground-level-ozone-pollution/ground-level-ozone-basics" },
    @{ File = "unep_air_topics.html"; Url = "https://www.unep.org/explore-topics/air" },
    @{ File = "unep_transport_topics.html"; Url = "https://www.unep.org/explore-topics/transport" },
    @{ File = "unep_sustainable_cities.html"; Url = "https://www.unep.org/explore-topics/sustainable-cities" },
    @{ File = "sdg_goal11.html"; Url = "https://sdgs.un.org/goals/goal11" },
    @{ File = "sdg_goal13.html"; Url = "https://sdgs.un.org/goals/goal13" }
)

foreach ($source in $sources) {

    $file = Join-Path $docsDir $source.File

    Write-Host "Downloading $($source.File)..."

    try {
        Invoke-WebRequest `
            -Uri $source.Url `
            -OutFile $file `
            -UseBasicParsing

        Write-Host "SUCCESS: $($source.File)" -ForegroundColor Green
    }
    catch {
        Write-Host "FAILED: $($source.File)" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "Download process completed."
Write-Host "Files are stored in:"
Write-Host $docsDir