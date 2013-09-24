%define _unpackaged_files_terminate_build 1
%define dist CPAN-Meta-Requirements
Name: perl-%dist
Version: 2.125
Release: alt1

Summary: a set of version requirements for a CPAN dist
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DA/DAGOLDEN/CPAN-Meta-Requirements-%{version}.tar.gz

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
* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 2.125-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.123-alt1
- automated CPAN update

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 2.122-alt1
- initial revision
