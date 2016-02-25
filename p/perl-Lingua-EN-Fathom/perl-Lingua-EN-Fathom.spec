%define module_version 1.18
%define module_name Lingua-EN-Fathom
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Lingua/EN/Syllable.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(locale.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.18
Release: alt2
Summary: Measure readability of English text
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/K/KI/KIMRYAN/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README examples
%perl_vendor_privlib/L*

%changelog
* Thu Feb 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.18-alt2
- to Sisyphus

* Fri Apr 17 2015 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1
- regenerated from template by package builder

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1
- initial import by package builder

