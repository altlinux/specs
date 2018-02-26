%define dist Math-BigInt-GMP
Name: perl-%dist
Version: 1.37
Release: alt1

Summary: Use the GMP library for Math::BigInt routines
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: libgmp-devel perl-Math-BigInt perl-Test-Pod perl-threads

%description
Provides support for big integer calculations via means of the GMP c-library.

Math::BigInt::GMP now no longer uses Math::GMP, but provides it's own XS layer
to access the GMP c-library. This cut's out another (perl sub routine) layer
and also reduces the memory footprint by not loading Math::GMP and Carp at
all.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README
%perl_vendor_archlib/Math
%perl_vendor_autolib/Math

%changelog
* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 1.37-alt1
- 1.24 -> 1.37
- built for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.24-alt1.1
- rebuilt with perl 5.12
- fixed test with Math::BigIng >= 1.90

* Mon Nov 23 2009 Mikhail Pokidko <pma@altlinux.org> 1.24-alt1
- Version up. Close: #22358

* Thu Sep 04 2008 Mikhail Pokidko <pma@altlinux.org> 1.22-alt2
- sisyphus_checks fixes

* Wed Jun 06 2007 Mikhail Pokidko <pma@altlinux.org> 1.22-alt1
- first build for ALT Linux Sisyphus

