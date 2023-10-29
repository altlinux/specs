%define _unpackaged_files_terminate_build 1

Name: perl-Test-MockRandom
Version: 1.01
Release: alt4
Summary: Replaces random number generation with non-random number generation
License: Apache-2.0
Group: Development/Perl
Url: https://github.com/dagolden/Test-MockRandom
Source: %name-%version.tar
BuildArch: noarch

BuildRequires:  perl(ExtUtils/MakeMaker.pm)

%description
This perhaps ridiculous-seeming module was created to test routines that
manipulate random numbers by providing a known output from rand. Given a
list of seeds with srand, it will return each in turn. After seeded
random numbers are exhausted, it will always return 0. Seed numbers must
be of a form that meets the expected output from rand as called with no
arguments -- i.e. they must be between 0 (inclusive) and 1 (exclusive).
In order to facilitate generating and testing a nearly-one number, this
module exports the function oneish, which returns a number just
fractionally less than one.

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

rm %buildroot%perl_vendor_archlib/auto/Test/MockRandom/.packlist

%files
%doc CONTRIBUTING Changes examples README
%perl_vendorlib/T*

%changelog
* Sun Oct 29 2023 Igor Vlasenko <viy@altlinux.org> 1.01-alt4
- set BuildArch: noarch

* Fri Aug 27 2021 Alexandr Antonov <aas@altlinux.org> 1.01-alt3
- release greater for autoimports

* Fri Aug 27 2021 Alexandr Antonov <aas@altlinux.org> 1.01-alt1
- initial build for ALT
