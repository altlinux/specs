%define pg_ver 14

Name: postgresql%pg_ver-timescaledb
Version: 2.8.1
Release: alt1
Summary: Open-source time-series database powered by PostgreSQL
Group: Databases
License: Apache-2.0 and Timescale License
Url: http://www.timescale.com
Source0: %name-%version.tar

BuildRequires: cmake
BuildRequires: libssl-devel libkrb5-devel
BuildRequires: postgresql%pg_ver-server-devel

Requires: postgresql%pg_ver-server

%description
TimescaleDB is an open-source database designed to make SQL scalable for
time-series data.  It is engineered up from PostgreSQL, providing automatic
partitioning across time and space (partitioning key), as well as full SQL
support.

%prep
%setup

%build
%cmake \
    -DUSE_OPENSSL=ON \
    -DSEND_TELEMETRY_DEFAULT=OFF \
    -DREGRESS_CHECKS=OFF \
    -DAPACHE_ONLY=OFF \
    -DPG_CONFIG=%_bindir/pg_config

%cmake_build

%install
%cmakeinstall_std

%post
echo "Execute the following psql command inside any database that you want to update:"
echo "ALTER EXTENSION timescaledb UPDATE;                                            "

%files
%doc README.md LICENSE LICENSE-APACHE
%_libdir/pgsql/*
%_datadir/pgsql/extension/*

%changelog
* Mon Nov 07 2022 Alexei Takaseev <taf@altlinux.org> 2.8.1-alt1
- 2.8.1

* Tue Jul 26 2022 Alexei Takaseev <taf@altlinux.org> 2.7.2-alt1
- 2.7.2

* Wed May 25 2022 Alexei Takaseev <taf@altlinux.org> 2.7.0-alt1
- 2.7.0

* Tue Apr 12 2022 Alexei Takaseev <taf@altlinux.org> 2.6.1-alt1
- 2.6.1

* Tue Feb 22 2022 Alexei Takaseev <taf@altlinux.org> 2.6.0-alt3
- Add BR: libkrb5-devel

* Mon Feb 21 2022 Alexei Takaseev <taf@altlinux.org> 2.6.0-alt2
- Rename to postgresql%pg_ver-%name
- Build with TSL extentions

* Sat Feb 19 2022 Alexei Takaseev <taf@altlinux.org> 2.6.0-alt1
- 2.6.0

* Mon Feb 08 2021 Alexey Shabalin <shaba@altlinux.org> 2.0.1-alt2
- add update instruction to %%post

* Fri Jan 29 2021 Alexey Shabalin <shaba@altlinux.org> 2.0.1-alt1
- new version 2.0.1

* Fri Jan 08 2021 Alexey Shabalin <shaba@altlinux.org> 2.0.0-alt1
- new version 2.0.0

* Fri Oct 02 2020 Alexey Shabalin <shaba@altlinux.org> 1.7.4-alt1
- Initial build.

