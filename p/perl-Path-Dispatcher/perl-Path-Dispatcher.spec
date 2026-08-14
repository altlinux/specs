%define _unpackaged_files_terminate_build 1
%define module_name Path-Dispatcher

Name: perl-%module_name
Version: 1.08
Release: alt2

Summary: Flexible and extensible dispatch

License: GPL-1.0-or-later OR Artistic-1.0-clause
Group: Development/Perl
URL: %CPAN %module_name
# Source-url: https://cpan.metacpan.org/authors/id/E/ET/ETHER/%module_name-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-Module-Build-Tiny
BuildRequires: perl-Moo perl-MooX-TypeTiny perl-Try-Tiny perl-Type-Tiny
BuildRequires: perl-Test-Fatal

%description
Path::Dispatcher is a flexible and extensible dispatch mechanism for
matching paths (or any other strings) against a set of rules and running
the corresponding handler.

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Path/Dispatcher
%perl_vendor_privlib/Path/Dispatcher.pm

%changelog
* Fri Jul 17 2026 Vitaly Lipatov <lav@altlinux.ru> 1.08-alt2
- fix License to SPDX expression

* Thu Jul 16 2026 Vitaly Lipatov <lav@altlinux.ru> 1.08-alt1
- initial build for ALT Sisyphus

