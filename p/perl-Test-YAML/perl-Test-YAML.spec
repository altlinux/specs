# BEGIN SourceDeps(oneline):
BuildRequires: perl(Data/Dumper.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/Base.pm) perl(Test/Base/Filter.pm) perl(Test/More.pm) perl(Test/Pod.pm)
# END SourceDeps(oneline)
%define module_version 1.05
%define module_name Test-YAML
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.05
Release: alt1
Summary: Testing Module for YAML Implementations
Group: Development/Perl
License: perl
URL: https://github.com/ingydotnet/test-yaml-pm

Source0: http://cpan.org.ua/authors/id/I/IN/INGY/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %name = %{?epoch:%epoch:}%version-%release

%description scripts
scripts for %module_name

%prep
%setup -n %{module_name}-%{module_version}
sed -i -e s,/usr/bin/bash,/bin/sh, bin/test-yaml

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README LICENSE Changes
%perl_vendor_privlib/T*

%files scripts
%_bindir/*

%changelog
* Sat Dec 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- initial import by package builder

