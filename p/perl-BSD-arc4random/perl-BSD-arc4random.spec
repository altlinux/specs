%define dist BSD-arc4random

Name: perl-%dist
Version: 1.50
Release: alt1

Summary: This module provides a Perl API for the BSDs' arc4random(3) suite of functions
License: %perl_license
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildRequires: rpm-build-licenses

# Automatically added by buildreq on Thu Feb 18 2016
# optimized out: perl-threads
BuildRequires: perl-Encode perl-devel

%description
This module provides a Perl API for the BSDs' arc4random(3) suite
of functions and adds a few high-level functions, such as the new
arc4random_uniform(3). The Perl functions are ithreads-safe (only
if threads::shared is required). Scalars can be tied to this pak-
kage, yielding uniformly distributed random numbers with an arbi-
trary upper bound on read access, contributing to the RC4 entropy
pool on write access. An exported global $RANDOM variable returns
15-bit unsigned random numbers, from [0; 32767], similar to mksh.
Furthermore, Perl's internal PRNG is seeded with entropy obtained
from the arc4random generator once on module load time.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc TODO README
%perl_vendor_archlib/BSD
%perl_vendor_autolib/BSD

%changelog
* Thu Feb 18 2016 Sergey Y. Afonin <asy@altlinux.ru> 1.50-alt1
- initial build
