BuildRequires: perl(Software/LicenseUtils.pm)
%define _unpackaged_files_terminate_build 1
%define dist Parallel-Iterator
Name: perl-%dist
Version: 1.001
Release: alt1

Summary: Simple parallel execution
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/A/AR/ARISTOTLE/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 12 2011
BuildRequires: perl-Module-Build

%description
This module provides a 'parallel map'. Multiple worker processes are
forked so that many instances of the transformation function may be
executed simultaneously.

%prep
%setup -q -n %{dist}-%{version}
rm boilerplate.pl

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README examples
%perl_vendor_privlib/Parallel

%changelog
* Sat Jul 16 2022 Igor Vlasenko <viy@altlinux.org> 1.001-alt1
- automated CPAN update

* Wed Oct 12 2011 Alexey Tourbin <at@altlinux.ru> 1.00-alt1
- initial revision, for perl-Devel-Cover
