%define dist Catalyst-Plugin-Authentication
Name: perl-%dist
Version: 0.10018
Release: alt2

Summary: Infrastructure plugin for the Catalyst
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 25 2011 (-bi)
BuildRequires: perl-Catalyst-Devel perl-Catalyst-Plugin-Session perl-Class-Accessor perl-Class-Inspector perl-Digest-SHA perl-Digest-SHA1 perl-Test-Exception perl-Tie-RefHash

%description
The authentication plugin provides generic user support for
Catalyst apps. It is the basis for both authentication (checking
the user is who they claim to be), and authorization (allowing
the user to do what the system authorises them to do).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Catalyst

%changelog
* Tue Oct 25 2011 Alexey Tourbin <at@altlinux.ru> 0.10018-alt2
- updated BuildRequires

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.10018-alt1
- automated CPAN update

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 0.10016-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Apr 20 2010 Alexey Tourbin <at@altlinux.ru> 0.10016-alt1
- 0.10007 -> 0.10016

* Mon Sep 08 2008 Michael Bochkaryov <misha@altlinux.ru> 0.10007-alt1
- 0.10007 version build
- fix directory ownership violation

* Tue Jul 01 2008 Michael Bochkaryov <misha@altlinux.ru> 0.10006-alt1
- 0.10006 version build

* Tue Mar 27 2007 Sir Raorn <raorn@altlinux.ru> 0.09-alt1
- first build for ALT Linux Sisyphus

