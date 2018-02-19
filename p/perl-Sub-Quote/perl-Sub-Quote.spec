%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Scalar/Util.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(threads.pm)
# END SourceDeps(oneline)
%define module_name Sub-Quote
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 2.005000
Release: alt1
Summary: efficient generation of subroutines via string eval
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/H/HA/HAARG/%{module_name}-%{version}.tar.gz
BuildArch: noarch
Conflicts: perl-Moo < 2.003000

%description
This package provides performant ways to generate subroutines from strings.
%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/S*

%changelog
* Mon Feb 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.005000-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.004000-alt1
- automated CPAN update

* Thu Jan 05 2017 Igor Vlasenko <viy@altlinux.ru> 2.003001-alt2
- to Sisyphus

* Sat Dec 17 2016 Igor Vlasenko <viy@altlinux.ru> 2.003001-alt1
- initial import by package builder

