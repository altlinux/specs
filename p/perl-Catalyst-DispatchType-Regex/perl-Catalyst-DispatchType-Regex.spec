%define module_version 5.90035
%define module_name Catalyst-DispatchType-Regex
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Benchmark.pm) perl(Catalyst.pm) perl(Catalyst/Controller.pm) perl(Catalyst/Request.pm) perl(Catalyst/Runtime.pm) perl(Catalyst/Test.pm) perl(Catalyst/Utils.pm) perl(Catalyst/View.pm) perl(Data/Dump.pm) perl(FindBin.pm) perl(MRO/Compat.pm) perl(Module/Build.pm) perl(Moose.pm) perl(Scalar/Util.pm) perl(Test/More.pm) perl(Text/Balanced.pm) perl(Text/SimpleTable.pm) perl(base.pm) perl(namespace/autoclean.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 5.90035
Release: alt2
Summary: Regex DispatchType
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/M/MG/MGRIMES/%{module_name}-%{module_version}.tar.gz
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
%doc Changes README
%perl_vendor_privlib/C*

%changelog
* Mon Mar 21 2016 Igor Vlasenko <viy@altlinux.ru> 5.90035-alt2
- to Sisyphus

* Thu Apr 02 2015 Igor Vlasenko <viy@altlinux.ru> 5.90035-alt1
- regenerated from template by package builder

* Thu Sep 26 2013 Igor Vlasenko <viy@altlinux.ru> 5.90033-alt1
- initial import by package builder

