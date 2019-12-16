Name: uvncrepeater-ac
%define unitname uvncrepeater-ac.service
Version: 1.0.0
Release: alt1

Source: %name-%version.tar

Summary: VNC repeater based on ultravnc repeater
Url: https://github.com/tenchman/uvncrepeater-ac
License: GPL-2.0-or-later
Group: Networking/Remote access

BuildRequires: gcc

%description
Ansi-C Version of uvncrepeater V14

Changes:
* removed C++ compiler dependency
* compilable with 'any?' Ansi-C compiler (tested with gcc, clang, tcc)
* IPv6 support
* support CIDR addresses in server lists

Uvncrepeater V14 is Jari Korhonen's Linux port of Ultravnc repeater source code.

%prep
%setup

%build
%make

%install
%makeinstall
install -pDm644 systemd/%unitname %buildroot%_unitdir/%unitname

%files
%_sysconfdir/uvnc/uvncrepeater-ac.ini
%_bindir/uvncrepeater-ac
%_unitdir/%unitname

%changelog
* Mon Dec 16 2019 Grigory Maksimov <zacat@altlinux.org> 1.0.0-alt1
- Initial build for ALT

