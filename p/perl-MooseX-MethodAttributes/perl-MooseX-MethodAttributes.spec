%define _unpackaged_files_terminate_build 1
%define dist MooseX-MethodAttributes
Name: perl-%dist
Version: 0.31
Release: alt1.1

Summary: code attribute introspection
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/E/ET/ETHER/MooseX-MethodAttributes-%{version}.tar.gz

BuildArch: noarch

# XXX inimported Moose functions
%add_findreq_skiplist */MooseX/MethodAttributes/Role/Meta/Role.pm
%add_findreq_skiplist */MooseX/MethodAttributes/Role.pm
%add_findreq_skiplist */MooseX/MethodAttributes.pm

# Automatically added by buildreq on Sun Jan 16 2011
BuildRequires: perl-MooseX-Types perl-Test-Exception perl-namespace-autoclean perl(Test/CheckDeps.pm) perl(Module/Build/Tiny.pm) perl(Test/Fatal.pm) perl(Test/Requires.pm) perl(MooseX.pm) perl(Class/MOP/Package.pm)

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
* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1.1
- rebuild to restore role requires

* Thu Oct 29 2015 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- automated CPAN update

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

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
