Name: lexmark2070
Version: 0.6
Release: alt2
License: GPL
Group: System/Configuration/Printing

URL: http://www.kornblum.i-p.com/2070/Lexmark2070.old.html
#site is dead
Source: %name-%version.tar.gz
Patch1:	Lexmark2070-LDFLAGS.patch
Patch2: Lexmark2070-ftbfs-gcc14.patch

Requires: c2070

Summary: Lexmark 2070 Printer B/W driver

%description
This filter allows to print in B/W a Lexmark 2070 (windows GDI) printer.

%prep
%setup
%patch1 -p0
%patch2 -p2

%build
make -f makefile

%install
install -d %buildroot%_bindir
install -m0755 Lexmark2070 %buildroot%_bindir/

%files
%doc README LICENSE
%_bindir/*

%changelog
* Mon Dec 02 2024 Oleg Solovyov <mcpain@altlinux.org> 0.6-alt2
- fix FTBFS with gcc14

* Tue Mar 26 2019 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1.1
- NMU: the build does not need libnetpbm-devel

* Tue May 29 2018 Oleg Solovyov <mcpain@altlinux.org> 0.6-alt1
- Initial build for ALT

