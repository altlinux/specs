%define _unpackaged_files_terminate_build 1
Name: perl-System-Command
Version: 1.122
Release: alt1

Summary: System::Command - Object for running system commands
License: Perl
Group: Development/Perl

Url: %CPAN System-Command
# Cloned from git://github.com/book/System-Command.git
Source0: http://www.cpan.org/authors/id/B/BO/BOOK/System-Command-%{version}.tar.gz

BuildRequires: perl-devel perl-Module-Build
BuildArch: noarch

%description
%summary

%prep
%setup -q -n System-Command-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/System/Command*
%doc Changes README

%changelog
* Thu Feb 09 2023 Igor Vlasenko <viy@altlinux.org> 1.122-alt1
- automated CPAN update

* Fri Jun 05 2020 Igor Vlasenko <viy@altlinux.ru> 1.121-alt1
- automated CPAN update

* Thu Apr 05 2018 Igor Vlasenko <viy@altlinux.ru> 1.119-alt1
- automated CPAN update

* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.118-alt1
- automated CPAN update

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.117-alt1
- automated CPAN update

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.115-alt1
- automated CPAN update

* Fri Dec 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.110-alt1
- automated CPAN update

* Tue Aug 06 2013 Vladimir Lettiev <crux@altlinux.ru> 1.103-alt1
- 1.103

* Fri Sep 28 2012 Vladimir Lettiev <crux@altlinux.ru> 1.07-alt1
- 1.0.4 -> 1.0.7

* Fri Jun 17 2011 Vladimir Lettiev <crux@altlinux.ru> 1.04-alt1
- New version 1.0.4

* Thu Jun 02 2011 Vladimir Lettiev <crux@altlinux.ru> 1.03-alt1
- initial build
