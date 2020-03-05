%define pg_ver 11

Name: postgresql%pg_ver-pg_partman
Version: 4.2.0
Release: alt2

Summary: pg_partman is an extension to create and manage both time-based and serial-based table partition sets.
License: PostgreSQL
Group: Databases
Url: https://badge.fury.io/pg/pg_partman

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: postgresql-devel

Requires: postgresql%pg_ver-server


%description
pg_partman is an extension to create and manage both time-based and serial-based
table partition sets. Native partitioning in PostgreSQL 10 is supported as of
pg_partman v3.0.1 and much more extensively as of 4.0.0 along with
PostgreSQL 11. Note that all the features of trigger-based partitioning
are not yet supported in native, but performance in both reads & writes is
significantly better.

%prep
%setup
%patch0 -p1

sed -i 's|#!.*python|&3|' $(find ./ -name '*.py')

%build
%make

%install
%makeinstall_std

%files
%_bindir/*
%_libdir/pgsql/pg_partman_bgw.so
%_datadir/pgsql/extension/*
%doc %_datadir/doc/postgresql/extension/*


%changelog
* Thu Mar 05 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.2.0-alt2
- Porting to python3.

* Wed Oct 02 2019 Alexei Takaseev <taf@altlinux.org> 4.2.0-alt1
- 4.2.0

* Sat May 18 2019 Alexei Takaseev <taf@altlinux.org> 4.1.0-alt1
- Initial build for ALT Linux
