%define dist Module-Metadata
Name: perl-%dist
Version: 1.000011
Release: alt1

Summary: Gather package and POD information from perl module files
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

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
* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 1.000011-alt1
- 1.000007 -> 1.000011

* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 1.000007-alt1
- initial revision
