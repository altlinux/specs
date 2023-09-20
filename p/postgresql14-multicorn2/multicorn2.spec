%define _unpackaged_files_terminate_build 1                                                                           
%define pg_ver 14

Name: postgresql%pg_ver-multicorn2
Version: 2.4
Release: alt1

Summary: Multicorn Python3 Wrapper for Postgresql %pg_ver Foreign Data Wrapper
License: PostgreSQL
Group: Databases
URL: https://github.com/pgsql-io/multicorn2

Source: multicorn2-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: postgresql%pg_ver-server-devel
BuildRequires: python3-dev
BuildRequires: python3-module-wheel

Requires: postgresql%pg_ver-server
Provides: multicorn2 = %EVR
AutoProv: yes,nopython3

%description
The Multicorn Foreign Data Wrapper allows you to fetch foreign data in Python
in your PostgreSQL server.

%prep
%setup -n multicorn2-%version
subst '/pip/d' Makefile
# Drop support deprecated module brigit
rm -rf python/multicorn/gitfdw.py

%build
%make_build
%pyproject_build

%install
%makeinstall_std
%pyproject_install

%files
%doc README.md
%doc %_defaultdocdir/postgresql/extension/multicorn.md
%_libdir/pgsql/*.so
%ifnarch %e2k
%_libdir/pgsql/bitcode/multicorn*
%endif
%python3_sitelibdir/multicorn/
%python3_sitelibdir/%{pyproject_distinfo multicorn}
%_datadir/pgsql/extension

%changelog
* Tue Sep 19 2023 Andrey Cherepanov <cas@altlinux.org> 2.4-alt1
- Initial build for Sisyphus.
