%define dist Term-Gnuplot
Name: perl-%dist
Version: 0.90380905
Release: alt2.2

Summary: Lowlevel graphics using gnuplot drawing routines
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: libX11-devel libfreetype-devel libgd2-devel libjpeg-devel libpng-devel perl-devel

%description
This module is intended for low-resolution or high-resolution graphics
using gnuplot low-level functions.

%prep
%setup -q -n %dist-%version
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
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.90380905-alt2.2
- rebuilt for perl-5.14

* Mon Nov 08 2010 Vladimir Lettiev <crux@altlinux.ru> 0.90380905-alt2.1
- rebuilt with perl 5.12

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.90380905-alt2
- fix directory ownership violation

* Sat Nov 11 2006 Vitaly Lipatov <lav@altlinux.ru> 0.90380905-alt0.1
- initial build for ALT Linux Sisyphus

