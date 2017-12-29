# BEGIN SourceDeps(oneline):
BuildRequires: /proc perl(ExtUtils/MakeMaker.pm) perl(IPC/System/Simple.pm) perl(Test.pm)
# END SourceDeps(oneline)
%define module_version 1.3101
%define module_name Unix-Process
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.3101
Release: alt2
Summary: perl module %module_name
Group: Development/Perl
License: lgpl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/J/JE/JETTERO/%{module_name}-%{module_version}.tar.gz
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
%doc README Changes
%perl_vendor_privlib/U*

%changelog
* Fri Dec 29 2017 Igor Vlasenko <viy@altlinux.ru> 1.3101-alt2
- to Sisyphus

* Sat May 03 2014 Igor Vlasenko <viy@altlinux.ru> 1.3101-alt1
- initial import by package builder

