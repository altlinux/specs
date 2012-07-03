%define dist Math-GMP
Name: perl-%dist
Version: 2.06
Release: alt1.2

Summary: High speed arbitrary size integer math
License: GPLv2+
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: libgmp-devel perl-devel

%description
Math::GMP was designed to be a drop-in replacement both for Math::BigInt
and for regular integer arithmetic.  Unlike BigInt, though, Math::GMP uses
the GNU gmp library for all of its calculations, as opposed to straight
Perl functions.  This can result in speed improvements.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README
%perl_vendor_archlib/Math
%perl_vendor_autolib/Math

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 2.06-alt1.2
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 2.06-alt1.1
- rebuilt with perl 5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 2.06-alt1
- automated CPAN update

* Tue Oct 21 2008 Mikhail Pokidko <pma@altlinux.org> 2.05-alt2
- x86_64 build fixes

* Mon Oct 20 2008 Mikhail Pokidko <pma@altlinux.org> 2.05-alt1
- version up

* Mon Oct 13 2008 Mikhail Pokidko <pma@altlinux.org> 2.04-alt4
- #17161

* Thu Sep 04 2008 Mikhail Pokidko <pma@altlinux.org> 2.04-alt3
- sisyphus_check fixes

* Wed Jan 24 2007 Mikhail Pokidko <pma@altlinux.ru> 2.04-alt2
- Build fix-up. Red-Hat patch for x86_64 by Sergey Y. Afonin (asy@)

* Wed Nov 15 2006 Mikhail Pokidko <pma@altlinux.ru> 2.04-alt1
- first build for ALT Linux Sisyphus
