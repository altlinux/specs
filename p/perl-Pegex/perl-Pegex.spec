Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(IO/All.pm) perl(Mo.pm) perl(Term/ANSIColor.pm) perl(Test/Pod.pm) perl(Text/Diff.pm) perl(XXX.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Pegex
Version:        0.70
Release:        alt1_5
Summary:        Pegex Parser Generator
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Pegex
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Pegex-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  perl(File/ShareDir/Install.pm)
# Run-time
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(JSON/XS.pm) perl(JSON/PP.pm)
BuildRequires:  perl(overload.pm)
BuildRequires:  perl(re.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(YAML/XS.pm)
# Tests
BuildRequires:  perl(base.pm)
BuildRequires:  perl(File/Basename.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Test/More.pm)
# TestML not used
# TestML::Compiler::Lite not used
Requires:       perl(Data/Dumper.pm)
Requires:       perl(JSON/XS.pm) perl(JSON/PP.pm)
Requires:       perl(warnings.pm)
Requires:       perl(YAML/XS.pm)
Source44: import.info

%description
Pegex is a Acmeist parser framework. It is a PEG parser grammar syntax,
combined with PCRE compatible regular expressions as the match tokens.
Pegex draws heavily from Perl 6 rules, but works equivalently in many
modern programming languages.

%prep
%setup -q -n Pegex-%{version}
## Remove bundled modules
#rm -r ./inc
#sed -i '63,$ d' Makefile.PL
sed -i -e '/^inc\//d' MANIFEST

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
#rm -f t/compiler-checks.t t/compiler-equivalence.t t/compiler.t t/error.t t/optimize.t t/tree-pegex.t t/tree.t
make test

%files
%doc Changes CONTRIBUTING LICENSE README
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.70-alt1_5
- update to new release by fcimport

* Mon Dec 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.70-alt1_2
- update to new release by fcimport

* Tue Nov 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.70-alt1
- automated CPAN update

* Wed Oct 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.67-alt1
- automated CPAN update

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.64-alt1
- automated CPAN update

* Sun Jan 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.63-alt1
- automated CPAN update

* Sat Jan 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1
- automated CPAN update

* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.61-alt1
- automated CPAN update

* Tue Dec 08 2015 Igor Vlasenko <viy@altlinux.ru> 0.60-alt2_4
- to Sisyphus

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1_4
- update to new release by fcimport

* Wed Apr 08 2015 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1_1
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1_3
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1_1
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_4
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_2
- update to new release by fcimport

* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_7
- update to new release by fcimport

* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_5
- fc import

