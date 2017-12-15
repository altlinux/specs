%define module_version 0.06
%define module_name Digest-GOST
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel perl(Benchmark.pm) perl(Crypt/RIPEMD160.pm) perl(Digest.pm) perl(Digest/base.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(List/Util.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(parent.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.06
Release: alt3.1.1.1
Summary: Perl interface to the GOST R 34.11-94 digest algorithm
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/G/GR/GRAY/%{module_name}-%{module_version}.tar.gz

%description
The `Digest::GOST' module provides an interface to the GOST R 34.11-94
message digest algorithm.

This interface follows the conventions set forth by the `Digest' module.

This module uses the default "test" parameters. To use the CryptoPro
parameters, use `Digest::GOST::CryptoPro'.


%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/D*
%perl_vendor_autolib/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.06-alt3.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.06-alt3.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.06-alt3.1
- rebuild with new perl 5.22.0

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.06-alt3
- to Sisyphus

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.06-alt2
- rebuild to get rid of unmets

* Mon Oct 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- initial import by package builder

