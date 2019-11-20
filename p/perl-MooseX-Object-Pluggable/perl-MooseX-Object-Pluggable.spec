Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Module/Build.pm) perl(Module/Runtime.pm) perl(Scalar/Util.pm) perl(Try/Tiny.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-MooseX-Object-Pluggable
Version:        0.0014
Release:        alt2_14
Summary:        Make your Moose classes pluggable
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/MooseX-Object-Pluggable
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Object-Pluggable-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  rpm-build-perl
BuildRequires:  perl(Dist/Zilla.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Module/Pluggable/Object.pm)
BuildRequires:  perl(Moose.pm)
BuildRequires:  perl(namespace/autoclean.pm)
BuildRequires:  perl(CPAN/Meta.pm)
BuildRequires:  perl(CPAN/Meta/Requirements.pm)
BuildRequires:  perl(Module/Build/Tiny.pm)
BuildRequires:  perl(Test/Fatal.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)


# keep rpmlint happy
Requires:       perl(strict.pm), perl(warnings.pm), perl(Moose.pm)


Source44: import.info

%description
This module aids in the development and deployment of plugin-enabled
Moose-based classes. It extends the Moose framework via roles to enable
this behavior.

%prep
%setup -q -n MooseX-Object-Pluggable-%{version}

perl -pi -e 's|^#!perl|#!/usr/bin/perl|; s|^#!/usr/local|#!/usr|' t/*.t

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} %{buildroot}/*

%check
AUTHOR_TESTING=1 make test

%files
%doc Changes README
%doc --no-dereference LICENSE
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.0014-alt2_14
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.0014-alt2_10
- update to new release by fcimport

* Sun Nov 05 2017 Igor Vlasenko <viy@altlinux.ru> 0.0014-alt2_8
- to Sisyphus as perl-PDL dep

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.0014-alt1_8
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.0014-alt1_7
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.0014-alt1_6
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.0014-alt1_5
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.0014-alt1_4
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.0014-alt1_3
- update to new release by fcimport

* Wed Apr 08 2015 Igor Vlasenko <viy@altlinux.ru> 0.0014-alt1_1
- update to new release by fcimport

* Tue Dec 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.0013-alt1_1
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.0011-alt1_15
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.0011-alt1_14
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.0011-alt1_13
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.0011-alt1_12
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.0011-alt1_11
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.0011-alt1_10
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.0011-alt1_8
- fc import

