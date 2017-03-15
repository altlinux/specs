%define _unpackaged_files_terminate_build 1
%define dist MooseX-Has-Sugar
Name: perl-%dist
Version: 1.000006
Release: alt1

Summary: Sugar Syntax for moose 'has' fields
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/K/KE/KENTNL/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Apr 25 2011
BuildRequires: perl-Module-Build perl-MooseX-Types perl-Test-Fatal perl-namespace-autoclean

%description
Moose "has" syntax is generally fine, but sometimes one gets bothered
with the constant typing of string quotes for things.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/MooseX

%changelog
* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.000006-alt1
- automated CPAN update

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 1.000004-alt1.1
- rebuild to restore role requires

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.000004-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.000002-alt1
- automated CPAN update

* Mon Jun 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.000001-alt1
- automated CPAN update

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.000000-alt1
- automated CPAN update

* Thu Nov 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.05070422-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.05070421-alt1
- automated CPAN update

* Mon Apr 25 2011 Alexey Tourbin <at@altlinux.ru> 0.05070419-alt1
- initial revision
