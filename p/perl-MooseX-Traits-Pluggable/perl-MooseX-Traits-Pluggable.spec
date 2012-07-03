%define dist MooseX-Traits-Pluggable
Name: perl-%dist
Version: 0.10
Release: alt1

Summary: Trait loading and resolution for Moose
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/R/RK/RKITOVER/MooseX-Traits-Pluggable-0.10.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Apr 20 2010
BuildRequires: perl-Class-C3-XS perl-Module-Install perl-Moose perl-Test-Exception perl-namespace-autoclean

%description
Use new_with_traits to construct an object with a list of traits and
apply_traits to apply traits to an instance.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/MooseX*

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Tue Apr 20 2010 Alexey Tourbin <at@altlinux.ru> 0.09-alt1
- initial revision
