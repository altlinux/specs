%define module_version 0.07
%define module_name Class-Virtual
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Carp/Assert.pm) perl(Class/Data/Inheritable.pm) perl(Class/ISA.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.07
Release: alt2
Summary: perl module %module_name
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/M/MS/MSCHWERN/%{module_name}-%{module_version}.tar.gz
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
%doc Changes
%perl_vendor_privlib/C*

%changelog
* Tue Mar 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt2
- to Sisyphus

* Thu Apr 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- regenerated from template by package builder

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- initial import by package builder

