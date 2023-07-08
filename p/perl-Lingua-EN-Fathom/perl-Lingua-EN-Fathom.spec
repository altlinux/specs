%define _unpackaged_files_terminate_build 1
%define module_name Lingua-EN-Fathom
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Lingua/EN/Syllable.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(locale.pm) perl(strict.pm) perl(warnings.pm) perl(Lingua/EN/Sentence.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.24
Release: alt1
Summary: Measure readability of English text
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/K/KI/KIMRYAN/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README examples
%perl_vendor_privlib/L*

%changelog
* Sat Jul 08 2023 Igor Vlasenko <viy@altlinux.org> 1.24-alt1
- automated CPAN update

* Tue Jun 13 2023 Igor Vlasenko <viy@altlinux.org> 1.23-alt1
- automated CPAN update

* Fri Nov 09 2018 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1
- automated CPAN update

* Thu Feb 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.18-alt2
- to Sisyphus

* Fri Apr 17 2015 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1
- regenerated from template by package builder

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1
- initial import by package builder

