%define dist CPAN-Meta-Requirements
Name: perl-%dist
Version: 2.122
Release: alt1

Summary: a set of version requirements for a CPAN dist
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# split from this package
Conflicts: perl-CPAN-Meta < 2.120921

# Automatically added by buildreq on Wed Sep 26 2012
BuildRequires: perl-Test-Script

%description
A CPAN::Meta::Requirements object models a set of version constraints like
those specified in the META.yml or META.json files in CPAN distributions.
It can be built up by adding more and more constraints, and it will reduce
them to the simplest representation.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/CPAN

%changelog
* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 2.122-alt1
- initial revision
