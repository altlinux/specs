%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel libssl-devel perl(AutoLoader.pm) perl(Crypt/OpenSSL/EC.pm) perl(DynaLoader.pm) perl(Exporter.pm) perl(ExtUtils/Constant.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(XSLoader.pm)
# END SourceDeps(oneline)
%define module_version 0.08
%define module_name Crypt-OpenSSL-ECDSA
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.08
Release: alt2.1
Summary: Perl extension for OpenSSL ECDSA (Elliptic Curve Digital Signature Algorithm)
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/M/MI/MIKEM/Crypt-OpenSSL-ECDSA-%{version}.tar.gz
Patch0: 0001-Port-to-OpenSSL-1.1.0.patch

%description
From summary: %summary

%prep
%setup -n %{module_name}-%{module_version}
%patch0 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/C*
%perl_vendor_autolib/*

%changelog
* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2.1
- rebuild with new perl 5.28.1

* Thu Sep 13 2018 Anton Farygin <rider@altlinux.ru> 0.08-alt2
- rebuilt with openssl 1.1

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1.1
- rebuild with new perl 5.24.1

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1.1
- rebuild with new perl 5.22.0

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- to Sisyphus

