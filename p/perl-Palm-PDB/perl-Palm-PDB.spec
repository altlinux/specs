# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(constant.pm) perl(vars.pm)
# END SourceDeps(oneline)
%define module_version 1.016
%define module_name Palm-PDB
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.016
Release: alt1
Summary: Parse Palm database files
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/C/CJ/CJM/Palm-PDB-%{version}.tar.gz
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
* Mon Jan 26 2015 Igor Vlasenko <viy@altlinux.ru> 1.016-alt1
- automated CPAN update

* Thu Dec 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.015-alt2
- moved to Sisyphus as dependency

* Thu Sep 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.015-alt1
- initial import by package builder

