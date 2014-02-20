# BEGIN SourceDeps(oneline):
BuildRequires: perl(Math/BigInt.pm) perl(Math/BigRat.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(Test/Simple.pm)
# END SourceDeps(oneline)
%define module_version 0.11
%define module_name Math-ContinuedFraction
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.11
Release: alt2
Summary: Create and Manipulate Continued Fractions.
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/J/JG/JGAMBLE/%module_name-%module_version.tar.gz
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
%doc README Changes
%perl_vendor_privlib/M*

%changelog
* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- initial import by package builder

