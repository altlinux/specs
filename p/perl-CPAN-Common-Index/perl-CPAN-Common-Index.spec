%define module_version 0.005
%define module_name CPAN-Common-Index
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN/DistnameInfo.pm) perl(CPAN/Meta/YAML.pm) perl(Carp.pm) perl(Class/Tiny.pm) perl(Cwd.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Basename.pm) perl(File/Fetch.pm) perl(File/Spec.pm) perl(File/Spec/Functions.pm) perl(File/Temp.pm) perl(HTTP/Tiny.pm) perl(IO/Uncompress/Gunzip.pm) perl(Module/Load.pm) perl(Path/Tiny.pm) perl(Search/Dict.pm) perl(Test/Deep.pm) perl(Test/FailWarnings.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(Tie/Handle/SkipHeader.pm) perl(URI.pm) perl(lib.pm) perl(parent.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.005
Release: alt2
Summary: Common library for searching CPAN modules, authors and distributions
Group: Development/Perl
License: apache
URL: https://github.com/dagolden/CPAN-Common-Index

Source0: http://cpan.org.ua/authors/id/D/DA/DAGOLDEN/%{module_name}-%{module_version}.tar.gz
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
%doc LICENSE README Changes Todo examples
%perl_vendor_privlib/C*

%changelog
* Sat Dec 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.005-alt2
- moved to Sisyphus as dependency

* Wed Oct 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- regenerated from template by package builder

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- regenerated from template by package builder

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- initial import by package builder

