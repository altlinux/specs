Name: pg_catcheck
Version: 1.4.0
Release: alt1
Epoch: 1

Summary: Simple tool for diagnosing system catalog corruption

License: PostgreSQL
Group: Databases
Url: https://github.com/EnterpriseDB/pg_catcheck

# Source-git: https://github.com/EnterpriseDB/pg_catcheck
Source: %name-%version.tar

# Automatically added by buildreq on Thu Jun 08 2017
# optimized out: libkrb5-devel libpq-devel libsasl2-3 libssl-devel libxml2-devel postgresql-devel python-base python-modules python3 python3-base setproctitle
BuildRequires: libecpg-devel-static libpam-devel libreadline-devel libselinux-devel libxslt-devel setproctitle-devel zlib-devel
BuildRequires: libssl-devel libkrb5-devel libzstd-devel liblz4-devel
BuildRequires: postgresql-devel

%description
pg_catcheck is a simple tool for diagnosing system catalog corruption.
If you suspect that your system catalogs are corrupted,
this tool may help you figure out exactly what problems you have
and how serious they are. If you are paranoid, you can run it routinely
to search for system catalog corruption that might otherwise go undetected.
However, pg_catcheck is not a general corruption detector. For that,
you should use PostgreSQL's checksum feature (initdb -k).

%prep
%setup

%build
%make_build

%install
%makeinstall_std

%files
%_bindir/*

%changelog
* Mon Sep 25 2023 Alexei Takaseev <taf@altlinux.org> 1:1.4.0-alt1
- 1.4.0

* Thu May 18 2023 Alexei Takaseev <taf@altlinux.org> 1:1.3.0-alt1
- 1.3.0

* Fri Dec 04 2020 Vitaly Lipatov <lav@altlinux.ru> 1:1.2.0-alt1
- new version 1.2.0 (with rpmrb script)
- set Epoche: 1 (was wrong version before)

* Fri Dec 04 2020 Vitaly Lipatov <lav@altlinux.ru> 9.6.3-alt3
- s/postgresql-devel-static/postgresql-devel/

* Wed Dec 06 2017 Vitaly Lipatov <lav@altlinux.ru> 9.6.3-alt2
- use buildreq postgresql-devel-static without version

* Thu Jun 08 2017 Konstantin Kondratyuk <kondratyuk@altlinux.org> 9.6.3-alt1
- Initial build
