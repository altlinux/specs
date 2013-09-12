%define _unpackaged_files_terminate_build 1
%define dist Module-Metadata
Name: perl-%dist
Version: 1.000018
Release: alt1

Summary: Gather package and POD information from perl module files
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/E/ET/ETHER/Module-Metadata-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Sep 26 2012
BuildRequires: perl-Encode perl-devel

%description
This module provides a standard way to gather metadata about a .pm file
without executing unsafe code.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Module

%changelog
* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.000018-alt1
- automated CPAN update

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.000016-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.000014-alt1
- automated CPAN update

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 1.000011-alt1
- 1.000007 -> 1.000011

* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 1.000007-alt1
- initial revision
