Name: ca-certificates-tlscc.ru
Version: 1.0
Release: alt1

Summary: TCI Root CA
License: Distributable
Group: Other
Url: https://tlscc.ru/

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

%description
%summary.

%prep
%setup

%install
install -Dpm 0644 ecdsa-a1.crt %buildroot%_datadir/pki/ca-trust-source/anchors/ecdsa-a1.crt
install -Dpm 0644 gost-a1.crt  %buildroot%_datadir/pki/ca-trust-source/anchors/gost-a1.crt

%files
%_datadir/pki/ca-trust-source/anchors/*.crt

%changelog
* Thu Jul 11 2024 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build.
