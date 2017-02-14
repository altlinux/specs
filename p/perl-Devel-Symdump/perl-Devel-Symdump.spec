%define _unpackaged_files_terminate_build 1
%define dist Devel-Symdump
Name: perl-%dist
Version: 2.18
Release: alt1

Summary: Perl module for inspecting Perl's symbol table
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/A/AN/ANDK/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 04 2011
BuildRequires: perl-Test-Pod

%description
The perl module Devel::Symdump provides a convenient way to inspect
perl's symbol table and the class hierarchie within a running program.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Devel

%changelog
* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 2.18-alt1
- automated CPAN update

* Wed Apr 20 2016 Igor Vlasenko <viy@altlinux.ru> 2.17-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 2.15-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 2.14-alt1
- automated CPAN update

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1
- automated CPAN update

* Fri Nov 01 2013 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1
- automated CPAN update

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1
- automated CPAN update

* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 2.08-alt2
- rebuilt

* Thu Apr 24 2008 Alexey Tourbin <at@altlinux.ru> 2.08-alt1
- 2.03 -> 2.08

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.03-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Sep 23 2003 Alexey Tourbin <at@altlinux.ru> 2.03-alt2
- descriptions updated

* Fri Nov 01 2002 Stanislav Ievlev <inger@altlinux.ru> 2.03-alt1
- Inital Release for ALT
