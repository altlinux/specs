%define pg_ver 15
%def_with jit

Name: postgresql%pg_ver-pg_partman
Version: 5.0.0
Release: alt1

Summary: pg_partman is an extension to create and manage both time-based and serial-based table partition sets.
License: PostgreSQL
Group: Databases
Url: https://badge.fury.io/pg/pg_partman

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3

# Automatically added by buildreq on Sat May 18 2019
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 python-base sh4
BuildRequires: postgresql%pg_ver-server-devel

Requires: postgresql%pg_ver-server

%description
pg_partman is an extension to create and manage both time-based and number-based table
partition sets. As of version 5.0.0, only built-in, declarative partitioning is
supported and the older trigger-based methods have been deprecated.

The declarative partitioning built into PostgreSQL provides the commands to create
a partitioned table and its children. pg_partman uses the built-in declarative features
that PostgreSQL provides and builds upon those with additional features and enhancements
to make managing partitions easier. One key way that pg_partman extends partitioning in
Postgres is by providing a means to automate the child table maintenance over time (Ex.
adding new children, dropping old ones based on a retention policy). pg_partman also has
features to turn an existing table into a partitioned table or vice versa.

%prep
%setup
%patch0 -p1

## py2 -> py3
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')
sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')
##

%build
%make

%install
%makeinstall_std

%files
%_bindir/*
%_libdir/pgsql/pg_partman_bgw.so
%if %pg_ver >= 11
%if_with jit
%_libdir/pgsql/bitcode/src/pg_partman_bgw*
%endif
%endif
%_datadir/pgsql/extension/*
%doc %_datadir/doc/postgresql/extension/*

%changelog
* Wed Oct 04 2023 Alexei Takaseev <taf@altlinux.org> 5.0.0-alt1
- 5.0.0
- Build only for PostgreSQL >= 14

* Mon Sep 11 2023 Alexei Takaseev <taf@altlinux.org> 4.7.4-alt1
- 4.7.4

* Thu Mar 30 2023 Alexei Takaseev <taf@altlinux.org> 4.7.3-alt1
- 4.7.3

* Sat Dec 17 2022 Alexei Takaseev <taf@altlinux.org> 4.7.2-alt1
- 4.7.2

* Fri Oct 14 2022 Alexei Takaseev <taf@altlinux.org> 4.7.1-alt1
- 4.7.1

* Mon Sep 19 2022 Michael Shigorin <mike@altlinux.org> 4.7.0-alt2
- add jit knob (on by default)

* Mon Aug 15 2022 Alexei Takaseev <taf@altlinux.org> 4.7.0-alt1
- 4.7.0

* Mon May 16 2022 Alexei Takaseev <taf@altlinux.org> 4.6.2-alt1
- 4.6.2

* Mon Apr 18 2022 Alexei Takaseev <taf@altlinux.org> 4.6.1-alt1
- 4.6.1
- Packaged bitecode files for PG >= 11

* Thu Jan 27 2022 Alexei Takaseev <taf@altlinux.org> 4.6.0-alt2
- Change BR from postgresql-devel to postgresql%pg_ver-server-devel

* Fri Oct 08 2021 Alexei Takaseev <taf@altlinux.org> 4.6.0-alt1
- 4.6.0

* Wed Sep 29 2021 Alexei Takaseev <taf@altlinux.org> 4.5.1-alt2
- Rebuild with PostgreSQL 14

* Fri Sep 03 2021 Alexei Takaseev <taf@altlinux.org> 4.5.1-alt1
- 4.5.1

* Thu Dec 24 2020 Alexei Takaseev <taf@altlinux.org> 4.4.1-alt1
- 4.4.1

* Mon Sep 28 2020 Alexei Takaseev <taf@altlinux.org> 4.4.0-alt2
- Rebuild with PostgreSQL 13

* Fri May 29 2020 Alexei Takaseev <taf@altlinux.org> 4.4.0-alt1
- 4.4.0

* Fri Feb 07 2020 Alexei Takaseev <taf@altlinux.org> 4.3.0-alt2
- 4.3.0

* Mon Dec 02 2019 Alexei Takaseev <taf@altlinux.org> 4.2.2-alt2
- Build with python 3

* Mon Oct 21 2019 Alexei Takaseev <taf@altlinux.org> 4.2.2-alt1
- 4.2.2

* Wed Oct 02 2019 Alexei Takaseev <taf@altlinux.org> 4.2.0-alt1
- 4.2.0

* Sat May 18 2019 Alexei Takaseev <taf@altlinux.org> 4.1.0-alt1
- Initial build for ALT Linux
