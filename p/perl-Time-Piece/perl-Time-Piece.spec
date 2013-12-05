%define _unpackaged_files_terminate_build 1
%define dist Time-Piece
Name: perl-%dist
Version: 1.24
Release: alt1

Summary: Object Oriented time objects
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/R/RJ/RJBS/Time-Piece-%{version}.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-devel

%description
This module replaces the standard localtime and gmtime functions with
implementations that return objects. It does so in a backwards
compatible manner, so that using localtime/gmtime in the way documented
in perlfunc will still return what you expect.

The module actually implements most of an interface described by
Larry Wall on the perl5-porters mailing list here:
http://www.xray.mpe.mpg.de/mailing-lists/perl5-porters/2000-01/msg00241.html

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Time
%perl_vendor_autolib/Time

%changelog
* Thu Dec 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.22-alt1
- 1.21 -> 1.22

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1
- automated CPAN update

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 1.20-alt2
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.20-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.20-alt1.1
- rebuilt with perl 5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1
- automated CPAN update

* Wed Oct 08 2008 Vitaly Lipatov <lav@altlinux.ru> 1.13-alt1
- new version 1.13 (with rpmrb script)

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.11-alt2
- fix directory ownership violation
- disable man packaging

* Mon Dec 11 2006 Vitaly Lipatov <lav@altlinux.ru> 1.11-alt1
- first build for ALT Linux Sisyphus
