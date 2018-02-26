%define dist Module-Install-ExtraTests
Name: perl-%dist
Version: 0.007
Release: alt1

Summary: contextual tests that the harness can ignore
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 13 2011 (-bi)
BuildRequires: perl-Module-Install

%description
This plugin adds one Module::Install command:

  extra_tests;

This declares that the test files found in the directory ./xt should be run
only in certain instances:

  ./xt/author  - run when the tests are being run in an author's working copy
  ./xt/smoke   - run when the dist is being smoked (AUTOMATED_TESTING=1)
  ./xt/release - run during "make disttest"

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Module

%changelog
* Fri Nov 11 2011 Alexey Tourbin <at@altlinux.ru> 0.007-alt1
- 0.006 -> 0.007

* Wed Mar 24 2010 Alexey Tourbin <at@altlinux.ru> 0.006-alt1
- initial revision
