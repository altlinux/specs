%define dist Term-Gnuplot
Name: perl-%dist
Version: 0.90380905
Release: alt5.1.1.qa1.1

Summary: Lowlevel graphics using gnuplot drawing routines
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

Patch: Term-Gnuplot-0.90380905-alt-fix-build-gnu11.patch

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: libX11-devel libfreetype-devel libgd2-devel libjpeg-devel libpng-devel perl-devel

%description
This module is intended for low-resolution or high-resolution graphics
using gnuplot low-level functions.

%prep
%setup -q -n %dist-%version
%patch -p1
sed -i- 's/-lvga//g' Makefile.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_archlib/Term
%perl_vendor_autolib/Term

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.90380905-alt5.1.1.qa1.1
- rebuild with new perl 5.26.1

* Tue Dec 12 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.90380905-alt5.1.1.qa1
- Fixed build with default gcc.

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.90380905-alt5.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.90380905-alt5.1
- rebuild with new perl 5.22.0

* Wed Nov 18 2015 Igor Vlasenko <viy@altlinux.ru> 0.90380905-alt5
- fixed build

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.90380905-alt4.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.90380905-alt4
- built for perl 5.18

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.90380905-alt3
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.90380905-alt2.2
- rebuilt for perl-5.14

* Mon Nov 08 2010 Vladimir Lettiev <crux@altlinux.ru> 0.90380905-alt2.1
- rebuilt with perl 5.12

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.90380905-alt2
- fix directory ownership violation

* Sat Nov 11 2006 Vitaly Lipatov <lav@altlinux.ru> 0.90380905-alt0.1
- initial build for ALT Linux Sisyphus

