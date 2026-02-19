Name: stplr-repo-aides
Version: 0.1.0
Release: alt2

Summary: Aides repository fo stplr
License: ALT-Public-Domain
Group: System/Configuration/Other
Url: https://pkgs.aides.space/

Requires: stplr
Requires(post,postun): stplr

BuildArch: noarch

%description
%summary.

%post
echo "[repo]
minVersion = 'v0.0.29'
url = 'https://altlinux.space/aides-community/aides.git'
mirrors = [
    'https://git.sourcecraft.dev/aides-community/aides.git',
    'https://github.com/aides-community/aides.git',
    'https://codeberg.org/aides-community/aides.git'
]
report_url = 'https://altlinux.space/aides-pkgs/{{ .BasePackageName }}/issues'

title = 'Aides'
homepage = 'https://aides.space'
icon = 'https://aides.space/logo.svg'" | stplr repo import --no-pull --ignore-existing aides - || true

%postun
stplr repo rm aides || true

%files

%changelog
* Wed Feb 18 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.1.0-alt2
- Sync repo config with upstream.
- Add Requires(post,postun): stplr to guarantee stplr is installed before %%post and 
  removed after %%postun scripts run (closes #57933).

* Tue Feb 03 2026 Semen Fomchenkov <armatik@altlinux.org> 0.1.0-alt1
- Initial build.
