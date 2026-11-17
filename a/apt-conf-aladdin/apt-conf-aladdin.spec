Name: apt-conf-aladdin
Summary: Official repository of Aladdin-RD
Version: 1.0
Release: alt1

License: Public-Domain
Group: System/Base
URL: https://www.aladdin.ru/

ExclusiveArch: x86_64

Source: %name-%version.tar

Requires: apt-gpgkeys-pki

%description
%{summary}.

%prep
%setup

%install
install -Dpm0644 aladdin.list %buildroot%_sysconfdir/apt/sources.list.d/aladdin.list
install -Dpm0644 aladdin-vendors.list %buildroot%_sysconfdir/apt/vendors.list.d/aladdin.list
install -Dpm0644 aladdin.asc %buildroot%_datadir/pki/apt-gpg/sources/aladdin.asc

%files
%config(noreplace) %_sysconfdir/apt/sources.list.d/aladdin.list
%_sysconfdir/apt/vendors.list.d/aladdin.list
%_datadir/pki/apt-gpg/sources/aladdin.asc

%changelog
* Tue Nov 17 2026 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
