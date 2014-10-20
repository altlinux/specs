%define dist Class-Accessor-Grouped
Name: perl-Class-Accessor-Grouped
Version: 0.10012
Release: alt1

Summary: Lets you build groups of accessors
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/R/RI/RIBASUSHI/Class-Accessor-Grouped-%{version}.tar.gz

BuildArch: noarch

BuildRequires: perl-Module-Runtime perl-Class-XSAccessor perl-Module-Install perl-Sub-Name perl-Test-Exception

%description
This class lets you build groups of accessors that will call
different getters and setters.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Class/Accessor/Grouped.pm

%changelog
* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.10012-alt1
- automated CPAN update

* Thu Jun 13 2013 Vladimir Lettiev <crux@altlinux.ru> 0.10010-alt1
- 0.10006 -> 0.10010

* Wed Sep 12 2012 Vladimir Lettiev <crux@altlinux.ru> 0.10006-alt1
- 0.10003 -> 0.10006

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.10003-alt1
- automated CPAN update

* Mon Dec 27 2010 Alexey Tourbin <at@altlinux.ru> 0.10002-alt1
- 0.09003 -> 0.10002

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.09003-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 0.09003-alt1
- automated CPAN update

* Fri Nov 13 2009 Michael Bochkaryov <misha@altlinux.ru> 0.09002-alt1
- 0.09002 version

* Mon Sep 08 2008 Michael Bochkaryov <misha@altlinux.ru> 0.08001-alt2
- fix directory ownership violation

* Sat May 24 2008 Michael Bochkaryov <misha@altlinux.ru> 0.08001-alt1
- 0.08001 version

* Thu Mar 22 2007 Sir Raorn <raorn@altlinux.ru> 0.03-alt1
- first build for ALT Linux Sisyphus
