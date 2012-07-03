%define dist ExtUtils-PkgConfig
Name: perl-%dist
Version: 1.12
Release: alt2

Summary: Perl interface to the pkg-config(1) command-line utility
License: LGPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

Requires: pkg-config

# Automatically added by buildreq on Tue Oct 04 2011
BuildRequires: perl-devel

%description
This module is a simplistic Perl interface to the pkg-config command-line
utility, for use in the Makefile.PLs used to build Perl modules which wrap
the libraries about which pkg-config knows.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/ExtUtils

%changelog
* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 1.12-alt2
- rebuilt

* Fri Dec 05 2008 Alexey Tourbin <at@altlinux.ru> 1.12-alt1
- 1.11 -> 1.12

* Thu Sep 25 2008 Alexey Tourbin <at@altlinux.ru> 1.11-alt1
- 1.05 -> 1.11

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.05-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Jul 30 2004 Alexey Tourbin <at@altlinux.ru> 1.05-alt1
- 1.03 -> 1.05

* Wed Feb 18 2004 Alexey Tourbin <at@altlinux.ru> 1.03-alt1
- 1.03

* Tue Nov 18 2003 Alexey Tourbin <at@altlinux.ru> 1.02-alt1
- 1.02

* Tue Oct 28 2003 Alexey Tourbin <at@altlinux.ru> 1.01-alt1
- 1.01

* Fri Oct 03 2003 Alexey Tourbin <at@altlinux.ru> 1.00-alt1
- initial revision
