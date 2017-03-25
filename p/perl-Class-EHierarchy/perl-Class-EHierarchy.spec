# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(Scalar/Util.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_name Class-EHierarchy
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 2.00
Release: alt1
Summary: Base class for hierarchally ordered objects
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/C/CO/CORLISS/%{module_name}/Class-EHierarchy-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGELOG LICENSE README
%perl_vendor_privlib/C*

%changelog
* Sat Mar 25 2017 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.93-alt1.1
- to Sisyphus

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.93-alt1
- initial import by package builder

