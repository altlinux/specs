%define dist Test-Number-Delta
Name: perl-%dist
Version: 1.03
Release: alt2

Summary: Compare the difference between numbers against a given tolerance
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 04 2011
BuildRequires: perl-devel

%description
At some point or another, most programmers find they need to compare
floating-point numbers for equality. The typical idiom is to test if
the absolute value of the difference of the numbers is within a
desired tolerance, usually called epsilon. This module provides such
functions (delta_within and delta_ok) for use with Test::Harness.
Usage is similar to other test functions described in Test::More.

%prep
%setup -q -n %dist-%version
mv Build.PL Build.PL.orig

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Test

%changelog
* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 1.03-alt2
- rebuilt

* Mon Jun 18 2007 Alexey Tourbin <at@altlinux.ru> 1.03-alt1
- initial revision (for perl-Cairo test suite)
