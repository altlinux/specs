%define module_version 0.10
%define module_name Test-Mock-Guard
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN/Meta.pm) perl(CPAN/Meta/Prereqs.pm) perl(Class/Load.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(List/Util.pm) perl(Module/Build.pm) perl(Scalar/Util.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.10
Release: alt2
Summary: Simple mock test library using RAII.
Group: Development/Perl
License: perl
URL: https://github.com/zigorou/p5-test-mock-guard

Source0: http://cpan.org.ua/authors/id/X/XA/XAICRON/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
Test::Mock::Guard is mock test library using RAII.
This module is able to change method behavior by each scope. See SYNOPSIS's sample code.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md LICENSE Changes
%perl_vendor_privlib/T*

%changelog
* Mon Dec 28 2015 Lenar Shakirov <snejok@altlinux.ru> 0.10-alt2
- build for Sisyphus

* Wed Jan 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- regenerated from template by package builder

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- initial import by package builder

