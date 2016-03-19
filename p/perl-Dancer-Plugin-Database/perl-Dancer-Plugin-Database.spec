%define _unpackaged_files_terminate_build 1
Name: perl-Dancer-Plugin-Database
Version: 2.12
Release: alt1
Summary: Dancer::Plugin::Database - easy database connections for Dancer applications

Group: Development/Perl
License: Perl
Url: %CPAN Dancer-Plugin-Database

BuildArch: noarch
Source: http://www.cpan.org/authors/id/A/AM/AMBS/Dancer-Plugin-Database-%{version}.tar.gz
BuildRequires: perl-devel perl-DBI perl-Dancer perl(Dancer/Plugin/Database/Core.pm)

%description
%summary

%prep
%setup -q -n Dancer-Plugin-Database-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Dancer/Plugin/Database*
%doc Changes README 

%changelog
* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1
- automated CPAN update

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1
- automated CPAN update

* Fri Dec 19 2014 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1
- automated CPAN update

* Fri Sep 28 2012 Vladimir Lettiev <crux@altlinux.ru> 2.01-alt1
- 1.81 -> 2.01

* Tue Apr 10 2012 Vladimir Lettiev <crux@altlinux.ru> 1.81-alt1
- New version 1.81

* Thu Dec 15 2011 Vladimir Lettiev <crux@altlinux.ru> 1.51-alt1
- New version 1.51

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.42-alt1
- automated CPAN update

* Mon Feb 28 2011 Vladimir Lettiev <crux@altlinux.ru> 1.20-alt1
- initial build
