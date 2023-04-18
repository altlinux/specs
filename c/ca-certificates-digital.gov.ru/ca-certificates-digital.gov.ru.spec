Name: ca-certificates-digital.gov.ru
Version: 1.1
Release: alt1

Summary: Russian Trusted Root CA
License: Distributable
Group: Other
Url: https://www.gosuslugi.ru/crt

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

%description
%summary.

%prep
%setup

%install
install -Dpm 0644 russian_trusted_root_ca_pem.crt %buildroot%_datadir/pki/ca-trust-source/anchors/russian_trusted_root_ca_pem.cer
install -Dpm 0644 russian_trusted_sub_ca_pem.crt  %buildroot%_datadir/pki/ca-trust-source/anchors/russian_trusted_sub_ca_pem.cer

%files
%_datadir/pki/ca-trust-source/anchors/*.cer

%changelog
* Tue Apr 18 2023 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- Packaged certificates (root and sub) from https://www.gosuslugi.ru/crt.

* Tue Mar 15 2022 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build.
