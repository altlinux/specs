%define module_version 0.001
%define module_name Devel-OverrideGlobalRequire
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(File/Find.pm) perl(File/Spec/Functions.pm) perl(File/Temp.pm) perl(List/Util.pm) perl(Test/More.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.001
Release: alt2
Summary: Override CORE::GLOBAL::require safely
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/Devel-OverrideGlobalRequire

Source0: http://cpan.org.ua/authors/id/D/DA/DAGOLDEN/%module_name-%module_version.tar.gz
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
%doc LICENSE README Changes
%perl_vendor_privlib/D*

%changelog
* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.001-alt2
- uploaded to Sisyphus as Scalar-Does dependency

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- initial import by package builder

