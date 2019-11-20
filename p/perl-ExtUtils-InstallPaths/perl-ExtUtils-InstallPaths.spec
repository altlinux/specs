Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		perl-ExtUtils-InstallPaths
Version:	0.012
Release:	alt1_7
Summary:	Build.PL install path logic made easy
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/ExtUtils-InstallPaths
Source0:	https://cpan.metacpan.org/modules/by-module/ExtUtils/ExtUtils-InstallPaths-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	rpm-build-perl
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
# Module
BuildRequires:	perl(Carp.pm)
BuildRequires:	perl(ExtUtils/Config.pm)
BuildRequires:	perl(File/Spec.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(warnings.pm)
# Test Suite
BuildRequires:	perl(Config.pm)
BuildRequires:	perl(File/Spec/Functions.pm)
BuildRequires:	perl(File/Temp.pm)
BuildRequires:	perl(Test/More.pm)
Source44: import.info
# Runtime

%description
This module tries to make install path resolution as easy as possible.

When you want to install a module, it needs to figure out where to install
things. The nutshell version of how this works is that default installation
locations are determined from ExtUtils::Config, and they may be individually
overridden by using the install_path attribute. An install_base attribute lets
you specify an alternative installation root like /home/foo and prefix does
something similar in a rather different (and more complicated) way. destdir
lets you specify a temporary installation directory like /tmp/install in case
you want to create bundled-up installable packages.

%prep
%setup -q -n ExtUtils-InstallPaths-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
# %{_fixperms} -c %{buildroot}

%check
make test

%files
%if 0%{?_licensedir:1}
%doc --no-dereference LICENSE
%else
%doc LICENSE
%endif
%doc Changes
%{perl_vendor_privlib}/ExtUtils/

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1_7
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1_2
- update to new release by fcimport

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1_1
- update to new release by fcimport

* Thu May 17 2018 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1
- automated CPAN update

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_11
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_10
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_8
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_7
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_4
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_1
- update to new release by fcimport

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1_2
- update to new release by fcimport

* Fri Nov 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1_1
- update to new release by fcimport

* Fri Nov 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- automated CPAN update

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1_5
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1_4
- update to new release by fcimport

* Mon Jul 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1_3
- converted for ALT Linux by srpmconvert tools

