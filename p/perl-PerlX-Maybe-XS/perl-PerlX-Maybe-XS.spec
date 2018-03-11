%define module_version 1.001
%define module_name PerlX-Maybe-XS
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel perl(Exporter.pm) perl(ExtUtils/Constant.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(XSLoader.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.001
Release: alt5
Summary: XS backend for PerlX::Maybe
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/PerlX-Maybe-XS

Source0: http://cpan.org.ua/authors/id/T/TO/TOBYINK/%module_name-%module_version.tar.gz

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE COPYRIGHT Changes README
%perl_vendor_archlib/P*
%perl_vendor_autolib/*

%changelog
* Sun Mar 11 2018 Igor Vlasenko <viy@altlinux.ru> 1.001-alt5
- to Sisyphus as perl-Dancer-Session-Cookie dep

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.001-alt4
- rebuild with perl 5.26

* Sun Feb 12 2017 Cronbuild Service <cronbuild@altlinux.org> 1.001-alt3
- rebuild to get rid of unmets

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 1.001-alt2.1
- rebuild with perl 5.22

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 1.001-alt2
- rebuild to get rid of unmets

* Mon Feb 24 2014 Igor Vlasenko <viy@altlinux.ru> 1.001-alt1
- regenerated from template by package builder

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 1.000-alt1
- initial import by package builder

