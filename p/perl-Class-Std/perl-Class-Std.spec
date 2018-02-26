# SPEC file for building Perl module Class-Std

%define real_name Class-Std
%define version 0.11
%define release alt1

Name: perl-Class-Std
Version: %version
Release: alt1.1

Summary: Perl module for creating standard "inside-out" classes 

License: Perl license
Group: Development/Perl
URL: http://search.cpan.org/~dconway/Class-Std/

BuildArch: noarch

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: http://search.cpan.org/CPAN/authors/id/D/DC/DCONWAY/%real_name-%version.tar.gz

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel
# Automatically added by buildreq on Sat May 24 2008
BuildRequires: perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage

%description
Perl module Class::Std provides the standard infrastructure 
required to create "inside-out" classes, as described in 
Chapters 15 and 16 of "Perl Best Practices" (O'Reilly, 2005).

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes

%perl_vendor_privlib/Class/Std*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Mar 08 2010 Nikolay A. Fetisov <naf@altlinux.ru> 0.11-alt1
- New version

* Sat May 24 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.0.9-alt1
- New version

* Thu Aug 09 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.0.8-alt1
- Initial build for ALT Linux Sisyphus

