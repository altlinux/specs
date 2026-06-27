Name: libcddb
Version: 1.3.2
Release: alt6.1

Summary: Libcddb is a C library to access data on a CDDB server
License: LGPL-2.0-or-later
Group: System/Libraries
Url: https://libcddb.sourceforge.net/

Source: https://prdownloads.sourceforge.net/libcddb/libcddb-%version.tar.bz2
Patch: libcddb-1.3.2-arch-pointer-types.patch

# Automatically added by buildreq on Mon Nov 23 2009
BuildRequires: libcdio-devel

%description
Libcddb is a C library to access data on a CDDB server (freedb.org). It allows to:
1. search the database for possible CD matches
2. retrieve detailed information about a specific CD
3. submit new CD entries to the database

%package devel
Summary: Headers for developing programs that will use %name
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains the headers that programmers will need to develop
applications which will use %name.

%package examples
Summary: Simple application that use %name
Group: Development/C
Requires: %name = %EVR

%description examples
This package contains the cddb_query is a simple app that use %name.

%prep
%setup
%patch -p1

%build
%autoreconf -I %_datadir/gettext/m4
%configure --disable-static

%make_build

%install
%makeinstall_std

%make -C examples clean

%files
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%doc NEWS README

%files examples
%_bindir/*
%doc examples

%changelog
* Sat Jun 27 2026 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt6.1
- fixed build with gettext-1.0

* Sat Dec 21 2024 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt6
- fixed build with gcc-14

* Fri Jan 12 2018 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt5
- rebuilt against libcdio.so.18

* Mon Jul 20 2015 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt4
- rebuilt against libcdio.so.16

* Mon Apr 25 2011 Dmitry V. Levin <ldv@altlinux.org> 1.3.2-alt3
- Fixed rpath issue.
- Rebuilt for debuginfo.

* Wed Nov 10 2010 Victor Forsiuk <force@altlinux.org> 1.3.2-alt2
- Rebuilt for soname set-versions.

* Mon Nov 23 2009 Victor Forsyuk <force@altlinux.org> 1.3.2-alt1
- 1.3.2
- Buildreq'ed, spec cleaned up, correct license.

* Sun Nov 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.3.0-alt2.2
- rebuild with new libcdio

* Wed Aug 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.3.0-alt2.1
- rebuild with new libcdio

* Fri Sep 26 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.3.0-alt2
- Cleanup BuildRequires.

* Thu Oct 19 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.3.0-alt1
- 1.3.0 release.

* Wed May 31 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.1-alt1.1
- Rebuild with libcdio.so.7 .

* Wed Nov 30 2005 Pavlov Konstantin <thresh@altlinux.ru> 1.2.1-alt1
- 1.2.1 release.

* Thu Feb 12 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.9.4-alt2
- do not build devel-static subpackage by default.
- subpackage with examples.
- restored changelog from orphaned package.

* Thu Jun 5 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.9.4-alt1
- 0.9.4

* Mon May 19 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.9.3-alt1
- 0.9.3

* Fri Apr 25 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Mon Apr 21 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.9.1-alt1
- First version of RPM package.
