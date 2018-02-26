%define dist MooseX-MethodAttributes
Name: perl-%dist
Version: 0.25
Release: alt1

Summary: code attribute introspection
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/B/BO/BOBTFISH/MooseX-MethodAttributes-0.25.tar.gz

BuildArch: noarch

# XXX inimported Moose functions
%add_findreq_skiplist */MooseX/MethodAttributes/Role/Meta/Role.pm

# Automatically added by buildreq on Sun Jan 16 2011
BuildRequires: perl-MooseX-Types perl-Test-Exception perl-namespace-autoclean

%description
This module allows code attributes of methods to be introspected using
Moose meta method objects.

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
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Sun Jan 16 2011 Alexey Tourbin <at@altlinux.ru> 0.24-alt1
- 0.23 -> 0.24

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- automated CPAN update

* Thu Jun 10 2010 Alexey Tourbin <at@altlinux.ru> 0.22-alt1
- 0.20 -> 0.22

* Wed Apr 14 2010 Alexey Tourbin <at@altlinux.ru> 0.20-alt1
- initial revision
