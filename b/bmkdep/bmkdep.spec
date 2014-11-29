Summary: NetBSD version of mkdep(1)
Name: bmkdep
Version: 20140112
Release: alt4
License: 2-clause BSD
Group: Development/Tools
URL: http://code.google.com/p/bmkdep/
Packager: Aleksey Cheusov <cheusov@altlinux.org>

Source0: http://bmkdep.googlecode.com/files/bmkdep-%{version}.tar.gz

BuildRequires: bmake

%description
This is NetBSD version of mkdep(1).
Because it is a C program and does all postprocessing and file
handling without calling any external programs, it is up to 10-percent
faster than the original BSD mkdep shell script. Also it contains
options not available in the original BSD mkdep.

%prep
%setup

%define env \
  unset MAKEFLAGS; \
  export BINOWN=`id -u` BINGRP=`id -g` \
    MANOWN=${BINOWN} MANGRP=${BINGRP} \
    MKHTML=no MKCATPAGES=no \
    PREFIX=%prefix \
    MANDIR=%_mandir \
    CFLAGS=-O2

%build
%env
bmake bmkdep

%install
%env
install -pDm644 bmkdep.1 %buildroot%_man1dir/bmkdep.1
install -pDm755 bmkdep %buildroot%_bindir/bmkdep

%files
%doc %{_mandir}/man1/bmkdep.1*
%{_bindir}/bmkdep

%changelog
* Thu Nov 29 2014 Aleksey Cheusov <cheusov@altlinux.org> 20140112-alt4
- Make hasher(1) happy

* Thu Nov 27 2014 Aleksey Cheusov <cheusov@altlinux.org> 20140112-alt3
- Fix .gear/rules

* Thu Nov 27 2014 Aleksey Cheusov <cheusov@altlinux.org> 20140112-alt2
- Adapted for gear.

* Thu Nov 27 2014 Aleksey Cheusov <cheusov@altlinux.org> 20140112-alt1
- Initial version for AltLinux.
