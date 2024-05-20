%define _unpackaged_files_terminate_build 1

Name: sqlsmith
Version: 1.4
Release: alt1

Summary: Random SQL query generator
Group: Development/Tools
License: GPL-3.0
URL: https://github.com/anse1/sqlsmith

Source0: %name-%version.tar

BuildRequires: autoconf-archive
BuildRequires: libpqxx-devel
BuildRequires: libpq5-devel
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
* Wed May 15 2024 Alexander Kuznetsov <kuznetsovam@altlinux.org> 1.4-alt1
- Initial build.
