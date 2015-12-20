Name:       insserv
Version:    1.16.0
Release:    alt2

Summary:    Tool for process controlling in System V boot scripts 
License:    GPLv2+
Group:      System/Configuration/Boot and Init
URL:        http://savannah.nongnu.org/projects/sysvinit

Packager:   Andrey Cherepanov <cas@altlinux.org>

Source0:    %name-%version.tar.bz2

Patch:      %name-build-with-gcc5.patch

BuildRequires: libdbus-devel
BuildRequires: /proc

%description
This small package provides a tool for process controlling
in System V boot scripts.

%prep
%setup
%patch -p2

%build
%make_build

%install
%makeinstall_std
rm -f %buildroot/lib/lsb/init-functions
rm -f %buildroot%_libexecdir/lsb/*_initd

%files
%config(noreplace) %_sysconfdir/%name.conf
/sbin/%name
%_man8dir/%name.8.*

%changelog
* Mon Dec 21 2015 Andrey Cherepanov <cas@altlinux.org> 1.16.0-alt2
- Do not use strict extension for man pages

* Sun Jun 14 2015 Andrey Cherepanov <cas@altlinux.org> 1.16.0-alt1
- New version
- Fix build with GCC 5

* Fri Feb 15 2013 Andrey Cherepanov <cas@altlinux.org> 1.14.0-alt2
- Remove conflct files

* Thu Feb 14 2013 Andrey Cherepanov <cas@altlinux.org> 1.14.0-alt1
- Initial import to ALT Linux

