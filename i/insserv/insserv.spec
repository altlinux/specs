Name: insserv
Version: 1.24.0
Release: alt1

Summary: Tool for process controlling in System V boot scripts 
License: GPL-2.0+
Group: System/Configuration/Boot and Init
URL: http://savannah.nongnu.org/projects/sysvinit

Source0: %name-%version.tar.bz2

BuildRequires: libdbus-devel
BuildRequires: /proc

%description
This small package provides a tool for process controlling
in System V boot scripts.

%prep
%setup

%build
%add_optflags -std=gnu17
%ifarch %ix86
%add_optflags -no-pie
%endif
%make_build

%install
%makeinstall_std
rm -f %buildroot/lib/lsb/init-functions
rm -f %buildroot%_libexecdir/lsb/*_initd

%files
%config(noreplace) %_sysconfdir/%name.conf
%_sbindir/%name
%_man8dir/%name.8.*

%changelog
* Wed Jun 03 2026 Andrey Cherepanov <cas@altlinux.org> 1.24.0-alt1
- New version.

* Fri Apr 23 2021 Slava Aseev <ptrnine@altlinux.org> 1.16.0-alt3
- Fix build on ix86 due to --enable-default-pie

* Mon Dec 21 2015 Andrey Cherepanov <cas@altlinux.org> 1.16.0-alt2
- Do not use strict extension for man pages

* Sun Jun 14 2015 Andrey Cherepanov <cas@altlinux.org> 1.16.0-alt1
- New version
- Fix build with GCC 5

* Fri Feb 15 2013 Andrey Cherepanov <cas@altlinux.org> 1.14.0-alt2
- Remove conflct files

* Thu Feb 14 2013 Andrey Cherepanov <cas@altlinux.org> 1.14.0-alt1
- Initial import to ALT Linux

