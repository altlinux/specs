# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(Test/More.pm) perl(XSLoader.pm)
# END SourceDeps(oneline)
%define module_version 1.00
%define module_name URI-UTF8-Punycode
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.00
Release: alt3.1
Summary: Punycode conversion of UTF-8 string.
Group: Development/Perl
License: gpl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/T/TW/TWINKLE/%module_name-%module_version.tar.gz

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE README Changes
%perl_vendor_archlib/U*
%perl_vendor_autolib/*

%changelog
* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3.1
- rebuild with new perl 5.24.1

* Sat Sep 24 2016 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3
- to Sisyphus

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 1.00-alt2.1
- rebuild with perl 5.22

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 1.00-alt2
- rebuild to get rid of unmets

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- initial import by package builder

