# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(FindBin.pm) perl(IO/Capture/Stderr.pm) perl(IO/Capture/Stdout.pm) perl(Module/Build.pm) perl(Module/CPANfile.pm) perl(Pod/Usage.pm) perl(base.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Module-CPANTS-Analyse
Version:        0.92
Release:        alt2_1
Summary:        Generate Kwalitee ratings for a distribution
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Module-CPANTS-Analyse/
Source0:        http://search.cpan.org/CPAN/authors/id/I/IS/ISHIGAKI/Module-CPANTS-Analyse-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Archive/Any/Lite.pm)
BuildRequires:  perl(Archive/Tar.pm)
BuildRequires:  perl(Array/Diff.pm)
BuildRequires:  perl(Class/Accessor.pm)
BuildRequires:  perl(CPAN/DistnameInfo.pm)
BuildRequires:  perl(CPAN/Meta/Validator.pm)
BuildRequires:  perl(CPAN/Meta/YAML.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Basename.pm)
BuildRequires:  perl(File/Find/Rule/VCS.pm)
BuildRequires:  perl(File/Spec/Functions.pm)
BuildRequires:  perl(File/stat.pm)
BuildRequires:  perl(IO/Capture.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Module/ExtractUse.pm)
BuildRequires:  perl(Module/Pluggable.pm)
BuildRequires:  perl(Set/Scalar.pm)
BuildRequires:  perl(Software/License.pm)
BuildRequires:  perl(Software/LicenseUtils.pm)
BuildRequires:  perl(Test/Deep.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/NoWarnings.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
BuildRequires:  perl(Test/Warn.pm)
BuildRequires:  perl(Text/Balanced.pm)
BuildRequires:  perl(version.pm)
BuildRequires:  perl(YAML/Any.pm)
Requires:       perl(Archive/Any/Lite.pm) >= 0.06
Requires:       perl(Archive/Tar.pm) >= 1.48
Requires:       perl(Array/Diff.pm) >= 0.04
Requires:       perl(Class/Accessor.pm) >= 0.19
Requires:       perl(CPAN/DistnameInfo.pm) >= 0.06
Requires:       perl(IO/Capture.pm) >= 0.05
Requires:       perl(Module/ExtractUse.pm) >= 0.30
Requires:       perl(Module/Pluggable.pm) >= 2.96
Requires:       perl(version.pm) >= 0.73
Source44: import.info

%description
CPANTS is an acronym for CPAN Testing Service. The goals of the CPANTS project
are to provide some sort of quality measure (called "Kwalitee") and lots of
metadata for all distributions on CPAN.

%prep
%setup -q -n Module-CPANTS-Analyse-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
# %{_fixperms} $RPM_BUILD_ROOT

%files
%doc Changes README TODO
%{_bindir}/cpants_lint.pl
%dir %{perl_vendor_privlib}/Module/
%dir %{perl_vendor_privlib}/Module/CPANTS/
%{perl_vendor_privlib}/Module/CPANTS/Analyse.pm
%{perl_vendor_privlib}/Module/CPANTS/Kwalitee.pm
%dir %{perl_vendor_privlib}/Module/CPANTS/Kwalitee/
%{perl_vendor_privlib}/Module/CPANTS/Kwalitee/*.pm
%{_mandir}/man1/cpants_lint.pl.1*

%changelog
* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.92-alt2_1
- Sisyphus build

* Tue Nov 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.92-alt1_1
- update to new release by fcimport

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_1
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.89-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.89-alt1_1
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.87-alt1_1
- update to new release by fcimport

* Thu Dec 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.86-alt1_4
- new fc rel

* Sun May 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.85-alt1_11
- fc import

