Name: ca-certificates-digital.gov.ru
Version: 1.0
Release: alt1

Summary: Russian Trusted Root CA
License: Distributable
Group: Other
Url: https://www.gosuslugi.ru/tls

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

%description
%summary.

%prep
%setup

%install
install -Dpm 0644 rootca_ssl_rsa2022.cer %buildroot%_datadir/pki/ca-trust-source/anchors/%name.cer

%files
%_datadir/pki/ca-trust-source/anchors/%name.cer

%changelog
* Tue Mar 15 2022 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build.
