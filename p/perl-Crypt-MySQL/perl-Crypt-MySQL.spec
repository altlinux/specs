# BEGIN SourceDeps(oneline):
BuildRequires: perl(Digest/SHA1.pm) perl(DynaLoader.pm) perl(Exporter.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(XSLoader.pm)
# END SourceDeps(oneline)
%define module_version 0.04
%define module_name Crypt-MySQL
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.04
Release: alt5
Summary: perl module %module_name
Group: Development/Perl
License: Perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/I/IK/IKEBE/%module_name-%module_version.tar.gz

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/C*
%perl_vendor_autolib/*

%changelog
* Wed Aug 05 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.04-alt5
- import for Sisyphus

* Fri Feb 01 2019 Cronbuild Service <cronbuild@altlinux.org> 0.04-alt4.1
- rebuild with perl 5.28.1

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt4
- rebuild with perl 5.26

* Sun Feb 12 2017 Cronbuild Service <cronbuild@altlinux.org> 0.04-alt3
- rebuild to get rid of unmets

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2.1
- rebuild with perl 5.22

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.04-alt2
- rebuild to get rid of unmets

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- initial import by package builder

