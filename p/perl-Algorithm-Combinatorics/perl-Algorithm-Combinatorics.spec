# BEGIN SourceDeps(oneline):
BuildRequires: perl(Benchmark.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(FindBin.pm) perl(List/PowerSet.pm) perl(Math/Combinatorics.pm) perl(Scalar/Util.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(base.pm)
# END SourceDeps(oneline)
%define module_version 0.27
%define module_name Algorithm-Combinatorics
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.27
Release: alt3.1.1
Summary: Efficient generation of combinatorial sequences
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/F/FX/FXN/%module_name-%module_version.tar.gz

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_archlib/A*
%perl_vendor_autolib/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.27-alt3.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.27-alt3.1
- rebuild with new perl 5.24.1

* Mon Mar 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.27-alt3
- to Sisyphus

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.27-alt2.1
- rebuild with perl 5.22

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.27-alt2
- rebuild to get rid of unmets

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- initial import by package builder

