# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    CACertOrg-CA
%define upstream_version 20210114.001

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_1

Summary:    CACert.org's CA root certificate in PEM format
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/release/%{upstream_name}
Source0:    https://cpan.metacpan.org/modules/by-module/CACertOrg/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/Spec/Functions.pm)
BuildRequires: perl(Test/More.pm)
BuildArch:  noarch
Source44: import.info

%description
CACertOrg::CA provides a copy of Certificate Authority certificate for
CACert.org. This is the Class 1 PKI Key.

sha1 13:5C:EC:36:F4:9C:B8:E9:3B:1A:B2:70:CD:80:88:46:76:CE:8F:33

md5 A6:1B:37:5E:39:0D:9C:36:54:EE:BD:20:31:46:1F:6B

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor

%make_build

%check
%make_build test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.json META.yml 
%perl_vendor_privlib/*

%changelog
* Sat Feb 27 2021 Igor Vlasenko <viy@altlinux.org> 20210114.001-alt1_1
- update by mgaimport

* Thu Jan 21 2021 Igor Vlasenko <viy@altlinux.ru> 20210114.001-alt1
- automated CPAN update

* Tue Jun 12 2018 Igor Vlasenko <viy@altlinux.ru> 20110724.005-alt1
- automated CPAN update

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 20110724.004-alt2_5
- update by mgaimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 20110724.004-alt2_4
- update by mgaimport

* Thu Oct 16 2014 Igor Vlasenko <viy@altlinux.ru> 20110724.004-alt2_3
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 20110724.004-alt2_2
- update by mgaimport

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 20110724.004-alt2_1
- moved to Sysiphus as dependency

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 20110724.004-alt1_1
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 20110724.001-alt1_3
- mga update

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 20110724.001-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 20110724.001-alt1_1
- converted for ALT Linux by srpmconvert tools

