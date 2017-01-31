# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(AutoLoader.pm) perl(Exporter.pm) perl(MIME/Base64.pm) perl-podlators
# END SourceDeps(oneline)
Name:           perl-LWP-Authen-Negotiate
Version:        0.08
Release:        alt2_10
Summary:        GSSAPI based Authentication Plugin for LWP
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/LWP-Authen-Negotiate/
Source0:        http://www.cpan.org/modules/by-module/LWP/LWP-Authen-Negotiate-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(GSSAPI.pm)
BuildRequires:  perl(LWP/Debug.pm)
BuildRequires:  perl(Test/More.pm)
Requires:       perl(GSSAPI.pm) >= 0.18
Requires:       perl(LWP/Debug.pm)
Source44: import.info

%description
WWW-Negotiate supporting Webservers are IIS or Apache with 
mod_auth_kerb for example.


%prep
%setup -q -n LWP-Authen-Negotiate-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

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

