%define _unpackaged_files_terminate_build 1                                                                  
%define pg_ver 16

Name:    postgresql%pg_ver-pg_probackup
Version: 2.5.16
Release: alt1

Summary: Backup and recovery manager for PostgreSQL %pg_ver
License: PostgreSQL
Group:   Databases
Url:     https://postgrespro.github.io/pg_probackup
Vcs:     https://github.com/postgrespro/pg_probackup

Source0: pg_probackup-%version.tar
Source1: pg-srchome.tar

BuildRequires: postgresql%pg_ver-server-devel
BuildRequires: libecpg6-%pg_ver-devel-static
BuildRequires: pkgconfig(krb5-gssapi)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(liblz4)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(pam)
BuildRequires: pkgconfig(libxslt)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libselinux)
BuildRequires: readline-devel
BuildRequires: setproctitle-devel

Requires: postgresql%pg_ver-server

%description
pg_probackup is utility to manage backup and recovery of PostgreSQL database
clusters.  It is designed to perform periodic backups of the PostgreSQL
instance that enable you to restore the server in case of a failure.

%prep
%setup -a1 -n pg_probackup-%version

%build
%make \
USE_PGXS=1 \
top_srcdir=./pg-srchome

%install
install -Dpm755 ./pg_probackup %buildroot%_bindir/pg_probackup

%check
./pg_probackup version
_tmp=$(mktemp -u)
_catalog="$(pwd)$_tmp"
./pg_probackup init -B $_catalog

%files
%doc *.md LICENSE
%_bindir/pg_probackup

%changelog
* Fri Jun 05 2026 Andrey Cherepanov <cas@altlinux.org> 2.5.16-alt1
- New version.

* Mon May 25 2026 Andrey Cherepanov <cas@altlinux.org> 2.5.15-alt2
- Built for p11.

* Mon Dec 09 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 2.5.15-alt1
- Initial build for ALT.
