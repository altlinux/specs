Name: ca-certificates-espd
Version: 1.0
Release: alt1

Summary: CA Certificate for ESPD
License: Distributable
Group: Other
Url: https://espd.rt.ru/settings/cert-install

# https://espd.rt.ru/docs/ca-root.crt
Source: %name-%version.tar

BuildArch: noarch

%description
%summary.

%prep
%setup

%install
install -Dpm 0644 ca-root.crt %buildroot%_datadir/pki/ca-trust-source/anchors/espd-ca-root.crt

%files
%_datadir/pki/ca-trust-source/anchors/*.crt

%changelog
* Tue Sep 16 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build.
