Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-MooseX-MarkAsMethods
Version:        0.15
Release:        alt1_20
Summary:        Mark overload code symbols as methods
License:        LGPLv2+
URL:            http://metacpan.org/release/MooseX-MarkAsMethods/
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSRCHBOY/MooseX-MarkAsMethods-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl(B/Hooks/EndOfScope.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Moose.pm)
BuildRequires:  perl(Moose/Exporter.pm)
BuildRequires:  perl(Moose/Util/MetaRole.pm)
BuildRequires:  perl(Moose/Role.pm)
BuildRequires:  perl(namespace/autoclean.pm)
# Tests only:
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(Test/Moose.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info

%description
MooseX::MarkAsMethods allows one to easily mark certain functions as Moose
methods. This will allow other packages such as namespace::autoclean to
operate without blowing away your overloads. After using
MooseX::MarkAsMethods your overloads will be recognized by Class::MOP as
being methods, and class extension as well as composition from roles with
overloads will "just work".

%prep
%setup -q -n MooseX-MarkAsMethods-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_20
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_16
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_14
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_13
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_12
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_11
- update to new release by fcimport

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_10.1
- rebuild to restore role requires

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_10
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_9
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_4
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_3
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_2
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_2
- fc import

