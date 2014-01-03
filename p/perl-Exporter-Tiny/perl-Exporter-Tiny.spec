%define module_version 0.032
%define module_name Exporter-Tiny
# BEGIN SourceDeps(oneline):
BuildRequires: perl(B.pm) perl(Carp.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.032
Release: alt1
Summary: an exporter with the features of Sub::Exporter but only core dependencies
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/Exporter-Tiny

Source: http://www.cpan.org/authors/id/T/TO/TOBYINK/Exporter-Tiny-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes COPYRIGHT LICENSE examples
%perl_vendor_privlib/E*

%changelog
* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.032-alt1
- automated CPAN update

* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.030-alt2
- uploaded to Sisyphus as Scalar-Does dependency

* Sat Oct 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.030-alt1
- regenerated from template by package builder

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.026-alt1
- initial import by package builder

