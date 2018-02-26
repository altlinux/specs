Name: sqlite
Version: 2.8.17
Release: alt2.2

Summary: An Embeddable SQL Database Engine, version 2
License: Public Domain
Group: Development/Databases

URL: http://www.sqlite.org
Source: sqlite-%version.tar.gz
Patch0: sqlite-2.8.17-cvs20070108.patch
Patch1: sqlite-2.8.17-CVE-2007-1888.patch
Patch2: sqlite-2.8.17-alt-libdir.patch
Patch3: sqlite-2.8.17-alt-tcl.patch
Patch4: sqlite-2.8.17-alt-sort+4.patch

Requires: lib%name = %version-%release

# Automatically added by buildreq on Mon Feb 14 2011
BuildRequires: libncurses-devel libreadline-devel tcl-devel

%package -n lib%name
Summary: An Embeddable SQL Database Engine, version 2 (shared library)
Group: System/Libraries
Conflicts: %name < %version

%package -n lib%name-devel
Summary: An Embeddable SQL Database Engine, version 2 (header files)
Group: Development/Databases
Requires: lib%name = %version-%release
Provides: %name-devel = %version
Obsoletes: %name-devel < %version

%package -n lib%name-devel-static
Summary: An Embeddable SQL Database Engine, version 2 (static library)
Group: Development/Databases
Requires: lib%name-devel = %version-%release
Provides: %name-devel-static = %version
Obsoletes: %name-devel-static < %version

%package tcl
Summary: An Embeddable SQL Database Engine, version 2 (Tcl bindings)
Group: Development/Tcl
Requires: lib%name = %version-%release

%package doc
Summary: An Embeddable SQL Database Engine, version 2 (documentation)
Group: Development/Documentation
Conflicts: %name < %version
Buildarch: noarch

%description
SQLite is a C library that implements an SQL database engine.
Programs that link with the SQLite library can have SQL database
access without running a separate RDBMS process.

%description -n lib%name
SQLite is a C library that implements an SQL database engine.
Programs that link with the SQLite library can have SQL database
access without running a separate RDBMS process.

%description -n lib%name-devel
SQLite is a C library that implements an SQL database engine.
Programs that link with the SQLite library can have SQL database
access without running a separate RDBMS process.

%description -n lib%name-devel-static
SQLite is a C library that implements an SQL database engine.
Programs that link with the SQLite library can have SQL database
access without running a separate RDBMS process.

%description tcl
SQLite is a C library that implements an SQL database engine.
Programs that link with the SQLite library can have SQL database
access without running a separate RDBMS process.

%description doc
SQLite is a C library that implements an SQL database engine.
Programs that link with the SQLite library can have SQL database
access without running a separate RDBMS process.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# lemon is now in sqlite3
rm doc/lemon.html

%build
autoreconf -fisv
%configure --enable-utf8 --enable-tempdb-in-ram
%make_build all doc
%make_build libtcl%name.la tcllibdir=%_tcllibdir

%install
%makeinstall_std
install -pD -m644 %name.1 %buildroot%_man1dir/%name.1

mkdir -p %buildroot%_tcllibdir %buildroot%_tcldatadir/%name
./libtool --mode=install install -p libtcl%name.la %buildroot%_tcllibdir/

dll=$(relative %_tcllibdir/libtcl%name.so %_tcldatadir/%name/pkgIndex.tcl)
echo "package ifneeded sqlite 2.0 [list load [file join \$dir $dll]]" \
	>%buildroot%_tcldatadir/%name/pkgIndex.tcl

%define pkgdocdir %_docdir/sqlite-2.8
mkdir -p %buildroot%pkgdocdir
install -p -m644 doc/*.* %buildroot%pkgdocdir/

%files
%_bindir/%name
%_man1dir/%name.*

%files -n lib%name
%_libdir/lib%name.so.?*

%files -n lib%name-devel
%_includedir/%name.h
%_libdir/lib%name.so
#_libdir/lib%name.la
%_pkgconfigdir/%name.pc

%files -n lib%name-devel-static
%_libdir/lib%name.a

%files tcl
%_tcllibdir/libtcl%name.so*
#_tcllibdir/libtcl%name.a
#_tcllibdir/libtcl%name.la
%dir %_tcldatadir/%name
%_tcldatadir/%name/pkgIndex.tcl

%files doc
%dir %pkgdocdir
%pkgdocdir/*.*

%changelog
* Mon Feb 14 2011 Alexey Tourbin <at@altlinux.ru> 2.8.17-alt2.2
- rebuilt for debuginfo
- made sqlite-doc noarch

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 2.8.17-alt2.1
- rebuild (with the help of girar-nmu utility)

* Fri Dec 12 2008 Denis Smirnov <mithraen@altlinux.ru> 2.8.17-alt2
- remove post_ldconfig/postun_ldconfig
- cleanup spec

* Wed Mar 26 2008 Alexey Tourbin <at@altlinux.ru> 2.8.17-alt1
- 2.8.16 -> 2.8.17+cvs20070108
- fix for buffer overflow in sqlite_decode_binary (CVE-2007-1888)
- split package sqlite-doc, renamed sqlite-devel to libsqlite-devel
- built with tcl 8.5

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 2.8.16-alt1.1.0
- Automated rebuild.

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.8.16-alt1.1
- Rebuilt with libreadline.so.5.

* Sat Mar 12 2005 Denis Smirnov <mithraen@altlinux.ru> 2.8.16-alt1
- version update

* Thu Feb 10 2005 Denis Smirnov <mithraen@altlinux.ru> 2.8.15-alt2
- fix version in sqlite.pc

* Fri Feb 04 2005 Denis Smirnov <mithraen@altlinux.ru> 2.8.15-alt1
- version update
- build requires rpm-build-tcl

* Sat Sep 04 2004 Denis Smirnov <mithraen@altlinux.ru> 2.8.13-alt5
- x86_64 build fixed

* Fri Jun 04 2004 Denis Smirnov <mithraen@altlinux.ru> 2.8.13-alt4
- Rebuild

* Thu Jun 03 2004 Denis Smirnov <mithraen@altlinux.ru> 2.8.13-alt2
- Fix for correcting update

* Mon May 31 2004 Denis Smirnov <mithraen@altlinux.ru> 2.8.13-alt1
- Some minor packaging fixes
- Tcl binding bugfix

* Sun Apr 11 2004 Denis Smirnov <mithraen@altlinux.ru> 2.8.5-alt3
- Tcl binding build

* Sat Dec 13 2003 Ott Alex <ott@altlinux.ru> 2.8.5-alt2
- Remove .la files

* Sun Jul 27 2003 Ott Alex <ott@altlinux.ru> 2.8.5-alt1
- New version

* Tue Jul 22 2003 Ott Alex <ott@altlinux.ru> 2.8.4-alt1
- Initial build
