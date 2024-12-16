Name: apt-conf-netpolice
Summary: Official repository of Netpolice applications for ALT
Version: 1.0
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
* Wed Oct 02 2024 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
