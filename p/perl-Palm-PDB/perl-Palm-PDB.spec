# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(constant.pm) perl(vars.pm)
# END SourceDeps(oneline)
%define module_version 1.015
%define module_name Palm-PDB
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.015
Release: alt2
Summary: Parse Palm database files
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/C/CJ/CJM/%{module_name}-%{module_version}.tar.gz
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
%doc README LICENSE Changes examples
%perl_vendor_privlib/P*

%changelog
* Thu Dec 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.015-alt2
- moved to Sisyphus as dependency

* Thu Sep 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.015-alt1
- initial import by package builder

