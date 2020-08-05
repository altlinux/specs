%define module_name Scalar-String
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Exporter.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(bytes.pm) perl(if.pm) perl(parent.pm) perl(strict.pm) perl(utf8.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.003
Release: alt3
Summary: string aspects of scalars
Group: Development/Perl
License: Perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/Z/ZE/ZEFRAM/%{module_name}-%{version}.tar.gz

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_archlib/S*
%perl_vendor_autolib/*

%changelog
* Wed Aug 05 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.003-alt3
- import for Sisyphus

* Fri Feb 01 2019 Cronbuild Service <cronbuild@altlinux.org> 0.003-alt2.1
- rebuild with perl 5.28.1

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.003-alt2
- rebuild with perl 5.26

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- regenerated from template by package builder

* Sun Feb 12 2017 Cronbuild Service <cronbuild@altlinux.org> 0.002-alt3
- rebuild to get rid of unmets

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.002-alt2.1
- rebuild with perl 5.22

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.002-alt2
- rebuild to get rid of unmets

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.002-alt1.1
- rebuild with new perl

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- initial import by package builder

