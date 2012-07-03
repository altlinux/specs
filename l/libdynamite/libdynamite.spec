%def_disable static

Name: libdynamite
Version: 0.1.1
Release: alt2

Summary: Extract data compressed with PKWARE Data Compression Library
License: MIT
Group: Archiving/Compression

Url: http://synce.sourceforge.net
Source: %name-%version.tar.gz

Packager: Mobile Development Team <mobile@packages.altlinux.org>

%if_enabled static
BuildRequires: glibc-devel-static
%endif

%description
See http://synce.sourceforge.net for more information.

%package devel
Summary: Extract data compressed with PKWARE Data Compression Library
Group: Development/C
Requires: %name = %version

%description devel
See http://synce.sourceforge.net for more information.

%if_enabled static
%package devel-static
Summary: Extract data compressed with PKWARE Data Compression Library
Group: Development/C
Requires: %name-devel = %version

%description devel-static
See http://synce.sourceforge.net for more information.
%endif

%prep
%setup

%build
%autoreconf
%configure %{subst_enable static}
%make

%install
%makeinstall

%files
%doc LICENSE ChangeLog
%_bindir/dynamite
%_libdir/libdynamite.so.*
%_man1dir/*

%files devel
%_includedir/libdynamite.h
%_libdir/libdynamite.so
%_libdir/pkgconfig/*.pc

%if_enabled static
%files devel-static
%_libdir/libdynamite.a
#_libdir/libdynamite.la
%endif

%changelog
* Wed Dec 21 2011 Michael Shigorin <mike@altlinux.org> 0.1.1-alt2
- drop RPATH

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1.qa2
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Thu Nov 19 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.1.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libdynamite
  * postun_ldconfig for libdynamite
  * postclean-05-filetriggers for spec file

* Sat Oct 04 2008 Alexey Shabalin <shaba@altlinux.ru> 0.1.1-alt1
- 0.1.1

* Sat Dec 08 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.1-alt2
- update to SVN 20071207 version

* Fri Sep 03 2004 Michael Shigorin <mike@altlinux.ru> 0.1-alt1
- built for ALT Linux (synce-kde dependency)

