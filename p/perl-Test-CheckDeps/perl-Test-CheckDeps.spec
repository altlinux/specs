%define _unpackaged_files_terminate_build 1
BuildRequires: perl(Module/Build.pm)
BuildRequires: perl(Module/Build/Tiny.pm)
%define dist Test-CheckDeps
Name: perl-%dist
Version: 0.007
Release: alt1

Summary: Check for presence of dependencies
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/L/LE/LEONT/Test-CheckDeps-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Sep 26 2012
BuildRequires: perl-CPAN-Meta-Check perl-Test-Script

%description
This module adds a test that assures all dependencies have been installed
properly.  If requested, it can bail out all testing on error.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Test

%changelog
* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1
- automated CPAN update

* Wed Jul 31 2013 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- automated CPAN update

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 0.002-alt1
- initial revision
