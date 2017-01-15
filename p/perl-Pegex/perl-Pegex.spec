%define _unpackaged_files_terminate_build 1
%define perl_bootstrap 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Capture/Tiny.pm) perl(File/Path.pm) perl(FindBin.pm) perl(IO/All.pm) perl(Mo.pm) perl(Safe.pm) perl(Test/Builder.pm) perl(Test/Pod.pm) perl(Text/Diff.pm) perl(Time/HiRes.pm) perl-devel perl-podlators perl(XXX.pm)
# END SourceDeps(oneline)
Name:           perl-Pegex
Version:        0.63
Release:        alt1
Summary:        Pegex Parser Generator
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Pegex/
Source0:        http://www.cpan.org/authors/id/I/IN/INGY/Pegex-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  perl(File/ShareDir/Install.pm)
# Run-time
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(JSON/XS.pm)
BuildRequires:  perl(overload.pm)
BuildRequires:  perl(re.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(YAML/XS.pm)
# Tests
BuildRequires:  perl(base.pm)
BuildRequires:  perl(File/Basename.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Test/More.pm)
%if !%{defined perl_bootstrap}
# Break dependency cycle: perl-Pegex a.. perl-TestML a.. perl-Pegex
BuildRequires:  perl(TestML.pm)
BuildRequires:  perl(TestML/Bridge.pm)
BuildRequires:  perl(TestML/Compiler/Lite.pm)
BuildRequires:  perl(TestML/Util.pm)
%endif
Requires:       perl(Data/Dumper.pm)
Requires:       perl(JSON/XS.pm)
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
# Remove bundled modules
rm -r ./inc
sed -i -e '/^inc\//d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
%if %{defined perl_bootstrap}
# Break dependency cycle: perl-Pegex → perl-TestML → perl-Pegex
make test TEST_FILES="$(find t -name '*.t' \
    \! -exec grep -q -e 'use TestML' {} \; -print | tr \"\\n\" ' ')"
%else
make test
%endif

%files
%doc Changes CONTRIBUTING LICENSE README
%{perl_vendor_privlib}/*

%changelog
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

