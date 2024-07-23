%define _unpackaged_files_terminate_build 1
%define soname 0

Name: libcowsql
Version: 1.15.6
Release: alt2
Summary: Library for distributed SQLite database

License: LGPLv3
Group: Development/Databases
Conflicts: libdqlite

URL: https://github.com/cowsql/cowsql
Source: %name-%version.tar

BuildRequires: libuv-devel >= 1.8.0
BuildRequires: libraft-devel >= 0.18.0
BuildRequires: libsqlite3-devel >= 3.22.0

%description
This package is a C library that implements an embeddable
and replicated SQL database engine with high availability
and automatic failover. Cowsql extends SQLite with a network
protocol that can connect together various instances of your
application and have them act as a highly-available cluster,
with no dependency on external databases.

%package -n %name%soname
Summary: Library for distributed SQLite databases
Group: Development/Databases

%description -n %name%soname
This package is a C library that implements an embeddable
and replicated SQL database engine with high availability
and automatic failover. Cowsql extends SQLite with a network
protocol that can connect together various instances of your
application and have them act as a highly-available cluster,
with no dependency on external databases.

%package devel
Summary: Library for distributed SQLite database (development files)
Group: Development/Databases
Conflicts: libdqlite-devel
Requires: %name%soname = %EVR

%description devel
This package is a C library that implements an embeddable
and replicated SQL database engine with high availability
and automatic failover. Cowsql extends SQLite with a network
protocol that can connect together various instances of your
application and have them act as a highly-available cluster,
with no dependency on external databases.

%prep
%setup

%build
%autoreconf
%configure --enable-replication --disable-static

%make_build all

%install
%makeinstall_std

%files -n %name%soname
%doc AUTHORS README.md LICENSE
%_libdir/*.so.%soname.*
%_libdir/*.so.%soname

%files devel
%_includedir/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Wed Jul 10 2024 Nadezhda Fedorova <fedor@altlinux.org> 1.15.6-alt2
- Fix libpackaging without provides. 

* Mon May 06 2024 Nadezhda Fedorova <fedor@altlinux.org> 1.15.6-alt1
- Initial version.
