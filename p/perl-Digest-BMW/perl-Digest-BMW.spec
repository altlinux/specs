%define module_version 0.04
%define module_name Digest-BMW
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel perl(Benchmark.pm) perl(Crypt/RIPEMD160.pm) perl(Digest.pm) perl(Digest/base.pm) perl(DynaLoader.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(List/Util.pm) perl(MIME/Base64.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(parent.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.04
Release: alt3.1.1.1
Summary: Perl interface to the Blue Midnight Wish digest algorithm
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/G/GR/GRAY/%{module_name}-%{module_version}.tar.gz

%description
The `Digest::BMW' module provides an interface to the Blue Midnight Wish
message digest algorithm. Blue Midgnight Wish is a candidate in the NIST
SHA-3 competition.

This interface follows the conventions set forth by the `Digest' module.


%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_archlib/D*
%perl_vendor_autolib/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt3.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt3.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.04-alt3.1
- rebuild with new perl 5.22.0

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.04-alt3
- to Sisyphus

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.04-alt2
- rebuild to get rid of unmets

* Mon Oct 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- initial import by package builder

