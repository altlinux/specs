%define module_version 0.11
%define module_name Crypt-UnixCrypt_XS
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel perl(Encode.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(XSLoader.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.11
Release: alt4
Summary: perl module %module_name
Group: Development/Perl
License: Perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/B/BO/BORISZ/%{module_name}-%{module_version}.tar.gz

%description
%summary

%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/C*
%perl_vendor_autolib/*

%changelog
* Wed Aug 05 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.11-alt4
- import for Sisyphus

* Fri Feb 01 2019 Cronbuild Service <cronbuild@altlinux.org> 0.11-alt3.1
- rebuild with perl 5.28.1

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt3
- rebuild with perl 5.26

* Sun Feb 12 2017 Cronbuild Service <cronbuild@altlinux.org> 0.11-alt2
- rebuild to get rid of unmets

* Mon Dec 05 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- regenerated from template by package builder

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2.1
- rebuild with perl 5.22

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.10-alt2
- rebuild to get rid of unmets

* Tue Jan 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- regenerated from template by package builder

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- initial import by package builder

