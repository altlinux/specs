# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Test/More.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    CACertOrg-CA
%define upstream_version 20110724.004

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt2_4

Summary:    CACert.org's CA root certificate in PEM format
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CACertOrg/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
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
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.json META.yml  README
%perl_vendor_privlib/*

%changelog
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

