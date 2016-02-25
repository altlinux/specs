%define module_version 0.30
%define module_name Lingua-EN-Syllable
Serial: 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.30
Release: alt2
Summary: perl module %module_name
Group: Development/Perl
License: perl
URL: https://github.com/neilb/Lingua-EN-Syllable

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/N/NE/NEILB/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README
%perl_vendor_privlib/L*

%changelog
* Thu Feb 25 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.30-alt2
- to Sisyphus

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.30-alt1
- regenerated from template by package builder

* Tue Dec 01 2015 Igor Vlasenko <viy@altlinux.ru> 1:0.29-alt1
- regenerated from template by package builder

* Thu Apr 02 2015 Igor Vlasenko <viy@altlinux.ru> 1:0.28-alt1
- regenerated from template by package builder

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.26-alt2
- regenerated from template by package builder

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.251-alt1
- initial import by package builder

