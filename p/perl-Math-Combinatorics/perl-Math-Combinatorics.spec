# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Data/Dumper.pm) perl(Exporter.pm) perl(Test/More.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Math-Combinatorics
%define upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt3_7

Summary:    Perform combinations and permutations on lists
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Math/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildArch: noarch
Source44: import.info

%description
Combinatorics is the branch of mathematics studying the enumeration,
combination, and permutation of sets of elements and the mathematical
relations that characterize their properties. As a jumping off point, refer
to:

 http://mathworld.wolfram.com/Combinatorics.html

This module provides a pure-perl implementation of nCk, nCRk, nPk, nPRk, !n
and n! (combination, multiset, permutation, string, derangement, and
factorial, respectively). Functional and object-oriented usages allow
problems such as the following to be solved:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes META.yml
%perl_vendor_privlib/*




%changelog
* Mon Mar 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.09-alt3_7
- to Sisyphus

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_7
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_6
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_4
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 0.09-alt2_3
- rebuild to get rid of unmets

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_3
- mga update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_1
- converted for ALT Linux by srpmconvert tools

