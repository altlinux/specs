%define _unpackaged_files_terminate_build 1

Name: sqlsmith
Version: 1.5
Release: alt1

Summary: Random SQL query generator
Group: Development/Tools
License: GPL-3.0
URL: https://github.com/anse1/sqlsmith

Source0: %name-%version.tar

BuildRequires: autoconf-archive
BuildRequires: libpqxx-devel
BuildRequires: libpq-devel
BuildRequires: boost-devel
BuildRequires: gcc-c++

%description
SQLsmith is a random SQL query generator. Its paragon is Csmith,
which proved valuable for quality assurance in C compilers.

It currently supports generating queries for PostgreSQL, SQLite 3 and MonetDB.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc README.org
%_bindir/sqlsmith

%changelog
* Fri Jun 19 2026 Alexander Kuznetsov <kuznetsovam@altlinux.org> 1.5-alt1
- Update to version 1.5.

* Thu Oct 02 2025 Alexei Takaseev <taf@altlinux.org> 1.4-alt2
- NMU: change BR libpq5-devel -> libpq-devel

* Wed May 15 2024 Alexander Kuznetsov <kuznetsovam@altlinux.org> 1.4-alt1
- Initial build.
