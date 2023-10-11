Name: apt-conf-r7
Summary: Official repository of R7 applications for ALT
Version: 1.0
Release: alt1

License: Public-Domain
Group: System/Base
URL: https://r7-office.ru/

BuildArch: noarch

Source: r7.list

%description
%{summary}.
Available packages: r7-office, r7organizer and R7Grafika.

%install
install -Dpm 0644 %SOURCE0 %buildroot%_sysconfdir/apt/sources.list.d/r7.list

%files
%config(noreplace) %_sysconfdir/apt/sources.list.d/r7.list

%changelog
* Wed Oct 11 2023 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
