# via
%define module IO-Digest
%define m_distro IO-Digest
%define m_name IO::Digest
%define m_author_id unknown
%define _enable_test 1

Name: perl-%module
Version: 0.11
Release: alt1

Summary: Calculate digests while reading or writing

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/C/CL/CLKAO/IO-Digest-%{version}.tar.gz

BuildRequires: perl-PerlIO perl-PerlIO-via-dynamic perl-devel

%description
This module allows you to calculate digests while reading or writing
file handles. This avoids the case you need to reread the same content
to compute the digests after written a file.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README CHANGES
%perl_vendor_privlib/IO/

%changelog
* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.10-alt2
- fix directory ownership violation

* Tue Feb 21 2006 Vitaly Lipatov <lav@altlinux.ru> 0.10-alt1
- initial build for ALT Linux Sisyphus

