%define _unpackaged_files_terminate_build 1
%define dist B-Hooks-EndOfScope
Name: perl-%dist
Version: 0.24
Release: alt1

Summary: Execute code after a scope finished compilation
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/E/ET/ETHER/%{dist}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: perl-Module-Install perl-Sub-Exporter-Progressive perl-Variable-Magic perl-Module-Implementation perl-Module-Runtime

%description
This module allows you to execute code when perl finished compiling the
surrounding scope.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/B/Hooks/EndOfScope*

%changelog
* Wed Apr 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- automated CPAN update

* Mon Feb 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Tue Jun 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Thu Jun 13 2013 Vladimir Lettiev <crux@altlinux.ru> 0.12-alt1
- 0.12

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

* Mon Apr 12 2010 Alexey Tourbin <at@altlinux.ru> 0.08-alt1
- initial revision, for namespace::clean
