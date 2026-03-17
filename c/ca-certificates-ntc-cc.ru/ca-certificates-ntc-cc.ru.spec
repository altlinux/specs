Name: ca-certificates-ntc-cc.ru
Version: 1.0
Release: alt1

Summary: NTC CC Root CA
License: Distributable
Group: Other
Url: https://digitalcryptography.ru/

Source: %name-%version.tar

BuildArch: noarch

%description
%summary.

%prep
%setup

%install
install -Dpm 0644 rootca-crt-2024.cer %buildroot%_datadir/pki/ca-trust-source/anchors/rootca-crt-2024.crt
install -Dpm 0644 sub.mdk-2-crt-2024.cer %buildroot%_datadir/pki/ca-trust-source/anchors/sub.mdk-2-crt-2024.crt

%files
%_datadir/pki/ca-trust-source/anchors/*.crt

%changelog
* Tue Mar 17 2026 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build.
