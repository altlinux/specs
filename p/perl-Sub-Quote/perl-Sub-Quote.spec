# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Scalar/Util.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(threads.pm)
# END SourceDeps(oneline)
%define module_version 2.003001
%define module_name Sub-Quote
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 2.003001
Release: alt2
Summary: efficient generation of subroutines via string eval
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/H/HA/HAARG/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch
Conflicts: perl-Moo < 2.003000

%description
This package provides performant ways to generate subroutines from strings.
%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/S*

%changelog
* Thu Jan 05 2017 Igor Vlasenko <viy@altlinux.ru> 2.003001-alt2
- to Sisyphus

* Sat Dec 17 2016 Igor Vlasenko <viy@altlinux.ru> 2.003001-alt1
- initial import by package builder

