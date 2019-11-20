Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Class-Mix
Summary:        Dynamic class mixing
Version:        0.006
Release:        alt1_7
License:        GPL+ or Artistic
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Class-Mix-%{version}.tar.gz
URL:            https://metacpan.org/release/Class-Mix
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(if.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(mro.pm)
BuildRequires:  perl(Params/Classify.pm)
BuildRequires:  perl(parent.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)

Requires:       perl(mro.pm)

# obsolete/provide old tests subpackage
# can be removed during F19 development cycle
Obsoletes:      %{name}-tests < 0.005-3
Provides:       %{name}-tests = %{version}-%{release}


Source44: import.info

%description
The mix_class function provided by this module dynamically generates
'anonymous' classes with specified inheritance.

%prep
%setup -q -n Class-Mix-%{version}

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README t/
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1_7
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1_3
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1_1
- update to new release by fcimport

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- automated CPAN update

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.005-alt2_15
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.005-alt2_14
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.005-alt2_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.005-alt2_12
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.005-alt2_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.005-alt2_9
- update to new release by fcimport

* Sat Mar 29 2014 Igor Vlasenko <viy@altlinux.ru> 0.005-alt2_8
- moved to Sisyphus as dependency

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1_8
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1_7
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1_6
- update to new release by fcimport

* Wed Aug 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1_5
- new release

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1_3
- fc import

