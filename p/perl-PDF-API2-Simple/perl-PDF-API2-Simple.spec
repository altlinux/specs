%define _unpackaged_files_terminate_build 1
## SPEC file for Perl module PDF::API2::Simple

%define real_name PDF-API2-Simple
%define module_version 1.1.4

Name: perl-PDF-API2-Simple
Version: 1.1.4u
Release: alt1

Summary: simplistic wrapper for the PDF::API2 modules

License: %pubdomain
Group: Development/Perl

URL: http://search.cpan.org/~redtree/PDF-API2-Simple/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: http://www.cpan.org/authors/id/R/RE/REDTREE/PDF-API2-Simple-%{version}.tar.gz

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: perl-devel rpm-build-licenses
# Automatically added by buildreq on Thu Feb 28 2008
BuildRequires: perl-Module-Install perl-PDF-API2 perl-Test-Pod

%description
Perl module  PDF::API2::Simple  is a wrapper  around  the excellent
PDF::API2 series of modules. This module is simply a simplification
of those modules, and has been known  to greatly  reduce production
time. This module is in the public domain, with a plea of 
notification.

%prep
%setup -q -n %real_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README examples
%exclude /.perl.req
%perl_vendor_privlib/PDF/API2/Simple*

%changelog
* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.4u-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Feb 28 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.1.4-alt1
- Initial build for ALT Linux Sisyphus

