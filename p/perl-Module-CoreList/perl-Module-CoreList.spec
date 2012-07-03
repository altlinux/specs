%define dist Module-CoreList
Name: perl-%dist
Version: 2.57
Release: alt1

Summary: What modules shipped with versions of perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011 (-bi)
BuildRequires: perl-Pod-Parser perl-Test-Pod

%description
Module::CoreList provides information on which core and dual-life modules
shipped with each version of perl.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%_bindir/corelist
%perl_vendor_privlib/Module

%changelog
* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 2.57-alt1
- 2.56 -> 2.57

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 2.56-alt1
- automated CPAN update

* Tue Sep 06 2011 Vitaly Lipatov <lav@altlinux.ru> 2.55-alt1
- new version 2.55 (with rpmrb script)
- update buildreqs

* Sun Jan 30 2011 Vitaly Lipatov <lav@altlinux.ru> 2.44-alt1
- new version 2.44 (with rpmrb script)

* Tue Dec 14 2010 Vitaly Lipatov <lav@altlinux.ru> 2.41-alt1
- new version 2.41 (with rpmrb script)

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 2.35-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 2.12-alt2
- fix directory ownership violation

* Sun Jul 22 2007 Vitaly Lipatov <lav@altlinux.ru> 2.12-alt1
- new version 2.12 (with rpmrb script)

* Sat Jul 30 2005 Vitaly Lipatov <lav@altlinux.ru> 2.02-alt2
- fix bug #7499 (fix unexpanded macros)

* Tue Jul 12 2005 Vitaly Lipatov <lav@altlinux.ru> 2.02-alt1
- first build for ALT Linux Sisyphus
