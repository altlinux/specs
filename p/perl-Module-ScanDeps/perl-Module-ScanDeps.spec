# BEGIN SourceDeps(oneline):
BuildRequires: perl(IPC/Run3.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
%define dist Module-ScanDeps
Name: perl-%dist
Version: 1.34
Release: alt1

Summary: Recursively scan Perl programs for dependencies
License: GPLv2+ or Artistic-2.0
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/R/RS/RSCHUPP/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Module-Build perl-Module-Pluggable perl-Term-Cap perl-Test-Pod perl-parent perl-threads perl-unicore perl(Test/Requires.pm) perl(Net/FTP.pm)

%description
An application of Module::ScanDeps is to generate executables from
scripts that contains necessary modules; this module supports two
such projects, PAR and App::Packer.

%prep
%setup -q -n %{dist}-%{version}
[ %version = 1.31 ] && rm t/18-findbin.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc AUTHORS Changes README
%_bindir/scandeps.pl
%_man1dir/scandeps.*
%perl_vendor_privlib/Module

%changelog
* Mon Sep 25 2023 Igor Vlasenko <viy@altlinux.org> 1.34-alt1
- automated CPAN update

* Sat Aug 05 2023 Igor Vlasenko <viy@altlinux.org> 1.33-alt1
- automated CPAN update

* Fri Jul 28 2023 Igor Vlasenko <viy@altlinux.org> 1.32-alt1
- automated CPAN update

* Mon Oct 11 2021 Igor Vlasenko <viy@altlinux.org> 1.31-alt1
- automated CPAN update

* Thu Feb 18 2021 Igor Vlasenko <viy@altlinux.org> 1.30-alt1
- automated CPAN update

* Sun Nov 01 2020 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1
- automated CPAN update

* Mon Jan 21 2019 Igor Vlasenko <viy@altlinux.ru> 1.27-alt1
- automated CPAN update

* Thu Dec 13 2018 Igor Vlasenko <viy@altlinux.ru> 1.26-alt1
- automated CPAN update

* Tue Aug 21 2018 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1
- automated CPAN update

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1
- automated CPAN update

* Thu Apr 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1
- automated CPAN update

* Thu Nov 13 2014 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1
- automated CPAN update

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1
- automated CPAN update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1
- automated CPAN update

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1
- automated CPAN update

* Sun Dec 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1
- automated CPAN update

* Tue Dec 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Mon Sep 30 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1
- automated CPAN update

* Tue Oct 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1
- automated CPAN update

* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 1.05-alt1
- 1.04 -> 1.05
- disabled build dependency on perl-Module-Install

* Wed Oct 26 2011 Alexey Tourbin <at@altlinux.ru> 1.04-alt1
- 0.96 -> 1.04

* Mon Apr 05 2010 Alexey Tourbin <at@altlinux.ru> 0.96-alt1
- 0.89 -> 0.96

* Tue Nov 04 2008 Alexey Tourbin <at@altlinux.ru> 0.89-alt1
- 0.83 -> 0.89

* Thu Apr 24 2008 Alexey Tourbin <at@altlinux.ru> 0.83-alt1
- 0.51 -> 0.83

* Sat Sep 10 2005 Alexey Tourbin <at@altlinux.ru> 0.51-alt1
- initial revision
