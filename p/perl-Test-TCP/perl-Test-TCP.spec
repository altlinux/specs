Name: perl-Test-TCP
Version: 2.16
Release: alt1

Summary: Test::TCP - testing TCP program
Group: Development/Perl
License: Perl

Url: %CPAN Test-TCP
# Cloned from git://github.com/tokuhirom/test-tcp.git
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl-Test-SharedFork perl-CPAN-Meta perl-Module-Build perl(IO/Socket/IP.pm)

%description
Test::TCP is test utilities for TCP/IP program.

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test/TCP*
%perl_vendor_privlib/Net/EmptyPort.pm
%doc Changes README.md

%changelog
* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.16-alt1
- automated CPAN update

* Mon Mar 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.15-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 2.14-alt1
- automated CPAN update

* Fri Jul 04 2014 Igor Vlasenko <viy@altlinux.ru> 2.06-alt1
- automated CPAN update

* Mon Jun 30 2014 Igor Vlasenko <viy@altlinux.ru> 2.05-alt1
- new version 2.05

* Mon Sep 30 2013 Vladimir Lettiev <crux@altlinux.ru> 2.01-alt1
- 1.17 -> 2.01

* Mon Oct 01 2012 Vladimir Lettiev <crux@altlinux.ru> 1.17-alt1
- 1.16 -> 1.17
- sources cloned from upstream git

* Fri Jul 06 2012 Vladimir Lettiev <crux@altlinux.ru> 1.16-alt1
- New version 1.16

* Thu Mar 03 2011 Vladimir Lettiev <crux@altlinux.ru> 1.12-alt1
- New version 1.12

* Tue Jan 11 2011 Vladimir Lettiev <crux@altlinux.ru> 1.11-alt1
- New version 1.11

* Fri Dec 03 2010 Vladimir Lettiev <crux@altlinux.ru> 1.07-alt1
- New version 1.07

* Mon Sep 20 2010 Vladimir Lettiev <crux@altlinux.ru> 1.06-alt1
- New version 1.06

* Mon Aug 30 2010 Vladimir Lettiev <crux@altlinux.ru> 1.04-alt1
- initial build
