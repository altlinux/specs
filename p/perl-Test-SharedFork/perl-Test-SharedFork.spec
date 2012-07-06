Name: perl-Test-SharedFork
Version: 0.20
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
%doc Changes README 

%changelog
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
