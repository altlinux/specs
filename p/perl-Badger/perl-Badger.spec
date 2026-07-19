%define _unpackaged_files_terminate_build 1
%define module_name Badger

Name: perl-%module_name
Version: 0.16
Release: alt1

Summary: Application programming toolkit and object system for Perl
License: GPL-1.0-or-later OR Artistic-1.0-clause
Group: Development/Perl
URL: %CPAN %module_name
# Source-url: https://cpan.metacpan.org/authors/id/A/AB/ABW/%module_name-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch
# Badger's metaclass bootstrap breaks B::PerlReq deparse; tolerate it.
%set_perl_req_method relaxed

BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-Encode perl-YAML

%description
Badger is a collection of useful modules and utilities for building Perl
applications. It provides an object base class, configuration management,
logging, exception handling, filesystem abstraction, codecs, data types
and other application programming facilities.

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Badger.pm
%perl_vendor_privlib/Badger/

%changelog
* Sun Jul 19 2026 Vitaly Lipatov <lav@altlinux.ru> 0.16-alt1
- initial build for ALT Sisyphus
