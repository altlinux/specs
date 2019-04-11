# BEGIN SourceDeps(oneline):
BuildRequires: perl(Math/BigInt.pm) perl(Math/BigRat.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(Test/Simple.pm)
# END SourceDeps(oneline)
%define module_name Math-ContinuedFraction
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.14
Release: alt1
Summary: Create and Manipulate Continued Fractions.
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/J/JG/JGAMBLE/%{module_name}-%{version}.tar.gz
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
%doc Changes CONTRIBUTING.md README.md
%perl_vendor_privlib/M*

%changelog
* Thu Apr 11 2019 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- initial import by package builder

