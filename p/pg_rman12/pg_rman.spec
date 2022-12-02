%define pg_ver 12

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lfs=relaxed

Name: pg_rman%pg_ver
Version: 1.3.14
Release: alt3
Summary: pg_rman is an online backup and restore tool for PostgreSQL
License: BSD-3-Clause
Group: Databases
Url: https://github.com/ossc-db/pg_rman

# https://github.com/ossc-db/pg_rman.git
Source: %name-%version.tar

# Automatically added by buildreq on Sat Apr 19 2014 (-bi)
# optimized out: elfutils libcloog-isl4 libcom_err-devel libkrb5-devel libpq-devel libsasl2-3 postgresql-devel python-base setproctitle
BuildRequires: libecpg-devel-static libpq5-devel-static libpam-devel libreadline-devel libselinux-devel libssl-devel setproctitle-devel zlib-devel
BuildRequires: postgresql%pg_ver-server-devel
BuildRequires: libkrb5-devel

Requires: postgresql%pg_ver-server

Conflicts: pg_rman
Conflicts: pg_rman10
Conflicts: pg_rman11
Conflicts: pg_rman13
Conflicts: pg_rman14

%description
The goal of the pg_rman project is providing a method for online
backup and PITR as easy as pg_dump. Also, it maintains a backup
catalog per database cluster. Users can maintain old backups
including archive logs with one command.

%prep
%setup

%build
%make_build PG_CONFIG=%_bindir/pg_server_config

%install
install -pD -m 755 pg_rman %buildroot%_bindir/pg_rman

mkdir examples
cp -r sql examples/

%files
%doc COPYRIGHT README.md
%doc docs
%doc examples
%_bindir/*

%changelog
* Fri Dec 02 2022 Alexei Takaseev <taf@altlinux.org> 1.3.14-alt3
- Add conflict to old package

* Tue Nov 22 2022 Alexei Takaseev <taf@altlinux.org> 1.3.14-alt2
- Use server depended pg_server_config for build

* Wed Mar 02 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.14-alt1
- Updated to upstream version 1.3.14.

* Thu Oct 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.9-alt2
- Rebuilt with PostgreSQL 13.

* Fri Nov 01 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.9-alt1
- Updated to upstream version 1.3.9.
- Rebuilt with PostgreSQL 12.
- This version may be incompatible with backups from older versions.

* Tue Jan 22 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.8-alt1
- Updated to upstream version 1.3.8.
- Rebuilt with PostgreSQL 11.
- This version may be incompatible with backups from older versions.

* Tue Sep 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.6-alt2
- Updated build dependencies.

* Thu Mar 01 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.6-alt1
- Updated to upstream version 1.3.6.
- Rebuilt with PostgreSQL 10.

* Mon Sep 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.5-alt1
- Updated to upstream version 1.3.5.
- Rebuilt with PostgreSQL 9.6.

* Wed Mar 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.8-alt1.1
- Rebuilt with PostgreSQL 9.4

* Sat Apr 19 2014 Andrew Clark <andyc@altlinux.org> 1.2.8-alt1
- version update 1.2.8-alt1

* Tue Jan 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.7-alt1.1
- Fixed build

* Wed Jan 8 2014 Andrew Clark <andyc@altlinux.org> 1.2.7-alt1
- version update 1.2.7-alt1

* Sat Mar 16 2013 Andrew Clark <andyc@altlinux.org> 1.2.5-alt1
- initial build for ALT.

