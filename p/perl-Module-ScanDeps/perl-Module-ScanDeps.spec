%define _unpackaged_files_terminate_build 1
%define dist Module-ScanDeps
Name: perl-%dist
Version: 1.23
Release: alt1

Summary: Recursively scan Perl programs for dependencies
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/R/RS/RSCHUPP/Module-ScanDeps-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Module-Build perl-Module-Pluggable perl-Term-Cap perl-Test-Pod perl-parent perl-threads perl-unicore perl(Test/Requires.pm)

%description
An application of Module::ScanDeps is to generate executables from
scripts that contains necessary modules; this module supports two
such projects, PAR and App::Packer.

%prep
%setup -q -n %dist-%version

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
