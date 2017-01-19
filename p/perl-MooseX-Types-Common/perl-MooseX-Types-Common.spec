%define _unpackaged_files_terminate_build 1
BuildRequires: perl(Module/Build/Tiny.pm)
%define dist MooseX-Types-Common
Name: perl-%dist
Version: 0.001014
Release: alt1

Summary: A library of commonly used type constraints
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/E/ET/ETHER/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 14 2010
BuildRequires: perl-Class-C3-XS perl-Module-Install perl-MooseX-Types perl-Test-Exception perl(Test/Fatal.pm) perl(Test/CheckDeps.pm) perl(Test/Warnings.pm) perl(Test/Deep.pm)

%description
A set of commonly-used type constraints that do not ship with Moose by default.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/MooseX*

%changelog
* Thu Jan 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.001014-alt1
- automated CPAN update

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.001013-alt1.1
- rebuild to restore role requires

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.001013-alt1
- automated CPAN update

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.001012-alt1
- automated CPAN update

* Sat Sep 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.001010-alt1
- automated CPAN update

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.001009-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.001008-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.001003-alt1
- automated CPAN update

* Wed Apr 14 2010 Alexey Tourbin <at@altlinux.ru> 0.001002-alt1
- initial revision
