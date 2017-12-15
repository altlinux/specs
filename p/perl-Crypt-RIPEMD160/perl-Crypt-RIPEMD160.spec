%define _unpackaged_files_terminate_build 1
%define dist Crypt-RIPEMD160
Name: perl-%dist
Version: 0.06
Release: alt1.1.1.1

Summary: Perl extension for the RIPEMD-160 Hash function
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/T/TO/TODDR/Crypt-RIPEMD160-%{version}.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-devel

%description
The Crypt::RIPEMD160 module allows you to use the RIPEMD160
Message Digest algorithm from within Perl programs.

The module is based on the implementation from Antoon Bosselaers from
Katholieke Universiteit Leuven.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_archlib/Crypt
%perl_vendor_autolib/Crypt

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt4.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt4
- built for perl 5.18

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt3
- rebuilt for perl-5.16

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.05-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt2.1
- rebuilt with perl 5.12

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.04-alt2
- fix directory ownership violation

* Sat Aug 27 2005 Vitaly Lipatov <lav@altlinux.ru> 0.04-alt1
- first build for ALT Linux Sisyphus
