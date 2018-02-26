%define dist DBD-CSV
Name: perl-%dist
Version: 0.33
Release: alt1

Summary: DBI driver for CSV files
License: GPL or Artistic
Group: Development/Perl

URL: http://search.cpan.org/dist/DBD-CSV/
Source: http://www.cpan.org/authors/id/H/HM/HMBRAND/DBD-CSV-0.33.tgz

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
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_privlib/DBD

%changelog
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
