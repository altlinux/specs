Name: qtmib
Version: 1.1.1
Release: alt1
License: GPLv2
Group: Networking/Other
Summary: SNMP MIB Browser for Linux platforms 
Url: http://sourceforge.net/projects/qtmib
Source0: %name-%version.tar
Patch0: qtmib-1.1.1-dont_strip.patch

BuildRequires: libqt4-devel gcc-c++

%description
qtmib is an easy-to-use SNMP MIB Browser based on QT4 library. It is
build as a front-end for net-snmp tools, and it allows the user to
query any SNMP enabled device. It supports SNMPv1 and SNMPv2c. qtmib
is released under GPL v2 license.

%prep
%setup
%patch0 -p0

%build
export QTDIR=%_qt4dir
export PATH=%_qt4dir/bin:$PATH
%configure
make

%install
%makeinstall_std

%files
%_bindir/%{name}*
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_man1dir/%{name}*
%doc README RELNOTES

%changelog
* Fri Dec 19 2014 Terechkov Evgenii <evg@altlinux.org> 1.1.1-alt1
- New upstream version

* Sat Sep 27 2014 Terechkov Evgenii <evg@altlinux.org> 1.1-alt1
- New upstream version

* Sat Aug 23 2014 Terechkov Evgenii <evg@altlinux.org> 1.0-alt3
- Build with debuginfo

* Sat Aug 23 2014 Terechkov Evgenii <evg@altlinux.org> 1.0-alt2
- Fix build in git.alt

* Fri Aug 22 2014 Terechkov Evgenii <evg@altlinux.org> 1.0-alt1
- Initial build for ALT Linux sisyphus

