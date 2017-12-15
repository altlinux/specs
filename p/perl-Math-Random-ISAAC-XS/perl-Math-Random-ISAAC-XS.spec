Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Benchmark.pm) perl(Chart/Bars.pm) perl(Config.pm) perl(Test/Valgrind.pm) perl(XSLoader.pm) perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Math-Random-ISAAC-XS
Version:        1.004
Release:        alt4_11.1.1.1.1
Summary:        C implementation of the ISAAC PRNG algorithm
License:        MIT or GPL+ or Artistic
URL:            http://search.cpan.org/dist/Math-Random-ISAAC-XS/
Source0:        http://www.cpan.org/authors/id/J/JA/JAWNSY/Math-Random-ISAAC-XS-%{version}.tar.gz
BuildRequires:  perl(ExtUtils/CBuilder.pm)
BuildRequires:  perl(ExtUtils/ParseXS.pm)
BuildRequires:  perl(Math/Random/ISAAC.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Test/LeakTrace.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/NoWarnings.pm)
Requires:       perl(Math/Random/ISAAC.pm)


Source44: import.info

%description
This module implements the same interface as Math::Random::ISAAC in C and can
be used as a drop-in replacement. This is the recommended implementation of the
module, based on Bob Jenkins' reference implementation in C.

%prep
%setup -q -n Math-Random-ISAAC-XS-%{version}
# rm -f weaver.ini dist.ini
sed -i 's/\r//' examples/*.pl

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes examples LICENSE README
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/Math*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.004-alt4_11.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.004-alt4_11.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.004-alt4_11.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.004-alt4_11.1
- rebuild with new perl 5.20.1

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.004-alt4_11
- update to new release by fcimport

* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.004-alt4_10
- build for Sisyphus (required for perl update)

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 1.004-alt3_10
- rebuild to get rid of unmets

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.004-alt2_10
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.004-alt2_9
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.004-alt2_8
- update to new release by fcimport

* Wed Jan 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.004-alt2_7
- update to new release by fcimport

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 1.004-alt2_6
- rebuild with new perl

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1_6
- update to new release by fcimport

* Tue May 29 2012 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1_4
- fc import

