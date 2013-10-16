%define module_version 1.702
%define module_name Number-Tolerant
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Math/BigFloat.pm) perl(Math/BigRat.pm) perl(Scalar/Util.pm) perl(Sub/Exporter.pm) perl(Sub/Exporter/Util.pm) perl(Test/Builder.pm) perl(Test/More.pm) perl(Test/Tester.pm) perl(base.pm) perl(overload.pm) perl(parent.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.702
Release: alt2
Summary: tolerance ranges for inexact numbers
Group: Development/Perl
License: perl
URL: https://github.com/rjbs/Number-Tolerant

Source0: http://cpan.org.ua/authors/id/R/RJ/RJBS/%module_name-%module_version.tar.gz
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
%doc README LICENSE Changes
%perl_vendor_privlib/T*
%perl_vendor_privlib/N*

%changelog
* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.702-alt2
- build for Sisyphus (required for perl update)

* Wed Oct 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.702-alt1
- regenerated from template by package builder

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.701-alt1
- initial import by package builder

