%define module_name match-simple-XS
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel perl(ExtUtils/MakeMaker.pm) perl(Test/Fatal.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.002
Release: alt2
Summary: XS backend for match::simple
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/match-simple-XS

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/T/TO/TOBYINK/%{module_name}-%{version}.tar.gz

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CREDITS LICENSE COPYRIGHT README Changes
%perl_vendor_archlib/m*
%perl_vendor_autolib/*

%changelog
* Sun Jul 30 2023 Igor Vlasenko <viy@altlinux.org> 0.002-alt2
- to Sisyphus as perl-IO-Prompter dep

* Wed Dec 14 2022 Igor Vlasenko <viy@altlinux.org> 0.002-alt1
- updated by package builder

* Wed Jun 16 2021 Igor Vlasenko <viy@altlinux.org> 0.001-alt6
- rebuild with perl 5.34.0

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.001-alt5.1
- rebuild with perl 5.30

* Fri Feb 01 2019 Cronbuild Service <cronbuild@altlinux.org> 0.001-alt4.1
- rebuild with perl 5.28.1

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.001-alt4
- rebuild with perl 5.26

* Sun Feb 12 2017 Cronbuild Service <cronbuild@altlinux.org> 0.001-alt3
- rebuild to get rid of unmets

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.001-alt2.1
- rebuild with perl 5.22

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.001-alt2
- rebuild with perl 5.20.1

* Fri Mar 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- initial import by package builder

