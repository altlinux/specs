%define module Geo-Proj4

Name: perl-%module
Version: 1.01
Release: alt1.2

Summary: PROJ.4 cartographic projections library
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: %module-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: libproj-devel perl-Test-Pod proj

%description
The Open Source PROJ.4 library converts between geographic coordinate
systems. It is able to convert between geodetic latitude and longitude
(LL, most commonly the WGS84 projection), into an enormous variety of
other cartographic projections (XY, usually UTM).

%prep
%setup -n %module-%version

# do not override default CCFLAGS
sed -i- '/CCFLAGS/d' Makefile.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Geo
%perl_vendor_autolib/Geo

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.01-alt1.2
- rebuilt for perl-5.14

* Thu Nov 04 2010 Vladimir Lettiev <crux@altlinux.ru> 1.01-alt1.1
- rebuilt with perl 5.12

* Tue Jun 15 2010 Victor Forsiuk <force@altlinux.org> 1.01-alt1
- Refresh BR to fix FTBFS.
- 1.01

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1.1
- NMU for unknown reason

* Mon Jun 16 2008 Michael Bochkaryov <misha@altlinux.ru> 0.99-alt1
- 0.99 version

* Wed Mar 21 2007 Sir Raorn <raorn@altlinux.ru> 0.98-alt1
- first build for ALT Linux Sisyphus
