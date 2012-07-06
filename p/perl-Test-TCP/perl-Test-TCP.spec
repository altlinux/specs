Name: perl-Test-TCP
Version: 1.16
Release: alt1

Summary: Test::TCP - testing TCP program
Group: Development/Perl
License: Perl

Url: %CPAN Test-TCP
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl-Test-SharedFork

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
%doc Changes README 

%changelog
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
