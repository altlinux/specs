Name: ca-certificates-digital.gov.ru
Version: 1.2
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
install -Dpm 0644 russian_trusted_sub_ca_2024_pem.crt %buildroot%_datadir/pki/ca-trust-source/anchors/russian_trusted_sub_ca_2024_pem.cer
install -Dpm 0644 rootca_ssl_rsa2022.crt %buildroot%_datadir/pki/ca-trust-source/anchors/rootca_ssl_rsa2022.cer

%files
%_datadir/pki/ca-trust-source/anchors/*.cer

%changelog
* Tue May 20 2025 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1
- Added russian_trusted_sub_ca_2024_pem.crt and rootca_ssl_rsa2022.crt.

* Tue Apr 18 2023 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- Packaged certificates (root and sub) from https://www.gosuslugi.ru/crt.

* Tue Mar 15 2022 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build.
