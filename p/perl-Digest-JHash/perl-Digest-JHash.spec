%define _unpackaged_files_terminate_build 1
%define dist Digest-JHash
Name: perl-%dist
Version: 0.10
Release: alt1.1.1

Summary: Perl extension for 32 bit Jenkins Hashing Algorithm
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/S/SH/SHLOMIF/Digest-JHash-%{version}.tar.gz

# Automatically added by buildreq on Tue Oct 11 2011
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description
The "Digest::JHash" module allows you to use the fast JHash hashing algorithm
developed by Bob Jenkins from within Perl programs. The algorithm takes as
input a message of arbitrary length and produces as output a 32-bit "message
digest" of the input in the form of an unsigned long integer.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Digest
%perl_vendor_autolib/Digest

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1.1
- rebuild with new perl 5.24.1

* Sat Nov 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1.1
- rebuild with new perl 5.20.1

* Tue Jan 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 0.07-alt4
- built for perl 5.18

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 0.07-alt3
- rebuilt for perl-5.16

* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 0.07-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Thu Nov 04 2010 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt1.1
- rebuilt with perl 5.12

* Thu Nov 19 2009 Vitaly Lipatov <lav@altlinux.ru> 0.05-alt1
- initial build for ALT Linux Sisyphus

