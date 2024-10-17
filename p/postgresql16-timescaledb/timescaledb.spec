%define pg_ver 16

Name: postgresql%pg_ver-timescaledb
Version: 2.16.1
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
    -DPG_CONFIG=%_bindir/pg_server_config

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
* Thu Oct 17 2024 Alexei Takaseev <taf@altlinux.org> 2.16.1-alt1
- 2.16.1

* Thu Aug 01 2024 Alexei Takaseev <taf@altlinux.org> 2.15.3-alt1
- 2.15.3

* Thu Mar 28 2024 Alexei Takaseev <taf@altlinux.org> 2.14.2-alt1
- 2.14.2

* Wed Jan 10 2024 Alexei Takaseev <taf@altlinux.org> 2.13.1-alt1
- 2.13.1

* Thu Dec 14 2023 Alexei Takaseev <taf@altlinux.org> 2.13.0-alt1
- 2.13.0
- Build for PostgreSQL 16

* Fri Aug 18 2023 Alexei Takaseev <taf@altlinux.org> 2.11.2-alt1
- 2.11.2

* Wed Jun 28 2023 Alexei Takaseev <taf@altlinux.org> 2.11.0-alt1
- 2.11.0

* Sun Apr 30 2023 Alexei Takaseev <taf@altlinux.org> 2.10.3-alt1
- 2.10.3

* Sun Apr 23 2023 Alexei Takaseev <taf@altlinux.org> 2.10.2-alt1
- 2.10.2

* Mon Apr 03 2023 Alexei Takaseev <taf@altlinux.org> 2.10.1-alt1
- 2.10.1

* Tue Feb 07 2023 Alexei Takaseev <taf@altlinux.org> 2.9.3-alt1
- 2.9.3

* Thu Feb 02 2023 Alexei Takaseev <taf@altlinux.org> 2.9.2-alt1
- 2.9.2

* Sat Nov 12 2022 Alexei Takaseev <taf@altlinux.org> 2.8.1-alt2
- Use server depended pg_server_config for build

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

