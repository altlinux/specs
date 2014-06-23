%define module_version 1.01
%define module_name Log-Report-Optional
%define _without_test 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(List/Util.pm) perl(String/Print.pm) perl(Test/More.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.01
Release: alt1
Summary: Log::Report in the lightest form
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/M/MA/MARKOV/%{module_name}-%{module_version}.tar.gz
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
%doc ChangeLog README
%perl_vendor_privlib/L*

%changelog
* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- regenerated from template by package builder

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt2
- moved to Sisyphus

* Fri Mar 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- initial import by package builder

