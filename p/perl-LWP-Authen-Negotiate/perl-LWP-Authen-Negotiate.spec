Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(AutoLoader.pm) perl(Exporter.pm) perl(MIME/Base64.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-LWP-Authen-Negotiate
Version:        0.08
Release:        alt2_20
Summary:        GSSAPI based Authentication Plugin for LWP
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/LWP-Authen-Negotiate
Source0:        https://cpan.metacpan.org/modules/by-module/LWP/LWP-Authen-Negotiate-%{version}.tar.gz
# Allow requesting a mutual authentication without a delegation, bug #1685192,
# CPAN RT#128699,
Patch0:         LWP-Authen-Negotiate-0.08-Add-LWP_AUTHEN_NEGOTIATE_MUTUAL-environment-variable.patch
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(GSSAPI.pm)
BuildRequires:  perl(LWP/Debug.pm)
BuildRequires:  perl(Test/More.pm)
Requires:       perl(GSSAPI.pm) >= 0.180
Requires:       perl(LWP/Debug.pm)
Source44: import.info

%description
WWW-Negotiate supporting Webservers are IIS or Apache with 
mod_auth_kerb for example.


%prep
%setup -q -n LWP-Authen-Negotiate-%{version}
%patch0 -p1

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install

make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2_20
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2_15
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2_13
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2_12
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2_11
- update to new release by fcimport

* Tue Jan 31 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2_10
- to Sisyphus

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_10
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_9
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_8
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_6
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_5
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_4
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_3
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_2
- initial fc import

