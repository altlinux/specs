Name: stplr-repo-aides
Version: 0.1.0
Release: alt1

Summary: Aides repository fo stplr
License: ALT-Public-Domain
Group: System/Configuration/Other
Url: https://pkgs.aides.space/

Requires: stplr

BuildArch: noarch

%description
%summary.

%post
echo "[repo]
minVersion = 'v0.0.28'
url = 'https://altlinux.space/aides-community/aides.git'
mirrors = [
    'https://git.sourcecraft.dev/aides-community/aides.git',
    'https://github.com/aides-community/aides.git',
    'https://codeberg.org/aides-community/aides.git'
]
report_url = 'https://altlinux.space/aides-pkgs/{{ .BasePackageName }}/issues'" | stplr repo import --no-pull --ignore-existing aides -

%postun
stplr repo rm aides || true

%files

%changelog
* Tue Feb 03 2026 Semen Fomchenkov <armatik@altlinux.org> 0.1.0-alt1
- Initial build.
