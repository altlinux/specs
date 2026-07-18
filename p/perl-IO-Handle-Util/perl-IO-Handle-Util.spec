%define module IO-Handle-Util

Name: perl-%module
Version: 0.02
Release: alt1

Summary: Functions for working with IO::Handle like objects

Group: Development/Perl
License: GPL-1.0-or-later OR Artistic-1.0-clause
Url: %CPAN %module
# Source-url: https://cpan.metacpan.org/authors/id/E/ET/ETHER/%module-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel /proc perl-Module-Build perl-IO-String perl(asa.pm) perl(Sub/Exporter.pm) perl(autodie.pm)

%description
This module provides a number of helpful routines to manipulate or
create IO::Handle like objects.  It includes utilities for creating
callback based filehandles, iterators, and adapting arbitrary objects
to behave like IO::Handle.

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README LICENCE CONTRIBUTING
%perl_vendor_privlib/IO/Handle/

%changelog
* Fri Jul 17 2026 Vitaly Lipatov <lav@altlinux.ru> 0.02-alt1
- initial build for ALT Sisyphus

