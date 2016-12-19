Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
#TODO: BR:/R: perl(WorePAN) a.. 0.09 when available

Name:           perl-Module-CPANTS-Analyse
Version:        0.96
Release:        alt1_5
Summary:        Generate Kwalitee ratings for a distribution
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Module-CPANTS-Analyse/
Source0:        http://search.cpan.org/CPAN/authors/id/I/IS/ISHIGAKI/Module-CPANTS-Analyse-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(ExtUtils/MakeMaker/CPANfile.pm)
# Module Runtime
BuildRequires:  perl(Archive/Any/Lite.pm)
BuildRequires:  perl(Array/Diff.pm)
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Class/Accessor.pm)
BuildRequires:  perl(CPAN/DistnameInfo.pm)
BuildRequires:  perl(CPAN/Meta/Converter.pm)
BuildRequires:  perl(CPAN/Meta/Validator.pm)
BuildRequires:  perl(CPAN/Meta/YAML.pm)
BuildRequires:  perl(Encode.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(File/Basename.pm)
BuildRequires:  perl(File/Copy.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Find/Object.pm)
BuildRequires:  perl(File/Spec/Functions.pm)
BuildRequires:  perl(File/stat.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(IO/Capture.pm)
BuildRequires:  perl(IO/Capture/Stderr.pm)
BuildRequires:  perl(IO/Capture/Stdout.pm)
BuildRequires:  perl(JSON/MaybeXS.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Module/CPANfile.pm)
BuildRequires:  perl(Module/ExtractUse.pm)
BuildRequires:  perl(Module/Pluggable.pm)
BuildRequires:  perl(Set/Scalar.pm)
BuildRequires:  perl(Software/License.pm)
BuildRequires:  perl(Software/License/CC_BY_SA_3_0.pm)
BuildRequires:  perl(Software/LicenseUtils.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Text/Balanced.pm)
BuildRequires:  perl(version.pm)
BuildRequires:  perl(warnings.pm)
# Test Suite
BuildRequires:  perl(Archive/Tar.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(File/Path.pm)
BuildRequires:  perl(FindBin.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Test/FailWarnings.pm)
BuildRequires:  perl(Test/More.pm)
# Release Tests (author tests not run as they are prone to failing)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
# Runtime
Requires:       perl(Archive/Any/Lite.pm) >= 0.06
Requires:       perl(Archive/Tar.pm) >= 1.48
Requires:       perl(Array/Diff.pm) >= 0.04
Requires:       perl(Class/Accessor.pm) >= 0.19
Requires:       perl(CPAN/DistnameInfo.pm) >= 0.06
Requires:       perl(CPAN/Meta/Validator.pm) >= 2.133.380
Requires:       perl(CPAN/Meta/YAML.pm) >= 0.008
Requires:       perl(Exporter.pm)
Requires:       perl(File/Find/Object.pm) >= 0.2.1
Requires:       perl(IO/Capture.pm) >= 0.05
Requires:       perl(Module/CPANfile.pm)
Requires:       perl(Module/Pluggable.pm) >= 2.96
Requires:       perl(Software/License.pm) >= 0.103.008
Requires:       perl(Software/License/CC_BY_SA_3_0.pm)
Requires:       perl(version.pm) >= 0.73

# Filter underspecified dependencies









Source44: import.info
%filter_from_requires /:__requires_exclude|}^perl\\(Archive.Any.Lite.pm\\)$/d
%filter_from_requires /^perl\\(Array.Diff.pm\\)$/d
%filter_from_requires /^perl\\(Class.Accessor.pm\\)$/d
%filter_from_requires /^perl\\(CPAN.DistnameInfo.pm\\)$/d
%filter_from_requires /^perl\\(CPAN.Meta.Validator.pm\\)$/d
%filter_from_requires /^perl\\(CPAN.Meta.YAML.pm\\)$/d
%filter_from_requires /^perl\\(File.Find.Object.pm\\)$/d
%filter_from_requires /^perl\\(Module.Pluggable.pm\\)$/d
%filter_from_requires /^perl\\(version.pm\\)$/d

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
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
# %{_fixperms} %{buildroot}

%files
%doc AUTHORS Changes README TODO
%dir %{perl_vendor_privlib}/Module/
%dir %{perl_vendor_privlib}/Module/CPANTS/
%{perl_vendor_privlib}/Module/CPANTS/Analyse.pm
%{perl_vendor_privlib}/Module/CPANTS/Kwalitee.pm
%dir %{perl_vendor_privlib}/Module/CPANTS/Kwalitee/
%{perl_vendor_privlib}/Module/CPANTS/Kwalitee/*.pm

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.96-alt1_5
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.96-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.96-alt1_3
- update to new release by fcimport

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.96-alt1_1
- update to new release by fcimport

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.96-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.95-alt1_2
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.92-alt2_2
- update to new release by fcimport

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

