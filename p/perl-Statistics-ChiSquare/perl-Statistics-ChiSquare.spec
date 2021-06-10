%define module_version 1.0000
%define module_name Statistics-ChiSquare
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.0000
Release: alt2
Summary: perl module %module_name
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/D/DC/DCANTRELL/%{module_name}-%{module_version}.tar.gz
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
%doc README CHANGELOG
%perl_vendor_privlib/S*

%changelog
* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1.0000-alt2
- to Sisyphus for perl-Crypt-Random

* Tue Nov 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.0000-alt1
- regenerated from template by package builder

* Sat Sep 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1
- regenerated from template by package builder

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1
- initial import by package builder

