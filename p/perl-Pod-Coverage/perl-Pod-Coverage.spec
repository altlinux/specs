%define dist Pod-Coverage
Name: perl-%dist
Version: 0.21
Release: alt1

Summary: Checks if the documentation of a module is comprehensive
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Nov 11 2011
BuildRequires: perl-Devel-Symdump perl-Module-Build perl-Pod-Parser perl-Test-Pod

%description
This module provides a mechanism for determining if the pod for a
given module is comprehensive.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%_bindir/pod*
%perl_vendor_privlib/Pod

%changelog
* Fri Nov 11 2011 Alexey Tourbin <at@altlinux.ru> 0.21-alt1
- 0.19 -> 0.21

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Sep 18 2008 Vitaly Lipatov <lav@altlinux.ru> 0.19-alt1
- new version 0.19 (with rpmrb script)

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.17-alt2
- fix directory ownership violation

* Fri Sep 02 2005 Vitaly Lipatov <lav@altlinux.ru> 0.17-alt1
- first build for ALT Linux Sisyphus
