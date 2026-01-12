Name: apt-conf-netpolice
Summary: Official repository of Netpolice applications for ALT
Version: 1.0.1
Release: alt1

License: Public-Domain
Group: System/Base
URL: https://www.netpolice.ru/page/getnetpolicelinux

ExclusiveArch: x86_64

Source: %name-%version.tar

%description
%{summary}.
Available packages: NetPoliceAltLinux

%prep
%setup

%install
install -Dpm 0644 netpolice.list %buildroot%_sysconfdir/apt/sources.list.d/netpolice.list

%files
%config(noreplace) %_sysconfdir/apt/sources.list.d/netpolice.list

%changelog
* Mon Jan 12 2026 Ajrat Makhmutov <rauty@altlinux.org> 1.0.1-alt1
- Update from p10 to p11 branch.

* Wed Oct 02 2024 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
