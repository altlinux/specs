Name: apt-conf-max
Summary: Official repository of MAX
Version: 1.0
Release: alt2

License: Public-Domain
Group: System/Base
URL: https://www.max.ru/

ExclusiveArch: x86_64

Source: %name-%version.tar

Requires: apt-https
Requires: apt-gpgkeys-pki
Requires: libxcbutil-cursor

%description
%{summary}.

%prep
%setup

%install
install -Dpm0644 max.list %buildroot%_sysconfdir/apt/sources.list.d/max.list
install -Dpm0644 max-vendors.list %buildroot%_sysconfdir/apt/vendors.list.d/max.list
install -Dpm0644 max.asc %buildroot%_datadir/pki/apt-gpg/sources/max.asc

%files
%config(noreplace) %_sysconfdir/apt/sources.list.d/max.list
%_sysconfdir/apt/vendors.list.d/max.list
%_datadir/pki/apt-gpg/sources/max.asc

%changelog
* Wed Apr 08 2026 Andrey Cherepanov <cas@altlinux.org> 1.0-alt2
- Required libxcbutil-cursor for max (ALT #58582).

* Tue Jan 27 2026 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
