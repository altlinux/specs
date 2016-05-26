# require if alternative not found
%filter_from_requires /^perl.Test2.Global.pm./d
%filter_from_requires /^perl.Test2.IPC.Driver.Files.pm./d

Name: perl-Test-SharedFork
Version: 0.35
Release: alt1

Summary: Test::SharedFork - fork test
Group: Development/Perl
License: Perl

Url: %CPAN Test-SharedFork
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl-Test-Requires

%description
Test::SharedFork is utility module for Test::Builder. This module makes
forking test!
This module merges test count with parent process & child process.

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test/SharedFork*
%doc Changes README.md

%changelog
* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Fri Jul 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- automated CPAN update

* Mon Jun 30 2014 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Fri Jul 06 2012 Vladimir Lettiev <crux@altlinux.ru> 0.20-alt1
- New version 0.20
- Added perl-Test-Requires test dependency

* Thu Mar 03 2011 Vladimir Lettiev <crux@altlinux.ru> 0.16-alt1
- New version 0.16
- Updated buildrequires

* Mon Sep 20 2010 Vladimir Lettiev <crux@altlinux.ru> 0.15-alt1
- New version 0.15

* Mon Aug 30 2010 Vladimir Lettiev <crux@altlinux.ru> 0.12-alt1
- initial build
