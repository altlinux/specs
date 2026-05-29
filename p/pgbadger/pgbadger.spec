%define _unpackaged_files_terminate_build 1
%def_without test

Name:    pgbadger
Version: 13.2
Release: alt1

Summary: A fast PostgreSQL Log Analyzer
License: PostgreSQL
Group:   Databases
Url:     https://github.com/darold/pgbadger

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel
BuildRequires: perl(Encode.pm)
BuildRequires: perl(JSON/XS.pm)
BuildRequires: perl(Pod/Man.pm)
BuildRequires: perl(Text/CSV_XS.pm)
BuildRequires: perl-Pod-Markdown
BuildRequires: /proc

%description
PostgreSQL log analyzer with fully detailed reports and graphs.

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc *.md
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Fri May 29 2026 Andrey Cherepanov <cas@altlinux.org> 13.2-alt1
- Initial build for Sisyphus.
