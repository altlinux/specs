%define m_distro Test-SharedFork
Name: perl-Test-SharedFork
Version: 0.16
Release: alt1
Summary: Test::SharedFork - fork test

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~tokuhirom/Test-SharedFork/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel

%description
Test::SharedFork is utility module for Test::Builder. This module makes
forking test!
This module merges test count with parent process & child process.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test/SharedFork*
%doc Changes README 

%changelog
* Thu Mar 03 2011 Vladimir Lettiev <crux@altlinux.ru> 0.16-alt1
- New version 0.16
- Updated buildrequires

* Mon Sep 20 2010 Vladimir Lettiev <crux@altlinux.ru> 0.15-alt1
- New version 0.15

* Mon Aug 30 2010 Vladimir Lettiev <crux@altlinux.ru> 0.12-alt1
- initial build
