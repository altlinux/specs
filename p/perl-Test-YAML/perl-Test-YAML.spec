%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Data/Dumper.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/Base.pm) perl(Test/Base/Filter.pm) perl(Test/More.pm) perl(Test/Pod.pm)
# END SourceDeps(oneline)
%define module_version 1.06
%define module_name Test-YAML
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.06
Release: alt1
Summary: Testing Module for YAML Implementations
Group: Development/Perl
License: perl
URL: https://github.com/ingydotnet/test-yaml-pm

Source: http://www.cpan.org/authors/id/I/IN/INGY/Test-YAML-%{version}.tar.gz
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
* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1
- automated CPAN update

* Sat Dec 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- initial import by package builder

