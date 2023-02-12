%define _unpackaged_files_terminate_build 1
%define module Graph

Name: perl-Graph
Version: 0.9726
Release: alt1

Summary: Graph - Perl module for dealing with graphs
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source0: http://www.cpan.org/authors/id/E/ET/ETJ/%{module}-%{version}.tar.gz

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch

# Automatically added by buildreq on Mon Aug 09 2010
BuildRequires: perl-Storable perl-Test-Pod perl-Test-Pod-Coverage perl(Heap/Fibonacci.pm) perl(Set/Object.pm)
BuildRequires: perl-Math-Complex

%description
Perl module for dealing with graphs, the abstract data structures.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/*
%exclude %perl_vendor_archlib

%changelog
* Sun Feb 12 2023 Igor Vlasenko <viy@altlinux.org> 0.9726-alt1
- automated CPAN update

* Mon Oct 11 2021 Igor Vlasenko <viy@altlinux.org> 0.9725-alt1
- automated CPAN update

* Fri Sep 17 2021 Igor Vlasenko <viy@altlinux.org> 0.9724-alt1
- automated CPAN update

* Wed Sep 01 2021 Igor Vlasenko <viy@altlinux.org> 0.9723-alt1
- automated CPAN update

* Sun Jul 11 2021 Igor Vlasenko <viy@altlinux.org> 0.9722-alt1
- automated CPAN update

* Wed Apr 21 2021 Igor Vlasenko <viy@altlinux.org> 0.9721-alt1
- automated CPAN update

* Wed Mar 31 2021 Igor Vlasenko <viy@altlinux.org> 0.9720-alt1
- automated CPAN update

* Mon Mar 15 2021 Igor Vlasenko <viy@altlinux.org> 0.9718-alt1
- automated CPAN update

* Mon Feb 01 2021 Igor Vlasenko <viy@altlinux.ru> 0.9717-alt1
- automated CPAN update

* Wed Jan 06 2021 Igor Vlasenko <viy@altlinux.ru> 0.9716-alt1
- automated CPAN update

* Fri Dec 25 2020 Igor Vlasenko <viy@altlinux.ru> 0.9714-alt1
- automated CPAN update

* Fri Dec 11 2020 Igor Vlasenko <viy@altlinux.ru> 0.9712-alt1
- automated CPAN update

* Tue Dec 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.9711-alt1
- automated CPAN update

* Mon Nov 23 2020 Igor Vlasenko <viy@altlinux.ru> 0.9709-alt1
- automated CPAN update

* Sun Nov 08 2020 Igor Vlasenko <viy@altlinux.ru> 0.9708-alt1
- automated CPAN update

* Sun Nov 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.9707-alt1
- automated CPAN update

* Sat Oct 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.9706-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.9704-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.96-alt1
- automated CPAN update

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 0.94-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Aug 09 2010 Victor Forsiuk <force@altlinux.org> 0.94-alt2
- Fix FTBFS by updating BuildRequires.

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.94-alt1
- automated CPAN update

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.84-alt1.1
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Mon Apr 21 2008 Michael Bochkaryov <misha@altlinux.ru> 0.84-alt1
- first build for ALT Linux Sisyphus

