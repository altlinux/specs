Name: apt-conf-r7
Summary: Official repository of R7 applications for ALT
Version: 1.1
Release: alt1

License: Public-Domain
Group: System/Base
URL: https://r7-office.ru/

ExclusiveArch: x86_64

Source: %name-%version.tar

Requires: apt-https

%description
%{summary}.
Available packages: r7-office, r7organizer and R7Grafika.

%prep
%setup

%install
install -Dpm 0644 r7.list %buildroot%_sysconfdir/apt/sources.list.d/r7.list
install -Dpm 0644 r7.xml %buildroot%_datadir/app-info/xmls/r7.xml
install -Dpm 0644 icons/default64.png %buildroot%_datadir/app-info/icons/altlinux/64x64/default64.png
install -Dpm 0644 icons/R7Grafika64x64.png %buildroot%_datadir/app-info/icons/altlinux/64x64/R7Grafika.png
install -Dpm 0644 icons/r7-office64.png %buildroot%_datadir/app-info/icons/altlinux/64x64/r7-office.png
install -Dpm 0644 icons/default128.png %buildroot%_datadir/app-info/icons/altlinux/128x128/default128.png
install -Dpm 0644 icons/R7Grafika128x128.png %buildroot%_datadir/app-info/icons/altlinux/128x128/R7Grafika.png
install -Dpm 0644 icons/r7-office128.png %buildroot%_datadir/app-info/icons/altlinux/128x128/r7-office.png

%files
%config(noreplace) %_sysconfdir/apt/sources.list.d/r7.list
%_datadir/app-info/xmls/*.xml
%_datadir/app-info/icons/altlinux/*/*.png

%changelog
* Tue Dec 26 2023 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- Add application descriptions and icons.

* Thu Oct 12 2023 Andrey Cherepanov <cas@altlinux.org> 1.0-alt2
- Built only for x86_64 (ALT #47967).
- Required apt-https (ALT #47968).

* Wed Oct 11 2023 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
