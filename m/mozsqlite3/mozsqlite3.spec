Name: mozsqlite3
Version: 3.6.19
Release: alt1

Summary: An Embeddable SQL Database Engine (Mozilla clone)
License: Public Domain
Group: Development/Databases

Packager: Alexey Gladkov <legion@altlinux.ru>

URL: http://www.sqlite.org/

Source0: mozsqlite3.tar
Patch0: mozsqlite3-change-name.patch
Patch1: 02-lemon-snprintf.patch

# Automatically added by buildreq on Tue Mar 10 2009
BuildRequires: gcc-c++ glibc-devel-static tcl

%package -n lib%name
Summary: An Embeddable SQL Database Engine (shared library)
Group: System/Libraries

%package -n lib%name-devel
Summary: An Embeddable SQL Database Engine (header files)
Group: Development/Databases
Requires: lib%name = %version-%release

%package -n lib%name-devel-static
Summary: An Embeddable SQL Database Engine (static library)
Group: Development/Databases
Requires: lib%name-devel = %version-%release

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

%prep
%setup -q -n %name
%patch0 -p1
%patch1 -p1

rm aclocal.m4 config.guess config.sub configure ltmain.sh

%build
export LDFLAGS=-ldl

# -DSQLITE_SECURE_DELETE=1 will cause SQLITE to 0-fill delete data so we
# don't have to vacuum to make sure the data is not visible in the file.
# -DSQLITE_ENABLE_FTS3=1 enables the full-text index module.
# -DSQLITE_CORE=1 statically links that module into the SQLite library.
export CFLAGS=" \
	-DSQLITE_THREADSAFE=1 \
	-DSQLITE_ENABLE_FTS3=1 \
	-DSQLITE_SECURE_DELETE=1 \
	-DSQLITE_CORE=1 \
	"
%autoreconf
%configure \
	--includedir=%_includedir/%name \
	--enable-threadsafe \
	--disable-amalgamation \
	--enable-load-extension \
	#
%make_build all

%install
%make_install install DESTDIR=%buildroot
rm -rf -- %buildroot/%_bindir
mv -f -- \
	%buildroot/%_pkgconfigdir/sqlite3.pc \
	%buildroot/%_pkgconfigdir/%name.pc

%files -n lib%name
%_libdir/lib%name.so.?*

%files -n lib%name-devel
%_includedir/%name/sqlite3.h
%_includedir/%name/sqlite3ext.h
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%files -n lib%name-devel-static
%_libdir/lib%name.a

%changelog
* Mon Oct 19 2009 Alexey Gladkov <legion@altlinux.ru> 3.6.19-alt1
- New version (3.6.19).

* Fri Sep 18 2009 Alexey Gladkov <legion@altlinux.ru> 3.6.18-alt1
- New version (3.6.18).

* Mon Aug 31 2009 Alexey Gladkov <legion@altlinux.ru> 3.6.17-alt1
- New version (3.6.17).

* Mon Jun 29 2009 Alexey Gladkov <legion@altlinux.ru> 3.6.16-alt1
- New version (3.6.16).

* Thu Jun 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 3.6.15-alt1
- New version (3.6.15).

* Mon Jun 01 2009 Alexey Gladkov <legion@altlinux.ru> 3.6.14.2-alt1
- New version (3.6.14.2).

* Mon Mar 09 2009 Alexey Gladkov <legion@altlinux.ru> 3.6.11-alt1
- Initial build
