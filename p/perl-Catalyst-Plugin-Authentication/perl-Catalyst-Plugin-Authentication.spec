%define dist Catalyst-Plugin-Authentication
Name: perl-%dist
Version: 0.10024
Release: alt2

Summary: Infrastructure plugin for the Catalyst
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/J/JJ/JJNAPIORK/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 25 2011 (-bi)
BuildRequires: perl-Catalyst-Devel perl-Catalyst-Plugin-Session perl-Class-Accessor perl-Class-Inspector perl-Digest-SHA perl-Digest-SHA1 perl-Test-Exception perl-Tie-RefHash
BuildRequires: perl(Test/Fatal.pm)

%description
The authentication plugin provides generic user support for
Catalyst apps. It is the basis for both authentication (checking
the user is who they claim to be), and authorization (allowing
the user to do what the system authorises them to do).

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Catalyst

%changelog
* Thu Jun 18 2026 Andrew A. Vasilyev <andy@altlinux.org> 0.10024-alt2
- NMU: fix FTBFS

* Thu Apr 03 2025 Igor Vlasenko <viy@altlinux.org> 0.10024-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.10023-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.10021-alt1
- automated CPAN update

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

