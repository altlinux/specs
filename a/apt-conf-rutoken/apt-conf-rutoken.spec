Name: apt-conf-rutoken
Summary: Official repository of Rutoken software for ALT
Version: 2.0
Release: alt1

License: Public-Domain
Group: System/Base
URL: https://www.rutoken.ru/

ExclusiveArch: %ix86 x86_64 aarch64

Source: %name-%version.tar

Requires: apt-https
Requires: apt-gpgkeys-pki

%description
%{summary}.

Available packages: libnpRutokenPlugin, librtengine1, librtpkcs11ecp and
rtcontrolcenter.

%prep
%setup
%ifarch %ix86
echo "rpm [rutoken] https://repo.rutoken.ru alt/stable/i586 classic" > rutoken.list
%endif
%ifarch x86_64
echo "rpm [rutoken] https://repo.rutoken.ru alt/stable/x86_64 classic" > rutoken.list
%endif
%ifarch aarch64
echo "rpm [rutoken] https://repo.rutoken.ru alt/stable/aarch64 classic" > rutoken.list
%endif

%install
install -Dpm 0644 rutoken.list %buildroot%_sysconfdir/apt/sources.list.d/rutoken.list
install -Dpm0644 rutoken-vendors.list %buildroot%_sysconfdir/apt/vendors.list.d/rutoken.list
install -Dpm0644 rutoken.asc %buildroot%_datadir/pki/apt-gpg/sources/rutoken.asc

%files
%config(noreplace) %_sysconfdir/apt/sources.list.d/rutoken.list
%_sysconfdir/apt/vendors.list.d/rutoken.list
%_datadir/pki/apt-gpg/sources/rutoken.asc

%changelog
* Thu Nov 12 2026 Andrey Cherepanov <cas@altlinux.org> 2.0-alt1
- Used signed repository.

* Wed Nov 27 2024 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
