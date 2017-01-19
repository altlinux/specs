%define dist MooseX-Traits-Pluggable
Name: perl-%dist
Version: 0.12
Release: alt1.2

Summary: Trait loading and resolution for Moose
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/R/RK/RKITOVER/MooseX-Traits-Pluggable-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Apr 20 2010
BuildRequires: perl-Class-C3-XS perl-Module-Install perl-Moose perl-Test-Exception perl-namespace-autoclean perl(List/MoreUtils.pm)

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
* Thu Jan 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1.2
- fixed build

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1.1
- rebuild to restore role requires

* Tue Jan 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated CPAN update

* Thu Jan 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Tue Apr 20 2010 Alexey Tourbin <at@altlinux.ru> 0.09-alt1
- initial revision
