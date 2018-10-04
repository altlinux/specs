Name:           perl-Authen-Simple
Version:        0.5
Release:        alt2
Summary:        Simple Authentication
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/Authen-Simple/
Source0:        http://www.cpan.org/authors/id/C/CH/CHANSEN/Authen-Simple-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(inc/Module/Install.pm)
BuildRequires:  perl(Module/Install/Metadata.pm)
BuildRequires:  perl(Module/Install/ReadmeFromPod.pm)
BuildRequires:  perl(Module/Install/WriteAll.pm)
BuildRequires:  perl(strict.pm)
# Run-time
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Class/Accessor/Fast.pm)
BuildRequires:  perl(Class/Data/Inheritable.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Crypt/PasswdMD5.pm)
BuildRequires:  perl(Digest/MD5.pm)
BuildRequires:  perl(Digest/SHA.pm)
BuildRequires:  perl(IO/Handle.pm)
BuildRequires:  perl(MIME/Base64.pm)
BuildRequires:  perl(Params/Validate.pm)
BuildRequires:  perl(warnings.pm)
# Tests
BuildRequires:  perl(IO/File.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Test/More.pm)
#BuildRequires:  apache2-mod_perl

%add_findreq_skiplist %perl_vendor_privlib/Authen/Simple/Apache.pm

%description
Simple and consistent framework for authentication.

%prep
%setup -q -n Authen-Simple-%{version}

# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Thu Oct 04 2018 Andrey Cherepanov <cas@altlinux.org> 0.5-alt2
- Initial build for Sisyphus.

* Mon Feb 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_16
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_13
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_12
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_11
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_10
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_7
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_5
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_4
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_3
- update to new release by fcimport

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_1
- fc import

