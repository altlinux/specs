%define dist MooseX-SemiAffordanceAccessor
Name: perl-%dist
Version: 0.09
Release: alt1

Summary: Name your accessors foo() and set_foo()
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DR/DROLSKY/MooseX-SemiAffordanceAccessor-0.09.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Apr 13 2010
BuildRequires: perl-Class-C3-XS perl-Module-Build perl-Moose

%description
This module does not provide any methods. Simply loading it changes
the default naming policy for the loading class so that accessors are
separated into get and set methods. The get methods have the same name
as the accessor, while set methods are prefixed with "set_".

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
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

* Fri Jul 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Tue Apr 13 2010 Alexey Tourbin <at@altlinux.ru> 0.05-alt1
- initial revision
