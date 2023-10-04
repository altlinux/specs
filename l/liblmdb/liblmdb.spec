%define _unpackaged_files_terminate_build 1
%def_with check

Name: liblmdb
Version: 0.9.31
Release: alt1

Summary: Symas Lightning Memory-Mapped Database
Group: System/Libraries
Url: https://symas.com/lmdb
License: OLDAP-2.8
# branch mdb.RE/0.9
Vcs: https://git.openldap.org/openldap/openldap.git
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
* Wed Oct 04 2023 Alexey Shabalin <shaba@altlinux.org> 0.9.31-alt1
- Updated to 0.9.31.

* Tue Sep 13 2022 Alexey Shabalin <shaba@altlinux.org> 0.9.29-alt1.1
- Build to sisyphus.

* Thu Sep 02 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.9.29-alt1
- Updated to 0.9.29.

* Thu Jul 29 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.9.28-alt1
- Updated to 0.9.28 with backported refixes from Engineering.

* Thu Oct 31 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.9.24-alt1
- Updated to 0.9.24.

* Tue Mar 19 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.9.23-alt1
- Updated to 0.9.23.

* Mon Jul 23 2018 Stanislav Levin <slev@altlinux.org> 0.9.22-alt1
- 0.9.18 -> 0.9.22

* Wed Apr 27 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9.18-alt1
- Updated to 0.9.18.

* Wed Apr 09 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9.11-alt1.gitfca18d25
- Initial build.
