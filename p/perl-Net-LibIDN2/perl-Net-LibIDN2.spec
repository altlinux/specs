%define module_name Net-LibIDN2
# BEGIN SourceDeps(oneline):
BuildRequires: libidn2-devel perl(Devel/CheckLib.pm) perl(Encode.pm) perl(ExtUtils/CBuilder.pm) perl(ExtUtils/ParseXS.pm) perl(Module/Build.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires(pre): rpm-build-perl rpm-build-licenses perl-devel perl-podlators

Name: perl-%module_name
Version: 1.02
Release: alt2
Summary: Perl bindings for GNU Libidn2
Group: Development/Perl
License: %perl_license
URL: https://metacpan.org/release/Net-LibIDN2

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/T/TH/THOR/%{module_name}-%{version}.tar.gz

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}
[ %version = 1.00 ] && rm t/001_basic.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README
%perl_vendor_archlib/N*
%perl_vendor_autolib/*

%changelog
* Sun Jul 02 2023 L.A. Kostis <lakostis@altlinux.ru> 1.02-alt2
- .spec: fix License.

* Fri Nov 04 2022 Igor Vlasenko <viy@altlinux.org> 1.02-alt1
- updated by package builder

* Wed Jun 16 2021 Igor Vlasenko <viy@altlinux.org> 1.01-alt3
- rebuild with perl 5.34.0

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2
- rebuild with perl 5.30

* Mon Nov 18 2019 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- updated by package builder

* Fri Feb 01 2019 Cronbuild Service <cronbuild@altlinux.org> 1.00-alt2.1
- rebuild with perl 5.28.1

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.00-alt2
- rebuild with perl 5.26

* Fri Sep 29 2017 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- regenerated from template by package builder

* Sun Feb 12 2017 Cronbuild Service <cronbuild@altlinux.org> 0.03-alt3
- rebuild to get rid of unmets

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2.1
- rebuild with perl 5.22

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.03-alt2
- rebuild to get rid of unmets

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- initial import by package builder

