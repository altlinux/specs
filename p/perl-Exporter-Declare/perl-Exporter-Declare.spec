Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Exporter-Declare
Version:        0.114
Release:        alt2_12
Summary:        Exporting done right
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Exporter-Declare
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Exporter-Declare-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(aliased.pm)
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(Fennec/Lite.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Meta/Builder.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Simple.pm)
BuildRequires:  perl(warnings.pm)
Requires:       perl(Meta/Builder.pm) >= 0.003

# Remove underspecified dependencies

Source44: import.info
%filter_from_requires /^perl(Meta.Builder\\)\s*$/d


%description
Exporter::Declare is a meta-driven exporting tool. Exporter::Declare tries
to adopt all the good features of other exporting tools, while throwing
away horrible interfaces. Exporter::Declare also provides hooks that allow
you to add options and arguments for import. Finally, Exporter::Declare's
meta-driven system allows for top-notch introspection.

%prep
%setup -q -n Exporter-Declare-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc README
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.114-alt2_12
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.114-alt2_8
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.114-alt2_6
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.114-alt2_5
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.114-alt2_4
- update to new release by fcimport

* Mon Sep 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.114-alt2_3
- to Sisyphus

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.114-alt1_3
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.114-alt1_2
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.114-alt1_1
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.113-alt1_5
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.113-alt1_4
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.113-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.113-alt1_2
- update to new release by fcimport

* Fri Jun 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.113-alt1_1
- update to new release by fcimport

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.112-alt1_1
- update to new release by fcimport

* Wed May 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.109-alt1_1
- initial fc import

