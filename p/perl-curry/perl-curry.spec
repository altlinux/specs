%define module_name curry
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Scalar/Util.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 2.000000
Release: alt1
Summary: Create automatic curried method call closures for any class or object
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/M/MS/MSTROUT/%{module_name}-%{version}.tar.gz
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
%doc README Changes
%perl_vendor_privlib/c*

%changelog
* Wed Dec 29 2021 Igor Vlasenko <viy@altlinux.org> 2.000000-alt1
- automated CPAN update

* Fri Feb 02 2018 Igor Vlasenko <viy@altlinux.ru> 1.001000-alt2
- to Sisyphus as perl-DBIx-Class-Schema-Loader dep

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.001000-alt1
- regenerated from template by package builder

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.000000-alt1
- initial import by package builder

