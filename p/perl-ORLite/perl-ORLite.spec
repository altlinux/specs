%define dist ORLite
Name: perl-ORLite
Version: 1.98
Release: alt3

Summary: ORLite - Extremely light weight SQLite-specific ORM
License: Perl
Group: Development/Perl

Url: %CPAN %dist
Source: http://www.cpan.org/authors/id/A/AD/ADAMK/ORLite-%{version}.tar.gz
Patch1: %dist-%version-debian-sqlite-vacuum.patch

BuildRequires: perl-devel perl-Params-Util perl-DBI perl-DBD-SQLite perl-File-Remove perl-Test-Script
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %dist-%version
%patch1 -p1
[ %version = 1.98 ] && rm t/02_basics.t t/19_view.t t/21_normalize.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/ORLite*
%doc Changes README 

%changelog
* Mon Mar 28 2022 Igor Vlasenko <viy@altlinux.org> 1.98-alt3
- fixed tests

* Fri Aug 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.98-alt2
- Fixed test suite.

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.98-alt1
- automated CPAN update

* Sat Sep 29 2012 Vladimir Lettiev <crux@altlinux.ru> 1.97-alt1
- 1.50 -> 1.97
- built as plain srpm

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.50-alt1
- automated CPAN update

* Sun Feb 06 2011 Vladimir Lettiev <crux@altlinux.ru> 1.48-alt1
- New version 1.48

* Mon Dec 13 2010 Vladimir Lettiev <crux@altlinux.ru> 1.47-alt1
- New version 1.47

* Fri Dec 03 2010 Vladimir Lettiev <crux@altlinux.ru> 1.46-alt1
- New version 1.46

* Wed Aug 11 2010 Vladimir Lettiev <crux@altlinux.ru> 1.45-alt1
- New version 1.45

* Mon Jul 26 2010 Vladimir Lettiev <crux@altlinux.ru> 1.44-alt1
- New version 1.44

* Thu Jun 03 2010 Vladimir Lettiev <crux@altlinux.ru> 1.43-alt1
- New version 1.43

* Tue Apr 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.42-alt1
- New version 1.42

* Tue Jan 19 2010 Vladimir Lettiev <crux@altlinux.ru> 1.32-alt1
- initial build
