%define dist Version-Requirements
Name: perl-%dist
Version: 0.101022
Release: alt1

Summary: A set of version requirements for a CPAN dist
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/R/RJ/RJBS/Version-Requirements-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Apr 28 2011
BuildRequires: perl-devel

%description
A Version::Requirements object models a set of version constraints like
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
%perl_vendor_privlib/Version

%changelog
* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.101022-alt1
- automated CPAN update

* Thu Apr 28 2011 Alexey Tourbin <at@altlinux.ru> 0.101020-alt1
- initial revision
