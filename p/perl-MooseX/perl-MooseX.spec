%define module_version 0.002
%define module_name MooseX
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(Test/More.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.002
Release: alt2.1
Summary: Document the MooseX namespace
Group: Development/Perl
License: perl
URL: https://github.com/moose/MooseX

Source0: http://cpan.org.ua/authors/id/E/ET/ETHER/%{module_name}-%{module_version}.tar.gz
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
%doc README Changes
%perl_vendor_privlib/M*

%changelog
* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.002-alt2.1
- rebuild to restore role requires

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.002-alt2
- to Sissyphus

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- regenerated from template by package builder

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- initial import by package builder

