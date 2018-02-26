%define dist Test-Exception
Name: perl-%dist
Version: 0.31
Release: alt1

Summary: Test exception based code
License: Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Dec 18 2010
BuildRequires: perl-Module-Build perl-Sub-Uplevel

%description
This module provides a few convenience methods for testing exception
based code.  It is built with Test::Builder and plays happily with
Test::More and friends.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%dir %perl_vendor_privlib/Test
%perl_vendor_privlib/Test/Exception.pm

%changelog
* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 0.31-alt1
- 0.29 -> 0.31

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Mar 30 2010 Alexey Tourbin <at@altlinux.ru> 0.29-alt1
- 0.27 -> 0.29
- alt-caller.patch: hackaround "Bizarre copy of ARRAY" problem, based
  on analysis posted by Bram on the perl5-porters mailing list
- t/stacktrace.t: disabled until a better upstream fix is devised

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.27-alt2
- fix directory ownership violation

* Tue Jun 17 2008 Vitaly Lipatov <lav@altlinux.ru> 0.27-alt1
- new version 0.27 (with rpmrb script)

* Sat Nov 11 2006 Vitaly Lipatov <lav@altlinux.ru> 0.21-alt2
- update buildreq

* Tue Jun 07 2005 Vitaly Lipatov <lav@altlinux.ru> 0.21-alt1
- first build for ALT Linux Sisyphus
