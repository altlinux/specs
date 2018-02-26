%define dist Class-C3-XS
Name: perl-%dist
Version: 0.13
Release: alt2.2

Summary: XS speedups for Class::C3
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-Module-Install perl-NEXT perl-Sub-Name perl-Test-Pod

%description
This contains XS performance enhancers for Class::C3 version 0.16 and
higher. The main Class::C3 package will use this package automatically
if it can find it. Do not use this package directly, use Class::C3
instead.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_archlib/Class
%perl_vendor_autolib/Class

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.13-alt2.2
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.13-alt2.1
- rebuilt with perl 5.12

* Tue Apr 27 2010 Alexey Tourbin <at@altlinux.ru> 0.13-alt2
- fixed directory packaging

* Thu Mar 04 2010 Mikhail Pokidko <pma@altlinux.org> 0.13-alt1
- Version up. files section fixes

* Thu Sep 04 2008 Mikhail Pokidko <pma@altlinux.org> 0.08-alt2
- sisyphus_check fixes

* Thu May 15 2008 Mikhail Pokidko <pma@altlinux.org> 0.08-alt1
- first build for ALT Linux Sisyphus

