%define dist Test-Warn
Name: perl-%dist
Version: 0.32
Release: alt1

Summary: Perl extension to test methods for warnings
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/B/BI/BIGJ/Test-Warn-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Apr 23 2011
BuildRequires: perl-Sub-Uplevel perl-Test-Pod perl-Tree-DAG_Node

%description
This module provides a few convenience methods for testing warning based code.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Test

%changelog
* Thu Dec 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- automated CPAN update

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- automated CPAN update

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- automated CPAN update

* Tue Sep 11 2012 Vladimir Lettiev <crux@altlinux.ru> 0.24-alt1
- 0.23 -> 0.24
- fixed build with Carp >= 1.25

* Sat Apr 23 2011 Alexey Tourbin <at@altlinux.ru> 0.23-alt1
- 0.21 -> 0.23

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Nov 13 2009 Michael Bochkaryov <misha@altlinux.ru> 0.21-alt1
- 0.21 version
- Changes and README files added to docs

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1.1
- NMU fixing directory ownershop violation

* Wed Jun 11 2008 Michael Bochkaryov <misha@altlinux.ru> 0.10-alt1
- first build for ALT Linux Sisyphus
