# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-ExtUtils-Typemaps-Default
Version:        1.05
Release:        alt2_6
Summary:        Set of useful typemaps
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/ExtUtils-Typemaps-Default/
Source0:        http://www.cpan.org/authors/id/S/SM/SMUELLER/ExtUtils-Typemaps-Default-%{version}.tar.gz
BuildArch:      noarch
# temporary fix until more recent version is available
BuildRequires:  perl(ExtUtils/Typemaps.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Test/More.pm)
Requires:       perl(ExtUtils/Typemaps.pm) >= 3.18

# Filtering unversioned requires

Source44: import.info
%filter_from_requires /^perl\\(ExtUtils.Typemaps.pm\\)$/d

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
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
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

