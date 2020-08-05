%define module_name Authen-DecHpwd
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Data/Integer.pm) perl(Digest/CRC.pm) perl(Exporter.pm) perl(Module/Build.pm) perl(Scalar/String.pm) perl(Test/More.pm) perl(constant.pm) perl(parent.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 2.007
Release: alt3
Summary: DEC VMS password hashing
Group: Development/Perl
License: GPL
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
%perl_vendor_archlib/A*
%perl_vendor_autolib/*

%changelog
* Wed Aug 05 2020 Andrew A. Vasilyev <andy@altlinux.org> 2.007-alt3
- import for Sysiphus

* Fri Feb 01 2019 Cronbuild Service <cronbuild@altlinux.org> 2.007-alt2.1
- rebuild with perl 5.28.1

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 2.007-alt2
- rebuild with perl 5.26

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.007-alt1
- regenerated from template by package builder

* Sun Feb 12 2017 Cronbuild Service <cronbuild@altlinux.org> 2.006-alt3
- rebuild to get rid of unmets

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 2.006-alt2.1
- rebuild with perl 5.22

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.006-alt2
- rebuild to get rid of unmets

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 2.006-alt1
- initial import by package builder

