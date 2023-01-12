%define _unpackaged_files_terminate_build 1
%define dist DBD-CSV
Name: perl-%dist
Version: 0.60
Release: alt1

Summary: DBI driver for CSV files
License: GPL or Artistic
Group: Development/Perl

URL: http://search.cpan.org/dist/DBD-CSV/
Source0: http://www.cpan.org/authors/id/H/HM/HMBRAND/%{dist}-%{version}.tgz

BuildArch: noarch

# Automatically added by buildreq on Sun Feb 13 2011
BuildRequires: perl-DBD-File perl-Test-Pod perl-Test-Pod-Coverage perl-Text-CSV_XS perl-unicore

%description
The DBD::CSV module is yet another driver for the DBI (Database independent
interface for Perl). This one is based on the SQL "engine" SQL::Statement
and the abstract DBI driver DBD::File and implements access to so-called
CSV files (Comma separated values). Such files are mostly used for exporting
MS Access and MS Excel data.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README CONTRIBUTING.md examples
%perl_vendor_privlib/DBD
%perl_vendor_privlib/Bundle/*

%changelog
* Thu Jan 12 2023 Igor Vlasenko <viy@altlinux.org> 0.60-alt1
- automated CPAN update

* Sat Jan 08 2022 Igor Vlasenko <viy@altlinux.org> 0.59-alt1
- automated CPAN update

* Tue Feb 16 2021 Igor Vlasenko <viy@altlinux.ru> 0.58-alt1
- automated CPAN update

* Fri Dec 25 2020 Igor Vlasenko <viy@altlinux.ru> 0.57-alt1
- automated CPAN update

* Fri Dec 11 2020 Igor Vlasenko <viy@altlinux.ru> 0.56-alt1
- automated CPAN update

* Tue Sep 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1
- automated CPAN update

* Tue Oct 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1
- automated CPAN update

* Wed May 23 2018 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1
- automated CPAN update

* Thu Apr 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1
- automated CPAN update

* Mon Mar 26 2018 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1
- automated CPAN update

* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1
- automated CPAN update

* Fri May 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.49-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1
- automated CPAN update

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1
- automated CPAN update

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1
- automated CPAN update

* Mon Sep 16 2013 Vladimir Lettiev <crux@altlinux.ru> 0.41-alt1
- 0.36 -> 0.41

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- automated CPAN update

* Sun Feb 13 2011 Alexey Tourbin <at@altlinux.ru> 0.31-alt1
- 0.22 -> 0.31

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1.1
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Mon Jul 14 2008 Michael Bochkaryov <misha@altlinux.ru> 0.22-alt1
- first build for ALT Linux Sisyphus
