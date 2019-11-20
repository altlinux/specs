Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Module-CPANTS-Analyse
Version:        1.01
Release:        alt1_1
Summary:        Generate Kwalitee ratings for a distribution
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Module-CPANTS-Analyse
Source0:        https://cpan.metacpan.org/modules/by-module/Module/Module-CPANTS-Analyse-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(ExtUtils/MakeMaker/CPANfile.pm)
# Module Runtime
BuildRequires:  perl(Archive/Any/Lite.pm)
BuildRequires:  perl(Archive/Tar.pm)
BuildRequires:  perl(Array/Diff.pm)
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Class/Accessor.pm)
BuildRequires:  perl(Class/Accessor/Fast.pm)
BuildRequires:  perl(CPAN/DistnameInfo.pm)
BuildRequires:  perl(CPAN/Meta/Converter.pm)
BuildRequires:  perl(CPAN/Meta/Validator.pm)
BuildRequires:  perl(CPAN/Meta/YAML.pm)
BuildRequires:  perl(Data/Binary.pm)
BuildRequires:  perl(Encode.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/Manifest.pm)
BuildRequires:  perl(File/Basename.pm)
BuildRequires:  perl(File/Copy.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Find/Object.pm)
BuildRequires:  perl(File/Spec/Functions.pm)
BuildRequires:  perl(File/stat.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(JSON/PP.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Module/CPANfile.pm)
BuildRequires:  perl(Perl/PrereqScanner/NotQuiteLite.pm)
BuildRequires:  perl(Module/Find.pm)
BuildRequires:  perl(Software/License.pm)
BuildRequires:  perl(Software/LicenseUtils.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Text/Balanced.pm)
BuildRequires:  perl(version.pm)
BuildRequires:  perl(warnings.pm)
# Test Suite
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(File/Path.pm)
BuildRequires:  perl(FindBin.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Test/FailWarnings.pm)
BuildRequires:  perl(Test/More.pm)
# Runtime
Requires:       perl(Archive/Any/Lite.pm) >= 0.060
Requires:       perl(Archive/Tar.pm) >= 1.760
Requires:       perl(Array/Diff.pm) >= 0.040
Requires:       perl(Class/Accessor.pm) >= 0.190
Requires:       perl(CPAN/DistnameInfo.pm) >= 0.060
Requires:       perl(CPAN/Meta/Validator.pm) >= 2.133.380
Requires:       perl(CPAN/Meta/YAML.pm) >= 0.008
Requires:       perl(Exporter.pm)
Requires:       perl(File/Find/Object.pm) >= 0.2.1
Requires:       perl(JSON/PP.pm)
Requires:       perl(Module/CPANfile.pm)
Requires:       perl(Software/License.pm) >= 0.103.012
Requires:       perl(version.pm) >= 0.730

# Filter underspecified dependencies








Source44: import.info
%filter_from_requires /:__requires_exclude\|}^perl(Archive.Any.Lite.pm)/d
%filter_from_requires /^perl(Array.Diff.pm)/d
%filter_from_requires /^perl(Class.Accessor.pm)/d
%filter_from_requires /^perl(CPAN.DistnameInfo.pm)/d
%filter_from_requires /^perl(CPAN.Meta.Validator.pm)/d
%filter_from_requires /^perl(CPAN.Meta.YAML.pm)/d
%filter_from_requires /^perl(File.Find.Object.pm)/d
%filter_from_requires /^perl(version.pm)/d

%description
CPANTS is an acronym for CPAN Testing Service. The goals of the CPANTS project
are to provide some sort of quality measure (called "Kwalitee") and lots of
metadata for all distributions on CPAN.

%prep
%setup -q -n Module-CPANTS-Analyse-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
# %{_fixperms} -c %{buildroot}

%files
%doc AUTHORS Changes README.md TODO
%dir %{perl_vendor_privlib}/Module/
%dir %{perl_vendor_privlib}/Module/CPANTS/
%{perl_vendor_privlib}/Module/CPANTS/Analyse.pm
%{perl_vendor_privlib}/Module/CPANTS/Kwalitee.pm
%dir %{perl_vendor_privlib}/Module/CPANTS/Kwalitee/
%{perl_vendor_privlib}/Module/CPANTS/Kwalitee/*.pm

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_1
- update to new release by fcimport

* Thu Aug 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- automated CPAN update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1_1
- update to new release by fcimport

* Mon Feb 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- automated CPAN update

* Sat Feb 09 2019 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1_1
- update to new release by fcimport

* Mon Jan 21 2019 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1
- automated CPAN update

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.96-alt1_10
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.96-alt1_8
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.96-alt1_7
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.96-alt1_6
- update to new release by fcimport

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

