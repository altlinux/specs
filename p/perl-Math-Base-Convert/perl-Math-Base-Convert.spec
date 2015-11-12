%define module_version 0.11
%define module_name Math-Base-Convert
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Benchmark.pm) perl(Config.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Math/BigInt.pm) perl(diagnostics.pm) perl(overload.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.11
Release: alt2
Summary: perl module %module_name
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/M/MI/MIKER/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/M*

%changelog
* Thu Nov 12 2015 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2
- to Sisyphus as SQL-Statement dependency

* Mon Oct 26 2015 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- regenerated from template by package builder

* Tue Jan 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- regenerated from template by package builder

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- initial import by package builder

