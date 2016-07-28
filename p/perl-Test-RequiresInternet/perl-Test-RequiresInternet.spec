%define module_version 0.05
%define module_name Test-RequiresInternet
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Socket.pm) perl(Test/More.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.05
Release: alt2
Summary: Easily test network connectivity
Group: Development/Perl
License: perl
URL: https://metacpan.org/dist/Test-RequiresInternet

Source0: http://cpan.org.ua/authors/id/M/MA/MALLEN/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE README Changes
%perl_vendor_privlib/T*

%changelog
* Thu Jul 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- to Sisyphus

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- regenerated from template by package builder

* Thu Feb 05 2015 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- regenerated from template by package builder

* Mon Sep 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- regenerated from template by package builder

* Tue Jul 15 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

