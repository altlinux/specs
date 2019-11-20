Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-ExtUtils-Typemaps-Default
Version:        1.05
Release:        alt2_16
Summary:        Set of useful typemaps
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/ExtUtils-Typemaps-Default
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/ExtUtils-Typemaps-Default-%{version}.tar.gz
BuildArch:      noarch
# temporary fix until more recent version is available
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/Typemaps.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Test/More.pm)
Requires:       perl(ExtUtils/Typemaps.pm) >= 3.180

# Filtering unversioned requires

Source44: import.info
%filter_from_requires /^perl(ExtUtils.Typemaps.pm)/d

%description
ExtUtils::Typemaps::Default is an ExtUtils::Typemaps subclass that provides
a set of default mappings (in addition to what perl itself provides). These
default mappings are currently defined as the combination of the mappings
provided by the following typemap classes which are provided in this
distribution:

ExtUtils::Typemaps::ObjectMap
ExtUtils::Typemaps::STL
ExtUtils::Typemaps::Basic

%prep
%setup -q -n ExtUtils-Typemaps-Default-%{version}

# this is fixed in BuildRequired version of ExtUtils::Typemap 3.18-292
sed -i 's/3.18_03/3.18/' Build.PL

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0

# %{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.05-alt2_16
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.05-alt2_12
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.05-alt2_10
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.05-alt2_9
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.05-alt2_8
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.05-alt2_7
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.05-alt2_6
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.05-alt2_5
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt2_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt2_2
- update to new release by fcimport

* Wed Feb 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt2_1
- moved to Sisyphus for Slic3r (by dd@ request)

* Tue Dec 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1_1
- update to new release by fcimport

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_1
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_5
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_4
- initial fc import

