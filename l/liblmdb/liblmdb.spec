Name: liblmdb
Version: 0.9.18
Release: alt1

Summary: Symas Lightning Memory-Mapped Database
Group: System/Libraries
Url: http://symas.com/mdb
License: LGPLv2+

Source: %name-%version.tar

Patch12: liblmdb-0.9.18-alt-deb-add-soname-fix-install.patch

%description
Lighting Memory-Mapped Database (LMDB) is an ultra-fast, ultra-compact
key-value embedded data store developed for the OpenLDAP Project. It
uses memory-mapped files, so it has the read performance of a pure
in-memory database while still offering the persistence of standard
disk-based databases, and is only limited to the size of the virtual
address space, (it is not limited to the size of physical RAM).

%package devel
Summary: %name library development package
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development library and header files needed for
developing applications with %name.

%package -n lmdb-utils
Summary: Lighting Memory-Mapped Database (LMDB) system utilities
Group: Databases
Requires: %name = %version-%release

%description -n lmdb-utils
This package provides tools for manipulating LMDB databases:
 * mdb_copy - LMDB environment copy tool
 * mdb_dump - LMDB environment export tool
 * mdb_load - LMDB environment import tool
 * mdb_stat - LMDB environment status tool

%prep
%setup -n libraries
%patch12 -p2

%build
%make_build -C %name XCFLAGS="%optflags"

%install
%makeinstall -C %name

rm %buildroot%_libdir/liblmdb.a

%check
make -C %name test

%files
%_libdir/%name.so.*

%files devel
%_includedir/lmdb.h
%_libdir/%name.so

%files -n lmdb-utils
%_bindir/mdb_*
%_man1dir/mdb_*

%changelog
* Wed Apr 27 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9.18-alt1
- Updated to 0.9.18.

* Wed Apr 09 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9.11-alt1.gitfca18d25
- Initial build.
