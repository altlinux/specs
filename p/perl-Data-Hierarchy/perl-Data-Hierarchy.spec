%define module Data-Hierarchy
%define m_distro %module
%define m_name Data::Hierarchy
%define m_author_id unknown
%define _enable_test 1

Name: perl-%module
Version: 0.34
Release: alt2.1

Summary: Handle data in a hierarchical structure

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/Data-Hierarchy-%version.tar.bz2

# Automatically added by buildreq on Sun Jun 03 2007
BuildRequires: perl-Log-Agent perl-Storable perl-Test-Exception

%description
Data::Hierarchy provides a simple interface for manipulating inheritable
data attached to a hierarchical environment (like filesystem).

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README CHANGES
%perl_vendor_privlib/Data/

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.34-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.34-alt2
- fix directory ownership violation

* Sun Jun 03 2007 Vitaly Lipatov <lav@altlinux.ru> 0.34-alt1
- new version 0.34 (with rpmrb script)
- update buildreqs

* Tue Feb 21 2006 Vitaly Lipatov <lav@altlinux.ru> 0.21-alt1
- initial build for ALT Linux Sisyphus

