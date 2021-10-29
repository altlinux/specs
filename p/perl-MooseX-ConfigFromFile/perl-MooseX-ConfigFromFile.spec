Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Module/Build.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define fontpkgname perl-MooseX-ConfigFromFile
Name:           perl-MooseX-ConfigFromFile
Version:        0.14
Release:        alt3_23
License:        GPL+ or Artistic
Summary:        An abstract Moose role for setting attributes from a configfile
URL:            https://metacpan.org/release/MooseX-ConfigFromFile
Source:         https://cpan.metacpan.org/modules/by-module/MooseX/MooseX-ConfigFromFile-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl(Module/Build/Tiny.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  sed
# Module Runtime
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Moose/Role.pm)
BuildRequires:  perl(MooseX/Types/Moose.pm)
BuildRequires:  perl(MooseX/Types/Path/Tiny.pm)
BuildRequires:  perl(namespace/autoclean.pm)
BuildRequires:  perl(warnings.pm)
# Test Suite
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(if.pm)
BuildRequires:  perl(Moose.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Test/Deep.pm)
BuildRequires:  perl(Test/Fatal.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Requires.pm)
BuildRequires:  perl(Test/Without/Module.pm)
# Optional Test Requirements
BuildRequires:  perl(CPAN/Meta.pm)
BuildRequires:  perl(CPAN/Meta/Prereqs.pm)
BuildRequires:  perl(MooseX/Getopt.pm)
# Dependencies

# Avoid doc-file dependencies from tests

Source44: import.info

%description
This is an abstract role which provides an alternate constructor for
creating objects using parameters passed in from a configuration file. The
actual implementation of reading the configuration file is left to concrete
subroles.

It declares an attribute 'configfile' and a class method 'new_with_config',
and requires that concrete roles derived from it implement the class method
'get_config_from_file'.

Attributes specified directly as arguments to 'new_with_config' supersede
those in the configfile.

%prep
%setup -q -n MooseX-ConfigFromFile-%{version}

# Fix shellbangs in tests to placate rpmlint
sed -i '1s,#!perl,#!%{__perl},' t/*.t

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0

%check
./Build test

%files
%doc --no-dereference LICENSE
%doc Changes CONTRIBUTING README t/
%{perl_vendor_privlib}/MooseX/

%changelog
* Fri Oct 29 2021 Igor Vlasenko <viy@altlinux.org> 0.14-alt3_23
- to Siayphus for ALT bugzilla

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 0.14-alt2_23
- update to new release by fcimport

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 0.14-alt2_22
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 0.14-alt2_21
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_20
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_20
- update to new release by fcimport

* Mon Jul 06 2020 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_19
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_18
- update to new release by fcimport

* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_17
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_16
- update to new release by fcimport

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_15
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_13
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_12
- update to new release by fcimport

* Sun Jul 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_11
- update to new release by fcimport

* Wed Apr 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_9
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_8
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_7
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_5
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_4
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_2
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_1
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_5
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_3
- update to new release by fcimport

* Wed May 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_2
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_7
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_5
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_4
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_2
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_2
- fc import

